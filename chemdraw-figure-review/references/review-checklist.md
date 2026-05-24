# Per-Figure Review Checklist

Walk this checklist for **every figure**, in order. Don't skip an item because it usually passes — your purpose is to be the second pair of eyes that catches what familiarity has worn smooth.

For each item, record one of: **Pass**, **Fail**, **N/A** (item doesn't apply to this figure type), or **?** (cannot be determined from rendered output). For Fail and ?, write a one-line note.

---

## A. Identification (record before reviewing)

1. Location (page / slide / scheme number).
2. Figure type (single structure / scheme / retrosynthesis / mechanism / table / cover graphic).
3. Caption or title text.
4. Compound numbers visible in this figure.

## B. Bond and structure rendering

5. Bond lengths look uniform across the figure.
6. Bond lengths are consistent with bond lengths in *other* figures in the same document. (Drift here often means a figure was pasted from a different template.)
7. Line widths are uniform; no figure has visibly thicker or thinner default lines than its neighbors.
8. Wedge bonds drawn with the wedge tool (solid triangle, narrow at one end), not the bold-bond tool.
9. Hash bonds drawn with the hash tool (parallel slashes), not the dashed-bond tool.
10. Wedge/hash counts at chiral centers look plausible (one wedge plus one hash from the same center is acceptable only at a real chiral center).
11. Aromatic rings drawn as recognizable rings, not stretched polygons.
12. Double-bond orientation is correct — both lines of a `C=C` parallel and not flipped to the outside of a ring inappropriately.
13. No dangling bonds — every bond ends in either an atom label or an implicit-carbon vertex.
14. No accidental free valences (a vertex where a bond is missing).

## C. Atom labels and text

15. Atom font is Helvetica (look for serifs as a tell — Helvetica has none).
16. Atom-label size matches the rest of the figure and the document template.
17. Compound numbers are *italicized* and roughly **2 pt larger** than atom labels.
18. Compound numbers are positioned consistently relative to their structures (below-center is the usual placement).
19. Subscripts and superscripts render correctly (no `H2O` written as `H2O` baseline; no `R^1` written `R1`).
20. Greek letters (α, β, γ, δ) use the Symbol font, not the look-alike letters.
21. Special characters render correctly: `°`, `–` (en dash), `·` (small bullet), `Å`.
22. No atom label is partially covered by a bond.

## D. Reagents, conditions, yields

23. Reagent equivalents formatted as `(1.1 equiv)` — no `eq.`, no `eq`, no period.
24. Solvent + temperature formatted as `solvent, NN °C` with one space before `°C`.
25. Yields formatted as `NN% yield` — no space before `%`, *yield* spelled out.
26. dr / ee follow group convention (`X : X dr` with spaces, `92% ee`).
27. "Step count" labeled as `# steps` or `N steps`.
28. Reagents stacked clearly above and below the arrow, not crowded into one line.
29. Reagent abbreviations are ACS-standard: `aq`, `Py` (or `py` for ligand), `min`, `h`. Spelled-out items (yield, room temperature, BORSM) are spelled out.

## E. Arrows

30. Each arrow's *type* matches its *meaning* (reaction / dashed / retrosynthetic / conceptual / resonance / equilibrium / curved / fishhook). Cross-reference `references/house-style.md` §5.
31. Reaction arrows are the standard solid arrow, not the bold variant.
32. Curved arrows in mechanisms terminate at the right place (atom, bond center, or lone pair) — flag if a curved arrow ends in empty space, but do not adjudicate the mechanism.
33. Fishhook arrows used for single-electron movement, never for two-electron movement.
34. Resonance arrows used only between resonance structures, not between tautomers.
35. Equilibrium arrows used between tautomers and equilibrating systems.
36. Arrow length and weight visually consistent across the figure.

## F. Layout and reading order

37. The figure reads **left to right**.
38. No "railroad" wrap that reverses direction within a row.
39. Reactants on the left of an arrow, products on the right.
40. Spacing between substrate / arrow / product is roughly equal across the scheme.
41. Compound-number positions don't collide with bonds or arrows from neighboring structures.
42. The natural product (if applicable in talk slides) is in the top-right corner, scaled appropriately.

## G. Color

43. Color is used for *emphasis*, not decoration. (A figure where every structure is colored is suspicious.)
44. Colors used are the in-house palette: Dark Blue (RGB 0,30,98), Red (RGB 213,0,50), Bright Blue (RGB 0,0,225). Black is always acceptable.
45. No yellow.
46. No red+green pairing for color-coded distinction.
47. Colored bonds drawn at the slightly heavier line width (between standard and bold) so the color reads.

## H. Image quality (if the figure is an inserted bitmap)

48. No visible pixelation along curves.
49. No anti-aliasing fringes around text.
50. Aspect ratio looks correct (no horizontal or vertical stretching).
51. Edges and lines have the same crispness as the surrounding text.

## I. Consistency with the rest of the document

(These items only fully resolve in the document-level pass — Stage 6 — but flag obvious cases per figure.)

52. Compound numbers in this figure are not duplicated in another figure with a different structure.
53. Reagent abbreviations match those used elsewhere in the document.
54. Style (font, bond length, arrow style) matches neighboring figures.
55. If the figure is part of a sequence (e.g., Scheme 3 → Scheme 4), flow makes visual sense.

---

## Outcome of the per-figure pass

After running the checklist, you should be able to answer two things:

- What **severity** does this figure earn? (Critical / Major / Minor / Cosmetic / Ready)
- Which checklist items are the *root cause* of the severity rating? (Don't list every Fail in the headline — group them.)

If you have more than ~6 Fails on a single figure, the figure is almost certainly Major or worse. If you have a Critical chemistry-presentation flag (item 13–14, 30, or anything from `references/chemistry-flags.md`), one Critical pulls the whole figure to Major revisions or worse, regardless of polish elsewhere.
