# ACS Journal Figure Requirements

When the user names a target journal in the ACS family (JACS, JOC, Org. Lett., JMC, Inorg. Chem., Anal. Chem., *Chem. Sci.*, etc.), apply this overlay **after** the group-style review. Journal items go in a *separate* section of the output so they are not confused with house-style issues.

The values in this file are the public ACS guidelines as of a recent revision. Specific journals refresh their requirements; verify against the journal's current author guidelines for a final-stage submission.

---

## A. Universal ACS figure conventions

These apply across the family.

### A1. Page widths

ACS journals use a two-column page layout. Figures must fit one of two widths.

| Column type | Approx. width |
|---|---|
| Single-column | 3.25 in (8.25 cm) |
| Double-column (full-page width) | 7.0 in (17.8 cm) |

A figure drawn at the `slides-bms` template scale (bond length 0.4167″) will not fit single-column without resizing. The publication template (`corey group sett`, bond length 0.2778″ at 100%) is the right starting point for a manuscript. If a figure is being lifted from a talk into a manuscript, it almost certainly needs redrawing at the publication settings.

### A2. Minimum text size at column scale

After scaling the figure to its target column width:

- **Atom labels and reagent text**: not smaller than ~6–7 pt at print scale. Below 6 pt is unreadable to most readers.
- **Compound numbers**: typically 8–10 pt at print scale.
- **Figure caption**: per journal style; usually 8 pt sans-serif.

Practical heuristic: if the rendered figure shrinks to fit single-column and the atom labels become illegibly small, the figure was drawn at the wrong starting scale. Recommend redrawing at `corey group sett` 100% rather than scaling down a slide-template figure.

### A3. Line widths at column scale

- All bond lines: at least 0.5 pt at final print scale (IUPAC GR-0.4; ACS aligned).
- A figure pasted-and-shrunk from a presentation may end up with bond lines below 0.5 pt — flag.

### A4. Color in figures

ACS journals accept color figures, but:

- Color must be *meaningful*. A figure where everything is colored for decoration is poor practice.
- Avoid red+green combinations (colorblindness).
- Some journals charge for color in print. *J. Org. Chem.* historically charged; *J. Am. Chem. Soc.* often allows free color online with B&W in print — verify current policy. If unsure, recommend the figure be designed to work in grayscale.
- The the in-house palette (Dark Blue 0,30,98; Red 213,0,50; Bright Blue 0,0,225) is ACS-acceptable and survives grayscale conversion well except for Red and Bright Blue, which can converge — recommend testing.

### A5. File format for submission

- ACS prefers TIFF or EPS for chemistry figures.
- Embedded ChemDraw objects in Word are accepted but should be high-resolution; flag any visibly bitmapped figure as a likely format problem.
- Resolution: 600 dpi minimum for line art (which includes structure drawings); higher for any embedded photographic content.

---

## B. Journal-specific items

### B1. *Journal of the American Chemical Society* (JACS)

- Two-column layout; column widths as above.
- Color figures in print typically allowed; verify current policy.
- Graphical abstract: 9 cm × 5 cm (3.5 in × 2 in), high-resolution. Should communicate the central finding visually; ChemDraw figures used as graphical abstracts must be sized for that aspect ratio specifically.
- *Communication* format manuscripts have especially tight figure-count budgets; redundant schemes are a flag.

### B2. *Journal of Organic Chemistry* (JOC)

- Historically more conservative on color in print — verify; may charge for color in print.
- Strong preference for clean, high-contrast B&W figures. A *J. Org. Chem.* figure that relies on color to convey distinct categories should also be distinguishable in grayscale.
- Compound numbering tradition: bold compound numbers in the manuscript text, italic compound numbers under structures (matches the in-house convention).

### B3. *Organic Letters* (OL)

- *Communication-only* journal — every figure earns its place. Multi-panel schemes are common but should be visually compact.
- Single-column format dominant; figures that span both columns must be justified by content.
- Recently strict on figure quality at submission — a bitmap-pasted scheme will be flagged in initial check.

### B4. *Journal of Medicinal Chemistry* (JMC)

- Two-column layout.
- Heavy use of structure–activity tables; alignment of substrate/structure columns with biological-activity data columns is critical.
- IC50 / Ki values formatted per ACS unit conventions: `IC50` with subscript 50, units `nM`, `μM`, `mM` italicized appropriately.
- Graphical abstract often combines a structure with a brief biological-activity callout — a more design-heavy figure than for OL or JOC.

### B5. *Inorganic Chemistry*, *Organometallics*

- Coordination compounds drawn with ACS-standard bonding conventions (specific dative-bond conventions per IUPAC GR-1.7).
- Crystal-structure thermal-ellipsoid plots are not ChemDraw output — separate review required, out of scope for this skill.

### B6. *Analytical Chemistry*, *J. Phys. Chem.*

- ChemDraw figures less central; flag when a figure that is clearly a chromatogram, NMR spectrum, or instrument output is being audited as a structure figure (different review criteria apply).

### B7. *Chemical Science* (RSC family — relevant for groups publishing in non-ACS venues)

- RSC house style differs from ACS but the underlying drawing conventions are similar.
- Strong preference for clean B&W structures; color reserved for emphasis as in ACS.
- Italic compound numbering under structures is RSC-standard (matches in-house).

---

## C. Submission-stage flags

When the user has indicated the document is submission-stage (not draft):

1. **Any figure rated Major or Critical is a submission blocker.**
2. **Any figure with bond length / font size visibly inconsistent with a single template is a blocker.**
3. **Any bitmap-pasted figure should be redrawn from the ChemDraw source before submission.**
4. **Any figure that does not pass the column-width test for the named journal is a blocker.**
5. **Graphical abstracts get a separate, stricter pass.** They are often the only figure most readers see.

Flag these explicitly in the journal-overlay section of the output, not the group-style section.

---

## D. What this overlay does NOT verify

- Citation formatting in figure references (defer to the manuscript prose review).
- Whether the figure is needed at all (editorial judgment, out of scope).
- Whether the data shown is reproducible or correct.
- Whether the SI figures match the main-text figures (do flag if compound numbering is inconsistent between main text and SI, since that is a visual symptom).
