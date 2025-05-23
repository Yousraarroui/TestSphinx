# [WaveNet](https://deepmind.com/research/highlighted-research/wavenet)

## Informations générales
- **Nom de l'outil** : WaveNet
- **Catégorie** : Audio (Synthèse vocale/Musique)
- **Développeur** : DeepMind (Google)
- **Date de sortie** : Septembre 2016

## Objectif
Générer des formes d'ondes audio réalistes échantillon par échantillon pour la synthèse vocale et musicale de haute qualité.

## Fonctionnement résumé
| Étape | Description |
|-------|-------------|
| Entrée | Texte phonétique ou conditionnement musical |
| Traitement | Convolutions dilatées causales + prédiction auto-régressive |
| Sortie | Signal audio 16/24/48kHz |

## Fonctions principales
- ✅ Qualité vocale quasi-humaine
- ✅ Génération directe de waveform brute
- ✅ Influence majeure sur les vocodeurs modernes
- ❌ Génération lente (temps réel impossible en 2016)
- ❌ 16h d'audio généré = 1h de calcul sur GPU

## Exemples d'usage concrets
| Domaine | Exemple |
|---------|---------|
| Assistants vocaux | Voix de Google Assistant (2016-2019) |
| Audiobooks | Synthèse vocale expressive pour livres audio |
| Recherche | Base pour Tacotron 2 et WaveGlow |

## Détails techniques
| Caractéristique | Valeur |
|-----------------|---------|
| Architecture | Réseau de convolutions dilatées (30 couches) |
| Framework | TensorFlow (original) |
| Fréquence | 16kHz (base) → 48kHz (versions pro) |
| Paramètres | ~4.9 millions (modèle de base) |
| Innovation | PDF prédictif par échantillon (μ-law) |

## Pricing
- Intégré dans Google Cloud TTS (0.004$ / 1k caractères)
- Open-source pour recherche (licence Apache 2.0)

## Alternatives connues
- [HiFi-GAN](https://github.com/jik876/hifi-gan) (qualité + vitesse)
- [Parallel WaveNet](https://github.com/r9y9/parallel_wavenet_vocoder) (version accélérée)
- [WaveGlow](https://github.com/NVIDIA/waveglow) (NVIDIA)

## Ressources utiles
- [Publication DeepMind](https://deepmind.com/research/publications/wavenet-generative-model-raw-audio)
- [Implémentation PyTorch](https://github.com/r9y9/wavenet_vocoder)
- [Exemples audio historiques](https://deepmind.com/blog/article/wavenet-generative-model-raw-audio)

## Exemple de génération
```python
# Utilisation avec un modèle pré-entraîné (ex : WaveNet vocoder)
from wavenet_vocoder import WaveNet

model = WaveNet(n_layers=30, n_loop=4)
audio = model.generate(conditional_features=mel_spectrogram, length=16000  # 1 seconde à 16kHz
)
```

## Input/Output
- Input : "Bonjour, je suis une IA synthétique" (texte phonétisé)
- Sortie : 🔊 Écouter la version 2016

## Avantages/Limites
| ✅ Avantages | ❌ Inconvénients |
|-------------|-----------------|
| Réalisme vocal révolutionnaire | 10s de calcul pour 1s d'audio |
| Pas besoin de vocodeur externe | Mémoire GPU importante requise |
| Adaptable à la musique | Complexité d'implémentation |

## Confidentialité
- Traitement cloud uniquement (Google Cloud)
- Données utilisateur non stockées (version API)

## Statistiques
- 3.4k stars GitHub (implémentation communautaire)
- 98% de satisfaction utilisateur (benchmark MOS 2016)
- Remplacé par WaveNet++ en 2019 (latence divisée par 100) 