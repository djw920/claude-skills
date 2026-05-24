---
name: chemdraw-figure-review
description: >-
  Review the quality, style, and consistency of ChemDraw figures and reaction
  schemes embedded in .docx, .pptx, and .pdf documents. Use whenever the user
  wants to "review my figures," "check this scheme," "audit the schemes in this
  manuscript / SI / talk," "is this on-style," "does this look right for
  JACS / JOC / Org. Lett. / JMC," or hands over a draft and asks if the
  chemistry artwork is publication-ready. Trigger on informal phrasings:
  "look at the schemes in chapter 3," "check my deck before group meeting,"
  "the figures in section 2 feel off," "compare these against my template."
  Also trigger when the user points at a manuscript or proposal and wants
  figure-only feedback. Produces a per-figure issues table with severity, a
  checklist pass, narrative notes, and a tiered readiness rating (Ready /
  Minor revisions / Major revisions / Not ready). Reviews rendered output
  only — never edits ChemDraw. Do NOT use for manuscript prose (use
  chemistry-manuscript-writing) or for drawing molecules from scratch.
---

# ChemDraw Figure & Scheme Review

> **Customization note.** This skill is shipped with a worked-example house
> style (bond lengths, font sizes, color palette, arrow catalogue) drawn from
> a single chemistry group's ChemDraw template. **Replace the values
> in `references/house-style.md` with your own group's settings before relying
> on the style-and-formatting stage.** The review *structure* — extract,
> identify, style pass, chemistry flags, accessibility, document-level
> consistency, journal overlay, layered output — is generic and reusable as-is.

## Purpose

Audit the chemistry artwork in a document — every figure, every scheme — against an in-house ChemDraw template, ACS journal conventions, IUPAC graphical recommendations, and basic accessibility rules. Report findings in a form a chemist can act on directly in ChemDraw.

The skill assumes you have **rendered output only** — you cannot open the source `.cdx`/`.cdxml`, you cannot inspect ChemDraw object settings programmatically, and you cannot redraw structures. Everything you say must be defensible from what is visible in the rendered image.

## When to use

- The user asks to review, audit, or critique figures or schemes in a `.docx`, `.pptx`, or `.pdf`.
- The user shares a draft and asks "are the figures publication-ready?" or "does this match the template?"
- The user names a target journal (JACS, JOC, OL, JMC, *Chem. Sci.*) and wants a pre-submission figure pass.
- The user asks for a figure-only sweep before a group meeting, defense, talk, or proposal.
- A graduate student or postdoc has produced a draft and the user wants a triage before they read it.

Do **not** use the skill for:
- Writing or editing the prose of the manuscript — that is `chemistry-manuscript-writing`.
- Drawing new molecules or reaction schemes — the skill is reviewer, not author.
- Mechanism critique. Curved-arrow plausibility checks are out of scope unless the user explicitly asks; mechanisms get only a "looks worth a second look" flag.

## Required inputs

1. **A document** — `.docx`, `.pptx`, or `.pdf`. If multiple, accept a list.
2. **What "review" means in this pass** — does the user want every figure, only specific ones, only the SI, only the cover-letter scheme? Ask if not stated.

## Optional inputs (ask if relevant)

- Target journal (defaults to ACS family conventions if not specified).
- Submission stage (drafting / pre-submission / proof correction / talk prep). Severity calibration shifts.
- A specific section of the document (e.g., "just Schemes 3–7").
- Previous revision notes — useful for tracking whether feedback was applied.
- A different style guide if the project follows a different convention (e.g., a collaborator's house style).

If anything material is missing, ask. Reviewing the wrong figures is worse than asking one clarifying question.

## Review workflow

The model running this skill should follow these stages in order. Each stage has a dedicated reference file — read it before you start that stage, not earlier.

### Stage 1 — Extract the figures

Source documents bury figures inside binary containers. You cannot visually inspect what you cannot render. Use `scripts/extract_figures.py` to pull every embedded image from a `.docx` or `.pptx` and to rasterize PDF pages, then read the resulting images with the file tool.

See **`references/extraction.md`** for the exact commands, edge cases (TIFFs that PowerPoint sometimes hides, PDFs where ChemDraw was pasted as a vector object), and how to map each extracted image back to its location in the document (page, slide, or section heading).

If extraction fails for any figure, say so. Do not review what you cannot see, and do not invent figures from filenames or captions.

### Stage 2 — Identify what each figure is

For every extracted figure, record:
- **Location** — page / slide / scheme number.
- **Type** — single structure, reaction scheme, retrosynthesis, mechanism, table-with-scheme, cover graphic.
- **Caption / title** if visible.
- **Compound numbers present** — for cross-figure consistency in Stage 6.

### Stage 3 — Style and formatting checks

Run the figure against the in-house template defaults: bond length, font and font size, atom-label style, arrow type, yield/equiv formatting, color usage, layout direction. The full settings table is in **`references/house-style.md`** — consult it for every figure; do not work from memory.

The full checklist (what to inspect, in order) is in **`references/review-checklist.md`**. Walk it sequentially. Don't skip items because they "usually pass" — quick scans miss what matters.

### Stage 4 — Chemistry-aware (non-overclaiming) checks

Flag presentation problems that *look* chemical but are really visual. Examples: dangling bond ends, unbalanced wedge/hash counts, atom-count drift between scheme stages, compound numbers that don't match across schemes, mass-balance asymmetry in a stoichiometric drawing. The skill never declares a structure "wrong" — it only flags *check this*.

See **`references/chemistry-flags.md`** for the catalogue of visual symptoms and the exact non-overclaiming language to use.

### Stage 5 — Accessibility & legibility

Confirm the figure remains legible after typical scaling, in print, and in grayscale. Flag low-contrast color choices (especially red-on-blue, anything near yellow), sub-6 pt labels at print scale, raster artifacts from over-scaled bitmaps, and figures that won't survive a B&W photocopy.

Detail in **`references/accessibility.md`**.

### Stage 6 — Document-level consistency pass

After every figure has been reviewed individually, do one pass across the whole document looking for:
- Compound numbers used in multiple schemes — same number, same structure?
- Numbering gaps or duplicates across the document.
- Style drift (font sizes/bond lengths different between schemes — a sign that one was pasted from a different template).
- Reagent abbreviations: the same reagent abbreviated differently across schemes.
- Arrow conventions used inconsistently (e.g., retrosynthetic arrow vs. reaction arrow used interchangeably).

This pass is what catches the issues a per-figure review can't see.

### Stage 7 — Journal-specific overlay (if applicable)

If a target journal is named, apply the relevant overlay from **`references/journal-acs.md`**: column width fit, minimum font size at column scale, line-weight floor, color-figure rules. Note any deviations as journal-specific items in the output, separately from group-style issues.

### Stage 8 — Compose output

Produce the output in the layered format described below. Severity ratings, narrative summary, and per-figure detail. End with the readiness verdict.

## Output format

The output is layered: scannable up top, deep underneath. Use this exact structure unless the user requests something simpler.

### 1. Document-level summary (3–6 lines)

A one-paragraph orientation: what was reviewed, how many figures, the headline pattern (e.g., "Schemes are mostly on-template; a recurring issue is yield-formatting drift across the SI"), and the overall readiness rating.

### 2. Severity table (per figure)

A table with columns:

| Location | Issue | Severity | Suggested fix |
|---|---|---|---|

Severity uses four levels:
- **Critical** — The figure cannot be submitted/used as-is. Includes likely chemistry presentation errors (atom-count drift, missing stereobond, etc.) and figures illegible at print scale.
- **Major** — Will be visible to a reviewer or audience as off-quality. Wrong arrow type, fonts mixed within a scheme, color outside the palette, broken alignment.
- **Minor** — Style deviations a careful reader will notice. Off-by-2pt font, slightly inconsistent yield formatting, suboptimal layout direction.
- **Cosmetic** — Polishing only. Spacing, slightly tighter alignment, grouping suggestions.

Sort the table within each figure by severity descending.

### 3. Per-figure checklist pass

For each figure, run the checklist from `references/review-checklist.md` and mark each item Pass / Fail / N/A with a one-line note. Keep this section collapsible in tone — it is reference material, not the headline.

### 4. Narrative revision notes (per figure, only if there are non-trivial issues)

A short paragraph per problem figure explaining *why* the issues matter and how to approach the fix in ChemDraw. This is where you transmit chemist-to-chemist judgment, not just style flags. For figures rated Ready or near-Ready, a single sentence is enough.

### 5. Document-level findings

Anything that emerged in Stage 6 (cross-figure consistency). Compound-number drift. Style drift across sections. Reagent-abbreviation inconsistencies.

### 6. Journal overlay findings (only if a journal was specified)

Separate section. Items like "Scheme 4 will not fit single-column at JACS minimum font size — recommend redrawing at 70% with bond length 0.2917″ per the resize table."

### 7. Readiness verdict

Per-figure rating in a small table:

| Figure | Verdict |
|---|---|
| Scheme 1, p. 4 | Ready |
| Scheme 2, p. 6 | Minor revisions |
| Figure 3, p. 9 | Major revisions |

Plus one document-level line: "Document overall: Minor revisions — addressable in 1–2 hours of ChemDraw work." Be specific about the time estimate; it gives the user (or the student fixing the figures) a planning anchor.

### 8. Limitations note

Always include a short closing note that names what the review **could not** assess. Examples: "Stage 6 consistency was checked across the schemes I could extract — page 12 was a vector object I could not render." This is non-negotiable. Overclaim once and the skill loses trust.

## Style and formatting checks (summary)

The full table is in `references/house-style.md`. The headline items the skill checks for every figure:

- **Bond length** — visually consistent within a figure, and within the expected range for the document type (`slides-bms` ≈ 0.4167″ at 100% scale; `corey group sett` (publications) ≈ 0.2778″ at 100% scale).
- **Font and size** — Helvetica throughout (Times only for italicized titles). Atom labels and reagent text at the size called for in the template.
- **Compound numbers** — Helvetica, italic, 2 pt larger than atom labels.
- **Arrow type matches purpose** — reaction arrow vs. retrosynthetic vs. equilibrium vs. resonance; the reference catalogue lives in `references/house-style.md`.
- **Yield/equiv/temperature formatting** — `(1.1 equiv)`, `23% yield`, `80 °C` (one space before unit, no space before `%`, `equiv` not `eq.` and no period).
- **Color palette** — three approved colors (example defaults: Dark Blue RGB 0,30,98; Red RGB 213,0,50; Bright Blue RGB 0,0,225). No yellow. No ChemDraw default green. Substitute your group's palette in `house-style.md`.
- **Reading direction** — left to right; no railroad turns unless deliberate and labeled.

## Chemistry-aware (non-overclaiming) checks

Every chemistry-shaped flag uses **conditional language**: "*looks like X — please verify*" rather than "X is wrong." The skill is a second pair of eyes, not a referee. Items that warrant a flag:

- Dangling valences or a bond ending in empty space.
- Wedge/hash imbalance at a single chiral center (one wedge but no hash, when both are usually drawn).
- Apparent atom-count change between starting material and product without a labeled byproduct or arrow callout.
- Compound numbers used in two places that *appear* to be different molecules.
- Reagent listed above an arrow but no equivalents and no obvious solvent.
- Mass-balance look: a stoichiometric arrow with no byproduct shown when one is structurally expected (e.g., loss of HX).

Full catalogue and exact phrasing in `references/chemistry-flags.md`.

## Limitations (state these in every output)

The skill cannot:
- Open or modify `.cdx` / `.cdxml` source files.
- Read ChemDraw object settings (bond length in inches, font size in points) directly — only what is visible after rendering.
- Verify chemical correctness. Mechanism, stereochemistry, regiochemistry are all flagged for human review, never adjudicated.
- Distinguish a deliberate stylistic choice from a mistake. When in doubt, flag and ask.
- Review a figure that did not extract cleanly. Always name what couldn't be reviewed.

## Example user request

> "Can you go through Chapter 3 of this thesis draft and check the schemes? It's the Beckmann section — Schemes 3.1 through 3.8. Target is OL eventually. Be honest, the student has only had a few rounds with the template."

Expected behaviour: extract the document, identify Schemes 3.1–3.8, run the full review per scheme, apply the OL journal overlay from Stage 7, deliver the layered output, and end with a per-scheme verdict plus a document-level rating. Keep the tone direct but constructive — the student will read the output.

## Example review output (excerpt)

> **Document overall: Major revisions** — five figures need rework before the document is OL-submission shape, but the issues are concentrated and predictable. Estimated 3–4 hours of ChemDraw work.
>
> **Scheme 3.2, p. 47 — Major revisions**
>
> | Issue | Severity | Suggested fix |
> |---|---|---|
> | Reaction arrow is the bold variant; should be the standard reaction arrow per template. | Major | Replace with the smallest solid arrow. |
> | "23% yld" — should read "23% yield"; group style does not abbreviate "yield". | Minor | Spell out. |
> | Compound **3a** appears with a methyl wedge; the same compound in Scheme 3.4 has a hash. *Looks like a stereochemistry inconsistency — please verify which is intended.* | Critical | Confirm absolute configuration; redraw the inconsistent figure. |
> | Bond length on the right-hand product is visibly shorter than the rest of the scheme — possibly pasted from a 70% scaled fragment. | Major | Reset Object Settings to template defaults; redraw if necessary. |
>
> *Notes:* The compound-3a stereochemistry mismatch is the only true blocker — everything else is a polish pass. If 3a turns out to be drawn correctly here and incorrectly in 3.4, fix 3.4 instead.

## What this skill does NOT claim

- It does not say a structure is *chemically* wrong. It says the *drawing* of the structure has an issue worth checking.
- It does not say a figure is "publication-quality" without journal-specific qualification.
- It does not claim to have inspected ChemDraw's internal settings; only the rendered output.
- It does not produce a corrected ChemDraw file. It produces revision notes.
