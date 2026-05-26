#!/usr/bin/env python3
"""Build PDF and EPUB books from MkDocs wiki documentation.

Preprocesses MkDocs-flavored markdown (admonitions, code blocks, mermaid diagrams,
images) and assembles chapters into a single document that pandoc + xelatex converts
to PDF/EPUB.

Usage:
    python build_book.py            # Genera el libro completo
    python build_book.py --preview  # Genera solo 2 secciones para iterar rápido
"""

from __future__ import annotations

import argparse
import base64
import logging
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zlib
from pathlib import Path
from typing import TypeAlias

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Type aliases
# ---------------------------------------------------------------------------

Section: TypeAlias = tuple[str, list[str]]
Chapter: TypeAlias = tuple[str, list[Section]]
BookStructure: TypeAlias = list[Chapter]

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PROJECT_NAME = "wiki-personal"
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR / "output"
MERMAID_CACHE = OUTPUT_DIR / ".mermaid"

KROKI_BASE_URL = "https://kroki.io/mermaid"
HTTP_TIMEOUT_SECONDS = 15
MERMAID_PNG_SCALE = 2.0
HTTP_USER_AGENT = "Mozilla/5.0"

PANDOC_METADATA: dict[str, str] = {
    "title": "La Wiki de un Ingeniero",
    "author": "Daniel Bazo Correa",
    "date": "2026",
    "lang": "es",
}

PDF_ENGINE = "xelatex"
PDF_VARIABLES: dict[str, str] = {
    "documentclass": "report",
    "geometry:margin": "2.5cm",
    "fontsize": "11pt",
    "mainfont": "Latin Modern Roman",
    "sansfont": "Latin Modern Sans",
    "monofont": "Latin Modern Mono",
    "monofontoptions": "Scale=0.85",
}

# ---------------------------------------------------------------------------
# Book structure
# ---------------------------------------------------------------------------

BOOK_STRUCTURE: BookStructure = [
    ("Sistemas operativos", [
        ("Linux", [
            "01_operative_systems/01_linux/section_1_fundamentals.md",
            "01_operative_systems/01_linux/section_2_administration.md",
            "01_operative_systems/01_linux/section_3_networking.md",
        ]),
    ]),
    ("Herramientas de desarrollo", [
        ("Git", [
            "02_dev_tools/01_git/section_1_fundamentals.md",
            "02_dev_tools/01_git/section_2_workflows.md",
            "02_dev_tools/01_git/section_3_practical_cases.md",
        ]),
        ("Scripting", [
            "02_dev_tools/02_scripting/section_1_bash.md",
            "02_dev_tools/02_scripting/section_2_makefile.md",
        ]),
    ]),
    ("Lenguajes de programación", [
        ("Python", [
            "03_programming/01_python/section_1_environments.md",
            "03_programming/01_python/section_2_fundamentals.md",
            "03_programming/01_python/section_3_libraries.md",
        ]),
        ("Rust", [
            "03_programming/02_rust/section_1_fundamentals.md",
        ]),
        ("CUDA", [
            "03_programming/03_cuda/section_1_fundamentals.md",
            "03_programming/03_cuda/section_2_cuda_c.md",
            "03_programming/03_cuda/section_3_cuda_python.md",
        ]),
        ("Desarrollo web", [
            "03_programming/04_web/section_1_fundamentals.md",
        ]),
    ]),
    ("Ingeniería de software", [
        ("Estructuras de datos y algoritmos", [
            "04_software_engineering/section_1_data_structure.md",
        ]),
        ("Diseño y código sostenible", [
            "04_software_engineering/section_2_sustainable_code.md",
        ]),
    ]),
    ("Infraestructura y servicios", [
        ("Bases de datos", [
            "05_infrastructure/01_databases/section_1_sql.md",
        ]),
        ("Cloud", [
            "05_infrastructure/02_cloud/section_1_fundamentals.md",
            "05_infrastructure/02_cloud/section_2_aws.md",
        ]),
    ]),
    ("DevOps", [
        ("Contenedores", [
            "06_devops/section_1_containers.md",
        ]),
        ("Orquestadores", [
            "06_devops/section_2_orchestrators.md",
        ]),
        ("CI/CD", [
            "06_devops/section_3_ci_cd.md",
        ]),
    ]),
    ("Machine learning", [
        ("Fundamentos y estadística", [
            "07_machine_learning/section_1_fundamentals.md",
            "07_machine_learning/section_2_statistics.md",
        ]),
        ("Modelos supervisados", [
            "07_machine_learning/section_3_supervised_models.md",
        ]),
        ("Agrupación y evaluación", [
            "07_machine_learning/section_4_clustering.md",
            "07_machine_learning/section_5_evaluation.md",
            "07_machine_learning/section_6_dimensionality_reduction.md",
        ]),
        ("Técnicas avanzadas", [
            "07_machine_learning/section_7_advanced.md",
        ]),
    ]),
    ("Deep learning", [
        ("Fundamentos", [
            "08_deep_learning/section_1_fundamentals.md",
            "08_deep_learning/section_2_math.md",
            "08_deep_learning/section_3_linear_models.md",
            "08_deep_learning/section_4_neural_networks.md",
        ]),
        ("Arquitecturas", [
            "08_deep_learning/section_5_cnn.md",
            "08_deep_learning/section_6_sequential_models.md",
            "08_deep_learning/section_7_other_paradigms.md",
        ]),
        ("Aplicaciones", [
            "08_deep_learning/section_8_generative_ai.md",
            "08_deep_learning/section_9_graph_neural_networks.md",
            "08_deep_learning/section_10_reinforcement_learning.md",
            "08_deep_learning/section_11_agents.md",
        ]),
        ("Librerías", [
            "08_deep_learning/libraries/jax.md",
            "08_deep_learning/libraries/pytorch.md",
            "08_deep_learning/libraries/tensorflow.md",
        ]),
    ]),
    ("MLOps", [
        ("Fundamentos", [
            "09_mlops/section_1_fundamentals.md",
        ]),
        ("Gestión de experimentos", [
            "09_mlops/section_2_experiment_management.md",
        ]),
        ("Despliegue y distribución", [
            "09_mlops/section_3_deployment.md",
        ]),
    ]),
    ("Desarrollo profesional", [
        ("Guía de empleo", [
            "10_career/cv_guide.md",
        ]),
    ]),
    ("Bibliografía", [
        ("Referencias", [
            "bibliography.md",
        ]),
    ]),
]

PREVIEW_STRUCTURE: BookStructure = [
    ("Herramientas de desarrollo", [
        ("Git", ["02_dev_tools/01_git/section_1_fundamentals.md"]),
    ]),
    ("DevOps", [
        ("Contenedores", ["06_devops/section_1_containers.md"]),
    ]),
]

ADMONITION_LABELS: dict[str, str] = {
    "note": "Nota",
    "tip": "Consejo",
    "warning": "Advertencia",
    "danger": "Peligro",
    "info": "Información",
    "example": "Ejemplo",
    "question": "Pregunta",
    "abstract": "Resumen",
    "success": "Éxito",
    "failure": "Fallo",
    "bug": "Bug",
    "quote": "Cita",
}

ADMONITION_COLORS: dict[str, str] = {
    "note": "adm-note",
    "tip": "adm-tip",
    "warning": "adm-warning",
    "danger": "adm-danger",
    "info": "adm-info",
    "example": "adm-example",
    "question": "adm-info",
    "abstract": "adm-note",
    "success": "adm-tip",
    "failure": "adm-danger",
    "bug": "adm-danger",
    "quote": "adm-note",
}

# Regex patterns compiled once for reuse
_ADMONITION_RE = re.compile(
    r"^( *)(!!!|(?:\?\?\?\+?))\s*(\w+)\s*(?:\"([^\"]*)\")?", re.MULTILINE
)
_BLOCKQUOTE_ADMONITION_RE = re.compile(
    r"^(>+ *)(!!!|\?\?\?\+?)\s*(\w+)\s*(?:\"([^\"]*)\")?", re.MULTILINE
)
_CODE_BLOCK_ATTRS_RE = re.compile(
    r"```(\w+)\s+(?:linenums=\"?\d+\"?\s*(?:hl_lines=\"[^\"]*\")?)\s*\n"
)
_IMAGE_WITH_ATTRS_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)\{[^}]*\}")
_IMAGE_RELATIVE_RE = re.compile(r"!\[([^\]]*)\]\((\.\.?/[^)]+)\)")
_HEADING_NEEDS_BLANK_LINE_RE = re.compile(r"([^\n])\n(#{1,6} )")
_HEADING_SHIFT_RE = re.compile(r"^(#{1,5}) ", re.MULTILINE)
_FRONTMATTER_TITLE_RE = re.compile(r"^title:\s*(.+)$", re.MULTILINE)
_MERMAID_BLOCK_RE = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)


# ---------------------------------------------------------------------------
# Markdown preprocessing
# ---------------------------------------------------------------------------


def _strip_frontmatter(content: str) -> str:
    """Remove YAML frontmatter block (---...---) from the beginning of content."""
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            return content[end + 3:].lstrip("\n")
    return content


def _build_admonition_style_latex(color: str) -> str:
    """Generate the LaTeX raw inline that sets the admonition border style."""
    return (
        f"`\\global\\mdfdefinestyle{{admonitionstyle}}"
        f"{{linewidth=2pt,linecolor={color},backgroundcolor={color}!5,"
        f"leftmargin=0pt,rightmargin=0pt,"
        f"innerleftmargin=10pt,innerrightmargin=10pt,"
        f"innertopmargin=8pt,innerbottommargin=8pt,"
        f"skipabove=10pt,skipbelow=10pt,"
        f"topline=false,rightline=false,bottomline=false,"
        f"nobreak=true}}`{{=latex}}"
    )


def _convert_admonitions_single_pass(content: str) -> str:
    """Convert MkDocs admonitions to LaTeX-styled blockquotes.

    Handles ``!!! type "title"``, ``!!!type "title"``, and ``???+ type "title"``
    syntax. Injects a raw LaTeX command before each blockquote to set the border
    color based on admonition type.
    """
    lines = content.split("\n")
    result: list[str] = []
    i = 0

    while i < len(lines):
        match = re.match(
            r"^( *)(!!!|(?:\?\?\?\+?))\s*(\w+)\s*(?:\"([^\"]*)\")?", lines[i]
        )
        if match:
            indent = match.group(1)
            adm_type = match.group(3)
            title = match.group(4)
            label = title or ADMONITION_LABELS.get(adm_type, adm_type.capitalize())
            content_indent = indent + "    "
            color = ADMONITION_COLORS.get(adm_type, "adm-note")

            result.append("")
            result.append(_build_admonition_style_latex(color))
            result.append("")
            result.append(f"{indent}> **{label}**")
            result.append(f"{indent}>")

            i += 1
            while i < len(lines):
                if lines[i].startswith(content_indent):
                    result.append(f"{indent}> {lines[i][len(content_indent):]}")
                elif lines[i].strip() == "":
                    result.append(f"{indent}>")
                else:
                    break
                i += 1
            result.append("")
        else:
            result.append(lines[i])
            i += 1

    return "\n".join(result)


def _convert_admonitions(content: str) -> str:
    """Convert admonitions with two passes to handle nested admonitions.

    The first pass converts top-level admonitions. The second pass catches any
    admonitions that were nested inside the content of a top-level admonition
    (now exposed after the first pass flattened the outer one).
    """
    content = _convert_admonitions_single_pass(content)
    content = _convert_admonitions_single_pass(content)
    return content


def _convert_blockquote_admonitions(content: str) -> str:
    """Convert residual admonitions nested inside blockquotes."""
    lines = content.split("\n")
    result: list[str] = []
    i = 0

    while i < len(lines):
        match = re.match(
            r"^(>+ *)(!!!|\?\?\?\+?)\s*(\w+)\s*(?:\"([^\"]*)\")?", lines[i]
        )
        if match:
            prefix = match.group(1)
            adm_type = match.group(3)
            title = match.group(4)
            label = title or ADMONITION_LABELS.get(adm_type, adm_type.capitalize())
            content_indent = prefix + "    "

            result.append(prefix)
            result.append(f"{prefix}**{label}**")
            result.append(prefix)

            i += 1
            while i < len(lines):
                if lines[i].startswith(content_indent):
                    result.append(f"{prefix}{lines[i][len(content_indent):]}")
                elif lines[i].rstrip() == prefix.rstrip() or lines[i].strip() == "":
                    result.append(prefix)
                else:
                    break
                i += 1
            result.append(prefix)
        else:
            result.append(lines[i])
            i += 1

    return "\n".join(result)


def _fix_code_blocks(content: str) -> str:
    """Remove MkDocs code block attributes (linenums, hl_lines)."""
    return _CODE_BLOCK_ATTRS_RE.sub(r"```\1\n", content)


def _resolve_image_path(alt: str, src: str, md_file: Path) -> str:
    """Resolve a relative image path to its absolute filesystem path."""
    if not src.startswith(("http://", "https://")):
        resolved = (md_file.parent / src).resolve()
        if resolved.exists():
            src = str(resolved)
    return f"![{alt}]({src})"


def _fix_images(content: str, md_file: Path) -> str:
    """Resolve relative image paths and strip ``{ width=... }`` attributes."""
    content = _IMAGE_WITH_ATTRS_RE.sub(
        lambda m: _resolve_image_path(m.group(1), m.group(2), md_file),
        content,
    )
    content = _IMAGE_RELATIVE_RE.sub(
        lambda m: _resolve_image_path(m.group(1), m.group(2), md_file),
        content,
    )
    return content


def _fix_figures(content: str) -> str:
    """Remove ``<figure>`` and ``<figcaption>`` HTML tags (pandoc uses alt as caption)."""
    content = re.sub(r"<figure[^>]*>\s*", "", content)
    content = re.sub(r"\s*</figure>", "", content)
    content = re.sub(r"\s*<figcaption>.*?</figcaption>", "", content)
    return content


def _fetch_url(url: str, timeout: int = HTTP_TIMEOUT_SECONDS) -> bytes:
    """Fetch content from a URL with a standard User-Agent header."""
    req = urllib.request.Request(url, headers={"User-Agent": HTTP_USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _render_mermaid_to_png(mmd_code: str, png_file: Path) -> bool:
    """Render a mermaid diagram to PNG via kroki.io. Returns True on success."""
    themed_code = mmd_code
    if not themed_code.startswith("%%{"):
        themed_code = "%%{init: {'theme': 'default'}}%%\n" + themed_code

    compressed = zlib.compress(themed_code.encode(), 9)
    encoded = base64.urlsafe_b64encode(compressed).decode()

    try:
        svg_data = _fetch_url(f"{KROKI_BASE_URL}/svg/{encoded}")
        import cairosvg
        cairosvg.svg2png(
            bytestring=svg_data, write_to=str(png_file), scale=MERMAID_PNG_SCALE
        )
        return True
    except ImportError:
        try:
            png_data = _fetch_url(f"{KROKI_BASE_URL}/png/{encoded}")
            png_file.write_bytes(png_data)
            return True
        except Exception as exc:
            logger.debug("Mermaid PNG fallback failed: %s", exc)
            return False
    except Exception as exc:
        logger.debug("Mermaid SVG render failed: %s", exc)
        return False


def _render_mermaid_blocks(content: str) -> str:
    """Replace mermaid code blocks with rendered PNG images (cached locally)."""
    blocks = list(_MERMAID_BLOCK_RE.finditer(content))
    if not blocks:
        return content

    MERMAID_CACHE.mkdir(parents=True, exist_ok=True)

    for i, match in enumerate(reversed(blocks)):
        mmd_code = match.group(1).strip()
        png_file = MERMAID_CACHE / f"diagram_{i}.png"

        if not png_file.exists():
            if not _render_mermaid_to_png(mmd_code, png_file):
                content = (
                    content[:match.start()]
                    + f"```\n{mmd_code}\n```"
                    + content[match.end():]
                )
                continue

        content = (
            content[:match.start()]
            + f"![Diagrama]({png_file})"
            + content[match.end():]
        )

    return content


def _ensure_blank_line_before_headings(content: str) -> str:
    """Ensure there is a blank line before markdown headings."""
    return _HEADING_NEEDS_BLANK_LINE_RE.sub(r"\1\n\n\2", content)


# ---------------------------------------------------------------------------
# File preprocessing pipeline
# ---------------------------------------------------------------------------


def preprocess_file(md_file: Path) -> str:
    """Apply all preprocessing transformations to a markdown file.

    Pipeline order:
        1. Strip YAML frontmatter
        2. Convert admonitions (two passes for nested)
        3. Convert blockquote-nested admonitions
        4. Remove code block attributes
        5. Render mermaid diagrams to PNG
        6. Resolve image paths
        7. Remove figure HTML tags
        8. Ensure blank lines before headings
    """
    content = md_file.read_text(encoding="utf-8")
    content = _strip_frontmatter(content)
    content = _convert_admonitions(content)
    content = _convert_blockquote_admonitions(content)
    content = _fix_code_blocks(content)
    content = _render_mermaid_blocks(content)
    content = _fix_images(content, md_file)
    content = _fix_figures(content)
    content = _ensure_blank_line_before_headings(content)
    return content


# ---------------------------------------------------------------------------
# Book assembly
# ---------------------------------------------------------------------------


def _extract_frontmatter_title(raw_content: str) -> str | None:
    """Extract the title field from YAML frontmatter, if present."""
    match = _FRONTMATTER_TITLE_RE.search(raw_content)
    return match.group(1).strip() if match else None


def _shift_headings(content: str, levels: int) -> str:
    """Shift all markdown headings down by the specified number of levels."""
    return _HEADING_SHIFT_RE.sub(
        lambda m: "#" * (len(m.group(1)) + levels) + " ",
        content,
    )


def build_book_markdown(structure: BookStructure) -> str:
    """Assemble the complete book markdown from the chapter/section structure.

    Each chapter becomes an H1, each section an H2, and document headings are
    shifted accordingly. If a section has multiple files and the document has a
    title distinct from the section name, it is inserted as an H3.
    """
    parts: list[str] = []

    for chapter_name, sections in structure:
        parts.append(f"# {chapter_name}\n")

        for section_name, files in sections:
            parts.append(f"## {section_name}\n")

            for file_path in files:
                full_path = DOCS_DIR / file_path
                if not full_path.exists():
                    logger.warning("⚠️  No encontrado: %s", full_path)
                    continue

                raw_content = full_path.read_text(encoding="utf-8")
                doc_title = _extract_frontmatter_title(raw_content)

                content = preprocess_file(full_path)

                # Insert document title as H3 when section has multiple files
                # and the title differs from the section name
                insert_title = (
                    doc_title is not None
                    and len(files) > 1
                    and doc_title.lower() != section_name.lower()
                )

                shift = 2 if insert_title else 1
                content = _shift_headings(content, shift)

                if insert_title:
                    parts.append(f"### {doc_title}\n")

                parts.append(content)
                parts.append("")

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Pandoc generation
# ---------------------------------------------------------------------------


def _check_dependencies() -> None:
    """Verify that pandoc and xelatex are available on PATH."""
    required_commands = ("pandoc", "xelatex")
    missing = [cmd for cmd in required_commands if not shutil.which(cmd)]
    if missing:
        logger.error("❌ Falta: %s", ", ".join(missing))
        logger.error("   sudo apt install pandoc texlive-xetex texlive-lang-spanish")
        sys.exit(1)


def _build_pandoc_command(
    input_path: Path, output_path: Path, fmt: str
) -> list[str]:
    """Construct the pandoc command with all necessary arguments."""
    cmd = [
        "pandoc",
        str(input_path),
        "-o", str(output_path),
        "--toc",
        "--toc-depth=3",
        "--highlight-style=tango",
        "--columns=50",
    ]

    for key, value in PANDOC_METADATA.items():
        cmd += ["-V", f"{key}={value}"]

    if fmt == "pdf":
        cmd += ["--pdf-engine", PDF_ENGINE, "--number-sections"]
        for key, value in PDF_VARIABLES.items():
            cmd += ["-V", f"{key}={value}"]
        cmd += ["-H", str(SCRIPT_DIR / "preamble.tex")]

    return cmd


def _run_pandoc(input_path: Path, output_path: Path, fmt: str) -> None:
    """Execute pandoc to generate the output file.

    Raises:
        SystemExit: If pandoc returns a non-zero exit code.
    """
    cmd = _build_pandoc_command(input_path, output_path, fmt)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        logger.error("❌ Error generando %s:\n%s", fmt, result.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# CLI and entry point
# ---------------------------------------------------------------------------


def _parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Genera un libro PDF y EPUB a partir de la wiki.",
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Genera solo 2 secciones para iterar rápido",
    )
    return parser.parse_args()


def main() -> None:
    """Entry point: assemble markdown, generate PDF and EPUB."""
    args = _parse_args()
    _check_dependencies()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    structure = PREVIEW_STRUCTURE if args.preview else BOOK_STRUCTURE

    logger.info("📖 Ensamblando el libro...")
    book_content = build_book_markdown(structure)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, encoding="utf-8"
    ) as f:
        f.write(book_content)
        tmp_path = Path(f.name)

    try:
        pdf_output = OUTPUT_DIR / f"{PROJECT_NAME}.pdf"
        epub_output = OUTPUT_DIR / f"{PROJECT_NAME}.epub"

        logger.info("🔧 Generando PDF...")
        _run_pandoc(tmp_path, pdf_output, "pdf")
        logger.info("✅ PDF: %s", pdf_output)

        logger.info("🔧 Generando EPUB...")
        _run_pandoc(tmp_path, epub_output, "epub")
        logger.info("✅ EPUB: %s", epub_output)
    finally:
        tmp_path.unlink(missing_ok=True)

    logger.info("🎉 Libro generado correctamente.")


if __name__ == "__main__":
    main()
