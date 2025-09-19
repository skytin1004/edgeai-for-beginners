<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-15T17:25:27+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "fr"
}
-->
# Guide de développement Edge AI avec AI Toolkit pour Visual Studio Code

## Introduction

Bienvenue dans le guide complet pour utiliser AI Toolkit avec Visual Studio Code dans le développement Edge AI. Alors que l'intelligence artificielle évolue du cloud centralisé vers des dispositifs edge distribués, les développeurs ont besoin d'outils puissants et intégrés capables de relever les défis uniques du déploiement edge - des contraintes de ressources aux exigences de fonctionnement hors ligne.

AI Toolkit pour Visual Studio Code comble cet écart en offrant un environnement de développement complet spécialement conçu pour créer, tester et optimiser des applications d'IA fonctionnant efficacement sur des dispositifs edge. Que vous développiez pour des capteurs IoT, des appareils mobiles, des systèmes embarqués ou des serveurs edge, cet outil simplifie l'ensemble de votre flux de travail de développement dans l'environnement familier de VS Code.

Ce guide vous accompagnera à travers les concepts essentiels, les outils et les meilleures pratiques pour exploiter AI Toolkit dans vos projets Edge AI, depuis la sélection initiale des modèles jusqu'au déploiement en production.

## Vue d'ensemble

AI Toolkit fournit un environnement de développement intégré pour le cycle de vie complet des applications Edge AI dans VS Code. Il offre une intégration transparente avec des modèles d'IA populaires de fournisseurs tels que OpenAI, Anthropic, Google et GitHub, tout en prenant en charge le déploiement local de modèles via ONNX et Ollama - des capacités cruciales pour les applications Edge AI nécessitant une inférence sur appareil.

Ce qui distingue AI Toolkit pour le développement Edge AI, c'est son focus sur l'ensemble du pipeline de déploiement edge. Contrairement aux outils traditionnels de développement d'IA qui ciblent principalement le déploiement cloud, AI Toolkit inclut des fonctionnalités spécialisées pour l'optimisation des modèles, les tests sous contraintes de ressources et l'évaluation des performances spécifiques au edge. L'outil comprend que le développement Edge AI nécessite des considérations différentes - des modèles plus petits, des temps d'inférence plus rapides, des capacités hors ligne et des optimisations spécifiques au matériel.

La plateforme prend en charge plusieurs scénarios de déploiement, allant de l'inférence simple sur appareil à des architectures edge complexes multi-modèles. Elle fournit des outils pour la conversion, la quantification et l'optimisation des modèles, essentiels pour un déploiement edge réussi, tout en maintenant la productivité des développeurs que VS Code est réputé offrir.

## Objectifs d'apprentissage

À la fin de ce guide, vous serez capable de :

### Compétences de base
- **Installer et configurer** AI Toolkit pour Visual Studio Code pour les flux de travail de développement Edge AI
- **Naviguer et utiliser** l'interface AI Toolkit, y compris le catalogue de modèles, le Playground et l'Agent Builder
- **Sélectionner et évaluer** des modèles d'IA adaptés au déploiement edge en fonction des performances et des contraintes de ressources
- **Convertir et optimiser** des modèles en utilisant le format ONNX et des techniques de quantification pour les dispositifs edge

### Compétences en développement Edge AI
- **Concevoir et implémenter** des applications Edge AI en utilisant l'environnement de développement intégré
- **Tester des modèles** dans des conditions similaires au edge en utilisant l'inférence locale et la surveillance des ressources
- **Créer et personnaliser** des agents d'IA optimisés pour les scénarios de déploiement edge
- **Évaluer les performances des modèles** en utilisant des métriques pertinentes pour le calcul edge (latence, utilisation mémoire, précision)

### Optimisation et déploiement
- **Appliquer des techniques de quantification et de pruning** pour réduire la taille des modèles tout en maintenant des performances acceptables
- **Optimiser les modèles** pour des plateformes matérielles edge spécifiques, y compris l'accélération CPU, GPU et NPU
- **Mettre en œuvre les meilleures pratiques** pour le développement Edge AI, y compris la gestion des ressources et les stratégies de secours
- **Préparer les modèles et les applications** pour le déploiement en production sur des dispositifs edge

### Concepts avancés de Edge AI
- **Intégrer avec des frameworks Edge AI** tels que ONNX Runtime, Windows ML et TensorFlow Lite
- **Implémenter des architectures multi-modèles** et des scénarios d'apprentissage fédéré pour les environnements edge
- **Résoudre les problèmes courants de Edge AI** tels que les contraintes de mémoire, la vitesse d'inférence et la compatibilité matérielle
- **Concevoir des stratégies de surveillance et de journalisation** pour les applications Edge AI en production

### Application pratique
- **Construire des solutions Edge AI de bout en bout** depuis la sélection des modèles jusqu'au déploiement
- **Démontrer une maîtrise** des flux de travail de développement spécifiques au edge et des techniques d'optimisation
- **Appliquer les concepts appris** à des cas d'utilisation Edge AI réels, y compris IoT, mobile et applications embarquées
- **Évaluer et comparer** différentes stratégies de déploiement Edge AI et leurs compromis

## Fonctionnalités clés pour le développement Edge AI

### 1. Catalogue de modèles et découverte
- **Support des modèles locaux** : Découvrir et accéder à des modèles d'IA spécifiquement optimisés pour le déploiement edge
- **Intégration ONNX** : Accéder à des modèles au format ONNX pour une inférence edge efficace
- **Support Ollama** : Exploiter des modèles fonctionnant localement via Ollama pour la confidentialité et le fonctionnement hors ligne
- **Comparaison de modèles** : Comparer les modèles côte à côte pour trouver le meilleur équilibre entre performances et consommation de ressources pour les dispositifs edge

### 2. Playground interactif
- **Environnement de test local** : Tester les modèles localement avant le déploiement edge
- **Expérimentation multimodale** : Tester avec des images, du texte et d'autres entrées typiques des scénarios edge
- **Réglage des paramètres** : Expérimenter avec différents paramètres de modèles pour optimiser les contraintes edge
- **Surveillance des performances en temps réel** : Observer la vitesse d'inférence et l'utilisation des ressources pendant le développement

### 3. Agent Builder pour les applications edge
- **Conception de prompts** : Créer des prompts optimisés fonctionnant efficacement avec des modèles edge plus petits
- **Intégration des outils MCP** : Intégrer des outils Model Context Protocol pour des capacités améliorées des agents edge
- **Génération de code** : Générer du code prêt pour la production optimisé pour les scénarios de déploiement edge
- **Sorties structurées** : Concevoir des agents fournissant des réponses cohérentes et structurées adaptées aux applications edge

### 4. Évaluation et test des modèles
- **Métriques de performance** : Évaluer les modèles en utilisant des métriques pertinentes pour le déploiement edge (latence, utilisation mémoire, précision)
- **Tests par lots** : Tester simultanément plusieurs configurations de modèles pour trouver les paramètres edge optimaux
- **Évaluation personnalisée** : Créer des critères d'évaluation personnalisés spécifiques aux cas d'utilisation Edge AI
- **Profilage des ressources** : Analyser les besoins en mémoire et en calcul pour la planification du déploiement edge

### 5. Conversion et optimisation des modèles
- **Conversion ONNX** : Convertir des modèles de divers formats en ONNX pour la compatibilité edge
- **Quantification** : Réduire la taille des modèles et améliorer la vitesse d'inférence grâce à des techniques de quantification
- **Optimisation matérielle** : Optimiser les modèles pour des matériels edge spécifiques (CPU, GPU, NPU)
- **Transformation de format** : Transformer des modèles de Hugging Face et d'autres sources pour le déploiement edge

### 6. Ajustement pour les scénarios edge
- **Adaptation au domaine** : Personnaliser les modèles pour des cas d'utilisation et des environnements edge spécifiques
- **Entraînement local** : Entraîner des modèles localement avec support GPU pour des exigences spécifiques au edge
- **Intégration Azure** : Exploiter Azure Container Apps pour un ajustement basé sur le cloud avant le déploiement edge
- **Apprentissage par transfert** : Adapter des modèles pré-entraînés pour des tâches et des contraintes spécifiques au edge

### 7. Surveillance des performances et traçage
- **Analyse des performances edge** : Surveiller les performances des modèles dans des conditions similaires au edge
- **Collecte de traces** : Collecter des données de performance détaillées pour l'optimisation
- **Identification des goulots d'étranglement** : Identifier les problèmes de performance avant le déploiement sur les dispositifs edge
- **Suivi de l'utilisation des ressources** : Surveiller la mémoire, le CPU et le temps d'inférence pour l'optimisation edge

## Flux de travail de développement Edge AI

### Phase 1 : Découverte et sélection des modèles
1. **Explorer le catalogue de modèles** : Utiliser le catalogue pour trouver des modèles adaptés au déploiement edge
2. **Comparer les performances** : Évaluer les modèles en fonction de leur taille, précision et vitesse d'inférence
3. **Tester localement** : Utiliser Ollama ou des modèles ONNX pour tester localement avant le déploiement edge
4. **Évaluer les besoins en ressources** : Déterminer les besoins en mémoire et en calcul pour les dispositifs edge cibles

### Phase 2 : Optimisation des modèles
1. **Convertir en ONNX** : Convertir les modèles sélectionnés au format ONNX pour la compatibilité edge
2. **Appliquer la quantification** : Réduire la taille des modèles via la quantification INT8 ou INT4
3. **Optimisation matérielle** : Optimiser pour le matériel edge cible (ARM, x86, accélérateurs spécialisés)
4. **Validation des performances** : Valider que les modèles optimisés maintiennent une précision acceptable

### Phase 3 : Développement d'applications
1. **Conception d'agents** : Utiliser Agent Builder pour créer des agents d'IA optimisés pour le edge
2. **Conception de prompts** : Développer des prompts fonctionnant efficacement avec des modèles plus petits
3. **Tests d'intégration** : Tester les agents dans des conditions simulées similaires au edge
4. **Génération de code** : Générer du code de production optimisé pour le déploiement edge

### Phase 4 : Évaluation et test
1. **Évaluation par lots** : Tester plusieurs configurations pour trouver les paramètres edge optimaux
2. **Profilage des performances** : Analyser la vitesse d'inférence, l'utilisation mémoire et la précision
3. **Simulation edge** : Tester dans des conditions similaires à l'environnement de déploiement edge cible
4. **Tests de résistance** : Évaluer les performances sous diverses conditions de charge

### Phase 5 : Préparation au déploiement
1. **Optimisation finale** : Appliquer les optimisations finales basées sur les résultats des tests
2. **Packaging pour le déploiement** : Préparer les modèles et le code pour le déploiement edge
3. **Documentation** : Documenter les exigences de déploiement et la configuration
4. **Configuration de la surveillance** : Préparer la surveillance et la journalisation pour le déploiement en production

## Public cible pour le développement Edge AI

### Développeurs Edge AI
- Développeurs d'applications créant des dispositifs edge et des solutions IoT alimentés par l'IA
- Développeurs de systèmes embarqués intégrant des capacités d'IA dans des dispositifs à ressources limitées
- Développeurs mobiles créant des applications d'IA sur appareil pour smartphones et tablettes

### Ingénieurs Edge AI
- Ingénieurs IA optimisant les modèles pour le déploiement edge et gérant les pipelines d'inférence
- Ingénieurs DevOps déployant et gérant des modèles d'IA sur une infrastructure edge distribuée
- Ingénieurs en performance optimisant les charges de travail IA pour les contraintes matérielles edge

### Chercheurs et éducateurs
- Chercheurs en IA développant des modèles et algorithmes efficaces pour le calcul edge
- Éducateurs enseignant les concepts Edge AI et démontrant des techniques d'optimisation
- Étudiants apprenant les défis et solutions du déploiement Edge AI

## Cas d'utilisation Edge AI

### Dispositifs IoT intelligents
- **Reconnaissance d'images en temps réel** : Déployer des modèles de vision par ordinateur sur des caméras et capteurs IoT
- **Traitement vocal** : Implémenter la reconnaissance vocale et le traitement du langage naturel sur des enceintes intelligentes
- **Maintenance prédictive** : Exécuter des modèles de détection d'anomalies sur des dispositifs industriels edge
- **Surveillance environnementale** : Déployer des modèles d'analyse de données de capteurs pour des applications environnementales

### Applications mobiles et embarquées
- **Traduction sur appareil** : Implémenter des modèles de traduction linguistique fonctionnant hors ligne
- **Réalité augmentée** : Déployer la reconnaissance et le suivi d'objets en temps réel pour des applications AR
- **Surveillance de la santé** : Exécuter des modèles d'analyse de santé sur des dispositifs portables et équipements médicaux
- **Systèmes autonomes** : Implémenter des modèles de prise de décision pour drones, robots et véhicules

### Infrastructure de calcul edge
- **Centres de données edge** : Déployer des modèles d'IA dans des centres de données edge pour des applications à faible latence
- **Intégration CDN** : Intégrer des capacités de traitement IA dans des réseaux de diffusion de contenu
- **Edge 5G** : Exploiter le calcul edge 5G pour des applications alimentées par l'IA
- **Fog Computing** : Implémenter le traitement IA dans des environnements de fog computing

## Installation et configuration

### Installation rapide
Installez l'extension AI Toolkit directement depuis le Visual Studio Code Marketplace :

```
Install: AI Toolkit for Visual Studio Code (ms-windows-ai-studio.windows-ai-studio)
```

### Prérequis pour le développement Edge AI
- **ONNX Runtime** : Installer ONNX Runtime pour l'inférence des modèles
- **Ollama** (optionnel) : Installer Ollama pour le service de modèles locaux
- **Environnement Python** : Configurer Python avec les bibliothèques d'IA nécessaires
- **Outils matériels edge** : Installer des outils de développement spécifiques au matériel (CUDA, OpenVINO, etc.)

### Configuration initiale
1. Ouvrez VS Code et installez l'extension AI Toolkit
2. Configurez les sources de modèles (ONNX, Ollama, fournisseurs cloud)
3. Configurez l'environnement de développement local pour les tests edge
4. Configurez les options d'accélération matérielle pour votre machine de développement

## Premiers pas avec le développement Edge AI

### Étape 1 : Sélection des modèles
1. Ouvrez la vue AI Toolkit dans la barre d'activités
2. Parcourez le catalogue de modèles pour trouver des modèles compatibles edge
3. Filtrez par taille de modèle, format (ONNX) et caractéristiques de performance
4. Comparez les modèles en utilisant les outils de comparaison intégrés

### Étape 2 : Tests locaux
1. Utilisez le Playground pour tester les modèles sélectionnés localement
2. Expérimentez avec différents prompts et paramètres
3. Surveillez les métriques de performance pendant les tests
4. Évaluez les réponses des modèles pour les exigences des cas d'utilisation edge

### Étape 3 : Optimisation des modèles
1. Utilisez les outils de conversion de modèles pour optimiser le déploiement edge
2. Appliquez la quantification pour réduire la taille des modèles
3. Testez les modèles optimisés pour garantir des performances acceptables
4. Documentez les paramètres d'optimisation et les compromis de performance

### Étape 4 : Développement d'agents
1. Utilisez Agent Builder pour créer des agents d'IA optimisés pour le edge
2. Développez des prompts fonctionnant efficacement avec des modèles plus petits
3. Intégrez les outils et API nécessaires pour les scénarios edge
4. Testez les agents dans des conditions simulées similaires au edge

### Étape 5 : Évaluation et déploiement
1. Utilisez l'évaluation en masse pour tester plusieurs configurations
2. Profilez les performances dans diverses conditions
3. Préparez les packages de déploiement pour les dispositifs edge cibles
4. Configurez la surveillance et la journalisation pour le déploiement en production

## Meilleures pratiques pour le développement Edge AI

### Sélection des modèles
- **Contraintes de taille** : Choisissez des modèles adaptés aux limitations de mémoire des dispositifs cibles
- **Vitesse d'inférence** : Priorisez les modèles avec des temps d'inférence rapides pour les applications en temps réel
- **Compromis de précision** : Équilibrez la précision des modèles avec les contraintes de ressources
- **Compatibilité de format** : Préférez les formats ONNX ou optimisés pour le matériel pour le déploiement edge

### Techniques d'optimisation
- **Quantification** : Utilisez la quantification INT8 ou INT4 pour réduire la taille des modèles et améliorer la vitesse
- **Pruning** : Supprimez les paramètres de modèle inutiles pour réduire les besoins en calcul
- **Distillation de connaissances** : Créez des modèles plus petits qui maintiennent les performances des modèles plus grands
- **Accélération matérielle** : Exploitez les NPUs, GPUs ou accélérateurs spécialisés lorsque disponibles

### Flux de travail de développement
- **Tests itératifs** : Testez fréquemment dans des conditions similaires au edge pendant le développement
- **Surveillance des performances** : Surveillez en continu l'utilisation des ressources et la vitesse d'inférence
- **Gestion des versions** : Suivez les versions des modèles et les paramètres d'optimisation
- **Documentation** : Documentez toutes les décisions d'optimisation et les compromis de performance

### Considérations de déploiement
- **Surveillance des ressources** : Surveillez la mémoire, le CPU et la consommation d'énergie en production
- **Stratégies de secours** : Implémentez des mécanismes de secours en cas de défaillance des modèles
- **Mécanismes de mise à jour** : Planifiez les mises à jour des modèles et la gestion des versions
- **Sécurité** : Implémentez des mesures de sécurité appropriées pour les applications d'IA en périphérie.

## Intégration avec les frameworks d'IA en périphérie

### ONNX Runtime
- **Déploiement multiplateforme** : Déployez des modèles ONNX sur différentes plateformes en périphérie.
- **Optimisation matérielle** : Exploitez les optimisations spécifiques au matériel d'ONNX Runtime.
- **Support mobile** : Utilisez ONNX Runtime Mobile pour les applications sur smartphones et tablettes.
- **Intégration IoT** : Déployez sur des appareils IoT grâce aux distributions légères d'ONNX Runtime.

### Windows ML
- **Appareils Windows** : Optimisez pour les appareils en périphérie et les PC basés sur Windows.
- **Accélération NPU** : Exploitez les unités de traitement neuronal sur les appareils Windows.
- **DirectML** : Utilisez DirectML pour l'accélération GPU sur les plateformes Windows.
- **Intégration UWP** : Intégrez avec les applications de la plateforme universelle Windows.

### TensorFlow Lite
- **Optimisation mobile** : Déployez des modèles TensorFlow Lite sur des appareils mobiles et embarqués.
- **Délégués matériels** : Utilisez des délégués matériels spécialisés pour l'accélération.
- **Microcontrôleurs** : Déployez sur des microcontrôleurs avec TensorFlow Lite Micro.
- **Support multiplateforme** : Déployez sur Android, iOS et systèmes Linux embarqués.

### Azure IoT Edge
- **Hybride cloud-périphérie** : Combinez l'entraînement dans le cloud avec l'inférence en périphérie.
- **Déploiement de modules** : Déployez des modèles d'IA sous forme de modules IoT Edge.
- **Gestion des appareils** : Gérez les appareils en périphérie et les mises à jour des modèles à distance.
- **Télémétrie** : Collectez des données de performance et des métriques de modèles depuis les déploiements en périphérie.

## Scénarios avancés d'IA en périphérie

### Déploiement multi-modèles
- **Ensembles de modèles** : Déployez plusieurs modèles pour améliorer la précision ou la redondance.
- **Tests A/B** : Testez différents modèles simultanément sur des appareils en périphérie.
- **Sélection dynamique** : Choisissez les modèles en fonction des conditions actuelles de l'appareil.
- **Partage des ressources** : Optimisez l'utilisation des ressources entre plusieurs modèles déployés.

### Apprentissage fédéré
- **Entraînement distribué** : Entraînez des modèles sur plusieurs appareils en périphérie.
- **Préservation de la vie privée** : Gardez les données d'entraînement locales tout en partageant les améliorations des modèles.
- **Apprentissage collaboratif** : Permettez aux appareils d'apprendre des expériences collectives.
- **Coordination périphérie-cloud** : Coordonnez l'apprentissage entre les appareils en périphérie et l'infrastructure cloud.

### Traitement en temps réel
- **Traitement en flux** : Traitez des flux de données continus sur des appareils en périphérie.
- **Inférence à faible latence** : Optimisez pour une latence minimale lors de l'inférence.
- **Traitement par lots** : Traitez efficacement des lots de données sur des appareils en périphérie.
- **Traitement adaptatif** : Ajustez le traitement en fonction des capacités actuelles de l'appareil.

## Résolution des problèmes de développement d'IA en périphérie

### Problèmes courants
- **Contraintes de mémoire** : Modèle trop volumineux pour la mémoire de l'appareil cible.
- **Vitesse d'inférence** : Inférence du modèle trop lente pour les exigences en temps réel.
- **Dégradation de la précision** : L'optimisation réduit la précision du modèle de manière inacceptable.
- **Compatibilité matérielle** : Modèle incompatible avec le matériel cible.

### Stratégies de débogage
- **Profilage des performances** : Utilisez les fonctionnalités de traçage de l'AI Toolkit pour identifier les goulots d'étranglement.
- **Surveillance des ressources** : Surveillez l'utilisation de la mémoire et du CPU pendant le développement.
- **Tests incrémentaux** : Testez les optimisations de manière incrémentale pour isoler les problèmes.
- **Simulation matérielle** : Utilisez des outils de développement pour simuler le matériel cible.

### Solutions d'optimisation
- **Quantification supplémentaire** : Appliquez des techniques de quantification plus agressives.
- **Architecture de modèle** : Envisagez des architectures de modèles différentes optimisées pour la périphérie.
- **Optimisation du prétraitement** : Optimisez le prétraitement des données pour les contraintes en périphérie.
- **Optimisation de l'inférence** : Utilisez des optimisations spécifiques au matériel pour l'inférence.

## Ressources et prochaines étapes

### Documentation
- [Guide des modèles AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/models)
- [Documentation du Model Playground](https://code.visualstudio.com/docs/intelligentapps/playground)
- [Documentation ONNX Runtime](https://onnxruntime.ai/)
- [Documentation Windows ML](https://docs.microsoft.com/en-us/windows/ai/)

### Communauté et support
- [GitHub AI Toolkit pour VS Code](https://github.com/microsoft/vscode-ai-toolkit)
- [Communauté ONNX](https://github.com/onnx/onnx)
- [Communauté des développeurs Edge AI](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [Marketplace des extensions VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Ressources d'apprentissage
- [Cours sur les fondamentaux de l'IA en périphérie](./Module01/README.md)
- [Guide des petits modèles linguistiques](./Module02/README.md)
- [Stratégies de déploiement en périphérie](./Module03/README.md)
- [Développement d'IA en périphérie sous Windows](./windowdeveloper.md)

## Conclusion

AI Toolkit pour Visual Studio Code offre une plateforme complète pour le développement d'IA en périphérie, allant de la découverte et l'optimisation des modèles au déploiement et à la surveillance. En exploitant ses outils intégrés et ses flux de travail, les développeurs peuvent créer, tester et déployer efficacement des applications d'IA fonctionnant sur des appareils en périphérie avec des ressources limitées.

Le support du toolkit pour ONNX, Ollama et divers fournisseurs cloud, combiné à ses capacités d'optimisation et d'évaluation, en fait un choix idéal pour le développement d'IA en périphérie. Que vous construisiez des applications IoT, des fonctionnalités d'IA mobile ou des systèmes d'intelligence embarquée, AI Toolkit fournit les outils et les flux de travail nécessaires pour un déploiement réussi d'IA en périphérie.

Alors que l'IA en périphérie continue d'évoluer, AI Toolkit pour VS Code reste à la pointe, offrant aux développeurs des outils et des capacités de pointe pour créer la prochaine génération d'applications intelligentes en périphérie.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.