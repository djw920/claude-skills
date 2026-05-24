#!/usr/bin/env python3
"""
extract_figures.py — pull every embedded figure out of a Word, PowerPoint, or
PDF document and dump them into a folder you can read with the file tools.

Usage:
    python extract_figures.py <input-file> <output-dir>

Supports:
    .docx   — unzips the Word container, copies word/media/* and writes a
              manifest mapping each image to the heading/section it appears
              under (best-effort, based on document.xml ordering).
    .pptx   — unzips the PowerPoint container, extracts each slide's media
              into output-dir/slide_<N>/, and writes a manifest mapping
              image -> slide number -> slide title.
    .pdf    — rasterizes each page at 200 dpi using pdftoppm (preferred) or
              pdf2image (fallback), into output-dir/page_<N>.png. Also
              attempts pdfimages -all to extract embedded bitmaps separately.

EMF/WMF figures (common in PowerPoint) are reported but not auto-rendered —
the script writes a "needs-rendering.txt" listing those files. Convert them
with libreoffice --convert-to png or inkscape if available.

ChemDraw OLE objects (oleObject*.bin in word/embeddings/ or ppt/embeddings/)
are reported as un-reviewable.

Designed to be tolerant: if a step fails, log it and continue. The goal is to
get as many figures into output-dir as possible, even if a few are stuck.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


W_NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}


def which(cmd):
    return shutil.which(cmd) is not None


# ----------------------------------------------------------------------------- #
# .docx
# ----------------------------------------------------------------------------- #


def extract_docx(input_path: Path, output_dir: Path) -> dict:
    media_dir = output_dir / "media"
    media_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "format": "docx",
        "source": str(input_path),
        "media": [],
        "warnings": [],
        "unreviewable": [],
    }

    with zipfile.ZipFile(input_path) as zf:
        names = zf.namelist()

        media_names = [n for n in names if n.startswith("word/media/")]
        for name in media_names:
            target = media_dir / Path(name).name
            with zf.open(name) as src, open(target, "wb") as dst:
                shutil.copyfileobj(src, dst)
            manifest["media"].append(
                {"file": str(target.relative_to(output_dir)), "source_in_zip": name}
            )

        # Flag OLE chemdraw embeds as unreviewable
        ole_names = [n for n in names if "embeddings/" in n and n.endswith(".bin")]
        for name in ole_names:
            manifest["unreviewable"].append(
                {
                    "source_in_zip": name,
                    "reason": "OLE object (likely ChemDraw .cdx); requires ChemDraw to render.",
                }
            )

        # Best-effort heading map: walk document.xml and note heading text
        # immediately before each drawing element.
        try:
            with zf.open("word/document.xml") as f:
                tree = ET.parse(f)
            section_map = _docx_section_map(tree.getroot())
            manifest["section_map"] = section_map
        except Exception as e:
            manifest["warnings"].append(f"Could not parse document.xml for sections: {e}")

    # Flag EMF/WMF as needing rendering
    needs = [
        m for m in manifest["media"]
        if m["file"].lower().endswith((".emf", ".wmf"))
    ]
    if needs:
        with open(output_dir / "needs-rendering.txt", "w") as f:
            for n in needs:
                f.write(n["file"] + "\n")
        manifest["warnings"].append(
            f"{len(needs)} EMF/WMF vector files need separate rendering "
            "(libreoffice --convert-to png or inkscape)."
        )

    return manifest


def _docx_section_map(root):
    """Walk the body and produce a list of (heading_text, drawing_count)."""
    body = root.find("w:body", W_NS)
    if body is None:
        return []

    sections = []
    current_heading = "(beginning of document)"
    drawings_in_section = 0

    for child in body:
        tag = child.tag.split("}", 1)[-1]
        if tag != "p":
            continue
        ppr = child.find("w:pPr", W_NS)
        style = None
        if ppr is not None:
            pstyle = ppr.find("w:pStyle", W_NS)
            if pstyle is not None:
                style = pstyle.attrib.get(
                    "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val"
                )

        text_parts = [t.text or "" for t in child.iter(f"{{{W_NS['w']}}}t")]
        text = "".join(text_parts).strip()

        drawings = list(child.iter(f"{{{W_NS['w']}}}drawing"))
        if drawings:
            drawings_in_section += len(drawings)

        if style and style.lower().startswith("heading"):
            if drawings_in_section:
                sections.append({"heading": current_heading, "drawings": drawings_in_section})
            current_heading = text or "(unnamed heading)"
            drawings_in_section = 0

    if drawings_in_section:
        sections.append({"heading": current_heading, "drawings": drawings_in_section})

    return sections


# ----------------------------------------------------------------------------- #
# .pptx
# ----------------------------------------------------------------------------- #


def extract_pptx(input_path: Path, output_dir: Path) -> dict:
    manifest = {
        "format": "pptx",
        "source": str(input_path),
        "slides": [],
        "warnings": [],
        "unreviewable": [],
    }

    with zipfile.ZipFile(input_path) as zf:
        names = zf.namelist()

        slide_names = sorted(
            [n for n in names if re.match(r"ppt/slides/slide\d+\.xml$", n)],
            key=lambda n: int(re.search(r"slide(\d+)\.xml", n).group(1)),
        )

        for slide_name in slide_names:
            slide_num = int(re.search(r"slide(\d+)\.xml", slide_name).group(1))
            slide_dir = output_dir / f"slide_{slide_num:03d}"
            slide_dir.mkdir(parents=True, exist_ok=True)

            slide_info = {
                "slide_number": slide_num,
                "title": _pptx_slide_title(zf, slide_name),
                "media": [],
            }

            rels_name = slide_name.replace(
                "ppt/slides/", "ppt/slides/_rels/"
            ) + ".rels"
            try:
                with zf.open(rels_name) as f:
                    rels_xml = f.read().decode("utf-8")
                referenced = re.findall(
                    r'Target="\.\.\/media\/([^"]+)"', rels_xml
                )
            except KeyError:
                referenced = []

            for media_filename in referenced:
                src_path = f"ppt/media/{media_filename}"
                if src_path not in names:
                    continue
                target = slide_dir / media_filename
                with zf.open(src_path) as src, open(target, "wb") as dst:
                    shutil.copyfileobj(src, dst)
                slide_info["media"].append(str(target.relative_to(output_dir)))

            manifest["slides"].append(slide_info)

        ole_names = [n for n in names if "embeddings/" in n and n.endswith(".bin")]
        for name in ole_names:
            manifest["unreviewable"].append(
                {
                    "source_in_zip": name,
                    "reason": "OLE object (likely ChemDraw .cdx); requires ChemDraw to render.",
                }
            )

    needs = []
    for slide in manifest["slides"]:
        for m in slide["media"]:
            if m.lower().endswith((".emf", ".wmf")):
                needs.append(m)
    if needs:
        with open(output_dir / "needs-rendering.txt", "w") as f:
            for n in needs:
                f.write(n + "\n")
        manifest["warnings"].append(
            f"{len(needs)} EMF/WMF vector files need separate rendering."
        )

    return manifest


def _pptx_slide_title(zf, slide_name):
    try:
        with zf.open(slide_name) as f:
            tree = ET.parse(f)
        # Title text is in a sp with ph type=title or ctrTitle
        for sp in tree.iter(f"{{{W_NS['p']}}}sp"):
            ph = sp.find(".//p:nvSpPr/p:nvPr/p:ph", W_NS)
            if ph is not None and ph.attrib.get("type") in ("title", "ctrTitle"):
                texts = [t.text or "" for t in sp.iter(f"{{{W_NS['a']}}}t")]
                title = "".join(texts).strip()
                return title or "(untitled)"
    except Exception:
        pass
    return "(untitled)"


# ----------------------------------------------------------------------------- #
# .pdf
# ----------------------------------------------------------------------------- #


def extract_pdf(input_path: Path, output_dir: Path) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "format": "pdf",
        "source": str(input_path),
        "pages": [],
        "embedded": [],
        "warnings": [],
    }

    if which("pdftoppm"):
        cmd = [
            "pdftoppm",
            "-r", "200",
            "-png",
            str(input_path),
            str(output_dir / "page"),
        ]
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            for png in sorted(output_dir.glob("page-*.png")):
                manifest["pages"].append(str(png.relative_to(output_dir)))
        except subprocess.CalledProcessError as e:
            manifest["warnings"].append(
                f"pdftoppm failed: {e.stderr.decode(errors='replace')[:500]}"
            )
    else:
        # Fallback: pdf2image (Python)
        try:
            from pdf2image import convert_from_path  # type: ignore
            images = convert_from_path(str(input_path), dpi=200)
            for i, img in enumerate(images, start=1):
                target = output_dir / f"page-{i:03d}.png"
                img.save(target, "PNG")
                manifest["pages"].append(str(target.relative_to(output_dir)))
        except Exception as e:
            manifest["warnings"].append(
                f"Neither pdftoppm nor pdf2image worked: {e}. "
                "Install poppler-utils or pip install pdf2image."
            )

    # Optionally extract embedded bitmaps separately
    if which("pdfimages"):
        embedded_dir = output_dir / "embedded"
        embedded_dir.mkdir(exist_ok=True)
        cmd = [
            "pdfimages",
            "-all",
            str(input_path),
            str(embedded_dir / "img"),
        ]
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            for img in sorted(embedded_dir.glob("img-*")):
                manifest["embedded"].append(str(img.relative_to(output_dir)))
        except subprocess.CalledProcessError as e:
            manifest["warnings"].append(
                f"pdfimages failed: {e.stderr.decode(errors='replace')[:500]}"
            )

    return manifest


# ----------------------------------------------------------------------------- #
# main
# ----------------------------------------------------------------------------- #


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("input", type=Path, help="Input file: .docx, .pptx, or .pdf")
    parser.add_argument("output_dir", type=Path, help="Where to write extracted figures")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Input not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    args.output_dir.mkdir(parents=True, exist_ok=True)

    suffix = args.input.suffix.lower()
    if suffix == ".docx":
        manifest = extract_docx(args.input, args.output_dir)
    elif suffix == ".pptx":
        manifest = extract_pptx(args.input, args.output_dir)
    elif suffix == ".pdf":
        manifest = extract_pdf(args.input, args.output_dir)
    else:
        print(f"Unsupported file type: {suffix}", file=sys.stderr)
        sys.exit(2)

    manifest_path = args.output_dir / "manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"Wrote {manifest_path}")
    if manifest.get("warnings"):
        print("\nWarnings:")
        for w in manifest["warnings"]:
            print(f"  - {w}")
    if manifest.get("unreviewable"):
        print(f"\n{len(manifest['unreviewable'])} item(s) marked un-reviewable.")


if __name__ == "__main__":
    main()
