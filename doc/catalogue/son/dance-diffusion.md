# Dance Diffusion

## Description
Dance Diffusion est un modèle de diffusion audio développé par Harmonai (filiale communautaire soutenue par Stability AI), spécialisé dans la génération de samples audio courts de haute qualité. Il permet de produire des loops, des one-shots et des textures sonores utilisables en production musicale.

## Caractéristiques techniques
- **Type** : Modèle de diffusion audio pour samples courts
- **Développeur** : Harmonai (soutenue par Stability AI)
- **Date de sortie** : Septembre 2022
- **Framework** : PyTorch (avec Hugging Face Diffusers)
- **Architecture** : DDPM (Diffusion) adaptée audio
- **Entrée** : Bruit initial aléatoire (option : prompt audio)
- **Sortie** : Sample audio de 1-8 secondes
- **Qualité** : 44.1kHz
- **Vocodeur** : Griffin-Lim
- **Dataset d'entraînement** : NSynth Dataset (305 979 sons instrumentaux)
- **Durée d'entraînement** : Plusieurs jours sur TPU (Google Cloud)
- **Objectif** : Génération rapide de haute fidélité (> 16kHz)

## Fonctionnement
Le modèle fonctionne en 3 étapes :
1. **Entrée** : Bruit aléatoire + (optionnellement) prompt audio ou style conditionné
2. **Diffusion inverse** : Suppression progressive du bruit pour produire un échantillon audio
3. **Sortie** : Fichier audio court (1 à 8 secondes)

## Techniques utilisées
- Diffusion latente audio adaptée pour spectrogrammes courts
- Conditionnement optionnel sur des catégories (drums, bass, synth)
- DDPM (Denoising Diffusion Probabilistic Model)
- GAN progressif conditionné

## Applications
- Génération de samples audio uniques pour packs de production
- Création rapide de one-shots pour drum machines, samplers
- Loops de musique électronique (techno, house, hip-hop)
- Textures sonores expérimentales pour sound design
- Synthèse rapide de notes individuelles (piano, guitare, synthétiseur)
- Interpolation fluide entre sons (morphing créatif)
- Création de nouvelles textures sonores pour musique électronique, jeux vidéo, recherche IA

## Exemples d'utilisation
| Domaine | Exemple |
|---------|---------|
| Beatmaking | Génération de snares, kicks, hi-hats inédits |
| DJing/Live sets | Création de loops rythmés originaux |
| Production sonore | Enrichissement de banques de sons pour musique, jeux vidéo, films |
| Synthétiseur IA | Générer des presets inédits de synthé |
| Musique électronique | Créer de nouveaux sons pour techno, ambient |
| Recherche audio IA | Étudier la morphologie sonore entre instruments |

## Avantages
- Génération de samples courts haute qualité
- Open-source, facile à expérimenter
- Compatible avec Hugging Face Diffusers
- Idéal pour la production musicale créative
- Haute fidélité audio (> 16kHz)
- Morphing créatif entre sons

## Inconvénients
- Limité à des boucles ou courts échantillons
- Pas de génération de musique longue/structurée
- Modèles lourds (nécessite GPU pour générer vite)
- Moins adapté à la musique classique ou acoustique

## Ressources utiles
- [Publication technique](https://github.com/Harmonai-org/dance-diffusion)
- [Code source](https://github.com/Harmonai-org/dance-diffusion)
- [Forum Harmonai](https://github.com/Harmonai-org/dance-diffusion/discussions)
- [Démo Colab](https://colab.research.google.com/github/Harmonai-org/dance-diffusion/blob/main/notebooks/dance_diffusion.ipynb)
- [WebUI communautaire](https://github.com/Harmonai-org/dance-diffusion-webui)

## Dataset d'entraînement
- NSynth Dataset (305 979 sons instrumentaux)
- Samples libres de droits
- FreeSound
- Packs audio publics 