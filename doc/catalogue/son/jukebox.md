# [Jukebox](https://github.com/openai/jukebox)

- **Nom de l'outil** : Jukebox
- **Catégorie** : Audio (Génération musicale end-to-end)
- **Développeur** : OpenAI
- **Date de sortie** : Avril 2020

## Objectif
Générer des chansons complètes (musique, chant, paroles) en audio brut à partir de prompts texte, en imitant styles et artistes.

## Fonctionnement résumé
| Étape | Description |
|-------|-------------|
| Entrée | Genre/artiste + paroles (optionnel) |
| Traitement | Compression VQ-VAE → Génération hiérarchique via Transformers |
| Sortie | Audio stéréo 44.1kHz (jusqu'à 1min) |

## Fonctions principales
- ✅ Génération audio brut (pas MIDI)
- ✅ Imitation de 1k+ artistes (Sinatra, Beatles, etc.)
- ✅ Intégration paroles synchronisées
- ❌ 9h de calcul/min audio
- ❌ Modèle non maintenu depuis 2022

## Exemples d'usage concrets
| Domaine | Exemple |
|---------|---------|
| Expérimentation | Covers IA de thèmes Super Mario 64 |
| Production | Génération de bases instrumentales pour remix |
| Recherche | Étude des espaces latents musicaux |

## Détails techniques
| Caractéristique | Valeur |
|-----------------|---------|
| Architecture | VQ-VAE 3 niveaux + Transformers 72 couches |
| Framework | PyTorch |
| Dataset | 1.2M chansons (dont 600k anglaises) |
| Contexte | 8192 codes (~24s audio top level) |
| Licence | MIT (code) / Restrictions données |

## Pricing
- Gratuit (code) • Coût cloud élevé (~$50/heure GPU)

## Releases clés
- [v1.0](https://github.com/openai/jukebox/releases/tag/v1) : Version initiale (04/2020)
- [v1.1](https://github.com/openai/jukebox/releases/tag/v1.1) : Optimisations GPU (06/2020)

## Alternatives connues
- [Dance Diffusion](https://github.com/harmonai-ai/dance-diffusion) (génération rapide)
- [AudioCraft](https://github.com/facebookresearch/audiocraft) (Meta)
- [Riffusion](https://github.com/riffusion/riffusion) (melodies structurées)

## Ressources utiles
- [GitHub Officiel](https://github.com/openai/jukebox)
- [Exemples audio](https://jukebox.openai.com)
- [Colab](https://colab.research.google.com/github/openai/jukebox/blob/master/jukebox/colab.ipynb)

## Workflow typique Colab
```python
git clone https://github.com/openai/jukebox.git
%cd jukebox
pip install -r requirements.txt  # Nvidia A100+ requis
```

## Input/Output
- Input : "Rock années 80, style Queen, paroles sur l'espace"
- Sortie : 🎸 Écouter l'extrait (bruit de fond perceptible)

## Avantages/Limites
| ✅ Avantages | ❌ Inconvénients |
|-------------|-----------------|
| Réalisme vocal | Bruit artefacts VQ-VAE |
| Structure musicale cohérente | Contrôle limité sur mélodie |
| Dataset multigenre | Compute prohibitif (TPU/GPU cluster) |

## Aspects légaux
- Risque de copyright avec imitation d'artistes
- Metadata originale non fournie

## Statistiques
- 4.7/5 sur GitHub (8.2k stars)
- 1k+ covers IA générés (2020-2022) 