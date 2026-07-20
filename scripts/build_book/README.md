# Build Book

Script para convertir la documentación de la wiki en un libro unificado en formato PDF y
EPUB.

## Requisitos

```bash
sudo apt install pandoc texlive-xetex texlive-lang-spanish fonts-dejavu
```

## Uso

```bash
python3 scripts/build_book/build_book.py
```

Los archivos generados se guardan en `scripts/build_book/output/`:

- `wiki-personal.pdf`
- `wiki-personal.epub`

## Estructura del libro

Cada _topic_ del proyecto se convierte en un **capítulo** y cada subtema en una
**sección**:

1. Sistemas Operativos
2. Herramientas
3. Programación
4. Inteligencia Artificial
5. Metodologías
6. Infraestructura
7. Otros

## Preprocesado

El script maneja automáticamente las peculiaridades de la sintaxis Zensical/MkDocs:

| Elemento                   | Transformación                                 |
| -------------------------- | ---------------------------------------------- |
| Admonitions (`!!!`)        | Blockquotes con etiqueta y emoji               |
| Frontmatter YAML           | Eliminado                                      |
| Code blocks con atributos  | Limpiados (`linenums`, `hl_lines`)             |
| Imágenes con `{ width= }`  | Atributos eliminados, rutas resueltas          |
| `<figure markdown="span">` | Convertido a markdown estándar con `*caption*` |
