# [Dance Diffusion](https://github.com/harmonai-ai/dance-diffusion)

- **Nom de l'outil** : Dance Diffusion
- **Catégorie** : Audio (Génération de samples musicaux)
- **Développeur** : Harmonai (Stability AI)
- **Date de sortie** : Septembre 2022

## Objectif
Générer des samples audio courts (loops, one-shots, beats) via des modèles de diffusion pour la production musicale.

## Fonctionnement résumé
| Étape | Description |
|-------|-------------|
| Entrée | Bruit aléatoire + prompt audio (optionnel) |
| Traitement | Diffusion inverse sur spectrogramme |
| Sortie | Sample 1-8s (44.1kHz) |

## Fonctions principales
- ✅ Génération de loops/one-shots
- ✅ Qualité studio (44.1kHz)
- ✅ Intégration avec outils DAW (Ableton, FL Studio)
- ❌ Limité à 8s max par génération
- ❌ GPU requis pour temps réel

## Exemples d'usage concrets
| Domaine | Exemple |
|---------|---------|
| Beatmaking | Création de kits de drums uniques |
| Musique électronique | Génération de boucles basse/synthé |
| Sound Design | Textures sonores expérimentales |

## Détails techniques
| Caractéristique | Valeur |
|-----------------|---------|
| Architecture | DDPM (Audio Diffusion) |
| Framework | PyTorch + Hugging Face Diffusers |
| Input | Tensor de bruit (256×256) |
| Output | WAV 44.1kHz (1-8s) |
| Licence | MIT |

## Pricing
- Gratuit • Self-hosted (coûts GPU possibles)

## Releases clés
- [v1.0](https://github.com/harmonai-ai/dance-diffusion/releases/tag/v1.0) : Version initiale (09/2022)
- [v1.5](https://github.com/harmonai-ai/dance-diffusion/releases/tag/v1.5) : Support HiFi-GAN (03/2023)

## Alternatives connues
- [Riffusion](https://github.com/riffusion/riffusion) (diffusion pour mélodies)
- [AudioCraft](https://github.com/facebookresearch/audiocraft) (Meta)
- [Stable Audio](https://stability.ai/stable-audio) (Stability AI)

## Ressources utiles
- [GitHub Officiel](https://github.com/harmonai-ai/dance-diffusion)
- [Colab Demo](https://colab.research.google.com/github/harmonai-ai/dance-diffusion/blob/main/notebooks/dance_diffusion.ipynb)
- [Documentation](https://huggingface.co/docs/diffusers/api/pipelines/dance_diffusion)

## Exemple de génération
```python
from diffusers import DanceDiffusionPipeline

pipe = DanceDiffusionPipeline.from_pretrained("harmonai/dance-diffusion")
audio = pipe("drum_loop", num_steps=100).audio
```

## Input/Output
- Input : "techno_kick_120bpm"
- Sortie : 🥁 Écouter le sample (kick drum 4s, 44.1kHz)

## Avantages/Limites
| ✅ Avantages | ❌ Inconvénients |
|-------------|-----------------|
| Samples prêts à l'emploi | Durée très limitée |
| Qualité professionnelle | Courbe d'apprentissage |
| Customisation via prompts | GPU nécessaire |

## Intégrations
- Export Ableton Live
- Plugin VST3 expérimental
- API REST (community)

## Confidentialité
- Modèle open-source
- Aucune collecte de données

## Statistiques
- 3.5k+ stars GitHub
- Utilisé dans 500+ packs samples commerciaux 