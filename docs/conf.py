# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "PIASO"
copyright = "2024"
author = "Min Dai"


# -- General configuration ---------------------------------------------------
# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "nbsphinx",
]

intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for EPUB output
epub_show_urls = "footnote"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = "sphinx_book_theme"
# html_theme_options = {
#     "body_min_width": "50%",
#     "body_max_width": "none"
# }

html_theme = 'pydata_sphinx_theme'
html_show_sphinx = False
html_show_sourcelink = False
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
html_logo = "source/_static/PIASO_logo.png"

html_theme_options = {
    # "logo": {
    #     "text": "SnapATAC2",
    #     "image_dark": "_static/logo-dark.svg",
    #     "alt_text": "SnapATAC2",
    # },

    # "github_url": "https://github.com/kaizhang/SnapATAC2",
    # "external_links": [
    #     {"name": "Learn", "url": "https://kzhang.org/epigenomics-analysis/"}
    # ],
    "header_links_before_dropdown": 6,
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "navbar_align": "left",

    "primary_sidebar_end": ["sidebar-ethical-ads"],
    # "show_version_warning_banner": switcher_version == "dev",

    # "switcher": {
    #     "version_match": switcher_version,
    #     "json_url": "https://raw.githubusercontent.com/kaizhang/SnapATAC2/main/docs/_static/versions.json", 
    # },
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]
