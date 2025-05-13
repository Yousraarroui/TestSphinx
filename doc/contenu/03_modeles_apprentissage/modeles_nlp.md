# Modèles généraux de NLP

1. ## **Réseaux de Neurones Récurrents (RNN)**

Les réseaux de neurones récurrents (RNN) sont conçus pour traiter **des données séquentielles**, c’est-à-dire des données où l’ordre a une importance (par exemple : du texte, de l'audio, des séries temporelles).

### **Structure d'un RNN**

1. **Mémoire du Passé**  
    La principale idée des RNNs est de **garder une mémoire** des informations passées.  
    À chaque instant, un RNN prend :  
   * L’entrée actuelle xt  
   * Son propre état précédent ht−1  
   * Il calcule un nouvel état ht​ en combinant les deux.

2. Cela permet au réseau de tenir compte des éléments précédents pour faire ses prédictions.

3. **Propagation sur la Séquence**  
    Contrairement à un réseau classique qui traite les données indépendamment, un RNN traite **toute la séquence** pas à pas :  
   ht​​ ​= tanh(Whht−1 ​+ Wx​xt​ \+ b)  
    où Wh​, Wx et b sont des poids appris pendant l’entraînement.

4. **Sortie**  
   * À chaque étape, le réseau peut produire une sortie yt​.  
   * Selon l’application, on peut vouloir une sortie à chaque pas de temps (ex : traduction automatique) ou seulement à la fin (ex : analyse de sentiment).

5. **Partage des Paramètres**  
    Tous les pas de temps partagent **les mêmes paramètres** (mêmes poids). Cela permet au modèle d'apprendre à généraliser le comportement sur toute la séquence.

### **Caractéristiques des RNNs**

* **Adaptés aux Séquences** : très efficaces pour traiter des données où l'ordre est important.  
* **Mémoire à Court Terme** : les RNNs sont capables de se souvenir d’informations récentes.  
* **Problèmes de Long Terme** : en pratique, il devient difficile pour un RNN de se souvenir d'informations lointaines dans la séquence à cause des problèmes de **vanishing gradient** (le gradient devient très petit et bloque l’apprentissage sur de longues distances).

Les RNNs ont été une avancée majeure pour des tâches comme la reconnaissance vocale, la génération de texte, ou encore la prévision de séries temporelles.  
 Cependant, pour résoudre certains de leurs problèmes, des architectures améliorées comme **LSTM** et **GRU** ont été développées par la suite.

![][image42]  
Image extraite de : [https://www.researchgate.net/figure/The-standard-RNN-and-unfolded-RNN\_fig1\_318332317](https://www.researchgate.net/figure/The-standard-RNN-and-unfolded-RNN_fig1_318332317)

2. ## **LSTM (Long Short-Term Memory)**

Les RNNs classiques peuvent rencontrer des problèmes pour apprendre des dépendances à long terme dans les séquences, car ils ont du mal à retenir des informations sur plusieurs étapes temporelles. Pour résoudre ce problème, les **Long Short-Term Memory (LSTM)** ont été introduits. Ils sont une extension des RNNs, conçus pour résoudre le problème de **vanishing gradients** et permettre la modélisation de dépendances temporelles sur de longues périodes.

Les LSTM introduisent des **cellules de mémoire** qui peuvent conserver des informations sur plusieurs étapes temporelles, ce qui permet à l’architecture de mieux gérer les dépendances longues.

### **Structure du LSTM**

Un LSTM est composé de plusieurs éléments clés :

1. **La cellule de mémoire** : Elle stocke l'information de manière persistante sur plusieurs étapes temporelles.

2. **Les portes (gates)** : Les portes contrôlent l'ajout ou la suppression d'informations dans la cellule de mémoire. Il y a trois portes principales :

   * **La porte d'oubli (Forget Gate)** : Elle détermine quelles informations doivent être oubliées de la cellule de mémoire.  
   * **La porte d'entrée (Input Gate)** : Elle détermine quelles nouvelles informations doivent être ajoutées à la cellule de mémoire.  
   * **La porte de sortie (Output Gate)** : Elle détermine quelles informations de la cellule de mémoire seront utilisées pour la sortie du LSTM à l'instant ttt.

### **Avantages des LSTM**

Les LSTM sont particulièrement utiles dans les tâches nécessitant l'apprentissage de dépendances longues dans les données temporelles. Par exemple :

* **Mémoire à long terme** : Ils conservent efficacement les informations importantes pendant plusieurs étapes temporelles.  
* **Résolution du problème de vanishing gradient** : Les LSTM sont capables de maintenir un gradient plus stable pendant l'entraînement, ce qui permet un apprentissage plus efficace sur de longues séquences.

#### **Applications des LSTM**

Les LSTM sont utilisés dans divers domaines :

* **Modélisation du langage** : Prédiction des mots suivants dans une phrase ou traduction automatique.  
* **Reconnaissance vocale** : Modélisation des dépendances temporelles dans les signaux audio.  
* **Prédiction des séries temporelles** : Prévisions économiques, prévisions météorologiques, etc.  
* **Génération de texte** : Génération automatique de contenu textuel basé sur un contexte donné.

Les LSTM sont un puissant outil pour traiter des séquences de données où la mémoire à long terme joue un rôle crucial. Grâce à leurs portes et leur cellule de mémoire, ils surpassent les RNNs classiques dans les tâches nécessitant une compréhension de dépendances complexes sur de longues périodes. Les LSTM sont une pièce maîtresse dans de nombreuses applications modernes de l’intelligence artificielle.

![][image43]  
Image extaite de : [https://fr.mathworks.com/discovery/lstm.html](https://fr.mathworks.com/discovery/lstm.html)

3. ## **Gated Recurrent Unit (GRU)**

Les **GRU (Gated Recurrent Unit)** sont une variante des RNNs, développée pour résoudre les problèmes de dépendances longues que les RNNs classiques ont du mal à gérer. Les GRU sont une version simplifiée des LSTM et visent à atteindre des performances similaires avec un nombre de paramètres réduits, ce qui les rend plus légers tout en restant efficaces pour la modélisation de séquences.

Les GRU, comme les LSTM, utilisent des portes pour contrôler l'information qui entre, reste ou sort du réseau. Toutefois, les GRU combinent certaines étapes de calcul des LSTM, ce qui réduit leur complexité sans sacrifier leurs performances.

### **Structure du GRU**

Le GRU utilise deux portes principales :

1. **La porte de mise à jour (Update Gate)** : Cette porte détermine dans quelle mesure l’état précédent doit être retenu ou mis à jour avec de nouvelles informations.  
2. **La porte de réinitialisation (Reset Gate)** : Elle détermine dans quelle mesure les informations passées doivent être oubliées avant d’ajouter de nouvelles informations.

### **Avantages des GRU**

Les **GRU** présentent plusieurs avantages qui les rendent attrayants :

* **Moins de paramètres** : Les GRU ont moins de paramètres que les LSTM, car ils utilisent moins de portes. Cela les rend plus rapides à entraîner et moins coûteux en termes de mémoire.  
* **Performances similaires** : Bien qu'ils aient moins de paramètres, les GRU obtiennent souvent des résultats très similaires à ceux des LSTM sur diverses tâches de séquences.  
* **Simplification** : La structure des GRU est plus simple que celle des LSTM, ce qui permet une meilleure interprétabilité tout en restant efficace pour capturer des dépendances longues.

### **Applications des GRU**

Les GRU sont utilisés dans les mêmes domaines que les LSTM, où la gestion des séquences est essentielle. Voici quelques exemples d'applications :

* **Modélisation du langage** : Prévision de la prochaine séquence de mots dans des tâches de génération de texte.  
* **Prédiction des séries temporelles** : Prévisions financières, prévisions météorologiques, etc.  
* **Reconnaissance vocale** : Compréhension et transcription de la parole.  
* **Traduction automatique** : Traduction de texte d'une langue à une autre, en capturant les dépendances contextuelles.

### **Conclusion**

Les **GRU** sont une alternative plus simple et plus rapide aux **LSTM**, tout en offrant des performances similaires dans des tâches impliquant des séquences. Grâce à leur structure plus légère et leurs portes efficaces, les GRU sont particulièrement adaptés aux applications nécessitant des modèles rapides à entraîner et capables de gérer des séquences longues sans la complexité des LSTM. Ils représentent une excellente option pour des tâches en traitement de langage naturel, reconnaissance vocale, et bien d'autres applications nécessitant l'analyse de données temporelles.

![][image44]  
Image extraite de : [https://www.oreilly.com/library/view/advanced-deep-learning/9781789956177/8ad9dc41-3237-483e-8f6b-7e5f653dc693.xhtml](https://www.oreilly.com/library/view/advanced-deep-learning/9781789956177/8ad9dc41-3237-483e-8f6b-7e5f653dc693.xhtml)

4. ##  **Modèles d'attention (Attention-based models)**

Les modèles d'attention sont devenus un élément central dans le domaine du deep learning, en particulier pour les tâches impliquant des séquences de données, comme la traduction automatique, la reconnaissance d'images ou encore la compréhension du langage naturel. Avant l'introduction des mécanismes d'attention, les modèles comme les RNNs, LSTM et GRU avaient du mal à capturer les dépendances à long terme dans les séquences. Les mécanismes d'attention ont révolutionné cette capacité en permettant au modèle de se concentrer sur les parties les plus pertinentes d'une séquence, tout en ignorant le reste.

### **Le principe de l'attention**

L'idée principale derrière l'attention est de permettre au modèle de "peser" différentes parties de l'entrée selon leur importance pour la tâche à accomplir. Ce mécanisme est inspiré de la façon dont les humains prêtent attention à certains éléments plus que d'autres lorsqu'ils accomplissent une tâche, comme lire un texte ou écouter une conversation.

### **Structure du mécanisme d'attention**

Un modèle d'attention calcule une **poids d'attention** pour chaque élément d'une séquence d'entrée, ce qui détermine l'importance de cet élément dans la prédiction de la sortie. Ce processus peut être décrit par les étapes suivantes :

1. **Calcul des scores d'attention** : Pour chaque élément de la séquence d'entrée, on calcule un score qui indique à quel point cet élément est important par rapport à un autre élément. Cela se fait généralement en calculant une similarité entre l'élément courant et les éléments précédents de la séquence.

2. **Normalisation des scores** : Les scores d'attention sont ensuite normalisés via une fonction softmax pour obtenir des poids qui somment à 1\. Ces poids déterminent l'importance relative de chaque élément de la séquence.

3. **Calcul de la sortie pondérée** : En utilisant ces poids d'attention, on calcule une somme pondérée des éléments de la séquence d'entrée. Cela donne une représentation de l'entrée, où les éléments les plus pertinents ont une plus grande influence.

### **L'attention dans les Transformers**

Le modèle Transformer, introduit dans le papier **"Attention is All You Need"**, repose entièrement sur des mécanismes d'attention, sans recourir à des architectures récurrentes comme les RNNs. Dans un Transformer, l'attention est utilisée à la fois pour encoder et pour décoder les séquences d'entrée et de sortie. Voici les deux types principaux d'attention utilisés dans un Transformer :

1. **Self-attention (ou intra-attention)** : Chaque élément de la séquence d'entrée accorde de l'attention à tous les autres éléments de la séquence. Cela permet au modèle de capturer les dépendances contextuelles entre les éléments de la séquence. Par exemple, dans une phrase, le mot "banque" pourrait se référer à une institution financière ou à la rive d'un fleuve, et le modèle pourrait utiliser la self-attention pour distinguer le sens correct selon le contexte.

2. **Attention encodage-décodage** : Dans la phase de décodage, l'attention est utilisée pour relier l'entrée et la sortie. Par exemple, dans la traduction automatique, l'attention permet au modèle de se concentrer sur les mots clés de la phrase source lorsqu'il génère la traduction.

### **Avantages des modèles d'attention**

Les mécanismes d'attention offrent plusieurs avantages qui les rendent particulièrement efficaces pour de nombreuses tâches :

* **Capturer les dépendances longues** : Contrairement aux RNNs ou LSTM, les modèles d'attention peuvent se concentrer directement sur des éléments spécifiques de la séquence, qu'ils soient proches ou éloignés dans la séquence, ce qui permet de mieux capturer les relations à long terme.

* **Parallélisation** : Contrairement aux RNNs, qui traitent les séquences élément par élément, l'attention permet de traiter toutes les positions d'une séquence en parallèle, ce qui accélère l'entraînement.

* **Flexibilité** : Le mécanisme d'attention peut être facilement intégré dans différents types d'architectures, y compris les réseaux de neurones convolutifs (CNN) et les réseaux récurrents (RNN).

### **Applications des modèles d'attention**

Les mécanismes d'attention ont été appliqués avec succès dans divers domaines du deep learning, notamment :

* **Traduction automatique** : Le modèle Transformer, qui repose entièrement sur l'attention, a largement remplacé les modèles basés sur RNNs et LSTM pour la traduction de texte entre langues.

* **Compréhension du langage naturel** : Les modèles comme BERT (Bidirectional Encoder Representations from Transformers) utilisent l'attention pour comprendre le contexte de chaque mot dans une phrase, ce qui est crucial pour des tâches comme l'analyse de sentiment, la réponse aux questions et la classification de texte.

* **Vision par ordinateur** : L'attention est également utilisée dans des architectures de type Vision Transformer (ViT), qui appliquent des mécanismes d'attention à des images en traitant celles-ci comme des séquences de "patches" d'images.

* **Résumé automatique** : L'attention aide à identifier les parties les plus importantes d'un texte pour générer un résumé significatif.

Les **modèles d'attention** ont transformé le domaine du deep learning, notamment pour le traitement des séquences. Grâce à leur capacité à se concentrer sur les parties les plus pertinentes des données d'entrée, ils permettent de traiter efficacement des dépendances à long terme et d'améliorer les performances des modèles. L'introduction de modèles comme les **Transformers** a permis d'atteindre des résultats remarquables dans des domaines variés comme la traduction, la compréhension du langage et la vision par ordinateur.

![][image45]

Image extraite de : [https://www.geeksforgeeks.org/self-attention-in-nlp/](https://www.geeksforgeeks.org/self-attention-in-nlp/)

#### **Liens Externes (Youtube, Medium, etc):**

* [Recurrent Neural Network (RNN)](https://medium.com/@RobuRishabh/recurrent-neural-network-rnn-8412b9abd755)  
* [Qu’est-ce qu’un RNN (réseau neuronal récurrent) ?](https://aws.amazon.com/fr/what-is/recurrent-neural-network/)  
* [Understanding LSTM: Architecture, Pros and Cons, and Implementation](https://medium.com/@anishnama20/understanding-lstm-architecture-pros-and-cons-and-implementation-3e0cca194094)  
* [Long Short-Term Memory : réseaux à mémoire longue](https://www.ionos.fr/digitalguide/sites-internet/developpement-web/long-short-term-memory/#:~:text=Long%20Short%2DTerm%20Memory%20\(LSTM,importantes%20sur%20le%20long%20terme.)  
* [Understanding Gated Recurrent Unit (GRU) in Deep Learning](https://medium.com/@anishnama20/understanding-gated-recurrent-unit-gru-in-deep-learning-2e54923f3e2)  
* [Qu’est-ce qu’une Gated Recurrent Unit (GRU) ?](https://www.intelligence-artificielle-school.com/ecole/technologies/gated-recurrent-unit/)  
* [What is Attention-Based Neural Networks?](https://www.aimasterclass.com/glossary/attention-based-neural-networks)  
* [Le Mécanisme de l’Attention en Deep Learning – Comprendre Rapidement](https://inside-machinelearning.com/mecanisme-attention/)

#### **Bibliographie**

* Schmidt, R.M., 2019\. Recurrent neural networks (rnns): A gentle introduction and overview. *arXiv preprint arXiv:1912.05911*.  
* Hochreiter, S. and Schmidhuber, J., 1997\. Long short-term memory. *Neural computation*, *9*(8), pp.1735-1780.  
* Dey, R. and Salem, F.M., 2017, August. Gate-variants of gated recurrent unit (GRU) neural networks. In *2017 IEEE 60th international midwest symposium on circuits and systems (MWSCAS)* (pp. 1597-1600). IEEE.  
* Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, Ł. and Polosukhin, I., 2017\. Attention is all you need. *Advances in neural information processing systems*, *30*.