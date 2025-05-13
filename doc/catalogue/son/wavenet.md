# WaveNet

## Description
WaveNet est un réseau neuronal de type auto-régressif développé par DeepMind (filiale IA de Google) pour la synthèse audio échantillon par échantillon. Il a révolutionné la synthèse vocale en produisant des sons beaucoup plus naturels que les systèmes traditionnels.

## Caractéristiques techniques
- **Type** : Réseau neuronal de type auto-régressif pour la synthèse audio échantillon par échantillon
- **Développeur** : DeepMind (filiale IA de Google)
- **Date de sortie** : 2016
- **Architecture** : Réseau de convolutions dilatées causales
- **Framework** : TensorFlow (originalement), PyTorch (réimplémentations)
- **Sortie audio** : Signal audio direct (waveform, pas de spectrogramme)
- **Entraînement** : Très lent sans accélérations modernes (TPU, optimisation)
- **Objectif** : Générer des échantillons audio ultra-réalistes (16kHz, 24kHz ou 48kHz)

## Objectif
WaveNet a été développé pour produire des sons réalistes directement à partir d'ondes audio, en générant échantillon par échantillon (sample by sample) plutôt que de passer par des représentations intermédiaires. Le résultat est une qualité audio beaucoup plus naturelle pour les voix humaines et les musiques, par rapport aux systèmes de synthèse vocale classiques de l'époque.

## Fonctionnement
| Étape | Description |
|-------|-------------|
| Entrée | Conditionnement optionnel (par ex. texte phonétique pour la synthèse vocale) |
| Génération | Prédiction auto-régressive d'un échantillon audio à partir du contexte précédent |
| Sortie | Signal audio continu reconstruit échantillon par échantillon |

## Techniques utilisées
- Convolutions causales dilatées pour élargir rapidement la "vue" temporelle sans perdre de résolution
- Modélisation probabiliste de la forme d'onde audio
- Conditionnement externe (texte, speaker ID) pour contrôler la génération vocale ou musicale

## Applications
- Synthèse vocale réaliste (ex : voix de Google Assistant)
- Génération musicale expérimentale (sons instrumentaux plus naturels)
- Amélioration des vocodeurs (post-traitement audio plus fluide)
- Applications téléphoniques / TTS (Text-to-Speech)

## Exemples d'utilisation
| Domaine | Exemple |
|---------|---------|
| Assistants vocaux | Synthèse naturelle de la voix de Google Assistant |
| Musique | Génération de sons d'instruments ou de textures audio |
| Accessibilité | Lecture vocale fluide pour malvoyants |

## Avantages
- Qualité audio exceptionnelle (très naturelle)
- Fonctionne directement sur le signal audio brut
- Conditionnement flexible (style, texte, identité vocale)
- Inspiré beaucoup de vocodeurs modernes (Tacotron 2, Parallel WaveGAN, etc.)

## Inconvénients
- Temps de génération très lent sans optimisation
- Difficile à entraîner à grande échelle sans puissants GPU/TPU
- Modèle lourd en mémoire et calcul
- Complexité technique élevée pour implémentation

## Ressources utiles
- [Publication scientifique officielle WaveNet (DeepMind)](https://arxiv.org/abs/1609.03499)
- [Code source non officiel de WaveNet en PyTorch](https://github.com/r9y9/wavenet_vocoder)
- [Explication technique sur le blog DeepMind](https://deepmind.com/blog/article/wavenet-generative-model-raw-audio)
- [Démo vocale WaveNet par DeepMind (archive)](https://deepmind.com/blog/article/wavenet-generative-model-raw-audio)
- [Colab – Implémentation WaveNet minimaliste en PyTorch](https://colab.research.google.com/github/r9y9/wavenet_vocoder/blob/master/notebooks/wavenet_vocoder_demo.ipynb) 