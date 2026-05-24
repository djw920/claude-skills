# Extracting Figures From Word, PowerPoint, and PDF

You cannot review what you cannot see. The figures in `.docx`, `.pptx`, and `.pdf` files are stored inside the binary container — to look at them, you have to extract them as standalone images. This file describes how, plus the edge cases.

A helper script is provided: `scripts/extract_figures.py`. Use it as the default approach. The notes below are for when the helper falls short or you need to know what is happening under the hood.

---

## How `.docx` and `.pptx` actually store figures

Both formats are zipped XML containers (Office Open XML). Embedded images live in the `media/` subfolder:

- `.docx`: images in `word/media/`
- `.pptx`: images in `ppt/media/`

Filenames inside `media/` are typically `image1.png`, `image2.emf`, `image3.tiff`, etc. — numbered in the order they were inserted, which usually but not always matches the order they appear in the document.

ChemDraw can be inserted into Word/PowerPoint several ways:

1. **As a vector EMF/WMF object** (Mac PowerPoint via paste). Stored as `.emf`/`.wmf`. These are vector and scale cleanly — but they need to be rasterized for you to view.
2. **As a high-quality PNG** (PowerPoint default copy/paste from ChemDraw on Mac). Easy to view directly.
3. **As a TIFF** (the workaround for slides going to PC). Easy to view directly.
4. **As a JPEG** (last-resort fallback). Easy to view but lossy — flag the loss as a quality issue.
5. **As an embedded ChemDraw object** (`.cdx` payload inside the document). Cannot be rendered without ChemDraw. Recognize this and report it as un-reviewable.

## How a `.pdf` stores figures

Two cases:

- **Vector ChemDraw passthrough**: the figure is part of the PDF's vector content. Extract by rasterizing the page (the easier route) or extracting embedded images (`pdfimages`).
- **Pasted bitmap**: the figure is an embedded image in the PDF. Extracted via `pdfimages`.

For review purposes, *rasterizing each page at 200–300 dpi* and reading the page images is usually sufficient. You can identify figures by their location on the page and crop later if needed.

---

## Using `scripts/extract_figures.py`

```
python scripts/extract_figures.py <input-file> <output-dir>
```

- For `.docx`: unzips the Word container, copies `word/media/*` into `<output-dir>/media/`, and writes a manifest mapping each image to the section/heading it appears under (best-effort, based on `document.xml` ordering).
- For `.pptx`: unzips the PowerPoint container, extracts each slide's media into `<output-dir>/slide_<N>/`, and writes a manifest mapping each image to its slide number and slide title.
- For `.pdf`: rasterizes each page at 200 dpi using `pdftoppm` (if available) or `pdf2image` (Python), saving to `<output-dir>/page_<N>.png`. Optionally extracts embedded images using `pdfimages` to `<output-dir>/embedded/` for separate inspection.
- For `.emf`/`.wmf` files extracted from a `.docx`/`.pptx`: attempts to rasterize via `libreoffice --convert-to png` if available, or `inkscape` as a fallback. If neither is available, the script reports the file but leaves it un-rasterized; flag those as un-reviewable.

The manifest is a small JSON file `<output-dir>/manifest.json` you can read to know what came from where.

## Manual extraction if the script is unavailable

### From `.docx`

```bash
unzip -o my-doc.docx -d my-doc-unzipped
ls my-doc-unzipped/word/media/
```

The order of images in `media/` is usually but not always the order they appear in the document. To map images to context, also inspect `my-doc-unzipped/word/document.xml` and search for `r:embed=` and surrounding text.

### From `.pptx`

```bash
unzip -o my-deck.pptx -d my-deck-unzipped
ls my-deck-unzipped/ppt/media/
ls my-deck-unzipped/ppt/slides/    # one XML per slide
```

Each `slide<N>.xml` references the media files used on that slide. Per-slide rels files (`ppt/slides/_rels/slide<N>.xml.rels`) map relationship IDs to media filenames.

### From `.pdf`

```bash
# Rasterize every page at 200 dpi:
pdftoppm -r 200 -png my-doc.pdf page

# Or extract embedded images (different content — only the bitmap embeds, not vector content):
pdfimages -all my-doc.pdf embedded
```

`pdftoppm` gives you what the page actually looks like (vector + raster combined). `pdfimages` gives you only the embedded bitmaps. For review purposes, prefer `pdftoppm` and crop to the figure region if you need to focus.

---

## Edge cases

### EMF / WMF vector objects (PowerPoint, Mac → Windows)

If the extracted media folder contains `.emf` or `.wmf` files, these are Windows-native vector formats that you cannot view directly. Convert:

```bash
libreoffice --headless --convert-to png my-figure.emf
# or
inkscape my-figure.emf --export-type=png --export-filename=my-figure.png
```

If neither tool is available, report the figure as un-reviewable and recommend the user export it manually.

### ChemDraw OLE objects (`oleObject1.bin` etc.)

If the document contains `.cdx`-bearing OLE binaries (visible as `oleObject*.bin` in `word/embeddings/` or `ppt/embeddings/`), you cannot open these without ChemDraw. The user must either:

- Open the document in Word/PowerPoint and copy each ChemDraw object to a PNG/TIFF, or
- Re-export the document with ChemDraw figures rasterized.

Report these as un-reviewable in the output and explicitly name them as a limitation. Do not attempt to review based on caption text alone.

### Multi-page PDFs

For long PDFs (>20 pages), rasterize all pages but only fully review the pages the user has asked about. Skim the rest for orientation. Token budget matters — a 100-page thesis rasterized at 300 dpi is a lot of pixel data. Drop to 150 dpi for the orientation pass and re-rasterize specific pages at 300 dpi for the deep review.

### Figures that span a page break

Sometimes a scheme is split across two pages of a PDF. The rasterizer gives you two half-figures. Note the split in your output (and recommend the figure be reflowed to fit on one page).

### Tables that contain ChemDraw figures

Common in JMC-style SAR figures. The table itself comes through as text/cells (not as an image), but the structures inside cells are individual images. Extraction will pull them as separate images. Reassemble mentally: each row is one structure, with its associated data in the surrounding cells.

### Cover/abstract images

Often these are the highest-resolution figures in a manuscript and the most reviewer-visible. Treat them as a separate, slightly stricter pass — the cover image is what most people will see if the paper is featured.

---

## After extraction: what you should have

For a `.docx`:
- A folder of images (PNG, TIFF, JPEG, EMF).
- A manifest mapping each image to a section or page.
- Notes on which (if any) images failed to extract or render.

For a `.pptx`:
- A folder per slide, each with the images that slide uses.
- A manifest mapping image → slide number → slide title.
- Notes on un-rendered EMF/WMF or OLE figures.

For a `.pdf`:
- Rasterized page images at 200 dpi.
- Optional: extracted embedded bitmaps.
- A page-to-figure mapping the user can refer to in the output.

Once you have these, you can run the per-figure review.

---

## What to record in the output

Always tell the user:

1. How many figures you extracted.
2. How many figures could not be extracted (and why).
3. Which figures you reviewed and which you skipped.

If extraction silently lost figures, the review is incomplete. Better to under-promise than over-claim.
