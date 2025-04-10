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

# Configuration de la page d'accueil personnalisée
html_additional_pages = {
    "index": "custom-landing-page.html"
}

# Configuration de la barre latérale
html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
    ]
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]

# Configuration des couleurs du thème
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#2C3E50",
        "color-brand-content": "#2C3E50",
        "color-background-primary": "#ffffff",
        "color-background-secondary": "#f8f9fa",
        "color-foreground-primary": "#000000",
        "color-foreground-secondary": "#5a5c63",
        "font-stack": "Arial, sans-serif",
        "font-stack--monospace": "Courier, monospace",
        "font-stack--headings": "Georgia, serif",
        "color-sidebar-brand-text": "#2C3E50",
        "color-sidebar-background": "#f8f9fa",
        "color-sidebar-background-border": "#e9ecef",
    },
    "dark_css_variables": {
        "color-brand-primary": "#34495E",
        "color-brand-content": "#34495E",
        "color-background-primary": "#111111",
        "color-background-secondary": "#1c1c1c",
        "color-foreground-primary": "#ffffff",
        "color-foreground-secondary": "#a3a3a3",
        "color-sidebar-brand-text": "#ffffff",
        "color-sidebar-background": "#1c1c1c",
        "color-sidebar-background-border": "#2c2c2c",
    },
    # Options de personnalisation supplémentaires
    "sidebar_hide_name": False,  # Afficher le nom du projet dans la barre latérale
    "navigation_with_keys": True,  # Activer la navigation au clavier
    "top_of_page_buttons": ["view", "edit"],  # Boutons en haut de page
    "announcement": "Bienvenue sur le catalogue des modèles d'IA !",  # Bannière d'annonce
    # Configuration des icônes de pied de page
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/yourusername/your-repo",
            "html": "",
            "class": "fa-brands fa-github fa-2x",
        },
        {
            "name": "Documentation",
            "url": "https://your-docs-url",
            "html": "",
            "class": "fa-solid fa-book fa-2x",
        },
        {
            "name": "Discord",
            "url": "https://discord.gg/your-invite",
            "html": "",
            "class": "fa-brands fa-discord fa-2x",
        },
    ],
}

# Configuration du style des blocs de code
pygments_style = "sphinx"
pygments_dark_style = "monokai"