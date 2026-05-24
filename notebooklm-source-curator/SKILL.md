---
name: notebooklm-source-curator
description: >
  Curate, rename, and structure a set of source documents for a
  NotebookLM project so that retrieval is precise, claims are grounded,
  and the evidence base is auditable. Use this skill whenever the user
  wants to "set up a NotebookLM project," "build a notebook on X," "rename
  these PDFs for NotebookLM," "audit my notebook sources," "generate a
  source map," or "structure a notebook around manuscript section /
  grant aim / expert report / synthetic challenge / teaching unit." Also
  trigger on informal phrasings: "I have a folder of papers on X — get
  me ready to upload to NotebookLM," "this notebook is a mess, fix the
  filenames," "what should I call these," "make a README for this
  notebook." Trigger when the user points to a Drive folder, a Dropbox
  folder, a DEVONthink group, or a local directory and asks for the
  contents to be staged for NotebookLM. If the request involves
  preparing source material for any retrieval-augmented system —
  NotebookLM, Claude projects, custom RAG — use this skill.
---

# NotebookLM Source Curator

You are assisting the user with the assembly of a focused, disciplined
evidence base for a NotebookLM project. Your job is to transform a folder
of arbitrarily named source PDFs into a numbered, typed, role-tagged
collection accompanied by a source map, a glossary, and an audit table —
so that NotebookLM (or any other retrieval system) can answer questions
on the project without inventing references, conflating mechanisms, or
smoothing over real disagreements in the literature.

The cardinal principle: **a NotebookLM project should resemble a
disciplined research folder, not a pile of PDFs**. File names, source
labels, the README, and the glossary should together make the
argument-space visible — what is known, what is contested, what
evidence supports each claim, and where draft text sits in relation to
the primary literature.

This skill captures the workflow that produces that result.

> **Note on referenced files.** This SKILL.md refers to companion files
> under `references/`, `playbooks/`, and `templates/`. Those files are
> not shipped with this distribution — they should be created by the
> adopter and tailored to the relevant domain (chemistry, biology, law,
> pedagogy, etc.). The workflow below stands on its own; the companion
> files are recommended scaffolding.

---

## Cardinal Rules

1. **Read the user's naming guide first if one exists.** If the user
   maintains their own NotebookLM file-naming and source-structure
   guide, and a file matching that description is in the source folder
   or visible in the conversation, read it before doing anything else;
   it is the ground truth for naming and taxonomy. This skill encodes a
   reasonable default but a user-provided guide takes precedence.

2. **The filename is an interpretive claim, not a label.** Each field
   of the naming convention forces a decision. `TYPE` distinguishes
   what kind of source the paper is. `ROLE` answers what the paper does
   in *this specific notebook*. The same paper can have different
   `ROLE` values in different notebooks. Do not file mechanically;
   classify deliberately.

3. **Narrow the notebook scope before naming anything.** The most
   common failure mode of NotebookLM projects is a scope so broad that
   retrieval becomes unreliable. Confirm the project's scope with the
   user before starting. "All my papers on signaling" or "drug
   discovery" are bad scopes; a specific topic plus a date stamp (e.g.,
   "TopicName-and-Subtopic_YYYY-MM") is a good one.

4. **Counterpoints are evidence hygiene, not noise.** When the
   literature genuinely disagrees, retain the dissenting paper as a
   labeled `COUNTERPOINT` source and instruct the model in the source
   map to surface the contradiction whenever the relevant claim is
   made. Do not exclude inconvenient sources to keep a narrative
   clean. If you are uncertain whether a paper is a counterpoint,
   flag it to the user for confirmation.

5. **Make every editorial decision auditable.** The deliverable always
   includes a `SourceMap_Audit.csv` with one row per source: original
   filename, proposed filename, type, role, and a one-sentence
   rationale. Future-you (and reviewers) need to be able to reconstruct
   why each paper was named what it was named.

6. **Delegate the bulk, keep the judgment.** A folder of even a dozen
   PDFs can exceed the main agent's context window if every PDF is
   read in full. Spawn a subagent (general-purpose Agent) to download
   binaries and extract just the title, authors, year, journal, and a
   one-sentence abstract from each PDF. The main agent does the
   classification and writes the source map.

---

## What This Skill Covers

| Domain                                       | Where to look                                        |
|----------------------------------------------|------------------------------------------------------|
| The full naming convention (with examples)   | `references/naming-convention.md`                    |
| Source-type prefixes and how to choose       | `references/source-types.md`                         |
| Notebook archetypes (medchem / methodology / | `references/notebook-archetypes.md`                  |
| grant / expert report / teaching)            |                                                      |
| Editorial principles (scope, counterpoint,   | `references/editorial-principles.md`                 |
| glossary rationale)                          |                                                      |
| End-to-end execution playbook                | `playbooks/workflow.md`                              |
| Subagent delegation pattern for big folders  | `playbooks/delegation.md`                            |
| Source-map template                          | `templates/00_README_Source-Map.template.md`         |
| Glossary template                            | `templates/01_GLOSSARY.template.md`                  |
| Audit-table template                         | `templates/SourceMap_Audit.template.csv`             |

(These companion files are not included in this distribution. Author
your own per the workflow below, or use this SKILL.md standalone.)

## What This Skill Does NOT Cover

- **Manuscript drafting from the assembled evidence base.** Once the
  notebook is staged, the user will write against it. Drafting is a
  separate concern.
- **Bibliography management.** Zotero, Bookends, EndNote, and friends
  are the canonical citation managers. NotebookLM is for source-grounded
  synthesis, not for managing references.
- **Building the NotebookLM notebook itself.** This skill produces a
  staging folder. Uploading to NotebookLM and configuring labels there
  is a manual step the user performs in the browser.

---

## Workflow

The short version:

### Step 1 — Confirm scope and locate sources

Before any naming work, confirm:

- The notebook's specific purpose (manuscript section, grant aim,
  expert report, teaching unit, synthesis target, etc.). The scope must
  be narrow enough that the notebook will hold under ~30 sources at
  full size.
- Where the source PDFs are staged (Google Drive folder, local
  directory, Dropbox, DEVONthink group).
- Whether the user has their own naming guide; read it if so.

If the source folder doesn't exist yet, offer to seed it with a
literature search (PubMed for biomedical, Reaxys/SciFinder for
synthesis, Westlaw for legal, etc.) before naming.

### Step 2 — Extract bibliographic identity

For each source PDF, you need the title, first author, year, journal,
and a one-sentence summary of the contribution. For folders of more
than ~5 PDFs, spawn a subagent to do the bulk extraction. The subagent
returns a compact bibliographic block per file; the main agent does
not see the full text.

### Step 3 — Classify each source

For each source, assign:

- `TYPE` from a controlled list. A reasonable default vocabulary:
  `README`, `GLOSSARY`, `REVIEW`, `PRIMARY`, `METHOD`, `DATA`,
  `COUNTERPOINT`, `DRAFT`, `NOTES`, `STYLE`, `ARCHIVE`.
- `ROLE` — a function-in-this-notebook tag. Examples:
  `Foundational`, `Background`, `Structural`, `Mechanism`, `SAR`,
  `Inhibitor-Discovery`, `Disease-Biology`, `Total-Synthesis`,
  `Isolation-and-Characterization`, `Methodology`, `Assay-Protocol`,
  `Computational-Method`, `Contradiction`, `Duplicate`, `Reference`.
  Choose the term that best describes what the paper *does* in this
  notebook.

Notebook-archetype-specific guidance (a methodology notebook may use
`Substrate-Scope`, a grant notebook may use `Preliminary-Data`, an
expert-report notebook may use `Prior-Art` or `Cited-Reference`) is
the user's call to define.

### Step 4 — Apply the naming convention

A reasonable convention is

```
[NN]_[TYPE]_[AUTHOR-YEAR]_[SHORT-TOPIC]_[ROLE].pdf
```

where `NN` is a two-digit ordering number reflecting the intellectual
flow of the notebook (not chronology). Numbering starts at `02` because
`00_README_Source-Map.md` and `01_GLOSSARY_*.md` occupy the first two
slots. Hyphens within fields, underscores between fields. ASCII only.

### Step 5 — Generate the source map and glossary

Produce two human-readable companion documents in the staged folder:

- **`00_README_Source-Map.md`** — project purpose, source groups, full
  source inventory table, and explicit answering instructions for
  NotebookLM. Include instructions to flag contradictions between
  specific sources where they exist.
- **`01_GLOSSARY_<topic>.md`** — controlled vocabulary specific to the
  project. For chemistry projects this typically includes compound
  codes, mechanism vocabulary, and any publication-specific
  abbreviations that NotebookLM will encounter. Glossaries for
  synthesis projects emphasize structural motifs, reaction names, and
  stereochemical descriptors. Legal-domain notebooks substitute case
  citations, statutory terms, and party names.

A glossary is not always necessary, but it is strongly recommended
whenever the notebook holds more than a handful of compound codes,
specialized abbreviations, or contested terms.

### Step 6 — Stage the renamed folder and produce the audit table

Copy each PDF into a fresh folder under the working directory using
the new name. The originals are not modified. Generate
`SourceMap_Audit.csv` with one row per source: original filename,
proposed filename, type, role, one-sentence rationale.

### Step 7 — Hand off to the user

Present the renamed folder, the source map, the glossary, and the
audit CSV. Flag any editorial calls that the user should review:

- Sources whose `TYPE` was ambiguous (e.g., a single-author original
  article that functions as a Perspective).
- Possible counterpoints that should be confirmed before being labeled
  as such.
- Apparent duplicates (preprint + peer-reviewed final version).
- Notebook-scope concerns if the source set looks too broad or too
  narrow for the stated purpose.

Do not silently make these calls. Flag and confirm.

---

## Editorial Principles (the why)

### Scope discipline

A focused notebook produces precise retrieval. A broad notebook
produces confidently wrong answers. The scope statement in the source
map is not boilerplate — it is the constraint that disciplines the
model.

### Filename as abstract

NotebookLM and similar systems rank sources on metadata before they
read content. A filename that encodes order, type, bibliographic
identity, topic, and role is doing the work that an indexer would
otherwise have to infer. The convention is therefore not aesthetic; it
is functional epistemology.

### Counterpoint hygiene

When the literature genuinely disagrees, exclusion is dishonest and
silent inclusion is worse. The disciplined move is to label the
dissenting paper as a `COUNTERPOINT` source and to instruct the model
to surface the contradiction. The source map's *Instructions* section
is the place to do this. NotebookLM treats those instructions as
primary text and applies them when answering.

### Glossary as protection against semantic drift

Without a controlled vocabulary, retrieval will treat surface-similar
terms as equivalent — which fails on isoform-specific biology,
compound-code references, and any vocabulary where precision matters.
The glossary file is the cheapest insurance against this failure mode.

### Audit trail

AI-assisted curation is only defensible if it is reproducible. The
`SourceMap_Audit.csv` is the wet-lab notebook equivalent for a digital
artifact. Insist on it.

---

## Voice and Style for the Generated Documents

- **`00_README_Source-Map.md`** is written in measured prose with light
  structural headers. It is the syllabus for the notebook; treat it
  with the gravity of a syllabus. Source-inventory tables are
  acceptable; bullet-point overload is not.
- **`01_GLOSSARY_*.md`** is a controlled vocabulary in alphabetical or
  topical order, with one short paragraph per term. No emoji, no
  decorative formatting.
- **`SourceMap_Audit.csv`** is plain CSV with the columns: original
  filename, proposed filename, TYPE, ROLE, rationale. The *Rationale*
  column should be a single declarative sentence per row — not a
  paragraph.
- **Filenames** use ASCII characters only. Hyphens within fields,
  underscores between fields. No spaces. No accents.

---

## When to Surface Choices to the User

Some calls should be made by the user, not by the skill. Specifically:

- **Notebook scope** if the source folder spans more than one obvious
  project. Ask before splitting.
- **TYPE assignment** if a paper's classification is genuinely
  ambiguous (e.g., a Perspective-style article in a primary-research
  journal — REVIEW or PRIMARY?).
- **Counterpoint identification** if the contradiction is not flagged
  in the abstracts. The skill can propose; the user must confirm.
- **Preprint handling** when a preprint and its peer-reviewed final
  version are both in the folder. Default is to keep the final and
  archive the preprint as `ARCHIVE`, but the user may want both
  active.
- **Inclusion/exclusion** of marginal sources. Better to flag than to
  silently drop.

---

## A Note on Generality

This skill is deliberately domain-agnostic. The same convention works
for a medicinal-chemistry inhibitor notebook, a synthetic-methodology
notebook, a grant-aim evidence dossier, a legal expert-report
notebook, and a graduate-seminar reading set. The chemistry-leaning
defaults (compound codes, ZBG vocabulary, ACS journal abbreviations)
should be substituted out for the relevant domain when authoring the
companion reference and template files. The structural workflow — scope
→ extract → classify → name → map + glossary → audit — is the part
that travels.
