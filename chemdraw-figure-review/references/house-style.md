# House ChemDraw Style — Example Defaults

> **READ THIS FIRST — CUSTOMIZATION REQUIRED.**
> The values in this file are a **worked example** drawn from one chemistry
> group's ChemDraw template. They are deliberately specific so that the skill
> has something to check against, but they are not universal. Before using the
> skill for real review work:
>
> 1. Replace the bond-length, font, color-palette, and arrow-catalogue values
>    below with **your group's actual settings**.
> 2. Update the template names (`slides-bms`, `corey group sett`) if your
>    group uses different ones.
> 3. Adjust the color RGBs to your house palette — or remove the palette
>    constraint entirely if your group does not use one.
>
> The *structure* of the file (which categories of settings the skill checks
> for) is reusable. The *values* are example-only.

This file captures one group's house style as a worked example, distilled from:

- An internal slide-deck template.
- The widely-circulated "Ultimate ChemDraw Guide" (originally the Stoltz Group ChemDraw and PowerPoint Handout) — used as the canonical template explanation, particularly the `slides-bms` settings for talks and `corey group sett` settings for publications/proposals.
- The IUPAC 2008 *Graphical representation standards for chemical structure diagrams* (Brecher) — used as the higher-level arbiter when the template is silent.

When inspecting a rendered figure, you will not see exact inch values for bond length or exact point sizes for atom labels. Your job is to compare what is visible against the *appearance* these settings produce, and flag what looks off. Use the values below as the reference, not as something you can measure.

## 1. Document-purpose template

| Purpose | Template name | Bond length defaults |
|---|---|---|
| Group meeting / research talk / poster | `slides-bms` | Larger (≈0.4167″ at 100% scale) |
| Publication, proposal, formal report | `corey group sett` | Smaller (≈0.2778″ at 100% scale) |

A figure should never mix templates. If a deck has one scheme that visibly looks like a publication-style scheme dropped into a talk-style deck, that is a Major issue.

## 2. ChemDraw object settings (for reference, not measurement)

### `slides-bms` template (research talks, posters, group meetings)

| Scale | Fixed Length | Bold Width | Line Width | Margin Width | Hash Spacing | Font Size (Helvetica) |
|---|---|---|---|---|---|---|
| 100 | 0.4167 | 0.0556 | 0.0222 | 0.0278 | 0.0701 | 18 |
| 80 | 0.3334 | 0.0445 | 0.0178 | 0.0222 | 0.0561 | 14 |
| 75 | 0.3125 | 0.0417 | 0.0167 | 0.0209 | 0.0526 | 14 |
| 70 | 0.2917 | 0.0389 | 0.0155 | 0.0195 | 0.0491 | 13 |
| 50 | 0.2084 | 0.0278 | 0.0111 | 0.0139 | 0.0351 | 9 |

### `corey group sett` template (publications, proposals)

| Scale | Fixed Length | Bold Width | Line Width | Margin Width | Hash Spacing | Font Size (Helvetica) |
|---|---|---|---|---|---|---|
| 125 | 0.3473 | 0.0521 | 0.0260 | 0.0348 | 0.0521 | 15 |
| 100 | 0.2778 | 0.0417 | 0.0208 | 0.0278 | 0.0417 | 12 |
| 80 | 0.2222 | 0.0334 | 0.0166 | 0.0222 | 0.0334 | 10 |
| 70 | 0.1945 | 0.0292 | 0.0146 | 0.0195 | 0.0292 | 9 |

**Resizing rule.** Never use ChemDraw's `Scale` function. Manually scale all five Object Settings (Fixed Length, Bold Width, Line Width, Margin Width, Hash Spacing) plus font size, all by the same factor, all to whole-number font sizes. A figure with one font size noticeably out of step with its bond length almost certainly violated this rule.

## 3. Fonts and font sizes

### `slides-bms` — research talks and posters

| Element | Font | Size | Style |
|---|---|---|---|
| Slide title | Times | 24–30 pt | italic, **not bold** |
| Reagents over a reaction arrow | Helvetica | 16 pt | regular |
| Atom labels | Helvetica | 18 pt | regular |
| Compound numbers (structure labels) | Helvetica | 18 pt | italic |
| References | Helvetica | 16 pt | ACS format (see §7) |

### `corey group sett` — publications and proposals

| Element | Font | Size | Style |
|---|---|---|---|
| Title / caption | Word, **not** ChemDraw | — | journal style |
| Reagents over a reaction arrow | Helvetica | 12 pt | regular |
| Atom labels | Helvetica | 12 pt | regular |
| Compound numbers | Helvetica | 14 pt | italic |
| References | Word document, ACS format | — | — |

### Slide-deck template overrides (example)

An example slide-deck template specifies the following on its instructions page:

- Text line spacing = 0.25 in
- Atom font = 18 pt
- General text font = 16 pt
- Atom number labels = 14 pt
- Activity / biological-activity caption = 14 pt italic
- Natural-product name = 18 pt **bold italic**
- Yields = 16 pt italic
- Mechanism / explanatory text = 14 pt
- Degree symbol typed as Option/Shift/8 (not the Symbol-font glyph)

**Universal rule.** Compound labels are *always italicized*, and *always 2 pt larger* than the default atom-label font in that template. If the atom labels are 18 pt, compound numbers are 20 pt italic. This rule travels with the structure when it is scaled.

## 4. Color palette (example — customize for your group)

Three approved colors. Anything else is a flag.

| Name | RGB | Use |
|---|---|---|
| Dark Blue | 0, 30, 98 | Default colored emphasis (yields, named reaction labels) |
| Red | 213, 0, 50 | Specific call-out (atom-numbering highlights, key callouts) |
| Bright Blue | 0, 0, 225 | Conceptual emphasis (e.g., named-reaction labels in mechanism panels) |

### Universal color rules (Stoltz handout, IUPAC GR-0.5)

- Black on white is the default. Color is used for *emphasis*, not decoration.
- **Avoid yellow at all costs.** It does not project, does not photocopy, and dies in PDF.
- **Avoid red+green combinations.** Roughly 10% of male readers are red-green colorblind.
- Default ChemDraw green is poor on a projector — use a dark green (e.g., "clover") only if green is needed.
- A bond highlighted in color should be drawn at line width ≈0.0389″ (between standard line width 0.0222″ and bold width 0.0556″ in `slides-bms`), so the color reads.
- Red and dark blue are the safest emphasis colors.

## 5. Arrow catalogue

Each arrow type has a *meaning*. Wrong arrow = wrong meaning. The Stoltz handout's catalogue is the canonical reference; reproduced here for quick lookup.

| Arrow | Meaning | Visual cue | Common misuse |
|---|---|---|---|
| Reaction arrow | One molecule converts to another | Smallest solid arrow, single line | Using the bold reaction arrow — never use it |
| Dashed reaction arrow | A transformation that has *not yet* been carried out | Dashed shaft, normal head | Used to indicate hypothetical chemistry |
| Retrosynthetic arrow | A retrosynthetic disconnection | Open at one end (small open-ended ChemDraw arrow) | Drawn the wrong direction; or used as a normal reaction arrow |
| Conceptual arrow | A conceptual progression with forward implication | Hollow forward-pointing arrow | Confused with retrosynthetic arrow |
| Resonance arrow | Two resonance structures of the *same* molecule | Double-headed straight arrow | Used between tautomers — tautomers get equilibrium arrows, not resonance |
| Equilibrium arrows | Equilibrating species or sets of reagents | Two parallel arrows (lengths can differ for shifted equilibrium) | Used as a stylistic alternative to a reaction arrow |
| Curved arrow | Catalytic-cycle progression OR mechanism electron-pair movement | Single curved line with full head | Drawn for radicals (use fishhook) |
| Fishhook arrow | Single-electron movement | Curved with half-head | Used for two-electron movement |

**Direction rule.** Arrows progress *left to right* in a scheme. Avoid "railroad" schemes that wrap right-to-left. If the page forces wrapping, end at the right edge and resume at the left of the next row — never reverse direction within a row.

## 6. Reagent / yield / condition formatting

| Element | Correct | Incorrect |
|---|---|---|
| Equivalents | `(1.1 equiv)` | `(1.1 eq)`, `(1.1 eq.)` |
| Stoichiometric quantity | `(2.0 equiv)` | `(2 eq)` |
| Solvent + temperature | `PhCH3, 80 °C` (one space between number and °C) | `PhCH3, 80°C` |
| Yield | `23% yield` (no space before `%`, *do not abbreviate yield*) | `23 %`, `23% yld` |
| dr / ee | `X : X dr`, `99:1 dr`, `92% ee` | `X:X dr` (Stoltz uses spaces) |
| Number of steps | `# steps` (or e.g. `4 steps`) | — |
| Single diastereomer | `single diastereomer` | `s.d.` |
| Aqueous | `aq` | `aq.` |
| Pyridine (reagent) | `Py`; (when ligand) `py` | — |
| Minutes | `min` | `mins.`, `min.` |
| Hours | `h` | `hr`, `hrs` |
| Room temperature | `room temperature` (or measure the actual T) | `rt`, `r.t.` |
| Based on recovered SM | spell it out | `BORSM` |

**Special characters (Mac shortcuts in ChemDraw):**

- ° → Option/Shift/8
- · (small bullet, e.g. `BF3·OEt2`) → Shift/Option/9 (or Option/8 per Stoltz, verify in template)
- α, β, γ, δ → letter, then change font to Symbol
- Δ → `D` then change font to Symbol (or Option/J)
- Å → Shift/Option/A
- → (temperature ramp arrow) → Character Map → Symbol font
- en dash for `(–)`-rotation labels → Option/− (minus key)

## 7. Reference style (for figures that include in-figure references)

Per the Stoltz handout (also the in-house convention): Helvetica 16 pt for `slides-bms`, ACS format. In publication-style (`corey group sett`) figures, references go in Word, not ChemDraw.

ACS format pattern:

> Wood, *J. Am. Chem. Soc.* **1995**, *117*, 10413–10414.

Notable formatting:

- Last name(s) only of the principal investigator(s); full author list not required for slide references.
- Journal abbreviation in italic.
- Year **bold**.
- Volume in *italic*.
- Page range with en-dash, full range unless single page.
- Period at the end of the reference.

## 8. Stereochemistry drawing conventions

From Stoltz handout §"Bonds — wedges and hashes":

- Use the wedge and hash bond *tools* in ChemDraw. Avoid the dashed and bold bond tools.
- A wedge and a hash drawn from the *same* center is acceptable only at a real chiral center. In carbonyl-α stereochemistry, indicate stereochemistry from the α-carbon, not the carbonyl carbon.
- Avoid sequential stereocenters drawn off rings. If two adjacent stereocenters need to be shown, indicate one with stereobonds and the other through a heteroatom or ring junction.
- For double bonds, ChemDraw sometimes places the second bond on the outside of a ring; cycle through bond positions by clicking with the bond tool.
- For carbonyls/imines with three or more drawn-out substituents, ChemDraw may flip the double-bond orientation — same fix.

## 9. Layout conventions

- Schemes read **left to right**.
- For natural-product synthesis sequences in talks: place the complete natural-product structure in the **top-right corner** of the slide, scaled to fit. The slide title is then centered between the left edge and the top-right structure (not centered on the slide itself).
- Tables: a general reaction at the top, data below in aligned columns. A table with no overhead reaction is hard to read.
- Heading rows separated from data by a solid horizontal line.
- Vertical alignment of substrate / product / yield columns is non-negotiable. Distribute Vertically after copying rows.

## 10. Insertion into Word / PowerPoint

- Build the figure entirely in ChemDraw. Do not assemble parts in PowerPoint or Word.
- Each slide is its own ChemDraw file (don't put many slides in one ChemDraw doc — it crashes).
- Paste from ChemDraw into PowerPoint/Word. Resize **in PowerPoint**, not in ChemDraw, if rescaling is needed.
- For very large figures, save as TIFF in ChemDraw and paste the TIFF; if that fails, JPEG via Photoshop. (PDF export occasionally drops large figures — TIFF is the fallback.)
- A figure that has been scaled non-uniformly (different x and y scaling) is broken — flag as Critical.

## 11. IUPAC graphical principles (used as backstop)

When the in-house/Stoltz guide is silent, the Brecher 2008 IUPAC standards apply:

- **Text size.** Print structure text 8–14 pt; below 5 pt is unacceptable. In presentation media, scale up — a bond length comfortable in print is too small projected.
- **Line widths.** Below 0.5 pt avoid. Most lines in a structure diagram should match the stroke width of the surrounding text.
- **Atoms.** All atoms should be labeled (the standard implicit-carbon convention is fine; what is meant is: *if you depart from convention*, label atoms explicitly).
- **Substituents preferentially upward.** When a chain or ring has a choice of substituent orientation, prefer up-and-out over down-and-in.
- **Rings drawn as rings.** A ring should look like a ring, not a polygon distorted to fit space.
- **Consistency across the document.** Whatever font, font size, and bond length you choose, hold them constant across every figure. Inconsistency reads as carelessness.
- **Color rules.** Black on white is default. Red is the preferred emphasis color. Dark blue / dark gray is poor for emphasis on a low-contrast background. Avoid red+green combinations. If the diagram colors atoms by element, do not contradict the long-standing molecular-modeling convention (O red, N blue, etc.); choose a different palette or stick to black.

## 12. Pasted-bitmap detection

A figure that was pasted as a low-resolution bitmap rather than a vector object will reveal itself as:

- Visible pixelation along curves and aromatic ring vertices.
- Anti-aliasing fringes around text.
- Edges that look soft or blurry compared to the rest of the document.

Flag this — it usually means the figure was screenshotted from a previous document rather than rebuilt from the ChemDraw source. Per the handout, if a slide is being given on PC, save as TIFF; otherwise use vector paste.
