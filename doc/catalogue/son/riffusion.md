# [Riffusion](https://riffusion.com)

- **Nom de l'outil** : Riffusion
- **Catégorie** : Audio (Text-to-Music)
- **Développeur** : Seth Forsgren & Hayk Martiros
- **Date de sortie** : Décembre 2022

## Objectif
Générer des boucles musicales et transitions fluides en temps réel à partir de prompts texte via une adaptation audio de Stable Diffusion.

## Fonctionnement résumé
| Étape | Description |
|-------|-------------|
| Entrée | Prompt texte (ex: "techno industrielle sombre") |
| Traitement | Diffusion sur spectrogrammes + interpolation latente |
| Sortie | Audio 48kHz (5-15s par défaut) |

## Fonctions principales
- ✅ Génération en temps réel (<2s sur GPU)
- ✅ Transitions fluides entre styles
- ✅ Intégration WebAudio pour démos interactives
- ❌ Limité à 30s sans bouclage manuel
- ❌ Résolution audio variable (artefacts HF)

## Exemples d'usage concrets
| Domaine | Exemple |
|---------|---------|
| DJing | Morphing live house → dubstep |
| Sound Design | Génération de textures évolutives |
| Prototypage | Exploration rapide de concepts musicaux |

## Détails techniques
| Caractéristique | Valeur |
|-----------------|---------|
| Architecture | Stable Diffusion audio (spectrogrammes) |
| Framework | PyTorch + ONNX |
| Input | Texte (emojis acceptés 🎸⚡️) |
| Output | WAV 48kHz (qualité variable) |
| Modèles | 4 modèles communautaires (techno/ambient/rock) |

## Pricing
- Gratuit • Open-source (MIT License)

## Releases clés
- [v1.0](https://github.com/riffusion/riffusion/releases/tag/v1.0) : Version initiale (12/2022)
- [v1.5](https://github.com/riffusion/riffusion/releases/tag/v1.5) : Support ONNX (03/2023)

## Alternatives connues
- [Stable Audio](https://stability.ai/stable-audio)
- [MusicGen](https://github.com/facebookresearch/audiocraft) (Meta)
- [AudioCraft](https://github.com/facebookresearch/audiocraft)

## Ressources utiles
- [Site interactif](https://riffusion.com)
- [GitHub](https://github.com/riffusion/riffusion)
- [Colab](https://colab.research.google.com/github/riffusion/riffusion)

## Exemple d'appel API
```python
from riffusion import RiffusionPipeline

pipe = RiffusionPipeline.from_pretrained("riffusion/riffusion-model")
audio = pipe("Synthwave nostalgique avec des nappes chaudes", num_inference_steps=50)
audio.export("synthwave.wav")
```

## Input/Output
- Input : "Guitare flamenco fusion électronique"
- Sortie : 🎸 Écouter (12s, 48kHz)

## Avantages/Limites
| ✅ Avantages | ❌ Inconvénients |
|-------------|-----------------|
| Génération immédiate | Artefacts hautes fréquences |
| Interface visuelle innovante | Pas de structure musicale complexe |
| Customisation via interpolation | Dataset limité aux styles électroniques |

## Confidentialité
- Aucun tracking utilisateur
- Traitement possible en local

## Statistiques
- 8.4k stars GitHub
- 1M+ tracks générés (2023)
- 4.2/5 sur les benchmarks créatifs 