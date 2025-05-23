# [Vidu](https://vidu.ai)

## Fiche d'identité
- **Nom de l'outil** : Vidu
- **Catégorie** : Vidéo, Multimodal
- **Développeur** : Shengshu Technology + Tsinghua University (Chine)
- **Date de sortie** : Avril 2024 (démo publique)

## Objectif
Créer des vidéos longues, réalistes et cohérentes à partir de texte, grâce à une architecture basée sur diffusion + LLM.

## Fonctionnement
| Étape | Description |
|-------|-------------|
| Entrée | Prompt texte décrivant la scène ou l'action souhaitée |
| Traitement | Modèle de diffusion guidé par un LLM multimodal → conversion en séquences visuelles cohérentes |
| Sortie | Vidéo réaliste jusqu'à 16 secondes, en 1080p |

## Fonctions principales
- Génération vidéo haute résolution (1080p)
- Longues séquences (jusqu'à 16 secondes)
- Compréhension des dynamiques physiques et spatiales
- Modèle basé sur diffusion + langage
- Génération à partir de texte uniquement
- Démo publique disponible en ligne

## Exemples d'usage
| Domaine | Exemple |
|---------|---------|
| Education | Génération de courtes vidéos explicatives (sciences, biologie, etc.) |
| Marketing | Création de vidéos promotionnelles à partir d'un simple brief |
| Dev/Produit | Simulation visuelle d'expériences utilisateur |
| Accessibilité | Contenus visuels à partir d'instructions verbales |

## Détails techniques
| Caractéristique | Valeur |
|-----------------|---------|
| Architecture | Diffusion + LLM (modèle texte-guidé) |
| Framework | Non spécifié (probablement PyTorch) |
| Input | Texte (prompt) |
| Output | Vidéo (MP4 ou autre, 1080p max, 16 sec max) |
| API | Pas encore disponible publiquement |
| Licence | Propriétaire / recherche académique |

## Tarifs
| Plan | Prix | Limites/détails |
|------|------|-----------------|
| Démo publique | Gratuit | Accessible via site officiel (printemps 2024) |
| Accès public | Payant (tarif non public) | - |
| Accès public | Gratuit à usage limité | 80 crédits disponibles par mois |

## Versions clés
- [v0.9 – Démo initiale d'avril 2024](https://vidu.ai/v0.9) - [GitHub](https://github.com/shengshu-tech/vidu-v0.9)
- [v1.0 – Lancement public complet (attendu en 2025)](https://vidu.ai/v1.0) - [GitHub](https://github.com/shengshu-tech/vidu-v1.0)

## Alternatives connues
- Sora (OpenAI)
- Lumiere (Google)
- Runway Gen-2
- Pika
- ModelScope

## Ressources utiles
- [Vidéo de démonstration sur Weibo](https://weibo.com/vidu)
- [Annonce officielle (Tsinghua News)](https://news.tsinghua.edu.cn)

## Exemple d'appel API (pas encore disponible – hypothétique)
```bash
curl -X POST https://api.vidu.ai/generate 
 -H "Authorization: Bearer YOUR_API_KEY" 
 -d '{"prompt":"Un panda mange du bambou dans une forêt tranquille", "duration":12}'
```

## Exemple Input/Output
**Prompt** : "Un train traverse un pont suspendu au coucher du soleil, avec une rivière brillante en dessous."
**Sortie** : Vidéo réaliste d'environ 14 secondes, mouvements fluides, bon rendu des couleurs et de la lumière.

## Avantages et Inconvénients
| Avantages | Inconvénients |
|-----------|---------------|
| Longues vidéos (jusqu'à 16 s) | Modèle propriétaire (non open source) |
| Bonne qualité visuelle | API non publique |
| Compréhension de scènes complexes | Texte uniquement (pas image/vidéo en entrée) |
| 80 crédits disponibles par mois | - |

## Sécurité et Confidentialité
- Aucune mention officielle sur filigranes ou sécurité des contenus (à surveiller)

## Compatibilité
- Plateformes : Web (démo), version complète en développement
- Plugins : Aucun plugin connu à ce jour

## Statistiques utilisateurs
- Modèle en phase de démonstration – fort engouement médiatique en Chine
- Première IA vidéo chinoise capable de rivaliser avec Sora

## Comparaison avec les alternatives
| Critère | Vidu | Sora | Lumiere (Google) |
|---------|------|------|------------------|
| Gratuit | ✅ (limité à 80 crédits) | ❌ | ❌ |
| API dispo | ❌ | ✅ | ❌ |
| Résolution max | 1080p | 1080p | 1024p |
| Longueur vidéo | 16 sec | 60 sec | 5 sec |
| Multimodal | ❌ (texte seul) | ✅ | ✅ | 