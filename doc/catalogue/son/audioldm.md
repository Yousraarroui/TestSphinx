# AudioLDM

## Description
AudioLDM est un modèle de génération audio développé par l'University of Surrey, capable de créer des sons et des ambiances à partir de descriptions textuelles. Il utilise une approche basée sur les modèles de diffusion latente, similaire à celle utilisée dans Stable Diffusion pour les images.

## Caractéristiques techniques
- **Type** : Modèle de diffusion latent pour audio
- **Développeur** : University of Surrey
- **Date de sortie** : Février 2023
- **Framework** : PyTorch
- **Vocodeur** : HiFi-GAN
- **Encodage texte/audio** : CLAP model
- **Résolution audio** : 16kHz

## Fonctionnement
Le modèle fonctionne en 4 étapes :
1. **Entrée** : Texte descriptif (ex: "sons d'oiseaux dans une forêt tropicale")
2. **Encodage** : Transformation du texte en représentation latente
3. **Génération** : Diffusion latente pour produire un spectrogramme
4. **Reconstruction** : Conversion du spectrogramme en audio .wav via le vocodeur

## Techniques utilisées
- Latent Diffusion Models (LDM) adaptés à l'audio
- CLAP (Contrastive Language-Audio Pretraining) pour l'alignement texte-son
- HiFi-GAN comme vocodeur

## Applications
- Génération de bruitages pour films, jeux vidéo, VR
- Création d'ambiances sonores thématiques
- Design sonore assisté par IA
- Exploration musicale de nouvelles textures sonores

## Exemples d'utilisation
| Domaine | Exemple |
|---------|---------|
| Films/Documentaires | Génération d'ambiances réalistes (jungle, ville futuriste) |
| Jeux vidéo | Production de bruitages dynamiques adaptés aux actions |
| Musique expérimentale | Création de textures sonores conceptuelles |

## Avantages
- Génération de sons complexes à partir de texte simple
- Grande variété sonore possible
- Démo Colab facile à utiliser
- Basé sur des techniques modernes de diffusion

## Inconvénients
- Limité à de courtes durées (quelques secondes)
- Sons parfois flous ou bruités avec des prompts vagues
- Pas optimisé pour les musiques longues et structurées
- Nécessite GPU pour des temps de génération rapides

## Ressources utiles
- [Publication scientifique](https://arxiv.org/abs/2301.12503)
- [Code source GitHub](https://github.com/haoheliu/AudioLDM)
- [Démo Colab](https://colab.research.google.com/drive/1G-G2CXCJD6yGFHAxcmcSu8aioU18TMiZ)
- [Documentation CLAP](https://github.com/LAION-AI/CLAP)

## Dataset d'entraînement
- AudioCaps
- Freesound
- UrbanSound8K 