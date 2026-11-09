# Revise Shorts v10 proofreading log

These counts come from `src/proof.py`. The before column is v9, the questions.json in git HEAD (2,469 questions). The after column is v10 (2,498 questions).

| Check | v9 | v10 | Action |
|---|---|---|---|
| Empty explanation | 261 | 0 | Wrote explanations: 152 in chemistry_more.txt and the rest in the generator templates (chemistry tables and mechanisms, maths statistics and sequences, physics GPE and resistors) |
| Short explanation (<25 chars) | 151 | 121 | Rewrote 30 explanations; the rest are formula hints, e.g. "V = E − Ir." |
| Unit not recognised or inconsistent | 81 | 0 | Normalised 83 units in the build (m/s → m s⁻¹, y → years …) |
| Duplicate question | 1 | 0 | Replaced the duplicate Cu question with the Cu²⁺ configuration |
| Off-spec term | 1 (+1 found by hand) | 0 | Removed 2,4-DNPH from two AQA questions; replaced a kinetic-energy question in 9MA0 maths (not on the spec) with a km/h distance question |
| Rounding or s.f. answer mismatch | 1 | 0 | The equator centripetal acceleration answer is now 33.8 mm s⁻² (3 s.f.), not 34 |
| Spelling | 3 | 0 | Fixed "delocalized" (duplicate keyword), "phenylketone" → aromatic ketone (phenylethanone), and "a aldehyde" → "an aldehyde" |
| MC duplicate or missing options, match/order clashes, KaTeX in questions, unbalanced $ in notes | 0 | 0 | No issues |

## Other accuracy fixes
- c-1-9: the rate-constant units now follow from the overall order; the old wording was "(units depend on order)".
- Notes: removed an SN1 mention from AQA-only notes, corrected the hydrolysis wording, and corrected a drag worked example to 9.0 J.

## Manual review
I checked these against the answers:
- All hand-written questions in physics.txt, physics_more.txt, maths.txt, maths_more.txt and chemistry.txt, about 1,000 in total.
- A random sample of 45 generated questions.

No further errors were found.

## Keyword marking
- Added 637 synonyms and alternative phrasings to 125 written questions, e.g. speed/rate, same/equal, bounce/reflect, "doesn't represent"/"not representative".
- Keywords shorter than 4 characters now need a whole-word match, so "ea" no longer matches inside "reaction".
- Curly apostrophes and "n't" are normalised.

Test set of 33 answers:

| | v9 | v10 |
|---|---|---|
| Correct paraphrases accepted | 17/23 | 23/23 |
| Wrong answers rejected | 10/10 | 10/10 |
