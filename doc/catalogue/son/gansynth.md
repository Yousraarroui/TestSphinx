# GANSynth

## Description
GANSynth est un modèle de synthèse audio basé sur les GANs (Generative Adversarial Networks) développé par Google Brain dans le cadre du projet Magenta. Il propose une approche innovante pour synthétiser des sons instrumentaux en générant des spectrogrammes plutôt que directement des signaux audio.

## Caractéristiques techniques
- **Type** : GAN (Generative Adversarial Network) pour audio basé sur spectrogrammes
- **Développeur** : Google Brain – Projet Magenta
- **Date de sortie** : Avril 2019
- **Architecture** : GAN progressif conditionné
- **Framework** : TensorFlow 1.x
- **Vocodeur utilisé** : Griffin-Lim
- **Dataset d'entraînement** : NSynth Dataset (305 979 sons instrumentaux)
- **Durée d'entraînement** : Plusieurs jours sur TPU (Google Cloud)
- **Objectif** : Génération rapide de haute fidélité (> 16kHz)

## Objectif
GANSynth propose une nouvelle approche pour synthétiser des sons instrumentaux en générant des spectrogrammes (plutôt que directement des signaux audio) et en les reconvertissant ensuite en sons grâce à des vocodeurs. Cette approche permet une génération plus rapide et de meilleure qualité que les approches précédentes comme NSynth.

## Fonctionnement
| Étape | Description |
|-------|-------------|
| Entrée | Vecteur latent aléatoire + conditionnement sur type d'instrument |
| Génération | GAN génère un spectrogramme cohérent |
| Reconstruction | Vocodeur transforme le spectrogramme en onde sonore .wav |

## Techniques utilisées
- Progressive Growing of GANs (croissance progressive de la complexité)
- Wasserstein GAN avec pénalité de gradient (WGAN-GP) pour stabiliser l'entraînement

## Applications
- Synthèse rapide de notes individuelles (ex : piano, guitare, synthétiseur)
- Interpolation fluide entre sons → morphing créatif
- Création de nouvelles textures sonores pour musique électronique, jeux vidéo, recherche IA

## Exemples d'utilisation
| Domaine | Exemple |
|---------|---------|
| Synthétiseur IA | Générer des presets inédits de synthé |
| Musique électronique | Créer de nouveaux sons pour techno, ambient |
| Recherche audio IA | Étudier la morphologie sonore entre instruments |

## Avantages
- Génération ultra rapide
- Haute fidélité sonore
- Interpolation créative fluide
- Open-source accessible

## Inconvénients
- Entraînement lourd sur TPU/GPU
- Génère uniquement des notes isolées
- TensorFlow 1.x (obsolète en 2025)
- Complexe à utiliser directement pour débutant

## Ressources utiles
- [Publication scientifique officielle sur arXiv](https://arxiv.org/abs/1902.08710)
- [Code source GANSynth (GitHub Magenta)](https://github.com/magenta/magenta/tree/main/magenta/models/gansynth)
- [Colab - Audio Models (Magenta)](https://colab.research.google.com/drive/1hyXI91iY8ABr9rFN8OytX5FtueaSThTm#scrollTo=ge3NZoqjBb6Y)

## Démonstrations
- [Exemple de code simple pour générer du son](https://colab.research.google.com/drive/1hyXI91iY8ABr9rFN8OytX5FtueaSThTm#scrollTo=ge3NZoqjBb6Y) 