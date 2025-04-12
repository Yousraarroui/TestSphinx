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

extensions = ['myst_parser', 'sphinx_nefertiti', 'sphinxemoji.sphinxemoji']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_nefertiti'
html_static_path = ['static']
html_theme_options = {
    "header_links": [
        {
            "text": "Comment ça marche",
            "link": "comment.html",
        },
        {
            "text": "Plus",
            "dropdown": [
                {
                    "text": "FAQ",
                    "link": "faq.html"
                },
                {
                    "text": "Contact",
                    "link": "contact.html"
                }
            ]
        }
    ],
    "footer_links":[
        {
            'text': 'Home',
            'link': 'index.html'
        },{
            'text': 'Documentation',
            'link': 'https://docs.google.com/document/d/1X9dO4tD5R5DBlG_WFETr6D9i2sSP5pHR8RI8enTSceU/edit?tab=t.0#heading=h.bg3x17yqchk'
        },{
            'text': 'Code',
            'link': 'https://github.com/Yousraarroui/TestSphinx.git'
        }
    ],
    "show_colorset_choices": True,
    "style_header_neutral": True,

    # Reset the user selected choice after milliseconds.
    # "reset_colorset_choice_after_ms": 0,
}
