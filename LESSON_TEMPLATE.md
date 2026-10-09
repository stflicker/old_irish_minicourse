# Template for a new `lessons/OI-D###.md`

The **metadata** below controls the HTML interface. The **body** controls the lesson text. The number, textbook anchor, and focus must come from `FIRST_28_DAYS.md`.

```md
---
id: OI-D002
title: Masculine o-stems
subtitle: 'ech: plural'
category: Nominal morphology
stifter: '6.4'
minutes: 12
word: ech
questions:
  - prompt: 'Which form or category ...?'
    options:
      - 'Answer A'
      - 'Answer B'
      - 'Answer C'
    correct: 1
    explanation: 'One-sentence reason B is correct.'
    hint: 'Point back to one form or contrast.'
  - prompt: 'What changes ...?'
    options:
      - 'Choice A'
      - 'Choice B'
    correct: 0
    explanation: 'One-sentence explanation.'
    hint: 'Look at the plural paradigm.'
---
## Paradigm

| Case | Form | Distinguishing feature |
|---|---|---|
| Nominative plural | **[verified form]** | ... |
| Accusative plural | **[verified form]** | ... |

## One point

One short explanation. Mention what must actually be recognised, not generic grammar background.

## Comparison (optional)

A short comparison with Latin, Greek, Sanskrit, Brittonic, or a reconstructed Proto-Celtic form, only where scholarly evidence supports it.
```

For reading sessions, replace `## Paradigm` with `## Text`, using only a short properly sourced passage or a clearly marked constructed example. Do not invent Stifter quotations or say unattested forms are attested.

Run `python scripts/build_site.py` to regenerate all pages from the Markdown before previewing them.