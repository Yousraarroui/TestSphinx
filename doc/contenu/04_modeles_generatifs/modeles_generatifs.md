# Modèles Génératifs

1. # Autoencodeur et VAE

   ## **Autoencodeur Classique**

Les **autoencodeurs** sont des réseaux de neurones conçus pour apprendre à représenter efficacement des données, généralement dans un espace de plus faible dimension. Leur objectif principal est de compresser une entrée en une représentation compacte, appelée **représentation latente** ou **vecteur latent**, puis de la reconstruire le plus fidèlement possible. Cette capacité en fait des outils précieux dans le contexte de l’intelligence artificielle générative, bien qu’ils aient aussi des applications en réduction de dimension, en débruitage ou encore en détection d’anomalies.

L’architecture d’un autoencodeur repose sur deux composants principaux : un **encodeur** et un **décodeur**.

### **Encodeur**

L’**encodeur** est un sous-réseau qui transforme les données d’entrée (par exemple, une image) en un vecteur de dimension beaucoup plus réduite. Cette compression se fait à travers une série de couches linéaires (ou convolutifs, selon le type de données), entrecoupées de fonctions d’activation non linéaires comme ReLU ou sigmoid. L’information est progressivement distillée jusqu’à atteindre un goulot d’étranglement, qui contient uniquement ce que le réseau considère comme essentiel à la reconstruction. Ce vecteur latent capture donc les principales caractéristiques de la donnée d’origine, mais dans un espace compact et abstrait.

### **Décodeur**

À partir de cette représentation comprimée, le **décodeur** tente de reconstruire les données d’entrée initiales. Il s’agit d’un réseau symétrique à l’encodeur, qui effectue des transformations inverses pour retrouver la forme et les dimensions originales. Le système est entraîné à minimiser l’écart entre l’entrée et la sortie reconstruite. Selon la nature des données, on utilise des fonctions de perte comme l’erreur quadratique moyenne (pour des valeurs continues) ou la cross-entropy binaire (pour des données normalisées entre 0 et 1, comme les images binaires). L’apprentissage du modèle se fait de manière non supervisée, sans besoin d’annotations, ce qui permet de l’utiliser facilement sur de grands ensembles de données brutes.

![][image46]

Image extraite de : [https://lilianweng.github.io/posts/2018-08-12-vae/](https://lilianweng.github.io/posts/2018-08-12-vae/)

Les autoencodeurs permettent donc de **découvrir la structure sous-jacente** des données, d’une manière non linéaire et plus flexible que des méthodes classiques comme l’ACP (analyse en composantes principales). Ils sont notamment utiles pour **prétraiter des données** avant un apprentissage supervisé, ou pour détecter des anomalies : si une donnée ne peut pas être bien reconstruite, c’est peut-être parce qu’elle est atypique par rapport à ce que le modèle a appris. En IA générative, les autoencodeurs ont été utilisés pour **reconstruire et modifier des images ou du texte**, mais avec des limitations importantes.

En effet, l’un des principaux défauts des autoencodeurs classiques est que l’**espace latent appris** n’est **pas structuré**. Il n’est **pas possible d’échantillonner** aléatoirement ce vecteur latent pour produire de nouvelles données réalistes, car les points générés dans cet espace n’ont pas forcément de sens pour le décodeur. De plus, le modèle est purement déterministe : une même entrée donne toujours la même sortie, ce qui limite la diversité des données générées.

Ces limites ont conduit à la création d’architectures plus avancées, comme les **Variational Autoencoders (VAE)**, qui imposent une structure probabiliste sur l’espace latent.

## **Autoencodeur Variationnel (VAE)**

Les **Variational Autoencoders**, ou VAE, sont une extension probabiliste des autoencodeurs classiques. Ils ont été conçus pour surmonter l’un des principaux défauts des autoencodeurs standards : l’absence de structure exploitable dans l’espace latent. Alors que les autoencodeurs apprennent à encoder chaque donnée en un point précis de cet espace, les VAE apprennent à **représenter** chaque donnée comme une **distribution**, ce qui rend possible l’**échantillonnage aléatoire** et **contrôlé de nouvelles données** — une capacité cruciale en génération.

### **Architecture**

L’architecture d’un VAE ressemble à celle d’un autoencodeur classique, avec un encodeur et un décodeur, mais leur fonctionnement est légèrement différent. L’encodeur ne produit pas directement un vecteur latent, mais apprend à estimer les paramètres d’une distribution gaussienne multivariée : un vecteur de moyennes (μ) et un vecteur d’écarts-types (σ). Ces deux vecteurs définissent une densité de probabilité dans l’espace latent. Pour chaque donnée d’entrée, on échantillonne ensuite un point dans cette distribution — c’est ce point échantillonné qui est transmis au décodeur.

### **Astuce de Reparamétrisation**

Comme cette étape d’échantillonnage introduit une opération non différentiable, une astuce appelée **astuce de reparamétrisation** (reparametrization trick) est utilisée pour permettre la rétropropagation : au lieu d’échantillonner directement z \~ N(μ, σ²), on échantillonne ε \~ N(0, 1\) et on calcule z \= μ \+ σ \* ε. Cela permet de **maintenir un flux de gradient à travers le réseau**.

Le **décodeur**, de son côté, prend ce vecteur latent z et tente de reconstruire l’entrée d’origine. L’entraînement du VAE repose sur une fonction de perte composée de deux termes : une erreur de reconstruction (comme pour l’autoencodeur classique), et un terme de régularisation mesurant la distance entre la distribution apprise (N(μ, σ²)) et une distribution normale standard (N(0, I)). Ce second terme, appelé **divergence de Kullback-Leibler (KL divergence)**, force les représentations latentes à rester proches d’une distribution bien connue, ce qui garantit la structure et la continuité de l’espace latent.

Grâce à cette contrainte, les VAE offrent un **espace latent plus régulier** et plus interprétable. Il devient possible d’interpoler entre deux données en naviguant de manière fluide entre leurs représentations latentes, ou de **générer de nouvelles instances** en échantillonnant simplement un vecteur latent aléatoire suivant la loi normale standard. Cette capacité à générer de la diversité tout en maintenant la cohérence des données produites en fait un outil clé dans le domaine de l’IA générative.

![][image47]

Image extraite de : [https://lilianweng.github.io/posts/2018-08-12-vae/](https://lilianweng.github.io/posts/2018-08-12-vae/)

Cependant, les VAE présentent aussi certaines limites. Les images générées, par exemple, peuvent **manquer de netteté** ou de précision par rapport à d’autres modèles génératifs plus récents comme les GANs. Cela s’explique en partie par le compromis entre fidélité de reconstruction et régularisation probabiliste, imposé par la fonction de perte.

Malgré cela, les VAE restent une approche fondamentale pour la génération de données, notamment dans les contextes où la structuration de l’espace latent est essentielle, comme en génération de texte conditionnelle, en bioinformatique ou dans certains systèmes de recommandation.

#### **Liens Externes (Youtube, Medium, etc):**

* [Autoencoders | Deep Learning Animated](https://youtu.be/hZ4a4NgM3u0?si=w84DhM8nqXmRhKp5)  
* [AE1/ Réseaux autoencodeurs (AE)](https://www.youtube.com/watch?v=ahJdTbAA_kk)  
* [Variational Autoencoders | Generative AI Animated](https://youtu.be/qJeaCHQ1k2w?si=IhJHyczx6Kbc1WMd)  
* [Variational Autoencoders \- EXPLAINED\!](https://youtu.be/fcvYpzHmhvA?si=IyDGPHgFoi-fDPz9)

#### **Bibliographie**

* Michelucci, U., 2022\. An introduction to autoencoders. *arXiv preprint arXiv:2201.03898*.  
* Pinheiro Cinelli, L., Araújo Marins, M., Barros da Silva, E.A. and Lima Netto, S., 2021\. Variational autoencoder. In *Variational methods for machine learning with applications to deep networks* (pp. 111-149). Cham: Springer International Publishing.

2. # Réseaux Antagonistes Génératifs (GAN)

Les **Réseaux Antagonistes Génératifs (Generative Adversarial Networks, GANs)**, proposés par Ian Goodfellow en 2014, constituent l’un des apports les plus marquants de l’intelligence artificielle moderne, en particulier dans le domaine de la génération de données. L’idée centrale des GANs est simple mais puissante : faire s’opposer deux réseaux de neurones dans un jeu à somme nulle, l’un générant des données, l’autre les évaluant.

### **Architecture et fonctionnement**

Un GAN se compose de **deux réseaux de neurones** qui sont entraînés simultanément, mais dans des rôles opposés :

* **Le générateur (G)**  
   Le générateur a pour mission de créer des données artificielles qui ressemblent aux données réelles. Il prend en entrée un vecteur aléatoire zzz, généralement échantillonné depuis une distribution normale ***N(0,1)***, et le transforme à travers une série de couches pour produire un échantillon synthétique *G(z)* – par exemple, une image de visage, un chiffre manuscrit ou un spectrogramme audio.  
   Ce réseau apprend progressivement à transformer le bruit en exemples réalistes. Il n’a jamais accès aux vraies données ; il apprend uniquement à tromper le discriminateur.

* **Le discriminateur (D)**  
   Le discriminateur agit comme un **juge**. Il reçoit en entrée soit une vraie donnée issue du dataset, soit une donnée synthétique produite par le générateur. Son objectif est de **classer correctement** l’entrée : vraie (label 1\) ou fausse (label 0).  
   Le discriminateur est donc un classificateur binaire, souvent construit comme un réseau de neurones convolutionnel dans les applications d’image.  
    
  ![][image48]

Image extraite de : [https://developers.google.com/machine-learning/gan/gan\_structure](https://developers.google.com/machine-learning/gan/gan_structure)

### **Le principe d’opposition**

Les deux réseaux sont connectés dans une **boucle adversariale**. Leur entraînement repose sur un **jeu compétitif** :

* Le générateur essaie de **tromper** le discriminateur en produisant des échantillons si crédibles que celui-ci les classe comme réels.

* Le discriminateur essaie de **distinguer** correctement les vrais échantillons des faux.

Cela se traduit par une fonction de perte commune, mais à objectif opposé :

* Le **discriminateur** maximise la probabilité de donner le bon label à chaque entrée.

* Le **générateur** essaie de minimiser la capacité du discriminateur à faire cette distinction.

Formellement, la perte globale s’écrit comme une minimax :

![][image49]

### **Entraînement**

L’entraînement se fait en alternant :

1. Une mise à jour des poids du discriminateur DDD, en utilisant à la fois des vraies données et des données synthétiques générées par GGG.

2. Une mise à jour des poids du générateur GGG, en cherchant à faire en sorte que DDD classe ses sorties comme vraies.

Ce **duel** entre les deux réseaux force le générateur à s’améliorer continuellement. Si le discriminateur devient trop fort, le générateur n’apprend rien. Si le générateur devient trop bon, le discriminateur est "trompé" tout le temps. L’équilibre entre les deux est donc crucial mais difficile à atteindre.

### **Applications**

Les GANs ont révolutionné de nombreux domaines :

* Génération d’images réalistes (visages, objets, paysages)

* Colorisation automatique d’images en noir et blanc

* Super-résolution (upscaling d’images)

* Transfert de style (changer le style d’une image)

* Création d’avatars, deepfakes, ou art génératif

### **Forces et faiblesses**

Les GANs produisent souvent des résultats **visuellement très convaincants**, bien plus nets que ceux issus d’autoencodeurs classiques. Ils peuvent apprendre une distribution complexe sans jamais la modéliser explicitement.

Cependant, ils souffrent aussi de **plusieurs problèmes majeurs** :

* **Instabilité d’entraînement** : il est fréquent que l’un des deux réseaux prenne trop d’avance sur l’autre, ce qui bloque l’apprentissage.

* **Mode collapse** : le générateur apprend à produire toujours les mêmes échantillons ou un nombre limité de variantes.

* **Absence de représentation latente exploitable** : contrairement aux autoencodeurs ou VAE, les GANs ne fournissent pas naturellement une structure compréhensible de l’espace latent.

De nombreuses variantes ont été proposées pour pallier ces défauts, comme les **Wasserstein GANs**, **DCGAN**, **StyleGAN**, ou encore les **Conditional GANs** qui permettent de contrôler ce qui est généré à partir de labels ou de données d’entrée (par exemple, générer un "chien" plutôt qu’un "chat").

#### **Liens Externes (Youtube, Medium, etc):**

* [Overview of GAN Structure](https://developers.google.com/machine-learning/gan/gan_structure)  
* [Qu’est-ce que les Generative Adversarial Networks (GAN) ?](https://www.intelligence-artificielle-school.com/ecole/technologies/quest-ce-que-les-generative-adversarial-networks/)  
* [Introduction aux GANs](https://youtu.be/QZpabZj1WOA?si=10XGfh5-KIoijNAK)  
*  [Generative Adversarial Networks (GANs) \- Computerphile](https://youtu.be/Sw9r8CL98N0?si=LlV974i3E-Jiu74a)  
* [GANs from Scratch 1: A deep introduction. With code in PyTorch and TensorFlow](https://medium.com/ai-society/gans-from-scratch-1-a-deep-introduction-with-code-in-pytorch-and-tensorflow-cb03cdcdba0f)  
* [Génerer les images à l’aide des GANs avec Tensorflow](https://yannicksergeobam.medium.com/g%C3%A9nerer-les-images-%C3%A0-laide-des-gans-avec-tensorflow-6c761311929d)

#### **Bibliographie**

* Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A. and Bengio, Y., 2020\. Generative adversarial networks. *Communications of the ACM*, *63*(11), pp.139-144.  
* Creswell, A., White, T., Dumoulin, V., Arulkumaran, K., Sengupta, B. and Bharath, A.A., 2018\. Generative adversarial networks: An overview. *IEEE signal processing magazine*, *35*(1), pp.53-65.

3. # Modèles de Diffusion

Les **modèles de diffusion** sont aujourd’hui au cœur de la génération d’images de haute qualité, popularisés par des systèmes comme **DALL·E 2**, **Stable Diffusion** ou **MidJourney**. Leur approche diffère fondamentalement de celle des GANs ou des autoencodeurs, puisqu’ils génèrent des données en inversant un processus de bruitage progressif.

### **Intuition générale**

L’idée derrière les modèles de diffusion repose sur **deux phases symétriques** :

1. **Diffusion (forward process)**  
    On part d’une image réelle, à laquelle on ajoute progressivement du **bruit gaussien**, étape par étape, jusqu’à obtenir une image totalement bruitée qui ressemble à du **pur bruit blanc**.  
    Ce processus est **stochastique** et se déroule généralement sur plusieurs centaines voire milliers d’étapes.

2. **Dénoising (reverse process)**  
    Le modèle est entraîné à **inverser** ce processus : en partant du bruit pur, il apprend à **supprimer le bruit étape par étape**, pour finalement reconstruire une image nette et réaliste.  
    Ce processus est **appris** à l’aide d’un réseau neuronal, souvent un **U-Net**, qui prédit le bruit à chaque étape.

Ainsi, la génération se fait **par raffinements successifs** : on ne génère pas une image d’un coup, mais on la fait émerger progressivement du bruit.

### **Architecture typique**

La plupart des modèles de diffusion reposent sur une architecture **U-Net** modifiée, adaptée au traitement d’images bruitées. Elle est combinée à deux éléments essentiels:

* **Un encodeur temporel**  
   À chaque étape de débruitage, le modèle doit savoir à quel moment du processus il se trouve. Cette information temporelle est encodée et injectée dans le réseau sous forme de vecteurs de position (ou embeddings).

* **Des mécanismes d’attention**  
   Inspirés des Transformers, ils permettent au réseau de mieux capturer les relations spatiales complexes dans l’image, améliorant considérablement la qualité visuelle.

![][image50]

Architecture Basique d’un réseau U-Net

Image extraite de : [https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/](https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/)

Certains modèles, comme **Stable Diffusion**, ajoutent aussi un **encodeur de texte (CLIP, T5, BERT...)** pour guider la génération à partir d’une instruction textuelle. On parle alors de **modèle de diffusion conditionnel**.

### **Fonction de perte**

Le modèle est **entraîné à prédire le bruit** ajouté à une image à un moment donné de la diffusion. Concrètement, à une étape *t*, on donne au réseau une image bruitée *xt*​, et on lui demande de retrouver le bruit ϵ\\epsilonϵ qui a été ajouté à l’image propre initiale *x0*.

La **fonction de perte typique** est donc une **erreur quadratique moyenne (MSE)** entre le bruit prédit et le vrai bruit :

![][image51]

Certaines variantes (comme **DDPM++**) utilisent d’autres formulations, notamment la prédiction directe de l’image débruitée *x0*​, ou encore une **perte perceptuelle**.

### **Pourquoi ça fonctionne ?**

Les modèles de diffusion génèrent des images **progressivement**, en inversant un processus bien défini, ce qui permet :

* un **contrôle précis** sur la qualité du résultat à chaque étape,

* une **diversité élevée** : chaque échantillon de bruit initial donne potentiellement une image différente,

* une **bonne stabilité d’entraînement** : contrairement aux GANs, il n’y a pas d’affrontement entre deux réseaux.

### **Applications**

Ils sont aujourd’hui utilisés pour :

* Génération d’images réalistes (visages, objets, paysages, art)

* Inpainting (complétion d’images)

* Super-résolution

* Text-to-image (image à partir d’une description)

* Synthèse vocale ou audio

Certains frameworks comme **Stable Diffusion** permettent même une génération **interactive** ou contrôlée, grâce à des techniques comme **ControlNet** ou **img2img**.

### **Forces et limites**

Les modèles de diffusion offrent une **qualité exceptionnelle**, rivalisant avec les meilleurs GANs, tout en étant **plus stables à entraîner**. De plus, leur capacité à **conditionner sur du texte, une esquisse, ou une autre image** ouvre un grand éventail d'applications créatives.

Cependant, ils présentent aussi des défis :

* **Temps d’inférence élevé** : générer une image demande plusieurs centaines de passes (même si des techniques récentes comme DDIM réduisent ce nombre).

* **Coût computationnel important** à l'entraînement et à l’inférence.

* **Complexité technique** plus élevée, notamment pour les utilisateurs non familiers avec les processus stochastiques.

### **DALL·E 2**

Développé par OpenAI, **DALL·E 2** est un système de génération d’images à partir de descriptions textuelles. Il repose sur une combinaison originale de plusieurs modèles puissants :

* Il utilise d’abord **CLIP** (un modèle de vision et langage) pour **comprendre le texte** et le transformer en une représentation latente visuelle.

* Cette représentation est ensuite utilisée pour **conditionner un modèle de diffusion**, qui va générer une image correspondant à ce texte.

La particularité de DALL·E 2 est de ne pas directement générer des pixels. Il **travaille dans un espace latent** plus compact et structuré, ce qui permet une génération plus rapide et plus contrôlée. À partir de cette image latente, un **décodeur** (souvent un autoencodeur ou un VQGAN) reconstruit l’image finale.

DALL·E 2 permet aussi des manipulations fines comme :

* **Inpainting** : remplir une zone vide dans une image

* **Editing** : modifier certains éléments à partir d’un nouveau texte

Il a été un des premiers modèles à populariser l’idée de création visuelle guidée par langage, avec un niveau de cohérence sémantique très avancé.

### **Stable Diffusion**

**Stable Diffusion**, développé par **Stability AI**, a marqué un tournant en rendant les modèles de diffusion **accessibles et modifiables** par le grand public.

Contrairement à DALL·E 2, Stable Diffusion :

* Utilise un **Latent Diffusion Model (LDM)** : au lieu de générer directement des images haute résolution, il travaille dans un espace **compressé** (latent) via un **autoencodeur**. Cela rend le processus **plus léger et rapide**.

* Peut être **guidé par du texte**, grâce à l’utilisation de **CLIP ou T5** comme encodeur de texte.

* Est **open-source**, ce qui a permis de nombreuses contributions : génération d’images stylisées, contrôle par esquisses (ControlNet), variation par bruit initial, etc.

L’architecture centrale reste un **U-Net modifié** avec des blocs de **self-attention** et une injection d’embeddings temporels et textuels.

Grâce à sa flexibilité, Stable Diffusion est aujourd’hui au cœur de nombreux outils créatifs open-source, allant de la génération artistique à la conception de personnages ou de scènes complexes.

### **MidJourney**

Contrairement aux deux précédents, **MidJourney** n’a pas publié tous les détails techniques de son modèle. Il est cependant largement admis que MidJourney repose également sur un **modèle de diffusion**, guidé par texte.

Les spécificités de MidJourney résident surtout dans :

* **L’aspect artistique** : les images générées sont souvent très stylisées, avec des rendus proches de la peinture, du concept art ou de l’illustration numérique.

* **L’interface utilisateur** : MidJourney est accessible via une interface très intuitive sur Discord, où l’utilisateur interagit avec un bot pour générer des images à partir de prompts textuels.

* **L’optimisation créative** : le système semble fortement biaisé vers des résultats visuellement impressionnants, au prix parfois d’une fidélité moindre aux instructions précises.

MidJourney se distingue ainsi par une orientation très forte vers **l’esthétique et l’inspiration artistique**, le rendant très populaire auprès des designers, illustrateurs et créateurs de contenu.

#### **Liens Externes (Youtube, Medium, etc):**

* [What are DiffusionModels?](https://youtu.be/fbLgFrlTnGU?si=RXN4SnaXvdjR8Zly)  
* [Diffusion Models for AI Image Generation](https://youtu.be/x2GRE-RzmD8?si=zBgLebzvcLw7CCpW)  
* [The Breakthrough Behind Modern AI Image Generators | Diffusion Models Part 1](https://youtu.be/1pgiu--4W3I?si=U6hMsWYP_bo4Db1I)  
* [L'algorithme derrière Midjourney : Comprendre les modèles de diffusion](https://youtu.be/lvMGTteb3EI?si=s6O3q-UXfsdsizi2)  
* [How AI Image Generators Work (Stable Diffusion / Dall-E) \- Computerphile](https://youtu.be/1CIpzeNxIhU?si=RrvhyGJ-vxVnzFQ3)  
* [Comment ces IA inventent-elles des images ?](https://youtu.be/tdelUss-5hY?si=gurxOei2nj4q1Hs0)  
* [Stable Diffusion explained (in less than 10 minutes)](https://youtu.be/QdRP9pO89MY?si=Ii8HBTj3W5O3gZg9)  
* [Qu’est-ce qu’un modèle de diffusion ?](https://www.ibm.com/fr-fr/think/topics/diffusion-models)  
* [Step by Step Visual Introduction to Diffusion Models](https://medium.com/@kemalpiro/step-by-step-visual-introduction-to-diffusion-models-235942d2f15c)

#### **Bibliographie**

* Yang, L., Zhang, Z., Song, Y., Hong, S., Xu, R., Zhao, Y., Zhang, W., Cui, B. and Yang, M.H., 2023\. Diffusion models: A comprehensive survey of methods and applications. *ACM Computing Surveys*, *56*(4), pp.1-39.  
* Bhullar, R., 2024\. Creative Artificial Intelligence: Exploring the Qualities of Popular AI Art Tools to Determine Effectiveness.

4. # Transformeurs

Les **Transformers** ont révolutionné le domaine de l’intelligence artificielle, notamment dans le traitement du langage naturel (NLP), la génération de texte, l’analyse de séquences, et même la génération d’images. Introduits par Vaswani et al. dans l’article *"Attention is All You Need"* (2017), ils sont aujourd’hui à la base des modèles les plus puissants comme GPT, BERT, T5 ou encore des modèles multimodaux comme Flamingo ou Gemini.

### **Structure générale**

Un transformeur est constitué d’un **empilement de blocs** identiques composés principalement de deux sous-composants essentiels :

1. **Le mécanisme d’attention (Self-Attention)**

2. **Un réseau de neurones feed-forward (MLP)**

Chaque bloc est également entouré de mécanismes d’**ajout résiduel** (residual connections) et de **normalisation de couche** (layer normalization), pour assurer une bonne circulation du gradient lors de l’apprentissage.

### **1\. Mécanisme d’Attention**

Le cœur du transformeur est le **self-attention**, qui permet à chaque mot (ou jeton) de **"regarder"** les autres mots de la séquence pour ajuster sa propre représentation. Cela permet de capturer les dépendances longues entre les éléments d’une séquence, ce qui était difficile avec les RNN ou LSTM.

Le mécanisme repose sur trois vecteurs par jeton : **Query (Q)**, **Key (K)** et **Value (V)**. On calcule des scores d’attention via une fonction de similarité entre les Q et K, puis on utilise ces scores pour pondérer les V.

Formule typique :

![][image52]

Cette opération est **parallélisable** et bien plus efficace que les RNN.

### **2\. Multi-Head Attention**

Plutôt qu’une seule attention, le modèle en apprend plusieurs en parallèle, appelées **têtes d’attention**. Cela permet au modèle de capturer différents types de relations entre jetons. Ces têtes sont ensuite concaténées et projetées vers l’espace d’origine.

### **3\. Réseau Feed-Forward**

Chaque couche contient aussi un **MLP à deux couches** avec une activation non-linéaire (souvent ReLU ou GELU). Il agit indépendamment sur chaque position de la séquence.

### **4\. Encodage de position**

Comme les transformeurs ne sont pas séquentiels (contrairement aux RNN), ils n’ont aucune notion de l’ordre des jetons. On ajoute donc un **vecteur de position** (sinusoïdal ou appris) à chaque entrée pour injecter l'information d’ordre.

### **Architecture complète**

On distingue généralement deux variantes :

* **Encodeur uniquement** (ex : BERT) — utile pour les tâches de classification, recherche d’information, etc.

* **Décodeur uniquement** (ex : GPT) — utilisé pour la génération de texte.

* **Encodeur-Décodeur** (ex : T5, BART) — utilisé pour la traduction, le résumé, la génération conditionnée.

### **Avantages des transformeurs**

* **Traitement parallèle des séquences** (plus rapide que les RNN)

* **Meilleure capacité de généralisation à long terme**

* **Modularité** : possibilité de les adapter à divers formats de données (texte, image, son)

  ## **Variantes populaires de Transformers**

Voici maintenant quelques-uns des modèles les plus influents et utilisés, chacun basé sur l’architecture des transformeurs.

### **BERT (Bidirectional Encoder Representations from Transformers)**

* Ne contient que **l’encodeur** de l’architecture transformer.

* Lit la séquence **dans les deux sens** (gauche et droite) pour créer un contexte riche.

* Pré-entraîné avec deux tâches : **Masked Language Modeling** (prédire des mots masqués) et **Next Sentence Prediction**.

* Très utilisé pour des tâches de classification, question/réponse, etc.

### **GPT (Generative Pre-trained Transformer)**

* N’utilise que le **décodeur** d’un transformeur, entraîné de manière **auto-régressive** (prédire le mot suivant).

* Très performant pour la **génération de texte** fluide et cohérente.

* GPT-3 et GPT-4 ont montré des capacités émergentes impressionnantes dans des tâches variées (résolution de problèmes, rédaction, programmation...).

### **T5 (Text-To-Text Transfer Transformer)**

* Utilise une **architecture encodeur-décodeur** complète.

* Toutes les tâches sont formulées comme un problème de conversion de texte : par exemple, “traduire anglais en français : Hello” ⟶ “Bonjour”.

* Très flexible et puissant pour le NLP multitâche.

### **BART (Bidirectional and Auto-Regressive Transformers)**

* Combine **un encodeur bidirectionnel (type BERT)** avec un **décodeur auto-régressif (type GPT)**.

* Excellente performance pour la **génération de texte conditionnée**, le **résumé automatique**, et les **tâches de reconstruction de séquences**.

### **Vision Transformer (ViT)**

* Applique le principe des transformeurs à des **images** : l’image est découpée en **patchs**, qui sont ensuite linéarisés et traités comme des jetons.

* A montré que les transformeurs peuvent rivaliser avec les CNN pour les tâches de vision (classification, détection...).

#### **Liens Externes (Youtube, Medium, etc):**

* [How Transformers Work: A Detailed Exploration of Transformer Architecture](https://www.datacamp.com/tutorial/how-transformers-work)  
* [Qu’est-ce qu’un modèle de transformeur ?](https://www.ibm.com/fr-fr/think/topics/transformer-model)  
* [Les Transformers, incontournables du Deep Learning](https://blent.ai/blog/a/transformers-deep-learning)  
* [Transformer Architecture explained](https://medium.com/@amanatulla1606/transformer-architecture-explained-2c49e2257b4c)  
* [Transformers (how LLMs work) explained visually | DL5](https://youtu.be/wjZofJX0v4M?si=kyDnEDpcHSWuvg17)  
*  [What are Transformers (Machine Learning Model)?](https://youtu.be/ZXiruGOCn9s?si=QoRwpflLXztVEzIK)  
* [Transformers, explained: Understand the model behind GPT, BERT, and T5](https://youtu.be/SZorAJ4I-sA?si=2rKDatjYU7AgoF_7)  
* [How ChatGPT Works Technically | ChatGPT Architecture](https://youtu.be/bSvTVREwSNw?si=3rt7c1Acg4SaH5tG)   
* [ChatGPT Explained Completely.](https://youtu.be/-4Oso9-9KTQ?si=0EJX1XbXrwrmtwCn)

#### **Bibliographie**

* Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, Ł. and Polosukhin, I., 2017\. Attention is all you need. *Advances in neural information processing systems*, *30*.  
* Yenduri, G., Ramalingam, M., Selvi, G.C., Supriya, Y., Srivastava, G., Maddikunta, P.K.R., Raj, G.D., Jhaveri, R.H., Prabadevi, B., Wang, W. and Vasilakos, A.V., 2024\. Gpt (generative pre-trained transformer)–a comprehensive review on enabling technologies, potential applications, emerging challenges, and future directions. *IEEE Access*.  
* Lewis, M., Liu, Y., Goyal, N., Ghazvininejad, M., Mohamed, A., Levy, O., Stoyanov, V. and Zettlemoyer, L., 2019\. Bart: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension. *arXiv preprint arXiv:1910.13461*.