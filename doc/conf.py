# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

master_doc = 'contents'  # Changed from 'index' to 'contents' to show the sidebar
project = 'IAn Vulgarisateur'
copyright = 'Ronan Sicre'

author = 'L3 Informatique'
release = '0.1'
version = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser', 
    'sphinx_nefertiti', 
    'sphinx_design',
    'sphinx_copybutton', 
    'sphinxemoji.sphinxemoji',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'myst_parser',
]

myst_enable_extensions = [
    'amsmath',
    'attrs_block',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'tasklist',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = 'sphinx_nefertiti'


html_theme_options = {
    "header_links": [],
    "footer_links":[
        {
            "text": "Issues",
            "link": "https://github.com/danirus/sphinx-nefertiti/issues",
        },{
            'text': 'Documentation',
            'link': 'https://docs.google.com/document/d/1X9dO4tD5R5DBlG_WFETr6D9i2sSP5pHR8RI8enTSceU/edit?tab=t.0#heading=h.bg3x17yqchk'
        },{
            'text': 'Repository',
            'link': 'https://github.com/Yousraarroui/TestSphinx.git'
        }
    ],
    "show_colorset_choices": True,
    "style_header_neutral": True,
    # Return user's to 'blue' after a day since color was picked.
    "reset_colorset_choice_after_ms": 1000 * 60 * 60 * 24,
}

# Configuration des chemins relatifs pour les images

