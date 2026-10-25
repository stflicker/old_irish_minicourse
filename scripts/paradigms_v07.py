"""Reviewed, explicit table content for the one-time v0.7 lesson migration.

These are course paradigm/model forms, not claims of individual attestation.
L/N/H are following-word effects, not suffixes. 0 means no prescribed L/N/H.
Source anchors: Stifter (2006), sections retained in each lesson; Strachan
(1909), nominal paradigms; UT Austin Old Irish Online sections 6, 13 and 18.
After migration, lessons/OI-D###.md remains the editable source of truth.
"""
from __future__ import annotations

CASES = ['Nominative', 'Genitive', 'Prepositional', 'Accusative', 'Vocative']
EFFECTS = {
    'mo': [('0','L'),('L','N'),('L','0'),('N','H'),('L','H')],
    'no': [('N','L'),('L','N'),('L','0'),('N','L'),('N','L')],
    'fa': [('L','H'),('H','N'),('L','0'),('N','H'),('L','H')],
}
NOUNS = {
 'ech': ('horse', 'masculine o-stem', 'mo', [
  ('ech','eich'),('eich','ech'),('euch / eoch','echaib'),
  ('ech','echu / euchu / eochu'),('a eich','a echu / a euchu / a eochu')]),
 'fer': ('man', 'masculine o-stem', 'mo', [
  ('fer','fir'),('fir','fer'),('fiur','feraib'),('fer','firu'),('a fir','a firu')]),
 'macc': ('son', 'masculine o-stem', 'mo', [
  ('macc','maicc'),('maicc','macc'),('macc','maccaib'),('macc','maccu'),('a maicc','a maccu')]),
 'cenn': ('head', 'neuter o-stem', 'no', [
  ('cenn','cenn [L] / cenna [H]'),('cinn','cenn'),('ciunn','cennaib'),
  ('cenn','cenn [L] / cenna [H]'),('a chenn','a chenn [L] / a chenna [H]')]),
 'dliged': ('law', 'neuter o-stem', 'no', [
  ('dliged','dliged [L] / dligeda [H]'),('dligid','dliged'),('dligud','dligedaib'),
  ('dliged','dliged [L] / dligeda [H]'),('a dliged','a dliged [L] / a dligeda [H]')]),
 'tuath': ('tribe, people', 'feminine a-stem', 'fa', [
  ('tuath','tuatha'),('tuaithe','tuath'),('tuaith','tuathaib'),('tuaith','tuatha'),('a thuath','a thuatha')]),
 'cell': ('church', 'feminine a-stem', 'fa', [
  ('cell','cella'),('cille','cell'),('cill','cellaib'),('ceill','cella'),('a chell','a chella')]),
 'ben': ('woman', 'irregular feminine', 'fa', [
  ('ben','mn\u00e1'),('mn\u00e1','ban'),('mn\u00e1i','mn\u00e1ib'),
  ('mn\u00e1i / bein','mn\u00e1'),('a ben','a mn\u00e1')]),
 'catt': ('cat', 'masculine o-stem', 'mo', [
  ('catt','caitt'),('caitt','catt'),('catt','cattaib'),('catt','cattu'),('a chaitt','a chattu')]),
 'ingen': ('girl, daughter', 'feminine a-stem', 'fa', [
  ('ingen','ingena'),('ingine','ingen'),('ingin','ingenaib'),('ingin','ingena'),('a ingen','a ingena')]),
 'ceile': ('companion', 'masculine io-stem', 'mo', [
  ('c\u00e9ile','c\u00e9li'),('c\u00e9li','c\u00e9ile'),('c\u00e9liu','c\u00e9ilib'),
  ('c\u00e9ile','c\u00e9liu'),('a ch\u00e9li','a ch\u00e9liu')]),
 'cride': ('heart', 'neuter io-stem', 'no', [
  ('cride','cride'),('cridi','cride'),('cridiu','cridib'),('cride','cride'),('a chride','a chride')]),
 'ban_adj': ('white', 'adjective, masculine o-stem forms', 'mo', [
  ('b\u00e1n','b\u00e1in'),('b\u00e1in','b\u00e1n'),('b\u00e1n','b\u00e1naib'),('b\u00e1n','b\u00e1nu'),('b\u00e1in','b\u00e1nu')]),
 'becc_adj': ('small', 'adjective, feminine a-stem forms', 'fa', [
  ('becc','becca'),('bicce','becc'),('bicc','beccaib'),('bicc','becca'),('becc','becca')]),
}
NOTES = {
 'ech': 'The spelling eoch/eochu is an alternative to euch/euchu; it is not an extra case.',
 'fer': 'Compare fer [0] as nominative singular with fer [N] as accusative singular: the noun looks the same, but its effect on a following adjective differs.',
 'macc': 'Prepositional singular macc has no written u-infection. Do not insert a u just because fer has fiur.',
 'cenn': 'Short neuter plurals carry [L]; the long -a plural is shown with the course default [H]. Lenition after -a is also found: this is a documented variation, not a universal ban on lenition.',
 'dliged': 'A preceding nasalizing article can produce a ndliged. That is an incoming effect on dliged, separate from the outgoing marker shown here. Long -a plurals can also be followed by lenition.',
 'cell': 'Cell / ceill / cill / cille are different singular case forms of one word. The plural rows are regular a-stem model forms; the active contrast here remains the singular vowel alternation.',
 'ben': 'The irregular stem shapes do not cancel the feminine case effects. Mna\u00ed/mn\u00e1i spelling varies; this course retains mn\u00e1i. Bein is the older accusative variant.',
 'ceile': 'C\u00e9li and c\u00e9liu also appear as c\u00e9ili and c\u00e9iliu in other conventions. Accusative singular is c\u00e9ile, not c\u00e9liu.',
 'cride': 'The short nominative/accusative plural cride has [L], while singular cride has [N]. Genitive singular cridi is not a second nominative plural.',
 'ban_adj': 'These are the adjective\u2019s unprefixed forms and their outgoing effects. Initial mutation received from the preceding noun is shown in the phrase examples, not built into the citation form.',
 'becc_adj': 'The adjective\u2019s initial mutation comes from the preceding noun. The markers here describe what this adjective form can do to a following closely connected word.',
}
KEY = ('**Following-word effects:** [L] lenition; [N] nasalization; '
       '[H] historical aspiration/gemination; [0] no regular L/N/H effect prescribed here. '
       'The marker belongs to the form before it and describes the next closely connected word, '
       'not a suffix. Effects need not be visible in spelling; phonological and syntactic restrictions still apply. '
       'Prepositional = the case often called dative. The vocative particle a itself lenites the noun; '
       'a marker at the end of the vocative phrase describes what follows the noun.')
SOURCE = ('*Effects cross-check:* [UT Austin, Old Irish Online, \u00a76](https://lrc.la.utexas.edu/eieol/iriol/20), '
          '[nominal paradigms, \u00a713](https://lrc.la.utexas.edu/eieol/iriol/30); '
          'the lesson\u2019s Stifter section remains its curricular reference. '
          'These are teaching paradigms, not a claim that every model form is separately attested.')


def table(title, headers, rows, note=''):
    assert headers and all(len(row) == len(headers) for row in rows)
    assert all(str(h).strip() for h in headers)
    out = [f'### {title}', '', '| ' + ' | '.join(headers) + ' |',
           '|' + '|'.join('---' for _ in headers) + '|']
    out += ['| ' + ' | '.join(str(v) for v in row) + ' |' for row in rows]
    if note:
        out += ['', note]
    return '\n'.join(out) + '\n'


def marked(form, effect):
    # A form containing variant-specific markers must keep those markers separate.
    if '[' in form:
        import re
        return re.sub(r'([^/\[\]]+?)\s*\[([LNH0])\]',
                      lambda m: '**' + m[1].strip() + '** [' + m[2] + ']', form)
    return f'**{form}** [{effect}]'


def noun(key):
    meaning, desc, cls, forms = NOUNS[key]
    lemma = forms[0][0]
    rows = [(case, marked(sg, effects[0]), marked(pl, effects[1]))
            for case, (sg, pl), effects in zip(CASES, forms, EFFECTS[cls])]
    return table(f'*{lemma}* \u2018{meaning}\u2019 \u00b7 {desc}',
                 ['Case', 'Singular form + effect', 'Plural form + effect'], rows,
                 NOTES.get(key, ''))


def article(gender):
    sg = {'masculine': ['in / int [0]', 'in / ind [L]', '-(s)in(d) [L]', 'in [N]'],
          'feminine': ['in / ind / int [L]', 'inna [H]', '-(s)in(d) [L]', 'in [N]'],
          'neuter': ['a [N]', 'in / ind [L]', '-(s)in(d) [L]', 'a [N]']}[gender]
    pl = ['in / ind [L]' if gender == 'masculine' else 'inna [H]',
          'inna [N]', '-(s)naib [0]', 'inna [H]']
    return table(f'Definite article \u00b7 {gender}',
                 ['Case', 'Singular article + effect', 'Plural article + effect'],
                 [(c, s, p) for c, s, p in zip(CASES[:4], sg, pl)],
                 'Here each marker describes **article \u2192 noun**, not noun \u2192 adjective. '
                 'Forms in -(s)in(d) and -(s)naib combine with a preceding preposition. '
                 'The choice in/ind/int also depends on the next sound; [0] is not a denial of article allomorphy. '
                 'There is no definite article in the vocative.')

VERBS = {
 'caraid': ('loves', ['caraim(m)', 'carai', 'caraid', 'carmai', 'carthae', 'carait'],
             ['n\u00ed\u00b7caraim(m)', 'n\u00ed\u00b7carai', 'n\u00ed\u00b7cara', 'n\u00ed\u00b7caram', 'n\u00ed\u00b7caraid', 'n\u00ed\u00b7carat']),
 'leicid': ('leaves, permits', ['leiciu / leicim(m)', 'leici', 'leicid', 'leicmi', 'leicthe', 'leicit'],
            ['n\u00ed\u00b7leiciu / n\u00ed\u00b7leicim(m)', 'n\u00ed\u00b7leici', 'n\u00ed\u00b7leici', 'n\u00ed\u00b7leicem', 'n\u00ed\u00b7leicid', 'n\u00ed\u00b7leicet']),
}
PERSONS = ['1st singular', '2nd singular', '3rd singular', '1st plural', '2nd plural', '3rd plural']
VERB_NOTE = ('These are **person/number**, not case, paradigms. Do not transfer noun-case L/N/H labels '
             'to finite-verb endings. The negative particle n\u00ed selects the conjunct series; '
             'the outgoing mutation of a nominal case is a separate grammatical question.')


def verb(key, select=None):
    meaning, absolute, conjunct = VERBS[key]
    indexes = range(6) if select is None else select
    return table(f'*{key}* \u2018{meaning}\u2019 \u00b7 present indicative',
                 ['Person / number', 'Absolute form', 'Conjunct form after n\u00ed'],
                 [(PERSONS[i], f'**{absolute[i]}**', f'**{conjunct[i]}**') for i in indexes], VERB_NOTE)


def phrase_table(title, rows, note=''):
    return table(title, ['Case / number', 'Phrase', 'Effect to notice'], rows, note)


def section(day):
    # All 28 entries are deliberate; absent days must never silently get a default.
    parts = []
    if day in (1,2,3,4,5,6,7,8,9,10,11,15,16,17,18,19,20,21,25,27,28):
        parts.append(KEY)
    if day in (1,2): parts += [noun('ech')]
    elif day == 3: parts += [noun('fer'), noun('ech')]
    elif day in (4,5): parts += [noun('cenn')]
    elif day == 6: parts += [noun('macc'), noun('cenn')]
    elif day == 7:
        parts += [table('Latin *equus* \u2018horse\u2019', ['Case','Singular form','Plural form'],
                        [('Nominative','**equus**','**equ\u012b**'),('Accusative','**equum**','**equ\u014ds**')],
                        'Irish mutation labels do not apply to this Latin comparison.'),
                  table('Sanskrit *a\u015bva-* \u2018horse\u2019', ['Case','Singular form','Plural form'],
                        [('Nominative','**a\u015bva\u1e25**','**a\u015bv\u0101\u1e25**'),('Accusative','**a\u015bvam**','**a\u015bv\u0101n**')],
                        'Sanskrit sandhi is not the Irish L/N/H system.'), noun('ech')]
    elif day in (8,9):
        parts += [article('masculine'), noun('fer'),
                  phrase_table('Article \u2192 noun \u2192 adjective', [
                   ('Nominative singular','**in fer**','in [0] \u2192 fer; fer [0] \u2192 a following adjective'),
                   ('Genitive singular','**ind fir**','ind [L] \u2192 fir; fir [L] \u2192 a following adjective'),
                   ('Accusative plural','**inna firu**','inna [H] \u2192 firu; firu [H] \u2192 a following adjective')],
                   'The two arrows show different grammatical boundaries. They must not be collapsed into a single phrase-wide marker.')]
    elif day == 10:
        parts += [article('neuter'), noun('cenn'), noun('dliged'),
                  '**Worked contrast:** a [N] + dliged gives **a ndliged**. The neuter noun dliged [N] '
                  'then has its own outgoing effect in the nominative/accusative singular. '
                  'The same article before cenn does not normally write an extra n: **a cenn**.']
    elif day == 11:
        parts += [noun('catt'), noun('ban_adj'),
                  phrase_table('Agreement and incoming mutation', [
                   ('Nominative singular','**in catt b\u00e1n**','catt [0] \u2192 b\u00e1n'),
                   ('Genitive singular','**in chaitt b\u00e1in**','caitt [L] \u2192 b\u00e1in; lenition of b is often unwritten'),
                   ('Accusative singular','**in catt mb\u00e1n**','catt [N] \u2192 mb\u00e1n'),
                   ('Nominative plural','**in chaitt b\u00e1in**','caitt [L] \u2192 b\u00e1in'),
                   ('Accusative plural','**inna cattu b\u00e1nu**','cattu [H] \u2192 b\u00e1nu')])]
    elif day in (12,13): parts += [verb('caraid')]
    elif day == 14:
        parts += [verb('caraid'),
                  table('*glanaid* \u2018cleans\u2019 \u00b7 selected present forms',
                        ['Person / number','Absolute form','Conjunct form after n\u00ed'],
                        [('2nd plural','**glantae**','**n\u00ed\u00b7glanaid**')], VERB_NOTE)]
    elif day == 15: parts += [noun('tuath')]
    elif day == 16: parts += [noun('tuath'),noun('cell')]
    elif day == 17: parts += [noun('ben')]
    elif day == 18: parts += [article('feminine'),noun('ingen')]
    elif day == 19:
        for prep, meaning, singular, plural in [
            ('do','to, for','don / dond','donaib'),('i','in','isin / isind','isnaib'),
            ('fo','under','fon / fond','fonaib')]:
            parts += [table(f'*{prep}* \u2018{meaning}\u2019 + definite article',
                            ['Case','Singular fused form + effect','Plural fused form + effect'],
                            [('Prepositional',marked(singular,'L'),marked(plural,'0'))])]
        parts += ['The badges describe the fused form\u2019s effect on the **following noun**. '
                  'Do not substitute the mutation of the bare preposition (for example i [N]) '
                  'for the mutation of the preposition-plus-article construction.']
    elif day == 20:
        parts += [noun('ingen'),noun('becc_adj'),
                  phrase_table('Feminine agreement in context', [
                   ('Nominative singular','**ind ingen becc**','ingen [L] \u2192 becc'),
                   ('Genitive singular','**inna ingine bicce**','ingine [H] \u2192 bicce'),
                   ('Prepositional singular','**dond ingin bicc**','ingin [L] \u2192 bicc'),
                   ('Accusative singular','**in n-ingin mbicc**','ingin [N] \u2192 mbicc'),
                   ('Nominative / accusative plural','**inna ingena becca**','ingena [H] \u2192 becca')],
                   'Case agreement selects becc/bicc/bicce/becca. The preceding noun separately controls initial mutation; not all such changes are written.')]
    elif day == 21:
        parts += [noun('tuath'),
                  table('Latin *rosa* \u2018rose\u2019 \u00b7 comparison only', ['Case','Singular form','Plural form'],
                        [('Nominative','**rosa**','**rosae**'),('Genitive','**rosae**','**ros\u0101rum**'),
                         ('Dative','**rosae**','**ros\u012bs**'),('Accusative','**rosam**','**ros\u0101s**'),
                         ('Vocative','**rosa**','**rosae**')],
                        'Rosa and tuath are not cognate words. This compares the inherited stem class. '
                        'The Latin dative is not identical in syntax to the Irish prepositional case; Irish mutation labels do not apply to Latin.')]
    elif day == 22: parts += [verb('leicid')]
    elif day == 23:
        parts += [verb('leicid'),
                  table('W2b *roithid* \u2018makes run\u2019 \u00b7 selected model forms',
                        ['Person / number','Absolute form','Conjunct form after n\u00ed'],
                        [('3rd singular','**roithid**','**n\u00ed\u00b7roithi**'),
                         ('3rd plural','**roithit**','**n\u00ed\u00b7roithet**')], VERB_NOTE),
                  table('W2b *sluindid* \u2018mentions, declares\u2019 \u00b7 citation only',
                        ['Use','Form'],[('Citation: 3rd singular absolute','**sluindid**')],
                        'This is a class-identification example, not a claim to supply its full paradigm.')]
    elif day == 24: parts += [verb('caraid'),verb('leicid', [2,5])]
    elif day == 25:
        parts += [table('Unstressed possessives \u00b7 effect on the possessed noun',
                        ['Possessor','Possessive form + effect','Example phrase'],[
                         ('My','**mo** [L]','**mo chenn**'),('Your (singular)','**do** [L]','**do chenn**'),
                         ('His','**a** [L]','**a chenn**'),('Her','**a** [H]','**a cenn**'),
                         ('Their','**a** [N]','**a cenn**; compare visibly nasalized **a ndliged** \u2018their law\u2019')],
                        'These pronouns distinguish possessors, not noun cases. Here L/N/H describe **possessive \u2192 noun**. '
                        'H is the historical aspiration/gemination class, not simply a synonym for \u2018no mutation\u2019.')]
    elif day == 26:
        parts += [
            '### Normalized classroom excerpt\n\n**Am gaeth i mmuir,**  \n**am tond trethan.**\n\n'
            '\u2018I am wind upon the sea; I am a wave of the ocean.\u2019\n',
            table('Read the construction', ['Element / form','Function','Sound relationship'],[
             ('**am**','1st-person copula: \u2018I am\u2019','A verbal form, not a case paradigm'),
             ('**gaeth**','Predicate noun: \u2018wind\u2019','No noun-case effect is inferred solely from its place in the quotation'),
             ('**i mmuir**','Prepositional phrase: \u2018in/upon the sea\u2019','i [N] \u2192 muir; nasalization is represented by mm'),
             ('**tond**','Predicate noun: \u2018wave\u2019','The following trethan is a genitive modifier')],
             'This is a reading key, not a declension table. The excerpt is normalized, not a diplomatic transcription; '
             'do not infer a complete paradigm from a single quoted occurrence.')]
    elif day == 27: parts += [noun('ceile'),noun('fer')]
    elif day == 28: parts += [noun('cride')]
    else: raise ValueError(f'No reviewed content for day {day}')
    if any('[L]' in p or '[N]' in p or '[H]' in p for p in parts):
        parts.append(SOURCE)
    return '\n\n'.join(parts).strip() + '\n'

SECTIONS = {day: section(day) for day in range(1,29)}
