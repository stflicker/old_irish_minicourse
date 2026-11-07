# Review of the first 28 days (syllabus + lesson Markdown)

*Status: review only. No lesson file has been changed. `FIRST_28_DAYS.md` stays locked until you approve changes.*

## 1. What this review is based on

| Source | What I could use | Limits |
|---|---|---|
| Stifter, *Sengoídelc* (2006), Drive file `Sengoídelc.pdf` (text layer) | Table of contents for all 58 lessons; full text of Lessons 1–12 (printed pp. 1–68). | The Drive connector returns only the first ~183,000 characters of the file, so the text stops at the end of §12.3 (p. 68). **Not readable: §12.4 (p. 69), Lesson 13 (the poem), Lesson 14 (io-stems), and everything after.** The OCR is noisy (superscripts such as ᴸ ᴺ ᴴ are sometimes lost). |
| Second Drive file (z-library scan of the same book) | — | Image-only, no text layer. Unusable. |
| Web | Search results about Stifter 2023, the Griffith chapter and the EIEOL site structure. | Direct page fetches to `lrc.la.utexas.edu`, `doi.org`, `ore.eu` and `pmc.ncbi.nlm.nih.gov` are blocked in this session, so I could not read those pages. |

Legend: ✅ checked against Stifter's text; ⚠️ problem found; ❓ could not be checked (text not available or source not readable).

## 2. Syllabus (`FIRST_28_DAYS.md`) against Stifter's contents

The order follows Stifter's order of presentation and the section numbers match the table of contents (§§6.4–6.8, 7.1–7.4, 8.3–8.5, 9.2, 10.1–10.3, 11.1–11.4, 12.1, 12.3, 12.4, 13.1, 14.1, 14.2). Weekly rhythm (N/N/N/N/N/T/H) is sound.

Gaps worth considering (none are errors):

1. **Lesson 5 is skipped entirely** (gender, number, case, adjectives, the article, **word order §5.7**). Days 26 onward and every phrase example (*in catt bán*, *inna ingine bicce*) rely on it. Suggest a short bridge lesson, or fold §5.7 into an existing exercise day.
2. **§8.1–8.2 (absolute vs conjunct, the dot notation, McCone's W/S/H classification)** is not a day of its own. Day 12 introduces *ní·* without Stifter's explanation that *any* preverbal element triggers conjunct inflection. Day 24 partly repairs this, but late.
3. **§9.1 "Varia"** contains rules the exercises need (the *d-* nasalization exception, *ar/do/i* case government, *ocus*, *acht*). Not scheduled.
4. **§6.8 (long vowels, diphthongs, hiatus, schwa, syncope)** is listed in Day 6's range, but Day 6 teaches *macc/cenn* and u-infection instead. Syncope (§6.8.5) matters for *dliged*, *sacart*, *ingen* — either schedule it or change Day 6's section label to §6.7 only.
5. **Day 26 (§13.1)**: the syllabus asks for "short poetic reading, only the grammar already known" from Stifter's §13.1. The lesson uses the *Am gáeth i mmuir* formula instead of Stifter's own poem (see D026 below). Stifter's Lesson 13 also has a **Test (13.4)** that is not used.
6. **§14.3 (io-adjectives) and §14.4 (exercise)** are not scheduled; both are natural Day 29–30 material (see `NEXT_28_DAYS_DRAFT.md`).

## 3. Findings that affect many lessons

### F1 — The "UT Austin" cross-check links are mislabelled (≈59 occurrences, 22 lessons) ⚠️
Every lesson ends its paradigm section with *"UT Austin, Old Irish Online, §6"* → `…/eieol/iriol/20` and *"nominal paradigms, §13"* → `…/eieol/iriol/30`. A web search shows that `iriol/20` is **Old Irish Online Lesson 2 (the text *Táin Bó Regamna*)** and `iriol/30` is **Lesson 3** (also a text lesson); the number in the URL is a page id, not a section number. Neither is a "§6" or a "nominal paradigms §13", and the same two URLs are also cited as "possessives §15.3", "copula §12", "*céile* declension", "*cride* declension", "adjective agreement". I could not open the pages (host blocked), so please open them once. Suggested fix: remove the boilerplate "Effects cross-check" line, and cite EIEOL's grammar pages by their real title once you have confirmed which page covers which paradigm.

### F2 — Markdown rendering bug: literal `**` visible on 13 pages ⚠️
Nested emphasis such as `**nominative *-s*** and **accusative *-m***` is not rendered. Seen as raw asterisks on Days 1, 2, 3, 6, 7, 14, 17, 20, 22, 23, 26, 27, 28 (1–4 occurrences each). Fix the Markdown (or the renderer).

### F3 — Boilerplate dominates ⚠️
The 70-word "Following-word effects" key is repeated verbatim in nearly every lesson; 14 of the 56 quiz hints are the generic "Check the contrast in the table." (Design point, already discussed; listed here because it also hides the lesson-specific content.)

### F4 — Citation hygiene ⚠️
* **Griffith (2020)** is cited as "The Cowgill particle" (D013, D014, D024). The actual chapter is *"The 'Cowgill particle', preverbal* ceta *'first', and prepositional cleft sentences in the Old Irish glosses"*, in Lash, Qiu & Stifter (eds.), De Gruyter 2020, pp. 239–268. It tests the particle in attested glosses; it is not the right single citation for the *origin* of the absolute/conjunct split. For the origin, cite Cowgill (1975) and the McCone/Schrijver discussions.
* **Stifter (2023) "The rise of gemination in Celtic"** exists (Open Research Europe, PMC10446051). D007 cites "§8.1" for the claim that h- after ordinary accusative-plural nouns is conjectural. I could read only the abstract; **please verify the section number and wording against the full text.**
* **Scribd link** to Thurneysen (D006) points to an unauthorised copy of a copyrighted book; replace with a section reference or an authorised source.
* D007 cites Thurneysen "§§240–241" for *inna-mmaccu* (Ml. 104d5). In the German *Handbuch*, §241 is the definition of gemination and §240 concerns numerals; the manuscript example needs checking in the English *GOI* before keeping the siglum.

## 4. Lesson-by-lesson table

| Day | Section | Paradigms / forms vs Stifter | Notes and required changes |
|---|---|---|---|
| 001 | 6.4 | ✅ *ech* table (p. 43): all forms and ᴸ/ᴺ/ᴴ marks agree, incl. *euch/eoch* variant (Note 1). | F1, F2. Quiz fine. |
| 002 | 6.4 | ✅ same table. PIE endings (*-ons*, *-oi* as pronominal ending, *-bhis/-ois*) agree with Stifter's reconstructions. | F1. |
| 003 | 6.5 | ✅ *fer* table (p. 45). Raising/lowering explanation matches Stifter and the McCone reference. | F1, F2. |
| 004 | 6.6 | ✅ *cenn* table (p. 46) incl. vocative *a chenn*ᴺ. | Mentions the article *a* before the article is taught (Day 8–10); reword. |
| 005 | 6.6 | ✅ short vs long plural; Stifter says the short plural "continues the Celtic and Indo-European preforms", which D005 reproduces correctly. | Tables identical to D004 — consider replacing the duplicate. |
| 006 | 6.7–6.8 | ✅ *cenn*, *fer*. *macc* is not a paradigm in Stifter (only an exercise word; Stifter's note says **no u-infection in *macc***, u-infection in *ball*). *macc/maicc/maccu* are standard but course-supplied. | ⚠️ §6.8 not taught (see §2). ⚠️ Scribd link. ❓ "Thurneysen §170a" claim — check in *GOI*. F2. |
| 007 | 6.4–6.6 | ✅ Latin/Sanskrit tables are standard. | ⚠️ **Only lesson written in Chinese** (the rest are English) — decide on one language. ⚠️ Stifter 2023 §8.1 and Thurneysen §§240–241 references to verify (F4). |
| 008 | 7.1–7.2 | ✅ masculine article (p. 50): nom *in* [0], gen *in/ind* ᴸ, prep *-(s)in* ᴸ, acc *in* ᴺ; pl *in/ind* ᴸ, *(i)na* ᴺ, *-(s)naib*, *(i)na* ᴴ. | Minor: gen. sg./nom. pl. also has *int* before *s-* (§7.2.2). |
| 009 | 7.1–7.2 | ✅ same. Phrase examples agree with Illustration 7.3. | — |
| 010 | 7.3 | ⚠️ **Neuter article plural**: D010 gives *inna* [H] for nom./acc. pl. In Stifter's OCR (Ill. 7.2/7.3/7.5) the neuter nom./acc. pl. article carries **no mutation mark** (the ᴸ/ᴴ in *inna cennᴸ(-aᴴ)* belongs to the noun). OCR is ambiguous: **check p. 51 in the printed book.** | *dliged* paradigm is course-supplied (Stifter only lists it as an exercise word, noting it has no syncope). |
| 011 | 7.4 | ✅ *in catt bán* phrases agree with Illustration 7.5; adjectives follow the noun. | — |
| 012 | 8.3–8.4 | ✅ W1 table (p. 56) exactly. | §8.1–8.2 missing (see §2). |
| 013 | 8.4 | ✅ plural forms; Stifter note 4 (1pl conj. *-am* has lenited *m*) not used. | F4 (Griffith). |
| 014 | 8.5; 9.2 | ✅ *glantae* (Stifter 8.4.5). | F4. |
| 015 | 10.1 | ✅ *tuath* (p. 59) all forms and marks. | — |
| 016 | 10.1–10.2 | ✅ *tuath* and *cell* (Ill. 10.2). PIE *-eh₂-es / -eh₂-ns* agree with Stifter. | — |
| 017 | 10.3 | ✅ *ben* (Ill. 10.3). Stifter writes *mnaí*, *mnaib*; the course normalises to *mnái*, *mnáib* and says so. | Optional: note Stifter's own spellings. |
| 018 | 11.1–11.2 | ✅ feminine article (p. 62); *ind/int* variants (§11.2). | Quiz distractor "da" is odd. |
| 019 | 11.3 | ✅ *don(d)/isin(d)/fon* and the s/no-s rule (§7.1.3, §11.3). | Italian *nel*: it is Italian *in + il*, not "Latin *in*" + article. |
| 020 | 11.4 | ✅ *ind ingen becc*… agree with Ill. 11.2. | — |
| 021 | 10–11 | ✅ PIE *-eh₂* → *-ā* standard. | ⚠️ "old **thematic** vowel" is misleading for ā-stems: "thematic" normally refers to the *e/o* stem vowel; say "stem vowel". |
| 022 | 12.1 | ✅ W2 table (Ill. 12.1) exactly. | ⚠️ Comparison ties W2a to the *-eyé-* suffix. Stifter (§12.1.3–4, §12.3 n. 5): W2a is mainly **denominative** (from o-/ā-stems); **W2b** are old **causative/iterative**; W2 as a whole merges primary *-eie/o-* verbs and athematic statives in *-eh₁ie/o-*. Rewrite. |
| 023 | 12.1 | ✅ *roithid* ← *reithid* and *sluindid* agree with Stifter. | Same W2a/*-eyé-* problem as D022. |
| 024 | 12.3 | ⚠️ **Does not teach Stifter §12.3.** §12.3 is a set of reconstructed ending tables for W1 and W2 (OIr / Prim. Irish / Insular Celtic / Pre-Celtic), e.g. abs. 3sg *-aid* < *\*-ati* (primary ending) vs. conj. 3sg *-a* < *\*-at* (secondary ending). The lesson instead teaches the Cowgill-particle theory, which Stifter does not discuss there. | Rewrite to present Stifter's tables first, then the Cowgill/McCone alternative as "other view"; correct "Source: Stifter §12.3" to apply only to the parts that are Stifter's. D013/D014's remark "do not equate absolute = PIE primary" should be rephrased: Stifter *does* tabulate it that way. |
| 025 | 12.4 | ✅ mutation effects match Stifter's lists (pp. 30–33): *mo/do/a* 'his' lenite, *a* 'her' aspirates, *a* 'their' nasalizes. ❓ §12.4 itself (p. 69) unreadable. | F1 ("§15.3" label). |
| 026 | 13.1 | ⚠️ *Am gáeth i mmuir* is the *Song of Amergin* from the *Lebor Gabála Érenn* tradition — **Middle Irish**, not Old Irish — and is not Stifter's poem. ❓ Stifter's §13.1 unreadable. | Retitle or replace with the poem in Stifter §13.1; F2. |
| 027 | 14.1 | ⚠️ Spelling: forms are given as *céli, céliu, céilib, a chéli*; the standard Old Irish forms are **céili** (gen. sg./nom. pl.), **céiliu**, **céilib**. D027's note says "other conventions" — but the headline forms should follow Stifter. ❓ p. 74 unreadable. | Verify against p. 74 and fix. |
| 028 | 14.2 | ❓ *cride* paradigm, and the claim that there is "no regular long plural" for neuter io-stems, cannot be checked (p. 75 unreadable). | Verify. |

## 5. What I need to finish the review

Please send **printed pages 69–76** (§12.4, Lesson 13, Lesson 14) as a short PDF or text, and — only if you want me to check the next-28 draft — pages 77–121 (Lessons 15–24). The easiest routes: attach the pages to the chat, or save an excerpt to Drive as a separate, small PDF (the connector's size limit is the problem, not the book).

## 6. Suggested order of fixes

1. F1 (mislabelled links) and F2 (rendering) — mechanical, affect everything.
2. D010 (neuter article plural) — needs one page check.
3. D024 (rewrite to Stifter §12.3), D022/D023 (W2a vs W2b history).
4. D026 (poem choice), D027 (spelling), D028 (verify).
5. D007 language decision; D006 §6.8 decision; citation clean-up (F4).
