from __future__ import annotations

import os
import sys
from pathlib import Path


DOCS_DIR = Path(__file__).resolve().parent
REPOSITORY_ROOT = DOCS_DIR.parent
sys.path.insert(0, str(REPOSITORY_ROOT))

project = "GOOD Developer Portal"
author = "GOOD project team"
copyright = "2026, GOOD project team"
version = os.environ.get("GOOD_DOCS_VERSION", "development")
release = version

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "breathe",
    "sphinxcontrib.mermaid",
]

source_suffix = {".md": "markdown", ".rst": "restructuredtext"}
master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "_content/**"]
nitpicky = True

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "substitution",
]
myst_heading_anchors = 4

autosummary_generate = True
autodoc_typehints = "description"
napoleon_google_docstring = True
napoleon_numpy_docstring = True

breathe_projects = {}
breathe_default_project = "GOOD"

html_theme = "furo"
html_title = "GOOD Developer Portal"
html_static_path = ["_static"]
html_css_files = ["good.css"]
html_show_sourcelink = True
html_last_updated_fmt = "%Y-%m-%d"

latex_documents = [
    (master_doc, "GOOD-Developer-Portal.tex", project, author, "manual"),
]
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "10pt",
}
