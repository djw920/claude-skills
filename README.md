# claude-skills

A curated collection of [Claude skills](https://www.anthropic.com/news/skills) for chemistry research and scientific writing. Skills are context files that Claude reads at the start of a task — they encode domain knowledge, workflows, and style conventions so you don't have to re-explain them each session.

All four skills are domain-relevant for synthetic and medicinal chemistry but have been written to be reusable across groups.

## Contents

- [Skills overview](#skills-overview)
- [Repository structure](#repository-structure)
- [Installation](#installation)
- [Skill reference](#skill-reference)
  - [rdkit](#rdkit)
  - [experimental-writing](#experimental-writing)
  - [chemdraw-figure-review](#chemdraw-figure-review)
  - [notebooklm-source-curator](#notebooklm-source-curator)
- [Customization](#customization)
- [Platform notes](#platform-notes)
- [License](#license)

---

## Skills overview

| Skill | What it does | Customization needed? |
|---|---|---|
| [`rdkit/`](#rdkit) | Cheminformatics API reference — SMILES/SDF I/O, descriptors, fingerprints, substructure search, 2D/3D generation, reactions | None — generic |
| [`experimental-writing/`](#experimental-writing) | Write and format organic chemistry experimental procedures and compound characterization data to ACS journal standards | None — generic |
| [`chemdraw-figure-review/`](#chemdraw-figure-review) | Audit ChemDraw figures in `.docx`/`.pptx`/`.pdf` against a house style, ACS conventions, and accessibility rules | **Yes** — edit `references/house-style.md` with your group's template settings |
| [`notebooklm-source-curator/`](#notebooklm-source-curator) | Curate and rename source PDFs for a NotebookLM project so that retrieval is precise and the evidence base is auditable | None for the workflow; author companion `references/` files per domain |

---

## Repository structure

```
claude-skills/
├── chemdraw-figure-review/
│   ├── SKILL.md                      # Main skill definition
│   ├── references/
│   │   ├── accessibility.md          # Legibility, color, and grayscale checks
│   │   ├── chemistry-flags.md        # 15 non-overclaiming visual chemistry flags
│   │   ├── extraction.md             # How to pull figures from .docx/.pptx/.pdf
│   │   ├── house-style.md            # ⚠ CUSTOMIZE: bond lengths, fonts, color palette
│   │   ├── journal-acs.md            # ACS journal-specific requirements (JACS, JOC, OL, JMC)
│   │   └── review-checklist.md       # 55-item per-figure checklist
│   └── scripts/
│       └── extract_figures.py        # Pulls embedded images from documents
├── experimental-writing/
│   ├── SKILL.md                      # Main skill definition
│   └── references/
│       ├── hrms-ions.md              # Ion type selection, formula verification, mass accuracy
│       ├── nmr-examples.md           # Annotated ACS-format NMR blocks (rotamers, CF coupling, 2D)
│       └── procedure-phrases.md      # Standard workup, purification, and condition phrases
├── notebooklm-source-curator/
│   └── SKILL.md                      # Main skill definition (workflow stands alone)
├── rdkit/
│   ├── SKILL.md                      # Main skill definition
│   ├── references/
│   │   ├── api_reference.md          # Complete RDKit Python API listing by module
│   │   ├── descriptors_reference.md  # All Descriptors module entries with usage
│   │   └── smarts_patterns.md        # SMARTS patterns for functional groups, rings, pharmacophores
│   └── scripts/
│       ├── molecular_properties.py   # Batch descriptor calculator (CLI + CSV output)
│       ├── similarity_search.py      # Fingerprint-based similarity screener
│       └── substructure_filter.py    # Substructure inclusion/exclusion filter
├── .gitignore
├── LICENSE
└── README.md
```

---

## Installation

Skills live under `~/.claude/skills/` on macOS/Linux (the directory may not exist yet — create it).

**Install one skill:**
```bash
mkdir -p ~/.claude/skills
cp -r chemdraw-figure-review ~/.claude/skills/
```

**Install all skills:**
```bash
mkdir -p ~/.claude/skills
cp -r chemdraw-figure-review experimental-writing notebooklm-source-curator rdkit ~/.claude/skills/
```

**Install directly from GitHub:**
```bash
mkdir -p ~/.claude/skills
git clone https://github.com/djw920/claude-skills.git /tmp/claude-skills
cp -r /tmp/claude-skills/rdkit ~/.claude/skills/
# repeat for other skills as needed
```

After installation, restart Claude (or your Claude client) so it re-indexes the skills directory.

---

## Skill reference

### rdkit

**Purpose:** Comprehensive reference for the RDKit Python cheminformatics library. Use whenever working with molecular structures — parsing SMILES, calculating descriptors, fingerprinting, substructure searching, generating 2D/3D coordinates, or running chemical reactions.

**Trigger phrases:** "parse this SMILES", "calculate LogP/TPSA/MW", "Morgan fingerprint", "substructure search", "generate conformers", "RDKit", "Tanimoto similarity".

**What the skill provides:**
- Core API for molecule I/O (SMILES, SDF, MOL, PDB, InChI)
- Sanitization, stereochemistry, and fragment handling
- All Descriptors module entries with usage examples
- Morgan, MACCS, RDKit, atom-pair, and torsion fingerprints
- Substructure matching and SMARTS pattern library
- Chemical reaction SMARTS
- 2D and 3D coordinate generation with force-field optimization
- Molecular visualization (PIL, Cairo, Jupyter)
- Clustering (Butina), scaffold analysis (Murcko), and standardization
- Drug-likeness workflows (Lipinski, QED, lead-likeness)

**Reference files loaded on demand:**
- `references/api_reference.md` — module-by-module API listing
- `references/descriptors_reference.md` — all `Descriptors.*` functions
- `references/smarts_patterns.md` — SMARTS for functional groups, rings, pharmacophores, PAINS

**Runnable scripts:**
```bash
# Calculate properties for a single molecule
python rdkit/scripts/molecular_properties.py "c1ccc(CC(=O)O)cc1"

# Batch properties to CSV
python rdkit/scripts/molecular_properties.py --file compounds.sdf --output props.csv

# Similarity search
python rdkit/scripts/similarity_search.py "c1ccccc1" database.smi --threshold 0.7

# Substructure filtering
python rdkit/scripts/substructure_filter.py compounds.smi --pattern "C(=O)N" -o amides.smi
python rdkit/scripts/substructure_filter.py compounds.smi --filter-type pains --exclude-mode -o clean.smi
```

**Note:** This skill covers advanced/fine-grained RDKit usage. For standard drug-discovery workflows with a simpler interface, consider using `datamol` (a wrapper around RDKit with sensible defaults).

---

### experimental-writing

**Purpose:** Write, format, and edit organic chemistry experimental procedures and compound characterization data to ACS journal standards. Works in two modes: **manuscript** (compact, journal-ready) and **thesis** (spaced, reader-friendly).

**Trigger phrases:** "write up compound X", "format my NMR data", "check my experimental", "draft the SI entry for", "format this characterization block", "write a general procedure for".

**What the skill provides:**
- General procedure template with all required elements
- Correct ordering of characterization data (mp → IR → ¹H → ¹³C → HRMS → [α]D)
- Data formatting rules for ¹H, ¹³C, ¹⁹F, ³¹P NMR; IR; HRMS; elemental analysis; optical rotation; chiral HPLC/SFC
- Complete typographic conventions: nuclei superscripts, *J* italic, stereodescriptors, alkyl prefixes, temperature formatting, SI units, solvent abbreviations, reagent salt interpuncts
- Quality checks: NMR integration, HRMS formula verification, internal consistency
- Manuscript vs. thesis font guidance (Times New Roman 12 pt vs. Arial 12 pt)

**Non-negotiable principle:** The skill never silently alters numerical data. Any value that looks inconsistent is flagged for user confirmation — it is never corrected without explicit permission.

**Reference files loaded on demand:**
- `references/nmr-examples.md` — annotated blocks for chiral compounds, rotamers, C–F coupling, organometallics, 2D-assigned natural products
- `references/hrms-ions.md` — ion type selection for ESI±/EI/APCI, formula verification, mass accuracy thresholds
- `references/procedure-phrases.md` — language bank for setup, monitoring, quench, workup, purification, physical forms, known-compound entries

**Calibration:** ACS-family journals (JOC, JACS, Org. Lett., JMC). RSC/Wiley/Elsevier targets are broadly compatible but may require minor adjustments to font and formatting defaults.

---

### chemdraw-figure-review

**Purpose:** Audit every ChemDraw figure and reaction scheme in a document against an in-house template, ACS journal conventions, IUPAC graphical recommendations, and accessibility rules. Produces a per-figure issues table with severity ratings (Critical / Major / Minor / Cosmetic) and a readiness verdict.

**Trigger phrases:** "review my figures", "check the schemes in this manuscript", "is this on-style", "does this look right for JACS/JOC/OL", "audit the schemes in chapter 3", "check my deck before group meeting".

**What the skill provides:**
An 8-stage review workflow:
1. **Extract** — pull all embedded images from `.docx`, `.pptx`, or `.pdf` using `scripts/extract_figures.py`
2. **Identify** — record location, type, caption, and compound numbers
3. **Style** — check bond length, font, atom labels, arrows, yield/equiv formatting, color palette, layout
4. **Chemistry flags** — 15 non-overclaiming visual checks (dangling bonds, wedge/hash imbalance, atom-count drift, compound-number collisions, etc.)
5. **Accessibility** — legibility at print scale, color contrast, grayscale survival, pixelation
6. **Document-level** — cross-figure consistency for compound numbers, abbreviations, style drift
7. **Journal overlay** — column-width fit, minimum text size, line weights for the named ACS journal
8. **Output** — layered report: severity table → checklist → narrative → verdict

**Reference files loaded by stage:**
- `references/house-style.md` — template settings (bond lengths, fonts, color palette, arrow catalogue)
- `references/review-checklist.md` — 55-item per-figure checklist
- `references/chemistry-flags.md` — visual chemistry flag catalogue with exact phrasing
- `references/accessibility.md` — legibility, contrast, grayscale, and aspect-ratio checks
- `references/journal-acs.md` — JACS, JOC, OL, JMC, Inorg. Chem., Anal. Chem. overlays
- `references/extraction.md` — how `.docx`/`.pptx`/`.pdf` store figures; edge cases (EMF/WMF, OLE objects)

**Figure extraction script:**
```bash
# Pull all figures from a Word document
python chemdraw-figure-review/scripts/extract_figures.py manuscript.docx ./extracted/

# Pull all figures from a PowerPoint deck
python chemdraw-figure-review/scripts/extract_figures.py talk.pptx ./extracted/

# Rasterize PDF pages at 200 dpi
python chemdraw-figure-review/scripts/extract_figures.py thesis.pdf ./extracted/
```
Outputs a `manifest.json` mapping each image to its document location, plus a `needs-rendering.txt` for EMF/WMF files that require external conversion.

**⚠ Customization required.** The values in `references/house-style.md` are a worked example from one group's ChemDraw template. Before using the skill for real review work, replace bond lengths, font sizes, template names, and color palette RGBs with your group's actual settings. The review *structure* is generic and reusable as-is.

**Scope:** Reviews rendered output only — never edits ChemDraw files. Does not adjudicate chemistry (only flags visual symptoms for human review).

---

### notebooklm-source-curator

**Purpose:** Transform a folder of arbitrarily named source PDFs into a numbered, typed, role-tagged collection ready for upload to NotebookLM (or any retrieval-augmented system). Deliverables: renamed PDFs, a `00_README_Source-Map.md`, a `01_GLOSSARY_<topic>.md`, and a `SourceMap_Audit.csv`.

**Trigger phrases:** "set up a NotebookLM project", "rename these PDFs for NotebookLM", "build a notebook on X", "generate a source map", "audit my notebook sources", "I have a folder of papers — get me ready to upload".

**What the skill provides:**
A 7-step workflow:
1. **Confirm scope** — narrow the notebook to a specific purpose before naming anything
2. **Extract bibliographic identity** — title, author, year, journal, one-sentence abstract per PDF
3. **Classify** — assign `TYPE` (REVIEW, PRIMARY, METHOD, DATA, COUNTERPOINT, DRAFT, …) and `ROLE` (Foundational, Mechanism, SAR, Inhibitor-Discovery, …)
4. **Apply naming convention** — `[NN]_[TYPE]_[AUTHOR-YEAR]_[SHORT-TOPIC]_[ROLE].pdf`
5. **Generate source map and glossary** — controlled vocabulary and answering instructions for NotebookLM
6. **Stage the renamed folder and audit table**
7. **Hand off** — flag ambiguous TYPE assignments, counterpoints, duplicates, and scope concerns

**Cardinal principles:**
- Scope before naming: a broad notebook produces confidently wrong answers
- Counterpoints are evidence hygiene, not noise — always label them, never exclude them
- Every editorial decision is auditable via `SourceMap_Audit.csv`
- User-provided naming guides take precedence over skill defaults

**Domain-agnostic.** Works for medicinal chemistry, synthetic methodology, grant aims, legal expert reports, and graduate seminars. The skill references companion files (`references/`, `playbooks/`, `templates/`) that are not bundled — author them per your domain. The workflow in `SKILL.md` stands alone without them.

---

## Customization

### chemdraw-figure-review
Open `chemdraw-figure-review/references/house-style.md` and replace:
- Bond lengths for each template and scale factor
- Font sizes for atom labels, compound numbers, reagents, and references
- Template names (`slides-bms`, `corey group sett` are examples — use your group's names)
- Color palette RGB values

The review structure (stages 1–8, all reference files, output format) does not need modification.

### notebooklm-source-curator
The SKILL.md workflow stands alone. For richer behaviour, author companion files in your copy of the skill:
- `references/naming-convention.md` — your group's exact naming rules
- `references/source-types.md` — expanded TYPE vocabulary
- `references/notebook-archetypes.md` — project-specific ROLE vocabularies
- `playbooks/workflow.md` — end-to-end execution notes
- `templates/` — source map, glossary, and audit CSV templates

### experimental-writing
No changes needed for ACS-family journals. For RSC, Wiley, or Elsevier venues, note that font and column-width defaults may differ; the data formatting rules (NMR, HRMS, IR) are broadly portable.

### rdkit
No customization needed. If your workflow consistently uses a specific fingerprint type or descriptor subset, you may annotate `SKILL.md` with that preference to avoid repeating it each session.

---

## Platform notes

| Platform | Skills directory |
|---|---|
| macOS / Linux | `~/.claude/skills/` |
| Windows | `%USERPROFILE%\.claude\skills\` |
| Warp (via Warp Drive) | Skills can also be stored in Warp Drive and loaded as rules |

Each skill must be in its own subdirectory with a `SKILL.md` at the root of that subdirectory. Reference files and scripts in subdirectories are loaded by the skill as needed — they do not need to be in the skills root.

---

## License

MIT — see [`LICENSE`](./LICENSE).
