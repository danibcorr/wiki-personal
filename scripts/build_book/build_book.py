#!/usr/bin/env python3
"""Genera un libro PDF y EPUB a partir de la documentación de la wiki.

Preprocesa la sintaxis Zensical/MkDocs (admonitions, code blocks con atributos,
figuras HTML, imágenes con atributos, diagramas mermaid) y ensambla el contenido
en un único documento que pandoc + xelatex convierte a PDF/EPUB.

Uso:
    python build_book.py            # Genera el libro completo
    python build_book.py --preview  # Genera solo 2 secciones para iterar rápido
"""

from __future__ import annotations

import base64
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
# Tipos
# ---------------------------------------------------------------------------

Section: TypeAlias = tuple[str, list[str]]
Chapter: TypeAlias = tuple[str, list[Section]]
BookStructure: TypeAlias = list[Chapter]

# ---------------------------------------------------------------------------
# Configuración
# ---------------------------------------------------------------------------

PROJECT_NAME = "wiki-personal"
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR / "output"
MERMAID_CACHE = OUTPUT_DIR / ".mermaid"

BOOK_STRUCTURE: BookStructure = [
    ("Sistemas Operativos", [
        ("Linux", [
            "topic_1_operative_systems/topic_1_1_linux/section_1_fundamentals.md",
            "topic_1_operative_systems/topic_1_1_linux/section_2_administration.md",
            "topic_1_operative_systems/topic_1_1_linux/section_3_networking.md",
        ]),
    ]),
    ("Herramientas", [
        ("Git", [
            "topic_2_tools/topic_2_1_git/section_1_fundamentals.md",
            "topic_2_tools/topic_2_1_git/section_2_workflows.md",
            "topic_2_tools/topic_2_1_git/section_3_practical_cases.md",
        ]),
        ("Scripting", [
            "topic_2_tools/topic_2_2_scripting/section_1_bash.md",
            "topic_2_tools/topic_2_2_scripting/section_2_makefile.md",
        ]),
    ]),
    ("Programación", [
        ("Python", [
            "topic_3_programming/topic_3_1_python/section_1_environments.md",
            "topic_3_programming/topic_3_1_python/section_2_fundamentals.md",
            "topic_3_programming/topic_3_1_python/section_3_libraries.md",
        ]),
        ("Rust", [
            "topic_3_programming/topic_3_2_rust/section_1_fundamentals.md",
        ]),
        ("CUDA", [
            "topic_3_programming/topic_3_3_cuda/section_1_fundamentals.md",
            "topic_3_programming/topic_3_3_cuda/section_2_cuda_c.md",
            "topic_3_programming/topic_3_3_cuda/section_3_cuda_python.md",
        ]),
        ("Desarrollo web", [
            "topic_3_programming/topic_3_4_front_end/section_1_fundamentals.md",
        ]),
    ]),
    ("Inteligencia Artificial", [
        ("Machine Learning", [
            "topic_5_artificial_intelligence/topic_5_1_machine_learning/section_1_fundamentals.md",
            "topic_5_artificial_intelligence/topic_5_1_machine_learning/section_2_statistics.md",
            "topic_5_artificial_intelligence/topic_5_1_machine_learning/section_3_supervised_models.md",
            "topic_5_artificial_intelligence/topic_5_1_machine_learning/section_4_clustering.md",
            "topic_5_artificial_intelligence/topic_5_1_machine_learning/section_5_evaluation.md",
            "topic_5_artificial_intelligence/topic_5_1_machine_learning/section_6_dimensionality_reduction.md",
            "topic_5_artificial_intelligence/topic_5_1_machine_learning/section_7_advanced.md",
        ]),
        ("Deep Learning", [
            "topic_5_artificial_intelligence/topic_5_2_deep_learning/section_1_fundamentals.md",
            "topic_5_artificial_intelligence/topic_5_2_deep_learning/section_2_math.md",
            "topic_5_artificial_intelligence/topic_5_2_deep_learning/section_3_linear_models.md",
            "topic_5_artificial_intelligence/topic_5_2_deep_learning/section_4_neural_networks.md",
            "topic_5_artificial_intelligence/topic_5_2_deep_learning/section_5_cnn.md",
            "topic_5_artificial_intelligence/topic_5_2_deep_learning/section_6_sequential_models.md",
            "topic_5_artificial_intelligence/topic_5_2_deep_learning/section_7_other_paradigms.md",
            "topic_5_artificial_intelligence/topic_5_2_deep_learning/section_8_generative_ai.md",
            "topic_5_artificial_intelligence/topic_5_2_deep_learning/section_9_graph_neural_networks.md",
            "topic_5_artificial_intelligence/topic_5_2_deep_learning/section_10_reinforcement_learning.md",
            "topic_5_artificial_intelligence/topic_5_2_deep_learning/section_11_agents.md",
        ]),
        ("Librerías de Deep Learning", [
            "topic_5_artificial_intelligence/topic_5_2_deep_learning/libraries/jax.md",
            "topic_5_artificial_intelligence/topic_5_2_deep_learning/libraries/pytorch.md",
            "topic_5_artificial_intelligence/topic_5_2_deep_learning/libraries/tensorflow.md",
        ]),
    ]),
    ("Metodologías", [
        ("Ingeniería de Software", [
            "topic_6_methodologies/topic_6_1_software/section_1_data_structure.md",
            "topic_6_methodologies/topic_6_1_software/section_2_sustainable_code.md",
        ]),
        ("DevOps", [
            "topic_6_methodologies/topic_6_2_devops/section_1_containers.md",
            "topic_6_methodologies/topic_6_2_devops/section_2_orchestrators.md",
            "topic_6_methodologies/topic_6_2_devops/section_3_ci_cd.md",
        ]),
        ("MLOps", [
            "topic_6_methodologies/topic_6_3_mlops/section_1_fundamentals.md",
            "topic_6_methodologies/topic_6_3_mlops/section_2_experiment_management.md",
            "topic_6_methodologies/topic_6_3_mlops/section_3_deployment.md",
        ]),
    ]),
    ("Infraestructura", [
        ("Bases de Datos", [
            "topic_7_infrastructure/topic_7_1_databases/section_1_sql.md",
        ]),
        ("Cloud", [
            "topic_7_infrastructure/topic_7_2_cloud/section_1_fundamentals.md",
            "topic_7_infrastructure/topic_7_2_cloud/section_2_aws.md",
        ]),
    ]),
    ("Otros", [
        ("Guía CV", [
            "topic_A_interviews/cv_guide.md",
        ]),
    ]),
]

PREVIEW_STRUCTURE: BookStructure = [
    ("Herramientas", [
        ("Git", ["topic_2_tools/topic_2_1_git/section_1_fundamentals.md"]),
    ]),
    ("Metodologías", [
        ("DevOps", ["topic_6_methodologies/topic_6_2_devops/section_1_containers.md"]),
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

# ---------------------------------------------------------------------------
# Preprocesado de markdown
# ---------------------------------------------------------------------------


def strip_frontmatter(content: str) -> str:
    """Elimina el bloque YAML frontmatter (---...---)."""
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            return content[end + 3 :].lstrip("\n")
    return content


def convert_admonitions(content: str) -> str:
    """Convierte admonitions MkDocs a blockquotes con estilo LaTeX por color.

    Soporta ``!!! type "title"``, ``!!!type "title"`` y ``???+ type "title"``.
    Inyecta un comando LaTeX raw antes de cada blockquote para cambiar el color
    del borde según el tipo de admonition.
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

            # Inyectar estilo LaTeX para este admonition
            style_def = (
                f"`\\global\\mdfdefinestyle{{admonitionstyle}}"
                f"{{linewidth=2pt,linecolor={color},backgroundcolor={color}!5,"
                f"leftmargin=0pt,rightmargin=0pt,"
                f"innerleftmargin=10pt,innerrightmargin=10pt,"
                f"innertopmargin=8pt,innerbottommargin=8pt,"
                f"skipabove=10pt,skipbelow=10pt,"
                f"topline=false,rightline=false,bottomline=false,"
                f"nobreak=true}}`{{=latex}}"
            )
            result.append("")
            result.append(style_def)
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


def convert_blockquote_admonitions(content: str) -> str:
    """Convierte admonitions residuales dentro de blockquotes (anidados)."""
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


def fix_code_blocks(content: str) -> str:
    """Elimina atributos de code blocks (linenums, hl_lines)."""
    return re.sub(
        r"```(\w+)\s+(?:linenums=\"?\d+\"?\s*(?:hl_lines=\"[^\"]*\")?)\s*\n",
        r"```\1\n",
        content,
    )


def fix_images(content: str, md_file: Path) -> str:
    """Resuelve rutas relativas de imágenes y elimina atributos ``{ width=... }``."""

    def resolve_local(alt: str, src: str) -> str:
        if not src.startswith(("http://", "https://")):
            resolved = (md_file.parent / src).resolve()
            if resolved.exists():
                src = str(resolved)
        return f"![{alt}]({src})"

    content = re.sub(
        r"!\[([^\]]*)\]\(([^)]+)\)\{[^}]*\}",
        lambda m: resolve_local(m.group(1), m.group(2)),
        content,
    )
    content = re.sub(
        r"!\[([^\]]*)\]\((\.\.?/[^)]+)\)",
        lambda m: resolve_local(m.group(1), m.group(2)),
        content,
    )
    return content


def fix_figures(content: str) -> str:
    """Elimina tags ``<figure>`` y ``<figcaption>`` (pandoc usa el alt como caption)."""
    content = re.sub(r"<figure[^>]*>\s*", "", content)
    content = re.sub(r"\s*</figure>", "", content)
    content = re.sub(r"\s*<figcaption>.*?</figcaption>", "", content)
    return content


def render_mermaid_blocks(content: str) -> str:
    """Renderiza bloques mermaid a PNG usando kroki.io (con caché local)."""
    blocks = list(re.finditer(r"```mermaid\n(.*?)```", content, re.DOTALL))
    if not blocks:
        return content

    MERMAID_CACHE.mkdir(parents=True, exist_ok=True)

    for i, match in enumerate(reversed(blocks)):
        mmd_code = match.group(1).strip()
        png_file = MERMAID_CACHE / f"diagram_{i}.png"

        if not png_file.exists():
            themed_code = mmd_code
            if not themed_code.startswith("%%{"):
                themed_code = "%%{init: {'theme': 'default'}}%%\n" + themed_code

            compressed = zlib.compress(themed_code.encode(), 9)
            encoded = base64.urlsafe_b64encode(compressed).decode()
            svg_url = f"https://kroki.io/mermaid/svg/{encoded}"
            req = urllib.request.Request(svg_url, headers={"User-Agent": "Mozilla/5.0"})

            try:
                with urllib.request.urlopen(req, timeout=15) as resp:
                    svg_data = resp.read()
                import cairosvg

                cairosvg.svg2png(
                    bytestring=svg_data, write_to=str(png_file), scale=2.0
                )
            except ImportError:
                png_url = f"https://kroki.io/mermaid/png/{encoded}"
                req = urllib.request.Request(
                    png_url, headers={"User-Agent": "Mozilla/5.0"}
                )
                try:
                    with urllib.request.urlopen(req, timeout=15) as resp:
                        png_file.write_bytes(resp.read())
                except Exception:
                    content = (
                        content[: match.start()]
                        + f"```\n{mmd_code}\n```"
                        + content[match.end() :]
                    )
                    continue
            except Exception:
                content = (
                    content[: match.start()]
                    + f"```\n{mmd_code}\n```"
                    + content[match.end() :]
                )
                continue

        content = (
            content[: match.start()]
            + f"![Diagrama]({png_file})"
            + content[match.end() :]
        )

    return content


# ---------------------------------------------------------------------------
# Ensamblado del libro
# ---------------------------------------------------------------------------


def preprocess_file(md_file: Path) -> str:
    """Aplica todas las transformaciones de preprocesado a un archivo markdown."""
    content = md_file.read_text(encoding="utf-8")
    content = strip_frontmatter(content)
    content = convert_admonitions(content)
    content = convert_admonitions(content)  # Segunda pasada para anidados
    content = convert_blockquote_admonitions(content)
    content = fix_code_blocks(content)
    content = render_mermaid_blocks(content)
    content = fix_images(content, md_file)
    content = fix_figures(content)
    # Asegurar línea vacía antes de headings
    content = re.sub(r"([^\n])\n(#{1,6} )", r"\1\n\n\2", content)
    return content


def build_book_markdown(structure: BookStructure | None = None) -> str:
    """Ensambla el markdown completo del libro con la estructura de capítulos."""
    if structure is None:
        structure = BOOK_STRUCTURE

    parts: list[str] = []

    for chapter_name, sections in structure:
        parts.append(f"# {chapter_name}\n")

        for section_name, files in sections:
            parts.append(f"## {section_name}\n")

            for file_path in files:
                full_path = DOCS_DIR / file_path
                if not full_path.exists():
                    print(f"⚠️  No encontrado: {full_path}", file=sys.stderr)
                    continue

                content = preprocess_file(full_path)
                # Bajar headings 1 nivel (## -> ###) para encajar en la jerarquía
                content = re.sub(
                    r"^(#{1,5}) ",
                    lambda m: "#" * (len(m.group(1)) + 1) + " ",
                    content,
                    flags=re.MULTILINE,
                )
                parts.append(content)
                parts.append("")

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Generación con pandoc
# ---------------------------------------------------------------------------


def check_dependencies() -> None:
    """Verifica que pandoc y xelatex están disponibles."""
    missing = [cmd for cmd in ("pandoc", "xelatex") if not shutil.which(cmd)]
    if missing:
        print(f"❌ Falta: {', '.join(missing)}", file=sys.stderr)
        print(
            "   sudo apt install pandoc texlive-xetex texlive-lang-spanish",
            file=sys.stderr,
        )
        sys.exit(1)


def run_pandoc(input_path: str, output_path: str, fmt: str) -> None:
    """Ejecuta pandoc para generar el archivo de salida."""
    cmd = [
        "pandoc",
        input_path,
        "-o",
        output_path,
        "--toc",
        "--toc-depth=4",
        "--highlight-style=tango",
        "--columns=50",
        "-V", "title=La Wiki de un Ingeniero",
        "-V", "author=Daniel Bazo Correa",
        "-V", "date=2026",
        "-V", "lang=es",
    ]

    if fmt == "pdf":
        cmd += [
            "--pdf-engine=xelatex",
            "--number-sections",
            "-V", "documentclass=report",
            "-V", "geometry:margin=2.5cm",
            "-V", "fontsize=11pt",
            "-V", "mainfont=Latin Modern Roman",
            "-V", "sansfont=Latin Modern Sans",
            "-V", "monofont=Latin Modern Mono",
            "-V", "monofontoptions=Scale=0.85",
            "-H", str(SCRIPT_DIR / "preamble.tex"),
        ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error generando {fmt}:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Punto de entrada
# ---------------------------------------------------------------------------


def main() -> None:
    """Punto de entrada principal del script."""
    check_dependencies()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    structure = PREVIEW_STRUCTURE if "--preview" in sys.argv else BOOK_STRUCTURE

    print("📖 Ensamblando el libro...")
    book_content = build_book_markdown(structure)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, encoding="utf-8"
    ) as f:
        f.write(book_content)
        tmp_path = f.name

    pdf_output = str(OUTPUT_DIR / f"{PROJECT_NAME}.pdf")
    epub_output = str(OUTPUT_DIR / f"{PROJECT_NAME}.epub")

    print("🔧 Generando PDF...")
    run_pandoc(tmp_path, pdf_output, "pdf")
    print(f"✅ PDF: {pdf_output}")

    print("🔧 Generando EPUB...")
    run_pandoc(tmp_path, epub_output, "epub")
    print(f"✅ EPUB: {epub_output}")

    Path(tmp_path).unlink()
    print("🎉 Libro generado correctamente.")


if __name__ == "__main__":
    main()
