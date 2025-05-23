# [Nous-Hermes 2 Mistral 7B DPO](https://github.com/NousResearch/Nous-Hermes-2-Mistral-7B-DPO)

- **Nom de l'outil** : Nous-Hermes 2 Mistral 7B DPO
- **Catégorie** : Texte (LLM)
- **Développeur** : Nous Research
- **Date de sortie** : 20 février 2024

## Objectif
Fournir un modèle de langage performant et accessible, optimisé pour les dialogues multi-tours, l'instruction-following et les tâches de raisonnement, tout en étant léger et déployable localement.

## Fonctionnement résumé
| Étape | Description |
|-------|-------------|
| Entrée | Texte (prompt utilisateur) |
| Traitement | Modèle Mistral 7B affiné avec DPO (Direct Preference Optimization) |
| Sortie | Texte généré en fonction de la tâche |

## Fonctions principales
- ✅ Génération de texte (rédaction, résumé, traduction)
- ✅ Réponse à des questions
- ✅ Instruction-following avancé
- ✅ Dialogue multi-tours avec format ChatML
- ✅ Raisonnement logique et résolution de problèmes
- ✅ Génération de code
- ❌ Pas de capacités multimodales

## Exemples d'usage concrets
| Domaine | Exemple |
|---------|---------|
| Éducation | Assistance à l'apprentissage |
| Développement | Génération de code |
| Recherche | Analyse de données |
| Service client | Support technique |
| Création de contenu | Rédaction d'articles |

## Détails techniques
| Caractéristique | Valeur |
|-----------------|---------|
| Architecture | Transformer (Mistral 7B) |
| Framework | PyTorch (via Hugging Face) |
| Input | Texte |
| Output | Texte |
| Licence | Apache 2.0 |

## Pricing
- Gratuit (open-source) • Coûts d'infrastructure selon l'usage

## Releases clés
- [Nous-Hermes 2 Mistral 7B DPO](https://huggingface.co/NousResearch/Nous-Hermes-2-Mistral-7B-DPO) : Version initiale (2024)

## Alternatives connues
- Mistral 7B Instruct (Mistral AI)
- OpenHermes 2.5 (Teknium)
- Zephyr 7B Beta (Hugging Face)

## Ressources utiles
- [Documentation](https://huggingface.co/NousResearch/Nous-Hermes-2-Mistral-7B-DPO)
- [GitHub](https://github.com/NousResearch/Nous-Hermes-2-Mistral-7B-DPO)

## Exemple d'appel API
```bash
curl https://api-inference.huggingface.co/models/NousResearch/Nous-Hermes-2-Mistral-7B-DPO \
-H "Authorization: Bearer YOUR_API_KEY" \
-H "Content-Type: application/json" \
-d '{
    "model": "claude-3.5-sonnet",
    "messages": [{"role": "user", "content": "Explique la théorie de la relativité"}]
}'
```

## Input/Output
- Input : "Explique la théorie de la relativité"
- Output : "La théorie de la relativité, développée par Albert Einstein..."

## Avantages/Limites
| ✅ Avantages | ❌ Inconvénients |
|-------------|-----------------|
| Modèle léger et performant | Pas de capacités multimodales |
| Excellent suivi d'instructions | Fine-tuning nécessaire pour tâches spécifiques |
| Licence permissive (Apache 2.0) | |

## Confidentialité
- Aucune collecte de données utilisateur (modèle open-source)
- Confidentialité dépend de l'implémentation

## Statistiques
- Plus de 18 000 téléchargements sur Hugging Face (depuis février 2024)

## Compatibilité
- PyTorch (via Hugging Face Transformers)
- API Hugging Face 