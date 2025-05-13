# Notions de Base de l'Apprentissage Profond

## Concepts Fondamentaux

### 1. Données Structurées et non Structurées

En **machine learning**, les données peuvent généralement être classées dans deux grandes catégories :

Les **données structurées** sont organisées sous forme de tableau, avec des colonnes représentant différentes caractéristiques décrivant chaque observation. Par exemple, des informations comme l'âge d'une personne, son revenu, ou le nombre de fois où elle a visité un site web au cours du mois précédent peuvent servir à prédire si elle va s'abonner à un service en ligne le mois suivant.

Les **données non structurées**, quant à elles, ne suivent pas cette organisation tabulaire. Elles incluent des formats comme des images, de l'audio ou du texte, qui ne s'intègrent pas naturellement dans des colonnes. Une image a une structure spatiale, un enregistrement audio a une structure temporelle, et une vidéo combine les deux. Mais comme ces informations ne sont pas organisées en colonnes prédéfinies, elles sont considérées comme non structurées.![][image1]

Image extraite de:  « Generative Deep Learning » par D. Foster

Le **deep learning** peut être utilisé avec des données structurées, mais sa véritable force — surtout dans les modèles génératifs — réside dans le traitement des données non structurées. En effet, dans la majorité des cas, l'objectif est de générer des sorties non structurées comme de nouvelles images ou des séquences de texte uniques.

**Liens Externes (Youtube, Medium, etc):**

* [Structured vs Unstructured Data Explained](https://youtu.be/5M2okstYF3A?si=PS0Oi3yGy5lEI_DG)  
* [What is the difference: Structured vs Unstructured data](https://medium.com/@gurkanc/whats-the-difference-structured-vs-unstructured-data-1bfe09077be6)  
* [Quelle est la différence entre les données structurées, semi-structurées et non structurées?](https://youtu.be/xINa3byXDQA?si=-bRkyJ0iTKqM4wbF)

**Bibliographie:**

* D. Foster, Generative Deep Learning, 2nd ed. Sebastopol, CA, USA: O'Reilly Media, Inc., 2023\.  
* Eberendu, A.C., 2016\. Unstructured Data: an overview of the data of Big Data. *International Journal of Computer Trends and Technology*, *38*(1), pp.46-50.

### 2. Apprentissage Supervisé et non Supervisé

Le machine learning se divise en deux grands domaines : **l'apprentissage supervisé** (*Supervised Learning*) et **l'apprentissage non supervisé** (*Unsupervised Learning*).

L'**apprentissage supervisé** consiste à entraîner un modèle sur des données annotées. Cela signifie que pour chaque entrée, on connaît la sortie correcte. Le modèle apprend ainsi à faire des prédictions ou des classifications en s'appuyant sur cette correspondance entrée-sortie.  
 On distingue deux grands types de problèmes en apprentissage supervisé : la **classification** et la **régression**.

En **classification**, l'objectif est d'attribuer une étiquette de classe à une observation, à partir d'un ensemble de classes possibles. Il existe deux types principaux de classification :

* la **classification binaire**, où l'on distingue exactement deux catégories,

* la **classification multiclasse**, avec plus de deux options possibles.

Par exemple, déterminer si un email est un spam ou non est un cas de classification binaire. En revanche, reconnaître si une image contient un chat, un chien ou un poisson relève de la classification multiclasse.  
 Parmi les modèles populaires utilisés en classification, on retrouve : SVM, arbres de décision (*Decision Trees*), régression logistique (*Logistic Regression*).

En **régression**, le but est de prédire une valeur numérique continue. Par exemple, estimer le salaire annuel d'une personne en fonction de son niveau d'études, de son âge et de sa localisation.  
 Les modèles les plus courants incluent la régression linéaire (*Linear Regression*), la régression polynomiale (*Polynomial Regression*), ainsi que la régression régularisée (Ridge, Lasso, ElasticNet).

L'**apprentissage non supervisé**, à l'inverse, s'applique à des données **non annotées**. Le modèle ne reçoit pas les réponses correctes et tente de découvrir seul des motifs, des regroupements ou des structures cachées dans les données.  
 On distingue quatre grandes approches en apprentissage non supervisé :

* le **clustering** (regroupement),

* la **réduction de dimensionnalité**,

* la **détection d'anomalies**,

* et l'**apprentissage des règles d'association**.

Le **clustering** regroupe les points de données similaires en fonction de motifs ou de caractéristiques communes. Les algorithmes populaires sont K-Means, DBSCAN et le **clustering hiérarchique** (*Hierarchical Clustering*).  
 La **réduction de dimensionnalité** permet de diminuer le nombre de variables d'entrée tout en conservant la structure ou la variance essentielle des données. Les méthodes connues incluent l'analyse en composantes principales (*PCA*), t-SNE, UMAP et les autoencodeurs (*Autoencoders*).  
 La **détection d'anomalies** (ou détection d'outliers) vise à identifier les données rares ou inhabituelles qui s'écartent fortement de la norme. Exemples : Isolation Forest, One-Class SVM.  
 Enfin, l'**apprentissage des règles d'association** cherche à découvrir des liens ou des motifs de cooccurrence entre des variables. Les algorithmes comme Apriori et FP-Growth sont souvent utilisés dans des cas comme l'analyse de panier d'achat.

**Liens Externes (Youtube, Medium, etc):**

* [Supervised vs Unsupervised Learning](https://youtu.be/W01tIRP_Rqs?si=zWHlVXArWMHSiwNr)  
* [Classification and Regression in Machine Learning](https://youtu.be/TJveOYsK6MY?si=NF8-i3sXMPIRqs6W)  
* [6 Types of Regression Models You Should Know About](https://medium.com/@uma.bollikonda/6-types-of-regression-models-in-machine-learning-you-should-know-about-ed1e83dd0c4d)  
* [Top 8 Most Important Unsupervised Learning Algorithms](https://medium.com/imagescv/top-8-most-important-unsupervised-machine-learning-algorithms-with-python-code-references-1222393b5077)  
* [Dimensionality Reduction](https://youtu.be/3uxOyk-SczU?si=4Kb8ccBMid2IZ_h2)  
* [What is Association Rule Learning?](https://medium.com/@ainsupriyofficial/what-is-association-rule-learning-a6ef399fdc01)  
* [Différence entre apprentissage machine supervisé et non-supervisé (cours exemple concret définition)](https://youtu.be/jTF2aLBHA80?si=qfNbQSAWrK-oFDQi)  
* [Comprendre L' Apprentissage Supervisé : Les 4 Piliers à Connaitre](https://youtu.be/iFE5Dz-YJCk?si=P8ggC6RAc6npzQAc)  
* [Apprentissage supervisé et non supervisé](https://cloud.google.com/discover/supervised-vs-unsupervised-learning?hl=fr)

**Bibliographie**

* A. Géron, Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, 2nd ed. Sebastopol, CA, USA: O'Reilly Media, Inc., 2019\.  
* Rajoub, B. (2020). *Supervised and unsupervised learning*. In W. Zgallai (ed.) *Biomedical Signal Processing and Artificial Intelligence in Healthcare*. Developments in Biomedical Engineering and Bioelectronics. Academic Press, pp. 51–89.   
* Nasteski, V., 2017\. An overview of the supervised machine learning methods. *Horizons. b*, *4*(51-62), p.56.  
* Celebi, M.E. and Aydin, K. eds., 2016\. *Unsupervised learning algorithms* (Vol. 1). Berlin: Springer International Publishing.  
* Pang, G., Shen, C., Cao, L. and Hengel, A.V.D., 2021\. Deep learning for anomaly detection: A review. *ACM computing surveys (CSUR)*, *54*(2), pp.1-38.

### 3. Surapprentissage et Sous-apprentissage

#### **1\. Le surapprentissage (Overfitting) en machine learning**

Le **surapprentissage** se produit lorsqu'un modèle s'adapte trop fortement aux données d'entraînement. Il apprend non seulement les motifs importants, mais aussi des détails inutiles comme le bruit ou les valeurs aberrantes.

Par exemple, imaginez qu'on essaie d'ajuster une courbe très complexe à un nuage de points. La courbe passe peut-être par tous les points, mais elle ne reflète pas vraiment la tendance générale. Le modèle fonctionne alors très bien sur les données d'entraînement, mais a du mal avec de nouvelles données.

Un modèle en surapprentissage, c'est un peu comme un élève qui apprend les réponses par cœur sans comprendre le cours. Il réussit aux examens blancs mais échoue aux vrais tests.

**Causes fréquentes du surapprentissage** :

* Le modèle est trop complexe.

* Le jeu de données d'entraînement est trop petit.

* Le modèle apprend des détails spécifiques au lieu de repérer des tendances générales.

#### **2\. Le sous-apprentissage (Underfitting) en machine learning**

Le **sous-apprentissage** est l'inverse du surapprentissage : le modèle est trop simple pour capturer la structure des données.

Par exemple, si vous tentez de tracer une droite sur des données qui suivent une courbe, la droite passera à côté de la majorité des points. Le modèle aura de mauvais résultats, aussi bien sur les données d'entraînement que sur les nouvelles données.

Un modèle en sous-apprentissage, c'est comme un élève qui n'a pas assez révisé : il échoue partout, que ce soit en entraînement ou en examen réel.

**Causes fréquentes du sous-apprentissage** :

* Le modèle est trop simple pour repérer les motifs pertinents.

* Les variables d'entrée ne décrivent pas assez bien les facteurs importants.

* Le jeu de données d'entraînement est trop limité.

* La régularisation est trop forte, empêchant le modèle d'apprendre correctement.

* Les caractéristiques ne sont pas bien mises à l'échelle (*feature scaling*), ce qui complique la détection des relations.

![][image2]  
Image extraite de:  [https://www.kevindegila.com/blog/underfitting-and-overfitting-explained/](https://www.kevindegila.com/blog/underfitting-and-overfitting-explained/)

**Liens Externes (Youtube, Medium, etc):**

* [Underfitting & Overfitting \- Explained](https://youtu.be/o3DztvnfAJg?si=QZ8OOZPniYrtkqnY)  
* [Overfitting vs. Underfitting: How to Balance Your Model](https://medium.com/@jimcanary/overfitting-vs-underfitting-how-to-balance-your-model-b2c19d5e23b6#:~:text=Level%201%3A%20Overfitting%20means%20your,models%20overfit%20\(high%20variance\).)  
* [Overfitting Et Underfitting: Les Ennemis Du Machine Learning, Comment Les Eviter?](https://youtu.be/iAQEswd38r4?si=7ddrpS65WUoshPYV)  
* [Overfitting et Underfitting : Quand vos algorithmes de Machine Learning dérapent \!](https://mrmint.fr/overfitting-et-underfitting-quand-vos-algorithmes-de-machine-learning-derapent)

**Bibliographie**

* Jabbar, H. and Khan, R.Z., 2015\. Methods to avoid over-fitting and under-fitting in supervised machine learning (comparative study). *Computer science, communication and instrumentation devices*, *70*(10.3850), pp.978-981.  
* Pothuganti, S., 2018\. Review on over-fitting and under-fitting problems in Machine Learning and solutions. *Int. J. Adv. Res. Electr. Electron. Instrum. Eng*, *7*(9), pp.3692-3695.  
* Van der Aalst, W.M., Rubin, V., Verbeek, H.M., van Dongen, B.F., Kindler, E. and Günther, C.W., 2010\. Process mining: a two-step approach to balance between underfitting and overfitting. *Software & Systems Modeling*, *9*, pp.87-111.

### 4. Métriques d'Évaluation et Fonctions de Perte

Chaque tâche d'apprentissage automatique relève soit de la régression, soit de la classification, et cela vaut également pour les métriques utilisées pour évaluer les performances. Il existe de nombreuses métriques adaptées à chaque type de problème, mais nous allons nous concentrer sur les plus courantes et sur ce qu'elles révèlent sur la qualité d'un modèle.

Il est important de faire la distinction entre **fonction de coût (loss function)** et **métrique (metric)**.

* Les fonctions de coût mesurent la qualité des prédictions pendant l'entraînement. Elles guident le processus d'apprentissage en minimisant l'erreur grâce à des techniques d'optimisation comme la descente de gradient (Gradient Descent). Elles sont généralement différentiables par rapport aux paramètres du modèle.  
* Les métriques, quant à elles, servent à évaluer les performances pendant l'entraînement **et** la phase de test, mais n'ont pas besoin d'être différentiables.

Cela dit, dans certains cas, une métrique peut également servir de fonction de coût si elle est différentiable. Par exemple, **l'erreur quadratique moyenne (Mean Squared Error, MSE)** est à la fois une métrique de régression courante et une fonction de coût, notamment lorsqu'elle est associée à des techniques de régularisation.

#### **Métriques pour les tâches de régression**

Les modèles de régression produisent des sorties continues. Leur évaluation nécessite donc des métriques capables de mesurer l'écart entre les prédictions et les valeurs réelles. Voici les principales métriques utilisées :

* **Erreur absolue moyenne (Mean Absolute Error, MAE)**

* **Erreur quadratique moyenne (Mean Squared Error, MSE)**

* **Racine de l'erreur quadratique moyenne (Root Mean Squared Error, RMSE)**

* **R² (coefficient de détermination)**

**Erreur quadratique moyenne (MSE)**  
 L'erreur quadratique moyenne mesure l'écart moyen au carré entre les valeurs prédites et les valeurs réelles. Plus les écarts sont importants, plus ils sont sévèrement pénalisés.

![][image3]

**Erreur absolue moyenne (MAE)**

Elle mesure la moyenne des écarts absolus entre les valeurs prédites et les valeurs réelles. Elle fournit une vision plus équilibrée de l'erreur, moins sensible aux valeurs extrêmes.

![][image4]

**Racine de l'erreur quadratique moyenne (RMSE)**  
Elle correspond à la racine carrée de la MSE. Cela permet d'interpréter l'erreur dans les mêmes unités que la variable cible, ce qui la rend plus lisible.

![][image5]

**R² (coefficient de détermination)**

Cette métrique mesure la proportion de la variance de la variable cible qui est expliquéepar les variables d'entrée. Elle évalue le pouvoir explicatif du modèle:

![][image6]

#### **Métriques pour les tâches de classification**

Les modèles de classification produisent des sorties discrètes (comme des étiquettes ou des classes). Leur évaluation repose sur des métriques qui examinent leur capacité à effectuer des prédictions correctes. Les plus utilisées sont :

* **Accuracy (exactitude)**

* **Précision (Precision)**

* **Rappel (Recall)**

* **F1-score**

Pour bien comprendre ces métriques, il est essentiel d'introduire la notion de **matrice de confusion (Confusion Matrix)**.

#### **Matrice de confusion**

C'est un tableau qui permet d'évaluer les performances d'un modèle de classification, en montrant combien de prédictions ont été correctes ou incorrectes pour chaque classe.

![][image7]

Image extraite de:  [https://www.blog.trainindata.com/confusion-matrix-precision-and-recall/](https://www.blog.trainindata.com/confusion-matrix-precision-and-recall/)

Dans le cas d'une classification binaire (par exemple, spam ou non spam), la matrice de confusion comprend les éléments suivants :

* **Vrai Positif (True Positive, TP)** : le modèle a prédit "positif", et c’était correct.

* **Vrai Négatif (True Negative, TN)** : le modèle a prédit "négatif", et c’était correct.

* **Faux Positif (False Positive, FP)** : le modèle a prédit "positif", mais c’était faux (erreur de type I).

* **Faux Négatif (False Negative, FN)** : le modèle a prédit "négatif", alors que c’était positif (erreur de type II).

Accuracy

L’**accuracy** mesure la proportion de prédictions correctes sur l’ensemble des données. C’est simple et souvent utile, mais elle peut être trompeuse en cas de déséquilibre entre les classes.

![][image8]

#### **Précision et rappel**

* **Précision (Precision)** : parmi toutes les prédictions positives du modèle, combien étaient correctes ? Elle est importante lorsque le **coût d’un faux positif** est élevé (par exemple, dans la détection de spam).

* **Rappel (Recall)** : parmi tous les cas positifs réels, combien ont été correctement identifiés par le modèle ? Elle est cruciale quand **rater un cas positif est risqué** (par exemple, en diagnostic médical).

![][image9]

![][image10]

#### **F1-score**

Le F1-score est la moyenne harmonique de la précision et du rappel. Il est utile lorsque l’on souhaite un compromis équilibré entre ces deux métriques, en particulier quand les faux positifs et les faux négatifs sont aussi problématiques l’un que l’autre.

![][image11]

#### **Entropie binaire : mesurer l'incertitude**

L’entropie binaire est un concept issu de la théorie de l’information. Elle mesure l’incertitude d’un système avec seulement deux résultats possibles (par exemple, "vrai" ou "faux", "chat" ou "chien", "0" ou "1"). En apprentissage automatique, elle permet d’estimer à quel point une prédiction probabiliste est proche de la vérité.

La formule de l’entropie binaire pour une probabilité est :

**![][image12]**

Cette formule atteint son maximum lorsque p=0.5, c’est-à-dire quand le système est le plus incertain. À l’inverse, si p=0 ou p=1, l’entropie est minimale (nulle), car il n’y a pas d’incertitude.

#### **Cross-entropy : comparer prédictions et vérité**

La **cross-entropy (ou entropie croisée)** est une généralisation de l’entropie. Elle est utilisée pour **mesurer l’écart entre deux distributions de probabilité** : une distribution réelle (ou cible) et une distribution prédite. Dans le contexte de la classification binaire, on compare souvent la **vraie étiquette** avec la **probabilité prédite**.

Sa formule est :

![][image13]

Cette fonction est souvent utilisée comme **fonction de perte** dans les modèles de classification binaire (par exemple, dans un réseau de neurones dont la sortie est une probabilité entre 0 et 1 grâce à une fonction **sigmoïde**).

#### **Pourquoi utiliser la cross-entropy ?**

* Elle pénalise fortement les mauvaises prédictions : par exemple, si la vraie étiquette est 1 mais que le modèle prédit 0.01, la perte sera très grande.

* Elle est dérivable, ce qui est important pour l’apprentissage par rétropropagation.

* Elle donne une mesure claire de la performance : plus la cross-entropy est faible, plus le modèle est proche de la vérité.

**Liens Externes (Youtube, Medium, etc):**

* [Evaluation Metrics in Machine Learning](https://youtu.be/LbX4X71-TFI?si=IHg5r7VopAAvQy4C)  
* [Performance Metrics in Machine Learning](https://neptune.ai/blog/performance-metrics-in-machine-learning-complete-guide)  
* [Machine Learning Regression Metrics](https://youtu.be/jyeNAByFL_A?si=RQpz65CH1PSJgQ54)  
* [Precision, Recall and F1 Score Intuitively Explained](https://youtu.be/8d3JbbSj-I8?si=9UDXCQZsfCVDyD7U)  
* [Accuracy vs Precision vs Recall in Machine Learning: What is the difference?](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall)  
* [Comment Evaluer La Performance De Votre Modèle De Classification : Fonctions De Perte Et Métriques](https://youtu.be/m3XQvhUsNJ8?si=u0CnUyaQJxkIvg4x)  
* [Machine Learning : Precision ou Recall ?](https://youtu.be/NrLOc9IFjrI?si=qcNjYm6lgsoPz2Hp)  
* [Précision, Rappel, F1 score, Accuracy, Matrice de Confusion : Que choisir et quand ?](https://youtu.be/ngvEcjZhSMY?si=8d1iH2dD0Oh1HYa3)  
* [Métriques en Machine Learning : Tout ce qu’il faut savoir](https://datascientest.com/metriques-en-machine-learning)  
* [Intuitively Understanding the Cross Entropy Loss](https://youtu.be/Pwgpl9mKars?si=k_0-YiaSuhe2ZGpC)

**Bibliographie**

* Naidu, G., Zuva, T. and Sibanda, E.M., 2023, April. A review of evaluation metrics in machine learning algorithms. In *Computer science on-line conference* (pp. 15-25). Cham: Springer International Publishing.  
* Tatachar, A.V., 2021\. Comparative assessment of regression models based on model evaluation metrics. *International Research Journal of Engineering and Technology (IRJET)*, *8*(09), pp.2395-0056.  
* Vujović, Ž., 2021\. Classification model evaluation metrics. *International Journal of Advanced Computer Science and Applications*, *12*(6), pp.599-606.  
* Buckland, M. and Gey, F., 1994\. The relationship between recall and precision. *Journal of the American society for information science*, *45*(1), pp.12-19.

### 5. Perceptron

Un **perceptron** est un type élémentaire de neurone artificiel utilisé pour des tâches de **classification binaire**. Il prend en entrée un ensemble de caractéristiques x₁, x₂, ..., xₙ​​, chacune étant multipliée par un poids correspondant w₁, w₂, ..., wₙ​, ajoute un terme de biais bbb, puis applique une **fonction d’activation** au résultat.

![][image14]

Image extraite de: [https://www.linkedin.com/pulse/perceptron-journey-through-history-challenges-current-santosh-kamble](https://www.linkedin.com/pulse/perceptron-journey-through-history-challenges-current-santosh-kamble))

La fonction d'activation *f* est généralement une **fonction en escalier** (produisant 0 ou 1), mais d’autres fonctions comme la **sigmoïde** peuvent également être utilisées.

Pendant l’apprentissage, le perceptron met à jour ses poids selon une règle d’apprentissage visant à réduire l’erreur entre les sorties prédites et les sorties attendues. Ce processus est répété jusqu’à ce que le modèle parvienne à correctement classer les données d'entraînement.

```{math}
  z = w₁x₁ + w₂x₂ + ⋯ + wₙxₙ + b

  output = f(z) = f(w₁x₁ + w₂x₂ + ⋯ + wₙxₙ + b)
```

Un perceptron à une seule couche fonctionne efficacement pour des problèmes **linéairement séparables**. Cependant, il est incapable de résoudre des tâches plus complexes et non linéaires. Pour traiter ce type de problèmes, il est nécessaire d'utiliser des perceptrons multicouches (Multi-Layer Perceptrons, MLP) et des modèles d'apprentissage profond.

**Liens Externes (Youtube, Medium, etc):**

* [Math Behind Perceptrons](https://medium.com/@iamask09/math-behind-perceptrons-7241d5dadbfc)  
* [Perceptron (Youtube)](https://youtu.be/4Gac5I64LM4?si=uVnzWhM34Z-k__Ae)  
* [Perceptrons w3Schools](https://www.w3schools.com/ai/ai_perceptrons.asp)  
* [LE PERCEPTRON \- DEEP LEARNING](https://youtu.be/VlMm4VZ6lk4?si=2dhuzU4q7MQatNAV)  
* [Perceptron : qu’est-ce que c’est et à quoi ça sert ?](https://datascientest.com/perceptron)

**Bibliographie**

* Islam, M.N., 2023\. *Introduction to the Perceptron and Its Applications* (Doctoral dissertation, Jahangirnagar University).  
* Kim, E.H. and Kim, H.S., 2021\. Perceptron: Basic Principles of Deep Neural Networks. *Cardiovascular Prevention and Pharmacotherapy*, *3*(3), pp.64-72.  
* Joshi, A.V., 2022\. Perceptron and neural networks. In *Machine learning and artificial intelligence* (pp. 57-72). Cham: Springer International Publishing.

### 6. Gradient Descent

Les algorithmes d'optimisation sont essentiels pour l'entraînement des modèles de machine learning. Ils permettent de mettre à jour les paramètres du modèle (par exemple les poids et les biais) de manière à minimiser la **fonction de perte**. L'objectif est de trouver les meilleurs paramètres possibles afin que le modèle puisse effectuer des prédictions précises. Sans optimisation, l'entraînement du modèle ne mènerait pas à des résultats pertinents ou fiables.  
Le **Gradient Descent** est un algorithme d'optimisation utilisé pour minimiser la fonction de coût (ou fonction de perte) dans les modèles de machine learning et les réseaux de neurones. Il ajuste les paramètres du modèle en calculant le gradient de la fonction de perte par rapport aux paramètres, puis en avançant dans la direction opposée au gradient. Le but est de trouver l'ensemble des paramètres qui minimise l'erreur.  
![][image15]

Image extraite de: [https://www.tpointtech.com/gradient-descent-in-machine-learning](https://www.tpointtech.com/gradient-descent-in-machine-learning)

La formule générale pour une itération est :  
![][image16]

#### **Batch Gradient Descent**

Le **Batch Gradient Descent** calcule le gradient en utilisant l'ensemble du jeu de données d'entraînement. Il effectue une mise à jour unique des paramètres par itération, basée sur le gradient moyen calculé à partir de toutes les données.

**Caractéristiques principales :**

* **Calcul :** Utilise l'ensemble complet des données pour calculer le gradient.

* **Efficacité :** Peut être lent pour les grands ensembles de données car tout le jeu de données doit être traité à chaque itération.

* **Convergence :** Garantit la convergence vers le minimum global pour les fonctions convexes, ou vers un minimum local pour les fonctions non convexes.

Batch Gradient Descent est en général plus stable et moins bruité. Le calcul du gradient est plus précis puisqu'il repose sur l'ensemble des données. Toutefois, il est coûteux en ressources pour les grands ensembles de données et nécessite une importante capacité mémoire.

#### **Stochastic Gradient Descent (SGD)**

Le Stochastic Gradient Descent (SGD) met à jour les paramètres du modèle après chaque échantillon individuel d'entraînement. Contrairement au batch gradient descent, il ne calcule pas le gradient sur l'ensemble des données mais réalise une mise à jour pour chaque donnée.

**Caractéristiques principales :**

* **Calcul :** Utilise un seul point de données à la fois pour calculer le gradient.

* **Efficacité :** Plus rapide que le batch gradient descent pour les grands ensembles de données.

* **Convergence :** Peut être bruité à cause des mises à jour sur des échantillons individuels, mais conduit souvent à une convergence plus rapide en pratique.

SGD permet des calculs plus rapides, particulièrement pour de grands ensembles de données. Sa nature aléatoire lui permet également d'échapper aux minima locaux dans les fonctions non convexes. Ses inconvénients incluent des mises à jour bruitées et une convergence moins stable. Il nécessite également un réglage minutieux du taux d'apprentissage pour éviter le dépassement du minimum.

#### **Mini-Batch Gradient Descent**

Le **Mini-Batch Gradient Descent** combine les avantages du batch gradient descent et du stochastic gradient descent. Il divise l'ensemble de données en petits lots (mini-batches) et calcule le gradient pour chaque mini-batch avant de mettre à jour les paramètres.

#### **Caractéristiques principales :**

* **Calcul** : Utilise un sous-ensemble (mini-batch) du jeu de données pour chaque mise à jour du gradient.

* **Efficacité** : Offre un équilibre entre l'efficacité computationnelle du batch gradient descent et la rapidité du SGD.

* **Convergence** : Apporte une convergence plus stable que le SGD tout en étant plus rapide que le batch gradient descent.

Le **Mini-Batch Gradient Descent** est plus efficace d'un point de vue computationnel que le batch gradient descent. Il est aussi moins bruité que le SGD, ce qui conduit à des mises à jour plus stables. De plus, il peut tirer avantage du parallélisme offert par le matériel comme les GPU. Cependant, il nécessite un ajustement précis de la taille du mini-batch et du taux d'apprentissage.

![][image17]  
Image extraite de: [https://alwaysai.co/blog/what-is-gradient-descent](https://alwaysai.co/blog/what-is-gradient-descent)

**Liens Externes (Youtube, Medium, etc):**

* [What is Gradient Descent Algorithm](https://www.analyticsvidhya.com/blog/2020/10/how-does-the-gradient-descent-algorithm-work-in-machine-learning/)  
* [Stochastic Gradient Descent Explained in Real Life](https://medium.com/data-science/stochastic-gradient-descent-explained-in-real-life-predicting-your-pizzas-cooking-time-b7639d5e6a32)  
* [Gradient Descent in Machine Learning](https://www.tpointtech.com/gradient-descent-in-machine-learning)  
* [Gradient Descent From Scratch](https://medium.com/@jaleeladejumo/gradient-descent-from-scratch-batch-gradient-descent-stochastic-gradient-descent-and-mini-batch-def681187473#:~:text=In%20batch%20gradient%20descent%2C%20the,in%20a%20single%20training%20iteration.)  
* [Gradient Descent | How Neural Networks Learn](https://youtu.be/IHZwWFHWa-w?si=GRQcHPtTETczyqgK)  
* [Batch GD vs Mini-Batch GD vs SGD](https://youtu.be/1xMs6A3DLYw?si=oh-ao1JDFh8W8sfX)   
* [Les bases de la descente de gradient | Réseaux de neurones](https://youtu.be/a5xuJLFTC7o?si=LtXpjVtpIHUHlKKU)  
* [La descente de gradient (stochastique) | Intelligence artificielle](https://youtu.be/Q9-vDFvDdfg?si=HuDzAVO4XfqM9dNT)

**Bibliographie**

* Ruder, S., 2016\. An overview of gradient descent optimization algorithms. *arXiv preprint arXiv:1609.04747*.  
* Ketkar, N., 2017\. Stochastic gradient descent. In *Deep learning with Python: A hands-on introduction* (pp. 113-132). Berkeley, CA: Apress.  
* Khirirat, S., Feyzmahdavian, H.R. and Johansson, M., 2017, December. Mini-batch gradient descent: Faster convergence under data sparsity. In *2017 IEEE 56th Annual Conference on Decision and Control (CDC)* (pp. 2880-2887). IEEE.  
* Adigun, A.A. and Yinka-Banjo, C., 2022, January. Comparing Stochastic Gradient Descent and Mini-batch Gradient Descent Algorithms. In *Informatics and Intelligent Applications: First International Conference, ICIIA 2021, Ota, Nigeria, November 25–27, 2021, Revised Selected Papers* (p. 283). Springer Nature.  
* Tian, Y., Zhang, Y. and Zhang, H., 2023\. Recent advances in stochastic gradient descent in deep learning. *Mathematics*, *11*(3), p.682.

### 7. Algorithmes d’Optimisation

Optimiser un modèle n'est pas toujours une tâche simple. Pour les modèles complexes comme les réseaux de neurones profonds, la fonction de perte est souvent non convexe, ce qui signifie qu'il existe plusieurs minima locaux et que les gradients peuvent être bruités, clairsemés ou s'annuler. Dans ces situations, des méthodes d'optimisation simples comme le batch gradient descent peuvent rencontrer des difficultés pour trouver une solution optimale, en particulier avec de grands ensembles de données.

C'est dans ce contexte que des algorithmes d'optimisation avancés comme Adam, RMSProp et le Gradient Descent avec Momentum interviennent. Ces techniques avancées permettent de mieux naviguer sur la surface de la fonction de perte en adaptant le taux d'apprentissage et en utilisant des stratégies comme l'inertie (momentum) et les taux d'apprentissage adaptatifs.

Voici pourquoi ces algorithmes avancés sont nécessaires :

* **Convergence plus rapide** : Le gradient descent classique peut être lent, en particulier lorsque les gradients varient rapidement ou que la surface de perte est irrégulière. Les algorithmes avancés accélèrent le processus de convergence.

* **Gestion des gradients bruités** : En deep learning, les gradients peuvent être instables, surtout avec de grands ensembles de données. Des algorithmes comme Adam et RMSProp ajustent les taux d'apprentissage pour maintenir des mises à jour stables.

* **Évitement des minima locaux** : Le Momentum et Adam permettent au modèle d'éviter de rester bloqué dans des minima locaux peu profonds, augmentant ainsi les chances de trouver de meilleures solutions.

* **Taux d'apprentissage adaptatif** : Contrairement au gradient descent classique, RMSProp et Adam modifient automatiquement le taux d'apprentissage au cours de l'entraînement, rendant le processus plus efficace et limitant le besoin d'un réglage manuel.

#### **Gradient Descent avec Momentum**

Le **Gradient Descent avec Momentum** est une amélioration du gradient descent de base. Il accélère le processus d'optimisation dans la bonne direction tout en atténuant les oscillations. Il introduit un terme d'inertie (momentum) qui prend en compte les gradients précédents pour lisser les mises à jour des paramètres.

La **formule de mise à jour** pour le Gradient Descent avec Momentum est la suivante :

![][image18]

#### **Avantages du Gradient Descent avec Momentum**

* **Réduction des oscillations** : Le momentum atténue les oscillations et permet une convergence plus rapide, en particulier dans les régions où les gradients changent fréquemment de direction.

* **Échappement aux minima locaux peu profonds** : En conservant une impulsion dans la bonne direction, le momentum aide le modèle à sortir des minima locaux peu profonds.

#### **Inconvénients du Gradient Descent avec Momentum**

* **Nécessité de réglage** : Le taux d'apprentissage ainsi que le facteur de momentum doivent être ajustés avec soin pour garantir une convergence optimale.

* **Risque de dépassement** : Si le facteur de momentum est trop élevé, le modèle peut dépasser le minimum recherché, entraînant une instabilité de l'optimisation.

![][image19]

Image extraite de: [https://towardsdatascience.com/gradient-descent-extensions-to-your-deep-learning-models-32045ccfa644/](https://towardsdatascience.com/gradient-descent-extensions-to-your-deep-learning-models-32045ccfa644/)

#### **RMSProp (Root Mean Square Propagation)**

RMSProp est un algorithme d'optimisation avec taux d'apprentissage adaptatif. Il ajuste dynamiquement le taux d'apprentissage en le divisant par une moyenne exponentiellement décroissante des carrés des gradients. RMSProp a été conçu pour résoudre le problème des gradients de grande amplitude durant l'entraînement, ce qui permet au modèle de converger plus rapidement.

Voici la formule de mise à jour utilisée par RMSProp :

![][image20]

#### **Avantages de RMSProp**

* **Taux d'apprentissage adaptatif** : Ajuste dynamiquement le taux d'apprentissage en fonction de la magnitude du gradient.

* **Efficace sur des objectifs non stationnaires** : Particulièrement utile pour l'entraînement de réseaux de neurones où la fonction de perte peut évoluer au cours du temps.

* **Convergence accélérée** : Conduit souvent à une convergence plus rapide que la descente de gradient classique.

#### **Inconvénients de RMSProp**

* **Nécessité d'un réglage fin** : Le taux d'apprentissage et le facteur de décroissance doivent être soigneusement ajustés.

* **Risque de dépassement** : Si les hyperparamètres ne sont pas bien choisis, RMSProp peut conduire à des dépassements du minimum optimal.

#### **Adam (Adaptive Moment Estimation)**

**Adam** est l'un des algorithmes d'optimisation les plus utilisés. Il combine les avantages de la descente de gradient avec momentum et de RMSProp. Adam **ajuste le taux d'apprentissage** pour chaque paramètre en calculant à la fois le premier moment (la moyenne) et le second moment (la variance non centrée) des gradients.

La règle de mise à jour est la suivante :

![][image21]

#### **Avantages d'Adam**

* **Combinaison des forces de momentum et de RMSProp** : Permet d'avoir des mises à jour rapides et stables.

* **Taux d'apprentissage adaptatif** : Ajuste dynamiquement le taux d'apprentissage en fonction de la moyenne et de la variance des gradients.

* **Robustesse** : Fonctionne bien sur une grande variété de problèmes et est souvent utilisé comme optimiseur par défaut dans l'entraînement de modèles de deep learning.

#### **Inconvénients d'Adam**

* **Nécessité d'un réglage des hyperparamètres** : Les paramètres β₁, β₂ et α doivent être soigneusement choisis.

* **Convergence sous-optimale possible** : Adam peut parfois converger vers solutions sous-optimales si les hyperparamètres ne sont pas bien ajustés.

**Liens Externes (Youtube, Medium, etc):**

* [Gradient Descent Extensions to Your Deep Learning Models](https://towardsdatascience.com/gradient-descent-extensions-to-your-deep-learning-models-32045ccfa644/)  
* [A visual Explanation of Gradient Descent Methods](https://medium.com/data-science/a-visual-explanation-of-gradient-descent-methods-momentum-adagrad-rmsprop-adam-f898b102325c)  
* [Gradient Descent With Momentum](https://youtu.be/k8fTYJPd3_I?si=dX8QjkiYdiRyfzqN)  
* [Understanding RMSProp](https://medium.com/@piyushkashyap045/understanding-rmsprop-a-simple-guide-to-one-of-deep-learnings-powerful-optimizers-403baeed9922)  
* [Deep Dive into Optimizers for Machine Learning](https://youtu.be/MD2fYip6QsQ?si=J5oi0bHBq0pHAIkl)  
* [Demystifying the Adam Optimizer in Machine Learning](https://medium.com/@weidagang/demystifying-the-adam-optimizer-in-machine-learning-4401d162cb9e)  
* [Adam Optimizer (Français)](https://www.ultralytics.com/fr/glossary/adam-optimizer)  
* [Optimisation pour l’apprentissage automatique](https://www.lamsade.dauphine.fr/~croyer/ensdocs/TUN/PolyTUN.pdf)

**Bibliographie**

* Choi, D., Shallue, C.J., Nado, Z., Lee, J., Maddison, C.J. and Dahl, G.E., 2019\. On empirical comparisons of optimizers for deep learning. *arXiv preprint arXiv:1910.05446*.  
* Nakerst, G., Brennan, J. and Haque, M., 2020\. Gradient descent with momentum---to accelerate or to super-accelerate?. *arXiv preprint arXiv:2001.06472*.  
* Huk, M., 2020\. Stochastic optimization of contextual neural networks with RMSprop. In *Intelligent Information and Database Systems: 12th Asian Conference, ACIIDS 2020, Phuket, Thailand, March 23–26, 2020, Proceedings, Part II 12* (pp. 343-352). Springer International Publishing.  
* Kingma, D.P. and Ba, J., 2014\. Adam: A method for stochastic optimization. *arXiv preprint arXiv:1412.6980*.

### 8. Couche Dense

**Introduction**

Avec la complexification croissante des problèmes de machine learning, notamment dans des domaines tels que la reconnaissance d'images, le traitement de la parole et la compréhension du langage naturel, les algorithmes traditionnels montrent souvent leurs limites. Les réseaux de neurones denses (DNN) sont des modèles puissants conçus pour capturer des schémas complexes dans les données en empilant plusieurs couches de neurones. Chaque couche apprend des caractéristiques de plus en plus abstraites, permettant aux DNN de résoudre des problèmes que les modèles peu profonds ne peuvent pas traiter.

Un DNN est composé d'une couche d'entrée, de plusieurs couches cachées et d'une couche de sortie. La profondeur (c'est-à-dire le nombre de couches) confère au modèle sa capacité d'expression, lui permettant d'approximer des fonctions non linéaires complexes. Dans un DNN, chaque neurone est connecté à l'ensemble des neurones de la couche suivante. Ces connexions, appelées poids, doivent être optimisées au cours du processus de rétropropagation.

![][image22]

Image extraite de: [https://www.researchgate.net/figure/General-Architecture-for-a-Deep-Neural-Network-with-Two-Hidden-Layers\_fig2\_353032163](https://www.researchgate.net/figure/General-Architecture-for-a-Deep-Neural-Network-with-Two-Hidden-Layers_fig2_353032163)

#### **Cas d'Utilisation : Classification et Régression**

Les réseaux de neurones profonds (DNN) peuvent être utilisés pour des tâches de classification et de régression :

* **Classification:** Les DNN sont largement utilisés dans des tâches telles que la classification d'images (par exemple, identifier des objets dans des photos), l'analyse de sentiments, et le diagnostic de maladies, où l'objectif est d'assigner les données d'entrée à des catégories discrètes.  
* **Régression** : Les DNN sont également efficaces pour prédire des valeurs continues, telles que les prix des maisons, les prix des actions ou la consommation d'énergie, où la sortie est un nombre réel plutôt qu'une étiquette de classe.

#### **Propagation Avant (Forward Propagation)**

1. La propagation avant est le processus par lequel les données d'entrée traversent le réseau pour produire une sortie. Chaque caractéristique d'entrée xi est multipliée par un poids correspondant *wi*​, et les résultats sont additionnés avec un biais *b* :  
                                               *z \= w₁x₁ \+ w₂x₂ \+ ⋯ \+ wₙxₙ \+ b*  
2. Le résultat *z* est ensuite passé par une fonction d'activation *f(z)*, telle que ReLU ou sigmoïde, introduisant ainsi de la non-linéarité.  
3. Ce processus se répète couche par couche, chaque sortie de couche devenant l'entrée de la couche suivante, jusqu'à ce que la prédiction finale soit obtenue à la couche de sortie.

#### **Rétropropagation (Backpropagation)**

La **rétropropagation** est l'algorithme utilisé pour entraîner le réseau de neurones en mettant à jour ses poids et ses biais afin de minimiser la perte.

Voici comment cela fonctionne étape par étape :

1. **Calcul de la Perte :** Après la propagation avant, nous calculons l'écart entre la sortie et la vérité de terrain en utilisant une fonction de perte (par exemple, l'entropie croisée pour la classification, l'erreur quadratique moyenne (MSE) pour la régression).

2. **Calcul du Gradient de la Perte :** En utilisant la règle de la chaîne en calcul différentiel, nous calculons la dérivée partielle de la perte par rapport à chaque poids et biais du réseau.

3. **Propagation des Erreurs en Arrière :** En partant de la couche de sortie, l'algorithme calcule le gradient de la perte par rapport à chaque sortie de neurone. Il se déplace en arrière à travers les couches, couche par couche, mettant à jour les poids et biais de chaque neurone en calculant combien ils ont contribué à l'erreur.

4. **Mise à Jour des Paramètres :** Une fois que les gradients sont calculés, les poids sont mis à jour en utilisant la descente de gradient ou l'une de ses variantes (comme Adam ou RMSProp).

Ce processus est répété pendant plusieurs itérations (époques) jusqu'à ce que le réseau apprenne à minimiser la fonction de perte.

**Liens Externes (Youtube, Medium, etc):**

* [Neural Network Animated](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.00428&showTestData=false&discretize=false&percTrainData=50&x=false&y=true&xTimesY=true&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)  
* [What is a deep neural network?](https://botpress.com/blog/deep-neural-network)  
* [But what is a Neural Network (Youtube)](https://youtu.be/aircAruvnKk?si=LXCNgKl9wx6gKf5P)  
* [Forward Propagation in Neural Networks](https://youtu.be/99CcviQchd8?si=mFmzX3500G0ifHE3)  
* [Backpropagation, intuitively](https://youtu.be/Ilg3gGewQ5U?si=8XcZPowJJVuScLu3)  
* [Backpropagation Calculus](https://youtu.be/tIeHLnjs5U8?si=_62VyRYKVCYrKxes)  
* [Backpropagation](https://youtu.be/dB-u77Y5a6A?si=gL9hKbcl2fF-j1WY)  
* [How to Evaluate a Neural Network’s Performance](https://youtu.be/NE1iCyqUMRI?si=ar9R7zh8EyYlkTsV)  
* [Comprendre les réseaux de neurones](https://youtu.be/bkoNl7ImPBU?si=mcZGz2Pc_t6_kwyR)  
* [Qu'est-ce qui se passe dans un réseau de neurones ?](https://youtu.be/yFcdKE6YI0E?si=q413Mrm_rCZkIFS9)

**Bibliographie**

* Bishop, C.M., 1994\. Neural networks and their applications. *Review of scientific instruments*, *65*(6), pp.1803-1832.  
* Zou, J., Han, Y. and So, S.S., 2009\. Overview of artificial neural networks. *Artificial neural networks: methods and applications*, pp.14-22.  
* Rojas, R. and Rojas, R., 1996\. The backpropagation algorithm. *Neural networks: a systematic introduction*, pp.149-182.  
* Hecht-Nielsen, R., 1992\. Theory of the backpropagation neural network. In *Neural networks for perception* (pp. 65-93). Academic Press.  
* Heaton, J., 2020\. Applications of deep neural networks. *arXiv preprint arXiv:2009.05673*.  
* Jain, B.A. and Nag, B.N., 1997\. Performance evaluation of neural network decision models. *Journal of Management Information Systems*, *14*(2), pp.201-216.

### 9. Couche Convolutionnelle

**Pourquoi avons-nous besoin de CNN ?**

Les réseaux de neurones denses traitent tous les pixels d’entrée de manière égale et ne tiennent pas compte de la structure spatiale de l’image. Cela entraîne deux problèmes :

* **Trop de paramètres** : Un réseau dense qui connecte chaque pixel à chaque neurone devient coûteux en termes de calcul pour des images de haute résolution.

* **Perte d'information spatiale** : Les couches denses ignorent la position relative des pixels, ce qui est crucial pour comprendre les images.

Les CNN résolvent ces problèmes de la manière suivante :

* **Partage des poids** à travers des noyaux, ce qui réduit considérablement le nombre de paramètres.

* **Préservation des relations spatiales**, ce qui aide le modèle à apprendre des caractéristiques comme les formes et les textures de manière plus efficace.

#### **L’opération de convolution**

Le cœur des CNN réside dans l’opération de convolution, qui extrait des caractéristiques des données d’entrée (généralement des images). Au lieu de connecter chaque neurone à toutes les entrées comme dans les réseaux denses, les CNN utilisent de petits filtres appelés **noyaux** qui glissent sur l’image, effectuent une multiplication élément par élément, puis une somme.

![][image23]

Image extraite de: [https://viso.ai/deep-learning/convolution-operations/](https://viso.ai/deep-learning/convolution-operations/)

#### **Calcul de la Convolution**

Pour calculer la convolution, le pixel central du noyau est placé sur un pixel de l'image source. Ensuite, chaque pixel de l'image source est multiplié par le pixel correspondant du noyau, et les résultats sont résumés. C'est ainsi que l'on obtient un pixel unique dans l'image résultante.

**Noyaux (Filtres)** : Ce sont de petites matrices (par exemple, 3×3 ou 5×5) qui détectent des motifs comme les bords, les coins ou les textures en scannant l'image.

**Stride** : Le stride détermine combien de pixels le noyau se déplace à chaque étape. Un stride plus grand réduit la taille de la sortie (sous-échantillonnage).

**Padding** : Pour contrôler la taille spatiale de la sortie, nous pouvons ajouter du padding (généralement des zéros) autour de l'image d'entrée. Cela aide à préserver la taille d'origine ou à contrôler combien elle rétrécit. Il existe 2 types de padding : **same** et **valid**.

Le résultat de la convolution s'appelle une **carte de caractéristiques** (ou carte d'activation), qui met en évidence la présence de motifs spécifiques détectés par le noyau.

#### **Changements de Dimension d'Image**

La taille de la carte de caractéristiques résultante après une convolution dépend de quatre facteurs :

* Taille de l'entrée (W)

* Taille du noyau (K)

* Padding (P)

* Stride (S)

La formule pour la dimension de la sortie (en supposant une entrée et un noyau carrés) est :

![][image24]

**Si le padding est 0 et le stride est 1, l'image rétrécit après chaque convolution.**

Si le padding est correctement choisi (appelé "same" padding), la taille de la sortie reste identique à celle de l'entrée.

Cela permet de contrôler la profondeur et la résolution du réseau à différentes étapes.

#### **Hiérarchies de Caractéristiques**

Les CNNs apprennent une hiérarchie de caractéristiques :

* **Les couches précoces** détectent des caractéristiques de bas niveau telles que les bords, les lignes et les textures simples.

* **Les couches intermédiaires** combinent ces caractéristiques pour former des caractéristiques intermédiaires, comme des formes ou des parties d'objets.

* **Les couches profondes** capturent des caractéristiques de haut niveau, telles que les visages, les objets ou des régions significatives de l'image.

Cette abstraction progressive est l'une des principales raisons pour lesquelles les CNNs réussissent si bien dans des tâches comme la reconnaissance d'objets, la détection de visages et l'analyse d'images médicales.

Il existe un grand nombre d'architectures CNN connues qui ont révolutionné le domaine de la vision par ordinateur, telles que AlexNet, VGG, LeNet, etc. Elles seront abordées dans les chapitres suivants.

**Liens Externes (Youtube, Medium, etc):**

* [What are Convolutional Neural Networks?](https://youtu.be/QzY57FaENXg?si=FfpNZf7dx6hMMgHS)  
* [CNNs Explained](https://youtu.be/YRhxdVk_sIs?si=WaFmOMZ_OpG4dbr7)  
* [Understanding the Convolutional Filter Operations in CNNs](https://medium.com/advanced-deep-learning/cnn-operation-with-2-kernels-resulting-in-2-feature-mapsunderstanding-the-convolutional-filter-c4aad26cf32)  
* [An Introduction to Convolutional Neural Networks](https://www.datacamp.com/tutorial/introduction-to-convolutional-neural-networks-cnns)  
* [Convolutional Neural Networks MIT](https://youtu.be/2xqkSUhmmXU?si=US_y4Fvbdkk8Vvn-)  
* [CNN1/ Réseaux convolutifs (CNN)](https://youtu.be/581X9wsnWJs?si=I6GQOeGaAkZ0BYwf)  
* [Les réseaux de convolution (CNN) | Intelligence artificielle 47](https://youtu.be/zG_5OtgxfAg?si=zleXRZTuWNiM1rcH)  
* [Introduction aux réseaux neuronaux convolutifs (CNN)](https://fr.mathworks.com/discovery/convolutional-neural-network.html)

**Bibliographie**

* O'shea, K. and Nash, R., 2015\. An introduction to convolutional neural networks. *arXiv preprint arXiv:1511.08458*.  
* Ajit, A., Acharya, K. and Samanta, A., 2020, February. A review of convolutional neural networks. In *2020 international conference on emerging trends in information technology and engineering (ic-ETITE)* (pp. 1-5). IEEE.  
* Aghdam, H.H. and Heravi, E.J., 2017\. Guide to convolutional neural networks. *New York, NY: Springer*, *10*(978-973), p.51.  
* Jain, S. and Chauhan, R., 2018\. Recognition of handwritten digits using DNN, CNN, and RNN. In *Advances in Computing and Data Sciences: Second International Conference, ICACDS 2018, Dehradun, India, April 20-21, 2018, Revised Selected Papers, Part I 2* (pp. 239-248). Springer Singapore.

### 10. Fonctions d’Activation

Les **fonctions d'activation** introduisent de la non-linéarité dans les réseaux neuronaux, leur permettant d'apprendre des modèles complexes. Sans elles, peu importe le nombre de couches du réseau, il se comporterait comme un modèle linéaire et échouerait à capturer la véritable structure des données réelles. Peu importe le nombre de couches, ce serait comme si nous travaillions avec un seul neurone.

Il existe une grande variété de fonctions d'activation, mais voici les plus couramment utilisées :

#### **ReLU (Rectified Linear Unit)**

Bien que ReLU apparaisse linéaire pour les entrées positives, elle est différentiable et supporte la rétropropagation, ce qui la rend à la fois efficace et performante sur le plan computationnel.

Un aspect clé de ReLU est qu'elle n'active pas tous les neurones simultanément. Les neurones sont activés uniquement lorsque la sortie de la transformation linéaire est supérieure à zéro ; sinon, ils restent inactifs.

**![][image25]**  
Voici la formule de ReLU:  
![][image26]

Un problème avec la fonction d'activation ReLU est le problème du "dying ReLU". Cela se produit lorsqu'un neurone génère une sortie de zéro pour toutes les entrées. Comme le gradient de ReLU est nul pour les entrées négatives, ces neurones cessent d'apprendre pendant l'entraînement et "meurent" effectivement. Une fois que cela se produit, ils ne contribuent plus aux prédictions ou aux mises à jour du modèle.

#### **Fonction Leaky ReLU**

Leaky ReLU est une version améliorée de la fonction ReLU pour résoudre le problème du Dying ReLU, car elle a une petite pente positive dans la zone négative. Cela permet aux neurones de continuer à apprendre, même si leur sortie est inférieure à zéro, en évitant ainsi qu'ils ne meurent.

![][image27]  
Voici la formule de LeakyReLU:  
![][image28]

Les avantages de Leaky ReLU sont les mêmes que ceux de ReLU, en plus du fait qu'il permet la rétropropagation, même pour les valeurs d'entrée négatives. En apportant cette légère modification pour les valeurs d'entrée négatives, le gradient du côté gauche du graphique devient non nul. Par conséquent, on ne rencontrera plus de neurones morts dans cette région.

#### **Fonction Sigmoïde**

Cette fonction accepte toute entrée réelle et produit une sortie comprise entre 0 et 1\. À mesure que l'entrée devient plus positive, la sortie approche de 1,0 ; à mesure que l'entrée devient plus négative, la sortie approche de 0,0, comme illustré ci-dessous.

![][image29]

Voici la formule de la fonction logistique:

![][image30]

La fonction sigmoïde (ou logistique) est largement utilisée, en particulier dans les modèles qui prédisent des probabilités. Étant donné que les probabilités varient entre 0 et 1, la fonction sigmoïde est idéale en raison de son intervalle de sortie.  
 Elle est également différentiable et fournit un gradient lisse et continu, ce qui aide à garantir un apprentissage stable. Cette transition douce est représentée visuellement par la courbe en forme de S de la fonction sigmoïde.

#### **Fonction Tanh**

La fonction Tanh est similaire à la fonction sigmoïde et possède également une courbe en forme de S. Cependant, son output varie entre \-1 et 1\. À mesure que l'entrée devient plus positive, la sortie approche de 1,0 ; à mesure que l'entrée devient plus négative, la sortie approche de \-1,0.

![][image31]  
Voici la formule de la fonction tanh :  
![][image32]

#### **Avantages de la fonction d'activation Tanh**

La sortie de la fonction Tanh est centrée autour de zéro, ce qui facilite l'interprétation des valeurs comme étant fortement négatives, neutres ou fortement positives.

Elle est couramment utilisée dans les couches cachées des réseaux neuronaux, car son output varie entre \-1 et 1\. Cela permet de centrer les données autour de zéro, ce qui peut améliorer l'efficacité de l'entraînement et rendre l'apprentissage plus facile pour la couche suivante.

#### **Fonction Softmax**

La fonction Softmax peut être considérée comme une combinaison de plusieurs sigmoïdes, et elle garantit que les probabilités qu’elle génère somment à 1\. Elle est principalement utilisée dans la couche de sortie d’un réseau neuronal lors de la classification multiclasses.

![][image33]

Images extraites de: [https://www.v7labs.com/blog/neural-networks-activation-functions](https://www.v7labs.com/blog/neural-networks-activation-functions)

**Liens Externes (Youtube, Medium, etc):**

* [Activation Functions in Neural Networks](https://www.v7labs.com/blog/neural-networks-activation-functions)  
* [Activation Functions Explained](https://youtu.be/s-V7gKrsels?si=8cBf9LJCHZQ_2L2T)  
* [Which Activation Function Should I Use?](https://youtu.be/-7scQpJT7uo?si=iKxFBwYjWZl6n_aa)  
* [Activation Functions: all you need to know\!](https://medium.com/analytics-vidhya/activation-functions-all-you-need-to-know-355a850d025e)  
* [Fonctions d'activation et réseaux de neurones](https://www.picsellia.fr/post/fonctions-dactivation-reseaux-neurones)  
*  [\[Deepmath\] 1.4. Fonctions d'activation](https://youtu.be/q0ZZ695vjkY?si=NnP-t4P8NwYdOocl)

**Bibliographie**

* Sharma, S., Sharma, S. and Athaiya, A., 2017\. Activation functions in neural networks. *Towards Data Sci*, *6*(12), pp.310-316.  
* Dubey, S.R., Singh, S.K. and Chaudhuri, B.B., 2022\. Activation functions in deep learning: A comprehensive survey and benchmark. *Neurocomputing*, *503*, pp.92-108.  
* Lederer, J., 2021\. Activation functions in artificial neural networks: A systematic overview. *arXiv preprint arXiv:2101.09957*.  
* Szandała, T., 2021\. Review and comparison of commonly used activation functions for deep neural networks. *Bio-inspired neurocomputing*, pp.203-224.

### 11. Dropout et Normalisation par Lots

Les réseaux neuronaux profonds peuvent facilement souffrir de sur-apprentissage, surtout lorsqu'ils sont formés avec des données limitées.

#### **Dropout**

Le ***dropout*** est une technique de régularisation qui aide à réduire le sur-apprentissage. Pendant l'entraînement, elle désactive (ou "élimine") aléatoirement une fraction des neurones d'une couche pour chaque passage avant. Cela signifie que le réseau ne peut pas trop dépendre de neurones spécifiques et doit apprendre des représentations redondantes et plus robustes. Les neurones sont désactivés pendant le passage avant et la rétropropagation.

Le **taux de *dropout*** (probabilité de suppression des neurones) est un hyperparamètre que vous pouvez ajuster. Typiquement, des valeurs comme 0.2 ou 0.5 sont utilisées, ce qui signifie que 20 % ou 50 % des neurones sont "abandonnés" à chaque itération.

![][image34]  
Image extraite de: [https://www.researchgate.net/figure/An-illustration-of-the-dropout-mechanism-within-the-proposed-CNN-a-Shows-a-standard\_fig23\_317277576](https://www.researchgate.net/figure/An-illustration-of-the-dropout-mechanism-within-the-proposed-CNN-a-Shows-a-standard_fig23_317277576)

#### **Résultats :**

* Améliore la généralisation en réduisant le sur-apprentissage.

* Force le réseau à devenir plus résilient et distribué dans l'apprentissage.

* Pendant les tests ou l'inférence, le *dropout* est désactivé et tous les neurones sont utilisés, avec leurs sorties mises à l'échelle en conséquence pour refléter le comportement d'entraînement.

#### **Normalisation par Lots (Batch Normalization)**

À mesure que les réseaux neuronaux deviennent plus profonds, l'entraînement peut devenir instable et lent. Une des raisons principales en est que la distribution des données à l'intérieur du réseau change constamment à mesure que les poids sont mis à jour — ce phénomène est appelé *shift de covariables internes* (internal covariate shift). Lorsque l'entrée de chaque couche change trop, le réseau doit constamment se réajuster, rendant l'apprentissage plus difficile.

La normalisation par lots résout ce problème en normalisant les entrées de chaque couche — c'est-à-dire en leur donnant une moyenne de 0 et un écart-type de 1\. Cela se fait pour chaque mini-lot pendant l'entraînement. Cette technique aide le réseau à apprendre plus rapidement, réduit la sensibilité à l'initialisation des poids et permet d'utiliser des taux d'apprentissage plus élevés.

![][image35]

Image extraite de: [https://kharshit.github.io/blog/2018/12/28/why-batch-normalization](https://kharshit.github.io/blog/2018/12/28/why-batch-normalization)

#### **Avantages :**

* Entraînement **plus rapide** et **plus stable**.

* **Réduit le *shift* des covariables** internes.

* Agit comme un **régulariseur**, réduisant le besoin de techniques comme le *dropout*.

* **Améliore** la **généralisation**.

**Liens Externes (Youtube, Medium, etc):**

* [Overfitting in a Neural Network Explained](https://youtu.be/DEMmkFC6IGM?si=rK-YZiAmT3jKdyMj)  
* [Understanding Dropout in Deep Learning](https://medium.com/@piyushkashyap045/understanding-dropout-in-deep-learning-a-guide-to-reducing-overfitting-26cbb68d5575)  
* [Understanding Dropout (YouTube)](https://youtu.be/ARq74QuavAo?si=v049TNWMEotcLLT1)  
* [Why Batch Normalization?](https://kharshit.github.io/blog/2018/12/28/why-batch-normalization)  
* [Batch Norm Explained Visually](https://towardsdatascience.com/batch-norm-explained-visually-how-it-works-and-why-neural-networks-need-it-b18919692739/)  
* [Qu’est-ce que la Normalisation Par Lots?](https://www.allaboutai.com/fr-fr/glossaire-ai/normalisation-par-lots/#:~:text=La%20normalisation%20par%20lots%20est,un%20%C3%A9cart%20type%20de%20un.)  
* [Le Dropout c’est quoi ? Deep Learning Explication Rapide](https://inside-machinelearning.com/le-dropout-cest-quoi-deep-learning-explication-rapide/)

**Bibliographie**

* Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I. and Salakhutdinov, R., 2014\. Dropout: a simple way to prevent neural networks from overfitting. *The journal of machine learning research*, *15*(1), pp.1929-1958.  
* Bjorck, N., Gomes, C.P., Selman, B. and Weinberger, K.Q., 2018\. Understanding batch normalization. *Advances in neural information processing systems*, *31*.  
* Balestriero, R. and Baraniuk, R.G., 2022\. Batch normalization explained. *arXiv preprint arXiv:2209.14778*.  
* Garbin, C., Zhu, X. and Marques, O., 2020\. Dropout vs. batch normalization: an empirical study of their impact to deep learning. *Multimedia tools and applications*, *79*(19), pp.12777-12815.