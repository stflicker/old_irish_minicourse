# Review of the first 28 days (syllabus + lesson Markdown)

*Status: review only. No lesson file has been changed. `FIRST_28_DAYS.md` stays locked until you approve changes.*

**Update 2 (full PDF received).** The attached full copy has a complete text layer (402 PDF pages; printed page = PDF page − 12). I re-checked everything that was previously ❓ and corrected two of my own first-round findings (D024 and D026, marked ✏️ below). Page images were used to confirm Stifter's superscript marks on p. 51 (neuter article) and p. 74 (io-stems), where the OCR was ambiguous.

## 1. What this review is based on

| Source | What I could use | Limits |
|---|---|---|
| Stifter, *Sengoídelc* (2006), full PDF attached to the session | Full text of Lessons 1–24 (all pages relevant to Days 1–28 and to the next-28 draft); page images for pp. 51 and 74. | Printed superscripts are sometimes lost in text extraction; where a mark mattered I looked at the page image. I did **not** re-read every page of Lessons 1–5 (mutation lists, categories) line by line. |
| Drive copies (first round) | Table of contents only. | The Drive connector truncates at ~p. 68; the second Drive file is an image-only scan. |
| Web | Search results about Stifter 2023, the Griffith chapter and the EIEOL site structure. | Direct page fetches to `lrc.la.utexas.edu`, `doi.org`, `ore.eu` and `pmc.ncbi.nlm.nih.gov` are blocked in this session, so those pages were not read. |

Legend: ✅ checked against Stifter's text or page image; ⚠️ problem found; ❓ could not be checked; ✏️ my earlier finding, corrected.

## 2. Syllabus (`FIRST_28_DAYS.md`) against Stifter's contents

The order follows Stifter's order of presentation and the section numbers match the table of contents (§§6.4–6.8, 7.1–7.4, 8.3–8.5, 9.2, 10.1–10.3, 11.1–11.4, 12.1, 12.3, 12.4, 13.1, 14.1, 14.2). Weekly rhythm (N/N/N/N/N/T/H) is sound.

Gaps worth considering (none are errors):

1. **Lesson 5 is skipped entirely** (gender, number, case, adjectives, the article, **word order §5.7**). Days 26 onward and every phrase example (*in catt bán*, *inna ingine bicce*) rely on it. Suggest a short bridge lesson, or fold §5.7 into an existing exercise day.
2. **§8.1–8.2 (absolute vs conjunct, the dot notation, McCone's W/S/H classification)** is not a day of its own. Day 12 introduces *ní·* without Stifter's explanation that *any* preverbal element triggers conjunct inflection. Day 24 partly repairs this, but late.
3. **§9.1 "Varia"** contains rules the exercises need (the *d-* nasalization exception, *ar/do/i* case government, *ocus*, *acht*). Not scheduled.
4. **§6.8 (long vowels, diphthongs, hiatus, schwa, syncope)** is listed in Day 6's range, but Day 6 teaches *macc/cenn* and u-infection instead. Syncope (§6.8.5) matters for *dliged*, *sacart*, *ingen* — either schedule it or change Day 6's section label to §6.7 only.
5. **Day 26 (§13.1)**: the syllabus asks for a short poetic reading from Stifter's §13.1 (a normalised 11th-century poem about a scribe, ascribed to Colum Cille). The lesson uses the *Am gáeth i mmuir* formula instead (see D026). Lesson 13 also has **§13.2 Varia** (the particle *inna(d)·*, new prepositions *cen, co, di, fo, frí, ó, tar*, the verb *creitid*), an exercise (13.3) and a **Test (13.4)**; none is used.
6. **§14.3 (io-adjectives) and §14.4 (exercise)** are not scheduled; both are natural Day 29–30 material (see `NEXT_28_DAYS_DRAFT.md`).

## 3. Findings that affect many lessons

### F1 — EIEOL cross-check links (22 lessons) ✏️ **corrected in update 3**
My first-round claim that these links are mislabelled was **wrong**. Checked against the live site: `…/eieol/iriol/20` is the Lesson 2 page, which carries **Grammar §6 “Initial Mutations”** (6.1 Lenition, 6.2 Nasalization, 6.3 Spirant Mutation); `…/iriol/30` is the Lesson 3 page, which carries **Grammar §13 “The Noun: o- and yo-Stems”**, §12 (copula/substantive verb) and **§15.3 possessive pronouns**. The labels “§6”, “§13”, “copula §12” and “possessives §15.3” are therefore right. What *is* wrong: the same `iriol/30` link is also used for the **article** (that is Grammar §30.3 on `iriol/60`), **adjective agreement** (§14/§24 on `iriol/30`/`iriol/50`) and **ā-stems** (§18 on `iriol/40`). Fix those links; the rest can stay. The repeated “Effects cross-check” boilerplate is still better removed (it is already gone from the rewritten Days 1–7).

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
| 010 | 7.3 | ⚠️ **Confirmed error (p. 51, page image):** Illustration 7.2 gives the neuter nom./acc. plural article as *(in)na* with **no mutation mark**; D010's table gives *inna* [H] in the nominative and accusative plural. Change both cells to [0]. (The ᴸ/ᴴ in *inna cennᴸ(-aᴴ)*, Ill. 7.3, belong to the noun, not the article.) Other cells ✅: nom./acc. sg. *a*ᴺ, gen. *in*ᴸ, prep. *-(s)in*ᴸ, gen. pl. *(i)na*ᴺ, prep. pl. *-(s)naib*. **Sources differ:** EIEOL Grammar §6.3 lists “the nominative plural feminine **and neuter** of the article” among the aspirating forms, i.e. [H]. Stifter (the course's reference) shows no mark. Decide which to follow and say so in the lesson. | *dliged* paradigm is course-supplied (Stifter only lists it as an exercise word, noting it has no syncope). |
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
| 024 | 12.3 | ✏️ **Corrected.** My first-round claim that Stifter does not discuss the origin of absolute/conjunct was wrong: §12.3 **note 6 (p. 68)** says the distinction "has nothing to do with the distinction between primary and secondary endings in PIE" but results from "early loss of final inherited short *\*-i*, but retention of the vowel before enclitic particles", with a parallel in early Old Welsh, and that the nature of the particles is "a matter of heated disputes". D024's particle-based story is therefore consistent with Stifter. | Still worth fixing: (a) the lesson never shows Stifter's reconstructed W1/W2 ending tables (Ills. 12.2–12.3) that the syllabus entry ("prehistory of W1/W2 endings") refers to; (b) it does not mention the **Old Welsh parallel** or the **loss of final \*-i** that Stifter uses as the key point; (c) "Cowgill particle" is the standard label in the literature but is not Stifter's wording; (d) F4 (Griffith citation). |
| 025 | 12.4 | ✅ Checked against Illustration 12.5 (p. 69): *mo*ᴸ, *do*ᴸ, *a* 'his/its'ᴸ, *a* 'her'ᴴ, *a* 'their'ᴺ — all agree. Stifter also lists *ar*ᴺ 'our' and *for/far/bar*ᴺ 'your (pl.)' and notes that possessives are uninflected and unaffected by a preceding mutating particle. | F1 ("§15.3" label). Optional additions from the page: *m'* / *t'* before vowels (*m'athair*), and the fused forms with prepositions (*dom, fort*, *dia*) — good material for a later day. |
| 026 | 13.1 | ✏️ **Softened.** Stifter's own §13.1 poem is also late (he dates it "approximately the 11th century", normalised, put in Colum Cille's mouth), so "not Old Irish" is not a reason to reject a text. The real problems: the lesson does **not use Stifter's poem** (four lines about a scribe: *Sínim mo phenn mbecc mbróenach / tar óenach lebor lígoll / cen scor fri selba segonn, / dian scith mo chrob ón scribonn*), although the syllabus points to §13.1; and *Am gáeth i mmuir* is described as "Old Irish" in the title. | Either replace the text with Stifter's stanza (it uses things already taught: *mo*, 1sg verb, nasalising feminine accusative, *tar* + acc.) or keep Amergin but label it "early Irish (later, normalised)". Add §13.2 Varia (new prepositions). F2. |
| 027 | 14.1 | ✅ marks (ᴸ/ᴺ/ᴴ) all agree with Illustration 14.1 (p. 74, page image). ⚠️ **Spelling**: Stifter gives gen. sg. **céili**, prep. sg. **céiliu**, voc. **a chéili**, nom. pl. **céili**, acc. pl. **céiliu**, voc. pl. **a chéiliu** (gen. pl. *céile*, prep. pl. *céilib*). D027 prints *céli / céliu / a chéli / a chéliu* — inconsistent with Stifter and with its own nominative *céile*. The "other conventions" note should not be needed. | Correct the spellings in the table, quiz options (*céli, céliu*) and prose. Stifter also gives the non-palatalised model *daltae* and the mnemonic "the vowel of *fer* corresponds to the io-stem ending" — good for the lesson. |
| 028 | 14.2 | ✅ Illustration 14.2 (p. 75): *cride*ᴺ, *cridi*ᴸ, *cridiu*ᴸ, *a chride*ᴺ; pl. *cride*ᴸ, *cride*ᴺ, *cridib*, *a chride*ᴸ — all agree (text extraction; superscripts not re-checked on the image). Stifter's mnemonic word is *cenn*. | Optional: add the non-palatalised model *cumachtae*. The statement about "no regular long plural" is consistent with Stifter's table (only one plural nom./acc. form is shown). |

## 5. What is still unchecked

* Lessons 1–5 (mutation lists, categories, word order) were used only where a lesson cites them (the possessive and article effects were confirmed).
* §6.8 (syncope etc.) and §9.1 (Varia) were not compared with any lesson because no lesson teaches them.
* Every external claim (Thurneysen section numbers, Stifter 2023 §8.1, Luján, Le Mair, the EIEOL pages) is still unverified because those sites cannot be fetched from this session.

## 6. Suggested order of fixes

1. F1 (mislabelled links) and F2 (rendering) — mechanical, affect everything.
2. D010 (neuter article plural) — confirmed error, two cells to change.
3. D022/D023 (W2a vs W2b history); D024 (add Stifter's ending tables, the Old Welsh parallel and the loss of final *\*-i*).
4. D027 (spelling), D026 (poem choice / label).
5. D007 language decision; D006 §6.8 decision; citation clean-up (F4).
