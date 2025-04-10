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

# Titre personnalisé pour la documentation
html_title = 'Découvrez tout sur les modèles d\'IA'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Configuration de la page d'accueil personnalisée
html_additional_pages = {
    "index": "custom-landing-page.html"
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

# Configuration des fichiers CSS
html_css_files = [
    'custom.css',
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
    'https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap',
]

# Configuration du logo
html_logo = "_static/logo.png"

# Configuration des couleurs du thème
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#17A2B8",  # Vert turquoise du logo
        "color-brand-content": "#17A2B8",
        "color-background-primary": "#ffffff",
        "color-background-secondary": "#f8f9fa",
        "color-foreground-primary": "#000000",
        "color-foreground-secondary": "#5a5c63",
        "font-stack": "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif",
        "font-stack--monospace": "'Montserrat', 'SFMono-Regular', Menlo, Consolas, Monaco, 'Liberation Mono', 'Lucida Console', monospace",
    },
    "dark_css_variables": {
        "color-brand-primary": "#17A2B8",  # Même vert turquoise pour la cohérence
        "color-brand-content": "#17A2B8",
        "color-background-primary": "#111111",
        "color-background-secondary": "#1c1c1c",
        "color-foreground-primary": "#ffffff",
        "color-foreground-secondary": "#a3a3a3",
    },
    # Options de personnalisation supplémentaires
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
pygments_style = "friendly"
pygments_dark_style = "native"

html_favicon = "images/favicon-32x32.png"
