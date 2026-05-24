# Accessibility & Legibility Checks

A figure that cannot be read at the size the audience will see it is broken, no matter how stylish. This pass is small but firm. Run it on every figure.

---

## 1. Final-output legibility

Ask: at what size will the audience actually see this figure?

- **Print at one column** (most ACS manuscripts): atom labels must clear ~6 pt; bond lines must clear 0.5 pt.
- **Print at two columns**: atom labels must clear ~7 pt.
- **Projected slide** (group meeting / talk): atom labels must clear roughly 18 pt at the *original* scale, accounting for resize-to-fit on the slide.
- **Poster**: atom labels must clear roughly 24 pt at original scale because posters are read from ~3 ft.
- **Screen-only (PDF on monitor)**: more forgiving but still no labels under 5 pt at zoom-to-fit.

If the figure was drawn at slide scale (`slides-bms`, 18 pt labels) and is being placed in a manuscript that will print single-column, the labels will compress to ~5–6 pt — a flag, not necessarily a fail, but a recommendation to redraw at publication scale.

## 2. Color contrast

For each colored element, ask: does it have enough contrast with the background and with surrounding elements?

- Black on white: always fine.
- **Yellow on white**: never fine. Flag immediately.
- **Light gray on white** (sometimes used to "de-emphasize" a structure): often fails contrast. Better to use a dashed outline or a labeled bracket.
- **Red on dark blue** (the in-house palette overlay accidents): poor contrast. The two emphasis colors should not be directly adjacent.
- **Bright Blue (RGB 0,0,225) on Dark Blue (RGB 0,30,98)**: very poor; nearly the same hue. Flag if seen on the same structure.
- **Color-only distinction**: if the only thing distinguishing two compounds in a figure is color (e.g., red structure vs. blue structure with no labels), the figure fails for color-blind readers and grayscale reproduction. Recommend adding a text label or different stereobond.

## 3. Grayscale survival

Mentally convert the figure to grayscale. For figures destined for print where color is expensive (some ACS journals), this is a real test, not a hypothetical:

- Do colored bonds disappear into the structure?
- Do red emphasis labels become invisible?
- Are there places where two differently-colored elements collapse to the same gray?

If yes to any: the figure is not grayscale-safe. Recommend either (a) using a non-color emphasis (bold, dashed, or a callout box) or (b) testing the actual grayscale conversion before submission.

## 4. Pixelation / raster artifacts

Visible pixelation is the tell of a bitmap-pasted figure rather than a vector paste. Causes:

- The figure was screenshotted, not copied from ChemDraw.
- The figure was scaled non-uniformly after pasting (broken aspect ratio).
- The figure was inserted at one resolution and then forced to a different size in PowerPoint/Word.

What to look for:

- Aromatic ring vertices that show staircase pixels.
- Anti-aliasing fringes around text labels.
- Edges that look soft compared to the rest of the document.
- A figure noticeably blurrier than its caption text.

Per the group style, the fix is to go back to the ChemDraw source and repaste, or to save as TIFF and insert the TIFF.

## 5. Text-on-text and label-on-bond conflicts

- Atom labels overlapping bonds drawn from neighboring atoms.
- Compound numbers crossing into adjacent structures.
- Reagent text on top of arrow shafts (acceptable when intended; flag when it looks crowded).
- Yields/conditions running into the next step's reagents.

Each of these makes the figure measurably harder to parse. Severity is usually Minor, but when it obscures a stereobond or a critical atom label, it can become Major.

## 6. Aspect ratio integrity

If a figure has been resized non-uniformly:

- Hexagons no longer have 120° angles internally.
- Circles in catalytic-cycle drawings become ovals.
- Text becomes condensed or expanded.

This is a Critical issue if visible. The figure must be redrawn at the correct aspect ratio.

## 7. Embedded font legibility

ChemDraw renders Helvetica at the size you specify. But if a figure was screenshotted and re-embedded as a bitmap, the Helvetica text becomes raster pixels at whatever resolution the screenshot was taken. If the resolution was too low, the text loses crispness and the chemistry becomes harder to read.

Flag any figure where text legibility is visibly worse than the document's surrounding caption text.

## 8. Color-blind safe palette check

Roughly 8% of men have a red-green color vision deficiency. Check:

- Is *any* meaningful distinction in this figure conveyed only by red vs. green? (Flag.)
- Is the in-house Red (213,0,50) being used near anything green? (Flag.)
- Is there at least one *non-color* visual difference between elements that need to be distinguished? (Bold, dashed, label, position.)

## 9. Background interaction

For talk slides specifically: a figure designed for white-background printing may render poorly on a colored slide background.

- White-filled atom labels become invisible on a white slide background but visible on a dark slide background, and vice versa.
- The the slide-deck template may have a colored background — verify atom labels do not become unreadable on it. Flag only if the figure was clearly imported from a different background context.

## 10. Scaling chain failures

A common failure mode: a figure was drawn at 100% of the publication template, then placed in a slide deck and resized to fit, then exported to PDF. At each step, font sizes and bond widths can become inconsistent. The visual symptoms:

- One scheme's atom labels visibly larger or smaller than another's.
- Bond widths visibly thicker or thinner across schemes that should be uniform.
- Compound-number sizes different between schemes.

This is the leading consistency issue across multi-figure documents. Always check it as part of Stage 6 (document-level pass).

---

## How to write accessibility findings in the output

Group accessibility issues with the per-figure severity rating. Use plain language:

- *"Atom labels in Scheme 4 will compress below ~6 pt at single-column print scale — recommend redrawing at the publication-scale template."*
- *"Compound 7 in Scheme 5 is highlighted in yellow. The yellow does not survive print, photocopy, or grayscale — change to red or a structural emphasis (bold bonds, callout box)."*
- *"The two products in Scheme 3 are distinguished only by color (red vs. blue). Recommend adding compound numbers or text labels so the distinction survives grayscale reproduction."*

Accessibility findings should land in the per-figure severity table, not as a separate section, unless the user has asked for an accessibility-only pass.
