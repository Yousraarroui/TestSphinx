# Sora

## Description
Sora est un modèle de génération de vidéos développé par OpenAI, capable de créer des vidéos à partir de descriptions textuelles, d'images ou d'autres vidéos.

## Caractéristiques techniques
- **Type** : Transformers + diffusion
- **Entrées possibles** : Texte, image, vidéo
- **Sortie** : Vidéo haute qualité
- **Statut** : Version beta (février 2024), accès public prévu pour décembre 2024

## Fonctionnement
Le modèle fonctionne en 8 étapes :
1. Input (texte, image ou vidéo)
2. Encodage du texte (LLM)
3. Analyse des images/vidéos (Vision)
4. Conversion en espace latent multimodal
5. Génération vidéo via modèle de diffusion
6. Transformers spatio-temporels pour la cohérence
7. Post-traitement (super-résolution, fluidité)
8. Output (vidéo finale)

## Caractéristiques techniques avancées
- Résolution jusqu'à 1080p
- Durée maximale : 1 minute
- Compréhension des relations spatiales et physiques
- Excellente cohérence temporelle entre les frames

## Avantages
- Haute qualité visuelle
- Longueur de vidéo importante (1 minute)
- Compréhension avancée des relations spatiales
- Multimodalité (texte, image, vidéo)
- Cohérence temporelle excellente
- Adapté à divers usages (cinéma, publicité, etc.)

## Limites
- Modèle propriétaire
- Accès limité et payant
- Pas de bande-son
- Besoin de prompts très détaillés
- Risque d'usage malveillant
- Temps de génération élevé

## Ressources utiles
- [Publication scientifique](https://arxiv.org/pdf/2402.17177)
- [Plan Open-Sora](https://arxiv.org/pdf/2412.00131)
- [Site officiel](https://sora.com/)
- [Documentation Wikipedia](https://en.wikipedia.org/wiki/Sora_(text-to-video_model))

## Exemples de prompts
| Niveau | Prompt | Caractéristiques testées |
|--------|--------|--------------------------|
| Facile | Un chat blanc assis sur un coussin regarde par la fenêtre pendant qu'il pleut | Animation légère, scène fixe |
| Moyen | Une femme en manteau jaune traverse un pont en bois au milieu d'une forêt d'automne, avec des feuilles qui tombent lentement autour d'elle | Mouvement, fluidité, ambiance naturelle |
| Difficile | Un homme en costume rouge marche lentement dans une rue de ville sous la pluie, la nuit. Les néons colorés se reflètent sur les flaques d'eau, le vent fait voler sa cravate, et une voiture passe doucement en arrière-plan | Mouvements complexes, lumière, physique, arrière-plan dynamique | 