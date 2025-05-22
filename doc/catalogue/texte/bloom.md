# [BLOOM](https://huggingface.co/bigscience/bloom)

- **Nom de l'outil** : BLOOM (BigScience Large Open-science Open-access Multilingual Language Model)
- **Catégorie** : Texte
- **Développeur** : BigScience (initiative collaborative coordonnée par Hugging Face)
- **Date de sortie** : 
  - Version initiale : 11 juillet 2022

## Objectif
Fournir un modèle de langage multilingue de grande taille, ouvert et transparent, accessible à la communauté scientifique et au grand public, afin de démocratiser l'accès aux technologies d'IA avancées et promouvoir une recherche éthique et responsable.

## Fonctionnement résumé
| Étape | Description |
|-------|-------------|
| Entrée | Texte |
| Traitement | Architecture Transformer de type décodeur uniquement |
| Sortie | Texte généré en fonction de la tâche spécifiée |

## Fonctions principales
- ✅ Génération de texte (rédaction, résumé, traduction)
- ✅ Réponse à des questions
- ✅ Classification de texte
- ✅ Analyse de sentiments
- ✅ Complétion de texte

## Exemples d'usage concrets
| Domaine | Exemple |
|---------|---------|
| Éducation | Génération de résumés de cours, traduction de documents |
| Développement | Génération de code, documentation automatique |
| Recherche | Extraction d'informations, synthèse de documents |
| Service client | Réponses automatisées aux questions fréquentes |
| Accessibilité | Assistance à la lecture et à la rédaction pour les personnes en situation de handicap |

## Détails techniques
| Caractéristique | Valeur |
|-----------------|---------|
| Architecture | Transformer (décodeur uniquement) |
| Framework | PyTorch (via Hugging Face Transformers) |
| Input | Texte |
| Output | Texte |
| API | Disponible via Hugging Face |
| Licence | RAIL (Responsible AI License) v1.0 |

## Pricing
BLOOM est un modèle open-source ; son utilisation est gratuite. Les coûts associés dépendent de l'infrastructure utilisée pour l'entraînement ou l'inférence.

## Releases clés
- **BLOOM** : 2022 – Version initiale avec 176 milliards de paramètres

## Alternatives connues
- ChatGPT (OpenAI)
- Gemini (Google)
- OPT (Meta AI)

## Ressources utiles
- [Site officiel](https://huggingface.co/bigscience/bloom)
- [Documentation API](https://huggingface.co/docs/transformers/model_doc/bloom)
- [Blog BigScience](https://bigscience.huggingface.co/blog/bloom)
- [GitHub BigScience](https://github.com/bigscience-workshop)

## Exemple d'appel API
```bash
curl https://api-inference.huggingface.co/models/bigscience/bloom 
-H "Authorization: Bearer YOUR_API_KEY" 
-H "Content-Type: application/json" 
-d { "inputs": "Traduire en français : The house is wonderful."
}
```

## Avantages/Limites
| ✅ Avantages | ❌ Inconvénients |
|-------------|-----------------|
| Modèle multilingue couvrant 46 langues naturelles et 13 langages de programmation | Nécessite des ressources computationnelles importantes pour l'entraînement et l'inférence |
| Open-source et accessible à tous | Peut nécessiter un fine-tuning pour des tâches spécifiques |
| Entraîné de manière transparente avec une collaboration internationale | |

## Confidentialité
En tant que modèle open-source, BLOOM ne collecte pas de données utilisateur. La confidentialité dépend de l'implémentation spécifique et de l'infrastructure utilisée.

## Compatibilité
- **Plateformes** : PyTorch (via Hugging Face Transformers)
- **Intégrations** : Hugging Face Transformers, API Hugging Face

## Statistiques
BLOOM a été téléchargé plus de 40 000 fois dès le premier mois suivant sa sortie en juillet 2022. Le projet a mobilisé plus de 1 000 chercheurs de 70 pays et 250 institutions, avec un entraînement de 117 jours sur le supercalculateur Jean Zay, nécessitant une subvention de calcul estimée à 3 millions d'euros.

## Comparaison rapide
| Modèle | Accès | Multimodal | Licence |
|--------|-------|------------|---------|
| ChatGPT3 | Payant | Non | Propriétaire |
| BERT | Open-source | Non | Apache 2.0 |

## Voir aussi
- [Fiche Llama3](llama.md)
- [Fiche T5](t5.md) 