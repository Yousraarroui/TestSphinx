# Stable Diffusion

## Description
Stable Diffusion est un modèle de génération d'images open source développé par Stability AI, permettant de créer des images à partir de descriptions textuelles ou d'autres images.

## Caractéristiques techniques
- **Type d'entrée/sortie** : Texte vers image (text-to-image) ou image vers image (image-to-image)
- **Modèle** : Modèle de diffusion
- **Statut** : Open source
- **Date de lancement** : 22 août 2022

## Fonctionnement
Le modèle fonctionne en 5 étapes :
1. Description par l'utilisateur
2. Compression de l'image par l'auto-encodeur variationnel (VAE)
3. Ajout de bruit gaussien
4. Débruitage par le bloc U-Net
5. Génération de l'image finale par le décodeur VAE

## Tarification
- **Gratuit** : Complètement gratuit (code open source)
- **Installation locale** : Possible sur machine personnelle

## Avantages
- Extrêmement rapide
- Photoréalisme élevé
- Flexibilité dans les styles
- Open source et modifiable
- Installation locale possible

## Inconvénients
- Aucune limitation d'utilisation (risque de deepfakes)
- Coûts de calcul élevés
- Courbe d'apprentissage importante
- Nécessite une bonne configuration matérielle

## Ressources utiles
- [GitHub officiel](https://github.com/CompVis/stable-diffusion)
- [Documentation technique](https://huggingface.co/docs/diffusers/using-diffusers/loading)
- [Guide d'installation](https://github.com/CompVis/stable-diffusion#installation)
- [Exemples d'utilisation](https://huggingface.co/spaces/stabilityai/stable-diffusion) 