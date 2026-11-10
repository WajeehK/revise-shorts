# Revise Shorts v11 hand-review log

Every question in the bank (2,639 in v11) was reviewed by hand, file by file. For each question I checked:

- the answer, by working it out again
- the distractors
- the units, significant figures and tolerance
- the wording
- that it fits the spec point and the tier

One-line explanations were rewritten as worked explanations. For the generator files (`gen_*.py`) each template was reviewed and rewritten, so every instance it produces is covered. Generated counts are the subject total minus the hand-written files.

| File | Questions | Errors fixed | Explanations expanded |
|---|---|---|---|
| chemistry.txt | 162 | 0 | 160 |
| chemistry_more.txt | 421 | 1 (NaBH₄ stoichiometry question reworded: each BH₄⁻ gives 4 hydride ions) | 263 |
| chemistry_figs.txt | 9 | 0 | 3 |
| chemistry_cov.txt (new in v11) | 33 | 1 duplicate titration question removed | all written in full |
| gen_chemistry.py | 484 generated | 3 (butanone ¹H NMR peaks 4 → 3; isotope % explanation hard-coded "63"; complex-shape explanation wrong for Ag⁺/Pt) | all templates, with worked numbers |
| physics.txt | 121 | 0 | 117 |
| physics_more.txt | 277 | 0 | 272 |
| physics_figs.txt | 13 | 0 | 8 |
| physics_cov.txt (new in v11) | 70 | 0 | all written in full |
| gen_physics.py | 427 generated | 6 (photoelectric KEmax could be negative; grating highest order wrong when d/λ is a whole number; hump-back bridge could give a negative reaction; electron-deflection values hit the plates; U-235 half-life seconds inconsistent with the stated 1 y = 3.15 × 10⁷ s; fluid-pressure wording) | all templates, with worked numbers |
| maths.txt | 101 | 0 | 92 |
| maths_more.txt | 232 | 2 (random-number sampling question had only 3 valid numbers for a "4th item"; unclear wording "needs no sampling frame strata") | 228 |
| maths_figs.txt | 8 | 0 | 6 |
| maths_cov.txt (new in v11) | 37 | 0 | all written in full |
| gen_maths.py | 244 generated | 4 (max of 1/(10 − R sin(x + α)) undefined when R = 13; perpendicular line shown as −0.333333x; "y = 1x + 0" in a question; ASCII minus signs and "1x" tidied in lib.py) | all templates, with worked numbers |

## Per subject

| Subject | Questions reviewed | Errors fixed | Notes |
|---|---|---|---|
| Chemistry (AQA 7405) | 1,109 | 5 (4 errors and 1 duplicate) | 33 new spec-coverage questions |
| Physics (OCR A H556) | 908 | 6 | 70 new spec-coverage questions |
| Maths (Edexcel 9MA0) | 622 | 6 | 37 new spec-coverage questions |
| **Total** | **2,639** | **17** | |

## Automatic checks after the review

- `src/proof.py` flags 0 issues. Short explanations went from 121 to 0, and spelling is clean.
- `src/coverage.py` reports 1,064/1,064 spec points covered by notes and questions (see `COVERAGE.md`).
- Every numeric question's `chk` expression is re-evaluated against its stored answer at build time.

---

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
