# ruff: noqa

"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

from __future__ import annotations

import importlib.metadata
import os
import sys

project = "cosmology.api"
author = "cosmology-api devs"
copyright = f"2023, {author}"
version = release = importlib.metadata.version("cosmology_api")


# -- General configuration ---------------------------------------------------

# By default, highlight as Python 3.
highlight_language = "python3"

sys.path.append(os.path.abspath("./_ext"))
extensions = [
    "sphinx.ext.autosummary",
    # "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinx_ext_autosummary_context",
    "sphinx_ext_cosmology_api",
]

source_suffix = [".rst", ".md"]
exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "Thumbs.db",
    ".DS_Store",
    ".env",
    ".venv",
]

# This is added to the end of RST files - a good place to put substitutions to
# be used globally.
rst_epilog = """
.. |author| replace:: {author}

.. _Python: http://www.python.org
"""

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]


intersphinx_mapping = {
    "python": (
        "https://docs.python.org/3/",
        (None, "http://data.astropy.org/intersphinx/python3.inv"),
    ),
    "numpy": (
        "https://numpy.org/doc/stable/",
        (None, "http://data.astropy.org/intersphinx/numpy.inv"),
    ),
    "scipy": (
        "https://docs.scipy.org/doc/scipy/reference/",
        (None, "https://docs.scipy.org/doc/scipy/objects.inv"),
    ),
}

nitpick_ignore = [
    ("py:class", "_io.StringIO"),
    ("py:class", "_io.BytesIO"),
]

always_document_param_types = True


# -- Options for HTML output -------------------------------------------------

html_theme = "furo"

html_title = f"{project} v{release}"

html_static_path = ["_static"]


# -- autodoc extension -------------------------------------------------------

# The default options for autodoc directives. They are applied to all autodoc
# directives automatically. It must be a dictionary which maps option names to
# the values.
autodoc_default_options = {
    "members": False,
    "inherited-members": False,
    "show-inheritance": True,
}

add_module_names = False

autosummary_generate = True


# -- numpydoc extension ------------------------------------------------------

# Whether to show all members of a class in the Methods and Attributes sections
# automatically. True by default.
numpydoc_show_class_members = True

# Whether to show all inherited members of a class in the Methods and
# Attributes sections automatically. If it's false, inherited members won't
# shown. True by default.
numpydoc_show_inherited_class_members = True

# Whether to create a Sphinx table of contents for the lists of class methods
# and attributes. If a table of contents is made, Sphinx expects each entry to
# have a separate page. True by default.
numpydoc_class_members_toctree = False

# A regular expression matching citations which should be mangled to avoid
# conflicts due to duplication across the documentation. Defaults to '[\w-]+'.
# > numpydoc_citation_re = '[\w-]+'

# Whether to format the Attributes section of a class page in the same way as
# the Parameter section. If it's False, the Attributes section will be
# formatted as the Methods section using an autosummary table. True by default.
numpydoc_attributes_as_param_list = False

# Whether to create cross-references for the parameter types in the
# Parameters, Other Parameters, Returns and Yields sections of the docstring.
numpydoc_xref_param_type = True

# Words not to cross-reference. Most likely, these are common words used in
# parameter type descriptions that may be confused for classes of the same
# name. This can be overwritten or modified in packages and is provided here
# for convenience.
numpydoc_xref_ignore = {
    "or",
    "default",
    "optional",
    "positional-only",
    "keyword-only",
}

# -- copybutton extension ------------------------------------------------------

copybutton_exclude = ".linenos, .gp, .go"
