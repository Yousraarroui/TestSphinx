# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ian Vulgarisateur'
copyright = 'Ronan Sicre'
author = 'L3 Informatique'
release = '0.1'
version = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_logo = "images/logo-transparent.png"
html_favicon = "images/favicon-32x32.png"

# Custom CSS
html_css_files = [
    'custom.css',
]

# Theme options
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#3498db",
        "color-brand-content": "#2980b9",
        "color-api-background": "#f8f9fa",
        "color-api-name": "#e74c3c",
        "color-api-pre-name": "#e74c3c",
        "color-api-keyword": "#9b59b6",
    },
    "dark_css_variables": {
        "color-brand-primary": "#3498db",
        "color-brand-content": "#2980b9",
        "color-api-background": "#2d2d2d",
        "color-api-name": "#e74c3c",
        "color-api-pre-name": "#e74c3c",
        "color-api-keyword": "#9b59b6",
    },
}

