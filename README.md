# Claude Skills — Chemistry & Research Workflow

A small collection of [Claude skills](https://www.anthropic.com/news/skills)
for chemistry research, manuscript work, and source-document curation. All
four skills are domain-relevant for synthetic and medicinal chemistry but
have been written to be reusable across groups.

## Skills

| Skill | Purpose | Status |
|---|---|---|
| [`rdkit/`](./rdkit) | Cheminformatics toolkit reference — SMILES/SDF parsing, descriptors, fingerprints, substructure search, 2D/3D generation, similarity, reactions. | Generic — ready to use. |
| [`experimental-writing/`](./experimental-writing) | Write, format, and edit organic-chemistry experimental procedures and compound characterization data to ACS journal standards. Manuscript and thesis modes. | Generic — ready to use. |
| [`chemdraw-figure-review/`](./chemdraw-figure-review) | Audit ChemDraw figures and schemes in `.docx`, `.pptx`, and `.pdf` documents against a house style, ACS journal conventions, IUPAC graphical recommendations, and accessibility rules. | **Customize `references/house-style.md`** with your group's actual settings before use. |
| [`notebooklm-source-curator/`](./notebooklm-source-curator) | Curate, rename, and structure source documents for a NotebookLM project (or any retrieval-augmented system) so that retrieval is precise, claims are grounded, and the evidence base is auditable. | Generic — companion `references/`, `playbooks/`, and `templates/` files are recommended but not bundled; author your own. |

## Installing in Claude

Skills live under `~/.claude/skills/` (or your platform's equivalent). To
install one of these:

```bash
cp -r chemdraw-figure-review ~/.claude/skills/
```

After install, restart Claude (or your Claude client) so it re-indexes the
skills directory.

## Customization notes

- **`chemdraw-figure-review`** ships with example values (bond lengths,
  font sizes, color palette, slide-template names) drawn from one
  group's working ChemDraw template. They are deliberately concrete so
  the skill has something to check against, but they are example-only.
  Replace the values in `references/house-style.md` with your group's
  settings before doing real review work. The *structure* of the
  review (extract → identify → style → chemistry flags → accessibility →
  document-level → journal overlay → layered output) is reusable as-is.

- **`notebooklm-source-curator`** SKILL.md references companion files
  under `references/`, `playbooks/`, and `templates/`. Those companion
  files are not bundled — author them per your domain (chemistry,
  biology, law, pedagogy). The workflow in SKILL.md stands alone.

- **`experimental-writing`** is calibrated to ACS-family journal
  conventions (JOC, JACS, Org. Lett., JMC). If your target venue uses
  different conventions (RSC, Wiley, Elsevier), the bulk of the
  guidance still applies but font and formatting defaults may need to
  be adjusted.

## License

MIT — see [`LICENSE`](./LICENSE).
