---
name: experimental-writing
version: 1.1.0
description: >
  Write, format, and edit organic chemistry experimental procedures and compound
  characterization data to ACS journal standards. Use this skill whenever the user
  asks to write, draft, correct, format, or polish an experimental section, a
  supporting information entry, or compound characterization data—including NMR,
  IR, HRMS, optical rotation, mp/bp, or yield reporting. Also trigger for requests
  to generate a general procedure template, check characterization data for errors,
  or prepare a compound data block for JMC, JACS, OL, or similar ACS-family journals.
  Trigger even when the request is phrased informally, e.g. "write up compound 3f,"
  "format my NMR data," or "check my experimental." Supports two output modes:
  manuscript (compact journal layout) and thesis (spaced, reader-friendly layout).
  Works interactively, never alters scientific data without explicit user permission,
  and flags ambiguities for confirmation before making data-level changes.
---

# Experimental Writing Skill
## Organic Chemistry Procedures and Characterization Data — ACS Standard

---

## CORE PRINCIPLES

### Non-Negotiable Data Integrity Rule

Never alter, infer, normalize, reinterpret, correct, round, or complete any scientific data without explicit user permission. This includes masses, volumes, equivalents, yields, temperatures, times, solvent identities, reagent names, stereochemical descriptors, spectroscopic values, peak assignments, molecular formulae, HRMS values, and chromatographic conditions. If a value appears inconsistent, ambiguous, incomplete, or likely incorrect, flag it clearly and ask the user whether to correct, preserve, or review it.

### Priority Order

When making decisions, follow this hierarchy:
1. User-provided source text (always paramount)
2. Data integrity rule (never silently alter data)
3. ACS Research Data Guidelines
4. User-provided example files
5. This skill document
6. General ACS-style organic chemistry conventions

### Tone

Precise, conservative, scientifically literate, editorial — never interpretive, never overconfident about unclear data.

---

## INTERACTIVE WORKFLOW

### Starting a Task

Ask only the minimum necessary:
1. Which mode: **manuscript** or **thesis**? (Default: manuscript)
2. Paste text or provide file content.
3. If a specific example file should be followed more closely, which one?

### For Each Task

1. Identify the requested output mode.
2. Review the user's source text.
3. Preserve all scientific content exactly unless the user authorizes changes.
4. Make formatting, grammar, punctuation, consistency, and style improvements that do not change meaning or data.
5. Present the response using this structure:

**1. Mode** — State manuscript or thesis.

**2. Polished Experimental Text** — The revised text.

**3. Flags / Items Requiring Confirmation** — Possible inconsistencies, ambiguities, or missing information.

**4. Optional Style Notes** — Brief notes on formatting decisions, if helpful.

### Allowed Changes Without Asking

Grammar, spelling, punctuation, capitalization, formatting, spacing, sentence flow, parallel structure, abbreviation consistency, order/presentation of data where no values change, standard wording for experimental descriptions if meaning is preserved.

### Changes Requiring Explicit Permission

Numerical values, chemical identities, assignments, interpretation of spectra, missing information, reaction conditions, product names, stereochemistry, yield calculations, molecular formulae, exact formatting conventions when multiple plausible standards exist and examples conflict.

---

## OUTPUT MODES

### Manuscript Mode (default)

- Compact, journal-style formatting
- Minimize extra spacing
- Combine related analytical data efficiently
- Concise, publication-oriented wording
- Avoid unnecessary headings unless the user requests them

### Thesis Mode

- More visual separation between experimental entries
- Clearer sectional spacing for readability
- Preserve full detail; make dense passages easier to navigate
- Allow slightly more explicit transitions and labels

### Output Formatting (both modes)

**Mode-specific font convention:**
- **Manuscript mode** → **Times New Roman, 12 pt** (ACS house convention; matches JOC, JACS, Org. Lett., and most ACS-family author-guideline defaults for submitted manuscripts). A serif body font is expected in chemistry manuscripts because dense technical prose with italic stereo-descriptors (*R*, *S*, *E*, *Z*, *anti*, *syn*), Greek letters (δ, ν, λ), superscripts, subscripts, and bold compound numbers disambiguates more cleanly in serif at print sizes.
- **Thesis mode** → **Arial, 12 pt** as default, but institutional thesis-formatting requirements take precedence; Times New Roman 12 pt is equally acceptable if institutional policy requires it.

**Font consistency within the body:** Whichever font is chosen for the mode, apply it throughout the experimental text including bold compound-name headings. Do not mix serif body text with sans-serif headings (or vice versa) inside an experimental block — typographic inconsistency inside a compound entry reads as an editing error.

**Font for figures, schemes, and embedded ChemDraw content:** Always **Arial** regardless of mode. ACS convention is sans-serif inside graphics; ChemDraw's default is Arial. This is independent of body-text font choice.

**Other formatting (both modes):**
- **Alignment**: Left-justified
- **Spacing**: Single-spaced
- **Paragraph breaks**: Single blank line between compound entries
- Deliver as a Word-ready block unless a different format is specified

---

## PART 1: EXPERIMENTAL PROCEDURE STRUCTURE

### 1.1 General Procedure Template

**General Procedure [Letter] for [Transformation Class].**
To a stirred solution of [substrate] ([mass] g, [mmol] mmol, [equiv] equiv) in [solvent] ([vol] mL) at [temp] under [atmosphere] was added [reagent] ([mass/vol], [mmol] mmol, [equiv] equiv) [dropwise/portionwise]. The reaction mixture was stirred at [temp] for [time] and monitored by TLC (R*f* = [value], [eluent]). Upon completion, the reaction was quenched with [solution] and the layers were separated. The aqueous phase was extracted with [solvent] (3 × [vol] mL). The combined organic extracts were washed sequentially with [solution], dried over [drying agent], filtered, and concentrated under reduced pressure. Purification by flash chromatography on silica gel ([gradient], v/v) afforded [product class] **[n]** as a [color and form].

### 1.2 Required Elements — Experimental Procedure

Include, in order:
1. Substrate identity, mass (g or mg), mmol, and equiv
2. Solvent and volume (mL); concentration if relevant to outcome
3. Atmosphere (N₂, Ar, air) when relevant
4. Temperature at each stage
5. Reagent(s): identity, mass/volume, mmol, equiv; order of addition
6. Reaction time and monitoring method (TLC, LC–MS, etc.)
7. Quench and workup: specify quench agent, extractions, washes, drying agent
8. Purification: method, stationary phase, eluent gradient, or recrystallization solvent
9. Isolated yield: mass, mmol, percent
10. Physical description: color, form (oil, foam, solid, gum, glass)
11. Special notes if applicable: dr, rotamers, instability, hygroscopicity

### 1.3 Tense and Voice

- Past tense throughout
- Passive or restrained active voice
- Do not write "The reaction was worked up in the usual way" — specify every step

### 1.4 Quantities

Always provide both mass (or volume) AND mmol AND equivalents.

> To a solution of ketone **7** (150 mg, 0.62 mmol, 1.0 equiv) in anhydrous THF (6.0 mL) at 0 °C was added LDA (1.0 m in THF/heptane/ethylbenzene, 0.75 mL, 0.75 mmol, 1.2 equiv) dropwise.

---

## PART 2: COMPOUND CHARACTERIZATION BLOCK

### 2.1 Standard Order of Characterization Data

1. Compound name and number (bold heading)
2. Yield, mmol, physical form
3. mp (crystalline solids; range, not false precision)
4. IR (ATR preferred; νmax, wavenumbers)
5. ¹H NMR
6. ¹³C NMR
7. Additional nuclei (¹⁹F, ³¹P, etc.) if present
8. HRMS
9. Optical rotation and enantiopurity (chiral compounds only)
10. Chiral HPLC/SFC conditions and retention times if applicable

### 2.2 Compound Heading Format

**Full IUPAC or semisystematic name (compound number).**

Example:
**4-Fluoro-*N*-methylbenzamide (1).**

Yield, physical form, and mass follow immediately in the same paragraph.

---

## PART 3: DATA FORMATTING RULES

### 3.1 ¹H NMR

Standard format:
> ¹H NMR (500 MHz, CDCl₃) δ 8.12 (d, *J* = 8.6 Hz, 2H), 7.64 (dd, *J* = 8.2, 1.6 Hz, 1H), 4.21 (t, *J* = 6.8 Hz, 2H), 2.78–2.71 (m, 2H).

Rules:
- Frequency (MHz) and solvent required for each spectrum
- δ values to two decimal places
- Integration as number of protons (e.g., 2H)
- *J* italicized; reported to one decimal place (Hz)
- Multiple *J* values listed in descending order
- Multiplicity abbreviations: s, d, t, q, quint, m, dd, dt, td, ddd, br
- Multiplet ranges with en-dash: 2.78–2.71
- List from downfield to upfield (high δ to low δ) consistently within paper
- Solvent formula preferred: CDCl₃ (not chloroform-*d*)

### 3.2 ¹³C NMR

Standard format:
> ¹³C NMR (126 MHz, CDCl₃) δ 168.2, 156.4, 147.9, 136.2, 129.4, 127.6, 124.2, 118.7, 37.8, 28.4.

Rules:
- δ values to one decimal place
- Multiplicities assigned only when DEPT or 2D data collected or when coupling to non-¹H nucleus is present
- List from downfield to upfield
- Note unobserved carbons when symmetry or low intensity is the cause
- Indicate rotamers, tautomers, or broadening explicitly when present

### 3.3 ¹⁹F NMR

> ¹⁹F NMR (471 MHz, CDCl₃) δ −113.6.

### 3.4 ³¹P NMR

> ³¹P NMR (202 MHz, CDCl₃) δ −6.56 (d, *J*P,P = 21.9 Hz).

### 3.5 IR

Format:
> IR (ATR) νmax 3310, 1672, 1541, 1240 cm⁻¹.

- List major diagnostic bands only (do not reproduce full spectrum)
- Wavenumbers as integers
- cm⁻¹ with superscript −1
- ATR preferred; specify neat, KBr, or Nujol mull if applicable
- Assignments (C=O, N–H, etc.) optional but useful for key functional groups

### 3.6 HRMS

Standard format:
> HRMS (ESI-TOF) *m/z* [M + H]⁺ calcd for C₁₃H₁₃N₄O₃ 273.0982, found 273.0980.

Rules:
- Specify ionization method: ESI, EI, APCI, FAB
- Specify analyzer: TOF, Orbitrap, etc.
- Include ion designation: [M + H]⁺, [M + Na]⁺, [M − H]⁻, [M]⁺•
- Formula in calcd corresponds to the **ion observed**, not the neutral molecule
- Mass match within 5 ppm (EI) or ≤10 ppm (ESI, APCI); report actual found value
- *m/z* in italic

### 3.7 Elemental Analysis (if required)

> Anal. Calcd for C₁₃H₁₂N₄O₃: C, 57.35; H, 4.44; N, 20.58. Found: C, 57.21; H, 4.51; N, 20.41.

Use only when sample purity and instrument quality warrant it.

### 3.8 Melting Point

> mp 142–144 °C.

- Range, not a single value
- Use en-dash
- Specify recrystallization solvent in procedure, not in mp line
- Do not imply false precision (±0.1 °C is excessive for routine mp)

### 3.9 Optical Rotation

> [α]²⁵D +18.6 (*c* 0.50, CHCl₃).

- Temperature as superscript; wavelength as subscript (D for sodium D line)
- *c* italicized; concentration in g/100 mL
- Solvent in parentheses; CHCl₃ preferred for new compounds
- Follow immediately with ee or er and method of determination if applicable

### 3.10 Chiral HPLC / SFC

State: column, mobile phase, flow rate, detection wavelength, retention times for each enantiomer/diastereomer, and er or dr assignment.

### 3.11 Yield Reporting

> 86 mg (0.31 mmol, 62%) as an off-white solid.

- Always report mass, mmol, and percent
- If mixture: "94 mg (0.28 mmol, 58%) as a 4.3:1 mixture of diastereomers (determined by ¹H NMR)"
- Yield is **isolated yield** unless explicitly stated otherwise

---

## PART 4: TYPOGRAPHIC AND NOTATION CONVENTIONS

### 4.1 Nuclei and Spectroscopy Labels

| Raw input | Correct output |
|-----------|---------------|
| 1H NMR | ¹H NMR |
| 13C NMR | ¹³C NMR |
| 19F NMR | ¹⁹F NMR |
| 31P NMR | ³¹P NMR |
| cm-1 | cm⁻¹ |
| Rf | *R*f (italic R, roman subscript f) |
| J = 8.0 Hz | *J* = 8.0 Hz (italic J) |
| ir, IR | IR |
| ms, MS | MS |
| tlc, TLC | TLC |
| [d6] DMSO | [*d*₆]DMSO |

### 4.2 Stereodescriptors

- (*R*)- and (*S*)- in italic parentheses: (*R*)-, (*S*)-
- (*E*)- and (*Z*)- in italic parentheses: (*E*)-, (*Z*)-
- *tert*- italic; *sec*- italic; *n*- roman preferred (or italic *n*-)
- *endo*-, *exo*-, *syn*-, *anti*- all italic

### 4.3 Alkyl Group Prefixes

| Raw | Correct |
|-----|---------|
| tBuOH | *t*-BuOH |
| nBuLi | *n*-BuLi |
| sBuOK | *s*-BuOK |

### 4.4 Temperature

- Always: numeral + space + °C → 25 °C, 0 °C, −78 °C
- Do not write "room temperature" or "rt" → use "ambient temperature" or specify °C
- Negative temperatures: en-dash or minus sign, not hyphen

### 4.5 Metal Oxidation States

- Roman numerals in parentheses, uppercase, no space: Iron(III), Copper(II), Palladium(0)

### 4.6 SI Units

| Raw | Correct |
|-----|---------|
| ml | mL |
| ul, µl | µL |
| l | L |
| M (molarity) | m (preferred ACS) or M (journal-dependent) |

### 4.7 Chemical Formulas in Text

- Subscript digits: C₁₃H₁₂N₄O₃
- Parenthetical groups: (CH₃)₂

### 4.8 Solvent Abbreviations

| Full name | Abbreviation |
|-----------|-------------|
| ethyl acetate | EtOAc |
| dimethyl sulfoxide | DMSO |
| dichloromethane | CH₂Cl₂ or DCM |
| tetrahydrofuran | THF |
| methanol | MeOH |
| hexanes | hexanes (plural) |
| magnesium sulfate | MgSO₄ |
| sodium sulfate | Na₂SO₄ |

### 4.9 Coupling Constants — Multiplicity

When reporting a doublet of doublets, list *J* values in descending order:
> dd, *J* = 12.4, 4.8 Hz

Report to one decimal place. Do not report to two decimal places.

### 4.10 Reagent Salt Interpunct

Use the bullet operator • (U+2022, Option-8 on Mac) for reagent salts and hydrates, not the middle dot · (U+00B7).

| Raw | Correct |
|-----|---------|
| EDC·HCl | EDC•HCl |
| MeONH2·HCl | MeONH₂•HCl |
| PPTS·H2O | PPTS•H₂O |
| NaIO4·H2O | NaIO₄•H₂O |

This is the standard ACS convention for coordination dots in salt and hydrate formulas.

### 4.11 Italic Locants and Prefixes in Compound Names

When rendering compound names in Word or Google Docs, italic text must appear as formatted italic, never as literal markup tags. The following elements within compound names require italic formatting:

- *O*-Methyl, *N*-Methyl, *S*-Benzyl (heteroatom locants)
- (*R*)-, (*S*)-, (*E*)-, (*Z*)- (stereodescriptors)
- *tert*-, *sec*-, *n*- (alkyl prefixes)
- *endo*-, *exo*-, *syn*-, *anti*- (stereochemical relationship prefixes)
- *ortho*-, *meta*-, *para*- (when written out, not as *o*-, *m*-, *p*-)

In plain-text or Markdown output, use asterisks for italic: `*O*-Methyl`. In Word documents, these must be rendered as true italic character formatting, not as markup.

---

## PART 5: QUALITY CHECKS

Before finalizing any characterization block, verify:

**NMR integrity**
- Integration totals match molecular formula
- No impossible multiplicities (e.g., a quartet where a doublet is expected)
- *J* values internally consistent across coupled partners
- ¹³C count consistent with structure (accounting for symmetry)
- Solvent and frequency match across all spectra in the compound block
- Unobserved ¹³C carbons noted if symmetry or poor sensitivity is the cause

**HRMS integrity**
- Molecular formula in calcd corresponds to the observed ion (not neutral molecule)
- m/z value consistent with ion charge state
- Calculated mass verifiable independently

**Internal consistency**
- Compound number matches scheme, table, SI spectrum filename, and biological data table
- Yield identical in procedure paragraph and characterization header
- Physical form consistent with mp data (no mp for oils)
- Optical rotation reported only for chiral, non-racemic compounds

**Procedure completeness**
- All quantities in mass + mmol + equiv
- Temperature at every stage
- Workup fully described (quench → partition → wash → dry → concentrate)
- Purification conditions specific (gradient stated)

---

## PART 6: BEHAVIOR WITH INCOMPLETE OR MESSY INPUT

If the user provides rough notes, fragmented text, or mixed formatting:
- Organize into a coherent experimental entry
- Preserve all provided content
- Mark unclear areas with brackets or a clear query
- Never invent missing details

---

## PART 7: BEHAVIOR WITH CONFLICTING REFERENCES

If the ACS guideline, example files, and this skill suggest different formatting choices:
- Preserve data integrity first
- Prefer ACS guideline defaults
- Then align with the user's example files where possible
- If the conflict affects scientific interpretation or required content, ask the user

---

## PART 8: REFERENCE FILES

For extended examples and edge cases, see:

- `references/nmr-examples.md` — Annotated ACS-format NMR blocks for complex natural products and medicinal compounds (rotamers, C–F coupling, 2D-assigned natural products, ³¹P NMR, solvent reference table)
- `references/hrms-ions.md` — Ion type selection guide (ESI+/−, EI, APCI), formula verification rules for each ion type, mass accuracy thresholds, common errors
- `references/procedure-phrases.md` — Standard transition phrases and workup language bank (setup, monitoring, quench, workup, purification, physical forms, special conditions, known compound entries)

Read these when handling unusual nuclei, atypical ionization modes, generating an extended general procedure section, or when the user's input requires edge-case formatting decisions.
