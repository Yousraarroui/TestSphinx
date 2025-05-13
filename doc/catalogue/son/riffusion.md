# Riffusion

## Description
Riffusion est un modèle de génération musicale basé sur la diffusion, développé par Seth Forsgren et Hayk Martiros. Il applique les principes de Stable Diffusion aux spectrogrammes pour générer de la musique en continu à partir de prompts textuels.

## Caractéristiques techniques
- **Type** : Diffusion model appliqué aux spectrogrammes pour la génération de musique en continu
- **Développeur** : Seth Forsgren et Hayk Martiros (projet indépendant)
- **Date de sortie** : Décembre 2022
- **Architecture** : Diffusion latente sur spectrogrammes
- **Framework** : PyTorch
- **Reconstruction audio** : ISTFT (Inverse Short-Time Fourier Transform)
- **Dataset d'entraînement** : Musique instrumentale issue de bases publiques
- **Durée de génération** : Quelques secondes pour 5-10 secondes d'audio
- **Objectif** : Génération musicale continue, pilotée par prompts texte

## Objectif
Riffusion vise à générer de la musique en temps réel à partir de prompts textuels. Il génère des spectrogrammes musicaux via un modèle de diffusion adapté à l'audio, puis les reconstruit en fichiers sonores .wav. Le résultat permet la création rapide de morceaux courts et des transitions fluides entre styles.

## Fonctionnement
| Étape | Description |
|-------|-------------|
| Entrée | Prompt texte (ex : "Jazz piano", "Electronic dance") |
| Génération | Modèle de diffusion génère un spectrogramme basé sur Stable Diffusion |
| Reconstruction | Transforme le spectrogramme en audio avec la transformée de Fourier inverse (ISTFT) |

## Techniques utilisées
- Adaptation de Stable Diffusion sur l'espace des spectrogrammes audio
- Interpolation latente entre prompts pour créer des transitions musicales continues
- Reconstruction du signal audio via ISTFT (Inverse Short-Time Fourier Transform)

## Applications
- Génération de boucles musicales pour DJ, beatmakers, producteurs
- Création de transitions fluides entre différents styles musicaux
- Exploration de nouvelles idées musicales à partir de simples mots clés
- Utilisation pour des projets artistiques génératifs interactifs

## Exemples d'utilisation
| Domaine | Exemple |
|---------|---------|
| Production musicale | Générer des loops "house", "jazz", "ambient" instantanément |
| DJing en live | Créer des transitions fluides entre deux styles musicaux |
| Recherche audio IA | Étudier comment l'IA gère le morphing entre genres sonores |

## Avantages
- Génération rapide de musique basée sur du texte
- Transitions fluides entre styles possibles
- Modèle léger (peut tourner en Colab)
- Open-source, facile à modifier

## Inconvénients
- Audio limité en durée (~10 secondes)
- Résolution sonore parfois moyenne (artefacts)
- Moins performant pour des compositions longues ou complexes
- Sons parfois répétitifs sans prompts complexes

## Ressources utiles
- [Publication / Projet officiel Riffusion](https://www.riffusion.com/)
- [Code source Riffusion sur GitHub](https://github.com/riffusion/riffusion)
- [Site officiel interactif Riffusion](https://www.riffusion.com/) (Écrire un prompt, générer une musique directement !)
- [Colab officiel Riffusion simple](https://colab.research.google.com/github/riffusion/riffusion/blob/main/notebooks/riffusion.ipynb) (Permet de générer ses propres spectrogrammes et sons à partir de textes) 