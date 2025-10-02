<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "65a22ed38b95f334dd8a893bf2c55806",
  "translation_date": "2025-10-02T10:48:28+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "fr"
}
-->
# Guide de développement Edge AI avec AI Toolkit pour Visual Studio Code

## Introduction

Bienvenue dans ce guide complet pour utiliser AI Toolkit dans Visual Studio Code pour le développement Edge AI. Alors que l'intelligence artificielle évolue du cloud centralisé vers des dispositifs distribués en périphérie, les développeurs ont besoin d'outils puissants et intégrés capables de relever les défis uniques du déploiement en périphérie, tels que les contraintes de ressources et les exigences de fonctionnement hors ligne.

AI Toolkit pour Visual Studio Code comble cet écart en offrant un environnement de développement complet spécialement conçu pour créer, tester et optimiser des applications d'IA fonctionnant efficacement sur des dispositifs en périphérie. Que vous développiez pour des capteurs IoT, des appareils mobiles, des systèmes embarqués ou des serveurs en périphérie, cet outil rationalise l'ensemble de votre flux de travail de développement dans l'environnement familier de VS Code.

Ce guide vous accompagnera à travers les concepts essentiels, les outils et les meilleures pratiques pour exploiter AI Toolkit dans vos projets Edge AI, depuis la sélection initiale du modèle jusqu'au déploiement en production.

## Vue d'ensemble

AI Toolkit pour Visual Studio Code est une extension puissante qui simplifie le développement d'agents et la création d'applications d'IA. L'outil offre des capacités complètes pour explorer, évaluer et déployer des modèles d'IA provenant d'une large gamme de fournisseurs, notamment Anthropic, OpenAI, GitHub, Google, tout en prenant en charge l'exécution locale des modèles via ONNX et Ollama.

Ce qui distingue AI Toolkit, c'est son approche complète du cycle de vie du développement d'IA. Contrairement aux outils traditionnels qui se concentrent sur des aspects spécifiques, AI Toolkit fournit un environnement intégré couvrant la découverte de modèles, l'expérimentation, le développement d'agents, l'évaluation et le déploiement, le tout dans l'environnement familier de VS Code.

La plateforme est spécialement conçue pour le prototypage rapide et le déploiement en production, avec des fonctionnalités telles que la génération de prompts, des démarrages rapides, des intégrations fluides avec MCP (Model Context Protocol) et des capacités d'évaluation étendues. Pour le développement Edge AI, cela signifie que vous pouvez développer, tester et optimiser efficacement des applications d'IA pour des scénarios de déploiement en périphérie tout en maintenant un flux de travail complet dans VS Code.

## Objectifs d'apprentissage

À la fin de ce guide, vous serez capable de :

### Compétences de base
- **Installer et configurer** AI Toolkit pour Visual Studio Code pour les flux de travail de développement Edge AI
- **Naviguer et utiliser** l'interface AI Toolkit, y compris le catalogue de modèles, le Playground et l'Agent Builder
- **Sélectionner et évaluer** des modèles d'IA adaptés au déploiement en périphérie en fonction des performances et des contraintes de ressources
- **Convertir et optimiser** des modèles au format ONNX et appliquer des techniques de quantification pour les dispositifs en périphérie

### Compétences en développement Edge AI
- **Concevoir et implémenter** des applications Edge AI en utilisant l'environnement de développement intégré
- **Tester les modèles** dans des conditions similaires à celles de la périphérie en utilisant l'inférence locale et la surveillance des ressources
- **Créer et personnaliser** des agents d'IA optimisés pour les scénarios de déploiement en périphérie
- **Évaluer les performances des modèles** en utilisant des métriques pertinentes pour l'informatique en périphérie (latence, utilisation de la mémoire, précision)

### Optimisation et déploiement
- **Appliquer des techniques de quantification et d'élagage** pour réduire la taille des modèles tout en maintenant des performances acceptables
- **Optimiser les modèles** pour des plateformes matérielles spécifiques en périphérie, y compris l'accélération CPU, GPU et NPU
- **Mettre en œuvre les meilleures pratiques** pour le développement Edge AI, y compris la gestion des ressources et les stratégies de repli
- **Préparer les modèles et les applications** pour le déploiement en production sur des dispositifs en périphérie

### Concepts avancés en Edge AI
- **Intégrer avec des frameworks Edge AI** tels que ONNX Runtime, Windows ML et TensorFlow Lite
- **Implémenter des architectures multi-modèles** et des scénarios d'apprentissage fédéré pour les environnements en périphérie
- **Résoudre les problèmes courants en Edge AI** tels que les contraintes de mémoire, la vitesse d'inférence et la compatibilité matérielle
- **Concevoir des stratégies de surveillance et de journalisation** pour les applications Edge AI en production

### Application pratique
- **Construire des solutions Edge AI de bout en bout** depuis la sélection du modèle jusqu'au déploiement
- **Démontrer une maîtrise** des flux de travail de développement spécifiques à la périphérie et des techniques d'optimisation
- **Appliquer les concepts appris** à des cas d'utilisation réels en Edge AI, y compris les applications IoT, mobiles et embarquées
- **Évaluer et comparer** différentes stratégies de déploiement Edge AI et leurs compromis

## Fonctionnalités clés pour le développement Edge AI

### 1. Catalogue de modèles et découverte
- **Support multi-fournisseurs** : Parcourez et accédez à des modèles d'IA provenant d'Anthropic, OpenAI, GitHub, Google et d'autres fournisseurs
- **Intégration de modèles locaux** : Découverte simplifiée des modèles ONNX et Ollama pour le déploiement en périphérie
- **Modèles GitHub** : Intégration directe avec l'hébergement de modèles GitHub pour un accès simplifié
- **Comparaison de modèles** : Comparez les modèles côte à côte pour trouver un équilibre optimal pour les contraintes des dispositifs en périphérie

### 2. Playground interactif
- **Environnement de test interactif** : Expérimentation rapide avec les capacités des modèles dans un environnement contrôlé
- **Support multi-modal** : Testez avec des images, du texte et d'autres entrées typiques des scénarios en périphérie
- **Expérimentation en temps réel** : Retour immédiat sur les réponses et les performances des modèles
- **Optimisation des paramètres** : Affinez les paramètres des modèles pour répondre aux exigences du déploiement en périphérie

### 3. Générateur de prompts (Agent Builder)
- **Génération en langage naturel** : Créez des prompts de démarrage à partir de descriptions en langage naturel
- **Affinement itératif** : Améliorez les prompts en fonction des réponses et des performances des modèles
- **Décomposition des tâches** : Divisez les tâches complexes avec des chaînes de prompts et des sorties structurées
- **Support des variables** : Utilisez des variables dans les prompts pour un comportement dynamique des agents
- **Génération de code de production** : Produisez du code prêt pour la production pour un développement rapide d'applications

### 4. Exécution en masse et évaluation
- **Test multi-modèles** : Exécutez plusieurs prompts sur des modèles sélectionnés simultanément
- **Tests efficaces à grande échelle** : Testez diverses entrées et configurations de manière efficace
- **Cas de test personnalisés** : Exécutez des agents avec des cas de test pour valider leur fonctionnalité
- **Comparaison des performances** : Comparez les résultats entre différents modèles et configurations

### 5. Évaluation des modèles avec des ensembles de données
- **Métriques standard** : Testez les modèles d'IA avec des évaluateurs intégrés (score F1, pertinence, similarité, cohérence)
- **Évaluateurs personnalisés** : Créez vos propres métriques d'évaluation pour des cas d'utilisation spécifiques
- **Intégration d'ensembles de données** : Testez les modèles avec des ensembles de données complets
- **Mesure des performances** : Quantifiez les performances des modèles pour les décisions de déploiement en périphérie

### 6. Capacités de fine-tuning
- **Personnalisation des modèles** : Adaptez les modèles à des cas d'utilisation et des domaines spécifiques
- **Adaptation spécialisée** : Ajustez les modèles pour répondre à des exigences et des domaines spécialisés
- **Optimisation pour la périphérie** : Affinez les modèles spécifiquement pour les contraintes de déploiement en périphérie
- **Entraînement spécifique au domaine** : Créez des modèles adaptés à des cas d'utilisation spécifiques en périphérie

### 7. Intégration avec les outils MCP
- **Connectivité avec des outils externes** : Connectez les agents à des outils externes via des serveurs Model Context Protocol
- **Actions dans le monde réel** : Permettez aux agents d'interroger des bases de données, d'accéder à des API ou d'exécuter une logique personnalisée
- **Serveurs MCP existants** : Utilisez des outils via des protocoles de commande (stdio) ou HTTP (événements envoyés par le serveur)
- **Développement MCP personnalisé** : Construisez et configurez de nouveaux serveurs MCP avec des tests dans l'Agent Builder

### 8. Développement et test d'agents
- **Support des appels de fonctions** : Permettez aux agents d'invoquer dynamiquement des fonctions externes
- **Tests d'intégration en temps réel** : Testez les intégrations avec des exécutions en temps réel et l'utilisation d'outils
- **Versionnage des agents** : Contrôle de version pour les agents avec des capacités de comparaison des résultats d'évaluation
- **Débogage et traçage** : Capacités de traçage et de débogage local pour le développement d'agents

## Flux de travail pour le développement Edge AI

### Phase 1 : Découverte et sélection de modèles
1. **Explorer le catalogue de modèles** : Utilisez le catalogue pour trouver des modèles adaptés au déploiement en périphérie
2. **Comparer les performances** : Évaluez les modèles en fonction de leur taille, précision et vitesse d'inférence
3. **Tester localement** : Utilisez des modèles Ollama ou ONNX pour des tests locaux avant le déploiement en périphérie
4. **Évaluer les besoins en ressources** : Déterminez les besoins en mémoire et en calcul pour les dispositifs en périphérie ciblés

### Phase 2 : Optimisation des modèles
1. **Convertir en ONNX** : Convertissez les modèles sélectionnés au format ONNX pour la compatibilité en périphérie
2. **Appliquer la quantification** : Réduisez la taille des modèles grâce à la quantification INT8 ou INT4
3. **Optimisation matérielle** : Optimisez pour le matériel en périphérie ciblé (ARM, x86, accélérateurs spécialisés)
4. **Validation des performances** : Vérifiez que les modèles optimisés maintiennent une précision acceptable

### Phase 3 : Développement d'applications
1. **Conception d'agents** : Utilisez l'Agent Builder pour créer des agents d'IA optimisés pour la périphérie
2. **Ingénierie des prompts** : Développez des prompts efficaces pour les modèles plus petits en périphérie
3. **Tests d'intégration** : Testez les agents dans des conditions simulées de périphérie
4. **Génération de code** : Produisez du code de production optimisé pour le déploiement en périphérie

### Phase 4 : Évaluation et tests
1. **Évaluation en lot** : Testez plusieurs configurations pour trouver les paramètres optimaux en périphérie
2. **Profilage des performances** : Analysez la vitesse d'inférence, l'utilisation de la mémoire et la précision
3. **Simulation en périphérie** : Testez dans des conditions similaires à l'environnement de déploiement en périphérie
4. **Tests de résistance** : Évaluez les performances sous diverses conditions de charge

### Phase 5 : Préparation au déploiement
1. **Optimisation finale** : Appliquez les optimisations finales en fonction des résultats des tests
2. **Emballage pour le déploiement** : Préparez les modèles et le code pour le déploiement en périphérie
3. **Documentation** : Documentez les exigences et la configuration du déploiement
4. **Configuration de la surveillance** : Préparez la surveillance et la journalisation pour le déploiement en périphérie

## Public cible pour le développement Edge AI

### Développeurs Edge AI
- Développeurs d'applications créant des dispositifs en périphérie et des solutions IoT alimentés par l'IA
- Développeurs de systèmes embarqués intégrant des capacités d'IA dans des dispositifs à ressources limitées
- Développeurs mobiles créant des applications d'IA sur appareil pour smartphones et tablettes

### Ingénieurs Edge AI
- Ingénieurs en IA optimisant les modèles pour le déploiement en périphérie et gérant les pipelines d'inférence
- Ingénieurs DevOps déployant et gérant des modèles d'IA sur une infrastructure distribuée en périphérie
- Ingénieurs en performance optimisant les charges de travail d'IA pour les contraintes matérielles en périphérie

### Chercheurs et éducateurs
- Chercheurs en IA développant des modèles et algorithmes efficaces pour l'informatique en périphérie
- Éducateurs enseignant les concepts Edge AI et démontrant des techniques d'optimisation
- Étudiants apprenant les défis et solutions liés au déploiement Edge AI

## Cas d'utilisation Edge AI

### Dispositifs IoT intelligents
- **Reconnaissance d'images en temps réel** : Déployez des modèles de vision par ordinateur sur des caméras et capteurs IoT
- **Traitement vocal** : Implémentez la reconnaissance vocale et le traitement du langage naturel sur des enceintes intelligentes
- **Maintenance prédictive** : Exécutez des modèles de détection d'anomalies sur des dispositifs industriels en périphérie
- **Surveillance environnementale** : Déployez des modèles d'analyse de données de capteurs pour des applications environnementales

### Applications mobiles et embarquées
- **Traduction sur appareil** : Implémentez des modèles de traduction linguistique fonctionnant hors ligne
- **Réalité augmentée** : Déployez la reconnaissance et le suivi d'objets en temps réel pour des applications AR
- **Surveillance de la santé** : Exécutez des modèles d'analyse de santé sur des dispositifs portables et équipements médicaux
- **Systèmes autonomes** : Implémentez des modèles de prise de décision pour drones, robots et véhicules

### Infrastructure Edge Computing
- **Centres de données en périphérie** : Déployez des modèles d'IA dans des centres de données en périphérie pour des applications à faible latence
- **Intégration CDN** : Intégrez des capacités de traitement IA dans des réseaux de diffusion de contenu
- **5G Edge** : Exploitez l'informatique en périphérie 5G pour des applications alimentées par l'IA
- **Fog Computing** : Implémentez le traitement IA dans des environnements de fog computing

## Installation et configuration

### Installation de l'extension
Installez l'extension AI Toolkit directement depuis le Visual Studio Code Marketplace :

**ID de l'extension** : `ms-windows-ai-studio.windows-ai-studio`

**Méthodes d'installation** :
1. **Marketplace VS Code** : Recherchez "AI Toolkit" dans la vue Extensions
2. **Ligne de commande** : `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Installation directe** : Téléchargez depuis [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Prérequis pour le développement Edge AI
- **Visual Studio Code** : Dernière version recommandée
- **Environnement Python** : Python 3.8+ avec les bibliothèques IA requises
- **ONNX Runtime** (optionnel) : Pour l'inférence des modèles ONNX
- **Ollama** (optionnel) : Pour le service local des modèles
- **Outils d'accélération matérielle** : CUDA, OpenVINO ou accélérateurs spécifiques à la plateforme

### Configuration initiale
1. **Activation de l'extension** : Ouvrez VS Code et vérifiez qu'AI Toolkit apparaît dans la barre d'activité
2. **Configuration des fournisseurs de modèles** : Configurez l'accès à GitHub, OpenAI, Anthropic ou d'autres fournisseurs de modèles
3. **Environnement local** : Configurez l'environnement Python et installez les packages requis
4. **Accélération matérielle** : Configurez l'accélération GPU/NPU si disponible
5. **Intégration MCP** : Configurez les serveurs Model Context Protocol si nécessaire

### Liste de contrôle pour la première configuration
- [ ] Extension AI Toolkit installée et activée
- [ ] Catalogue de modèles accessible et modèles découvrables
- [ ] Playground fonctionnel pour les tests de modèles
- [ ] Agent Builder accessible pour le développement de prompts
- [ ] Environnement de développement local configuré
- [ ] Accélération matérielle (si disponible) correctement configurée

## Premiers pas avec AI Toolkit

### Guide de démarrage rapide

Nous recommandons de commencer avec les modèles hébergés par GitHub pour une expérience simplifiée :

1. **Installation** : Suivez le [guide d'installation](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) pour configurer AI Toolkit sur votre appareil
2. **Découverte de modèles** : Depuis la vue de l'extension, sélectionnez **CATALOG > Models** pour explorer les modèles disponibles
3. **Modèles GitHub** : Commencez avec les modèles hébergés par GitHub pour une intégration optimale
4. **Tests dans le Playground** : Depuis une fiche de modèle, sélectionnez **Try in Playground** pour commencer à expérimenter les capacités du modèle

### Développement Edge AI étape par étape

#### Étape 1 : Exploration et sélection de modèles
1. Ouvrez la vue AI Toolkit dans la barre d'activité de VS Code
2. Parcourez le catalogue de modèles pour trouver ceux adaptés au déploiement en périphérie
3. Filtrez par fournisseur (GitHub, ONNX, Ollama) en fonction de vos besoins en périphérie
4. Utilisez **Try in Playground** pour tester immédiatement les capacités des modèles

#### Étape 2 : Développement d'agents
1. Utilisez le **Prompt (Agent) Builder** pour créer des agents d'IA optimisés pour la périphérie
2. Générer des invites de départ à partir de descriptions en langage naturel  
3. Itérer et affiner les invites en fonction des réponses du modèle  
4. Intégrer les outils MCP pour améliorer les capacités des agents  

#### Étape 3 : Tests et Évaluation  
1. Utiliser **Bulk Run** pour tester plusieurs invites sur des modèles sélectionnés  
2. Exécuter les agents avec des cas de test pour valider leur fonctionnalité  
3. Évaluer la précision et les performances à l'aide de métriques intégrées ou personnalisées  
4. Comparer différents modèles et configurations  

#### Étape 4 : Ajustement et Optimisation  
1. Personnaliser les modèles pour des cas d'utilisation spécifiques  
2. Appliquer un ajustement spécifique au domaine  
3. Optimiser en fonction des contraintes de déploiement en périphérie  
4. Versionner et comparer différentes configurations d'agents  

#### Étape 5 : Préparation au Déploiement  
1. Générer du code prêt pour la production avec l'Agent Builder  
2. Configurer les connexions au serveur MCP pour une utilisation en production  
3. Préparer les packages de déploiement pour les appareils en périphérie  
4. Configurer les métriques de surveillance et d'évaluation  

## Bonnes Pratiques pour le Développement d'IA en Périphérie  

### Sélection de Modèles  
- **Contraintes de Taille** : Choisir des modèles adaptés aux limitations de mémoire des appareils cibles  
- **Vitesse d'Inférence** : Prioriser les modèles avec des temps d'inférence rapides pour les applications en temps réel  
- **Compromis de Précision** : Équilibrer la précision des modèles avec les contraintes de ressources  
- **Compatibilité de Format** : Privilégier les formats ONNX ou optimisés pour le matériel pour le déploiement en périphérie  

### Techniques d'Optimisation  
- **Quantification** : Utiliser la quantification INT8 ou INT4 pour réduire la taille des modèles et améliorer leur vitesse  
- **Élagage** : Supprimer les paramètres inutiles des modèles pour réduire les besoins en calcul  
- **Distillation de Connaissances** : Créer des modèles plus petits tout en conservant les performances des modèles plus grands  
- **Accélération Matérielle** : Exploiter les NPUs, GPUs ou accélérateurs spécialisés lorsque disponibles  

### Flux de Travail de Développement  
- **Tests Itératifs** : Tester fréquemment dans des conditions similaires à celles de la périphérie pendant le développement  
- **Surveillance des Performances** : Surveiller en continu l'utilisation des ressources et la vitesse d'inférence  
- **Gestion des Versions** : Suivre les versions des modèles et les paramètres d'optimisation  
- **Documentation** : Documenter toutes les décisions d'optimisation et les compromis de performance  

### Considérations pour le Déploiement  
- **Surveillance des Ressources** : Surveiller la mémoire, le CPU et la consommation d'énergie en production  
- **Stratégies de Repli** : Mettre en place des mécanismes de repli en cas de défaillance des modèles  
- **Mécanismes de Mise à Jour** : Planifier les mises à jour des modèles et la gestion des versions  
- **Sécurité** : Implémenter des mesures de sécurité adaptées aux applications d'IA en périphérie  

## Intégration avec les Cadres d'IA en Périphérie  

### ONNX Runtime  
- **Déploiement Multi-plateforme** : Déployer des modèles ONNX sur différentes plateformes en périphérie  
- **Optimisation Matérielle** : Exploiter les optimisations spécifiques au matériel d'ONNX Runtime  
- **Support Mobile** : Utiliser ONNX Runtime Mobile pour les applications sur smartphones et tablettes  
- **Intégration IoT** : Déployer sur des appareils IoT avec les distributions légères d'ONNX Runtime  

### Windows ML  
- **Appareils Windows** : Optimiser pour les appareils en périphérie basés sur Windows et les PC  
- **Accélération NPU** : Exploiter les unités de traitement neuronal sur les appareils Windows  
- **DirectML** : Utiliser DirectML pour l'accélération GPU sur les plateformes Windows  
- **Intégration UWP** : Intégrer avec les applications Universal Windows Platform  

### TensorFlow Lite  
- **Optimisation Mobile** : Déployer des modèles TensorFlow Lite sur des appareils mobiles et embarqués  
- **Délégués Matériels** : Utiliser des délégués matériels spécialisés pour l'accélération  
- **Microcontrôleurs** : Déployer sur des microcontrôleurs avec TensorFlow Lite Micro  
- **Support Multi-plateforme** : Déployer sur Android, iOS et systèmes Linux embarqués  

### Azure IoT Edge  
- **Hybride Cloud-Périphérie** : Combiner l'entraînement dans le cloud avec l'inférence en périphérie  
- **Déploiement de Modules** : Déployer des modèles d'IA sous forme de modules IoT Edge  
- **Gestion des Appareils** : Gérer les appareils en périphérie et les mises à jour des modèles à distance  
- **Télémétrie** : Collecter des données de performance et des métriques de modèles à partir des déploiements en périphérie  

## Scénarios Avancés d'IA en Périphérie  

### Déploiement Multi-modèles  
- **Ensembles de Modèles** : Déployer plusieurs modèles pour améliorer la précision ou la redondance  
- **Tests A/B** : Tester différents modèles simultanément sur des appareils en périphérie  
- **Sélection Dynamique** : Choisir des modèles en fonction des conditions actuelles de l'appareil  
- **Partage de Ressources** : Optimiser l'utilisation des ressources entre plusieurs modèles déployés  

### Apprentissage Fédéré  
- **Entraînement Distribué** : Entraîner des modèles sur plusieurs appareils en périphérie  
- **Préservation de la Vie Privée** : Garder les données d'entraînement locales tout en partageant les améliorations des modèles  
- **Apprentissage Collaboratif** : Permettre aux appareils d'apprendre des expériences collectives  
- **Coordination Périphérie-Cloud** : Coordonner l'apprentissage entre les appareils en périphérie et l'infrastructure cloud  

### Traitement en Temps Réel  
- **Traitement de Flux** : Traiter des flux de données continus sur des appareils en périphérie  
- **Inférence à Faible Latence** : Optimiser pour une latence minimale d'inférence  
- **Traitement par Lots** : Traiter efficacement des lots de données sur des appareils en périphérie  
- **Traitement Adaptatif** : Ajuster le traitement en fonction des capacités actuelles de l'appareil  

## Résolution de Problèmes dans le Développement d'IA en Périphérie  

### Problèmes Courants  
- **Contraintes de Mémoire** : Modèle trop volumineux pour la mémoire de l'appareil cible  
- **Vitesse d'Inférence** : Inférence du modèle trop lente pour les exigences en temps réel  
- **Dégradation de Précision** : L'optimisation réduit la précision du modèle de manière inacceptable  
- **Compatibilité Matérielle** : Modèle incompatible avec le matériel cible  

### Stratégies de Débogage  
- **Profilage des Performances** : Utiliser les fonctionnalités de traçage de l'AI Toolkit pour identifier les goulots d'étranglement  
- **Surveillance des Ressources** : Surveiller l'utilisation de la mémoire et du CPU pendant le développement  
- **Tests Incrémentaux** : Tester les optimisations de manière incrémentale pour isoler les problèmes  
- **Simulation Matérielle** : Utiliser des outils de développement pour simuler le matériel cible  

### Solutions d'Optimisation  
- **Quantification Supplémentaire** : Appliquer des techniques de quantification plus agressives  
- **Architecture de Modèle** : Considérer différentes architectures de modèles optimisées pour la périphérie  
- **Optimisation du Prétraitement** : Optimiser le prétraitement des données pour les contraintes de la périphérie  
- **Optimisation de l'Inférence** : Utiliser des optimisations spécifiques au matériel pour l'inférence  

## Ressources et Prochaines Étapes  

### Documentation Officielle  
- [Documentation Développeur AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Guide d'Installation et de Configuration](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Documentation VS Code Intelligent Apps](https://code.visualstudio.com/docs/intelligentapps)  
- [Documentation Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Communauté et Support  
- [Répertoire GitHub AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [Problèmes GitHub et Demandes de Fonctionnalités](https://aka.ms/AIToolkit/feedback)  
- [Communauté Discord Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Marketplace des Extensions VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Ressources Techniques  
- [Documentation ONNX Runtime](https://onnxruntime.ai/)  
- [Documentation Ollama](https://ollama.ai/)  
- [Documentation Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Documentation Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Parcours d'Apprentissage  
- [Cours Fondamentaux sur l'IA en Périphérie](../Module01/README.md)  
- [Guide des Petits Modèles de Langage](../Module02/README.md)  
- [Stratégies de Déploiement en Périphérie](../Module03/README.md)  
- [Développement d'IA en Périphérie sous Windows](./windowdeveloper.md)  

### Ressources Supplémentaires  
- **Statistiques du Répertoire** : Plus de 1,8k étoiles, 150+ forks, 18+ contributeurs  
- **Licence** : Licence MIT  
- **Sécurité** : Les politiques de sécurité de Microsoft s'appliquent  
- **Télémétrie** : Respecte les paramètres de télémétrie de VS Code  

## Conclusion  

AI Toolkit pour Visual Studio Code représente une plateforme complète pour le développement moderne d'IA, offrant des capacités de développement d'agents simplifiées particulièrement utiles pour les applications d'IA en périphérie. Avec son vaste catalogue de modèles prenant en charge des fournisseurs tels qu'Anthropic, OpenAI, GitHub et Google, combiné à une exécution locale via ONNX et Ollama, le toolkit offre la flexibilité nécessaire pour divers scénarios de déploiement en périphérie.  

La force du toolkit réside dans son approche intégrée : de la découverte et de l'expérimentation des modèles dans le Playground au développement sophistiqué d'agents avec le Prompt Builder, en passant par des capacités d'évaluation complètes et une intégration fluide des outils MCP. Pour les développeurs d'IA en périphérie, cela signifie un prototypage rapide et des tests d'agents d'IA avant le déploiement en périphérie, avec la possibilité d'itérer rapidement et d'optimiser pour des environnements à ressources limitées.  

Les principaux avantages pour le développement d'IA en périphérie incluent :  
- **Expérimentation Rapide** : Tester rapidement les modèles et agents avant de s'engager dans le déploiement en périphérie  
- **Flexibilité Multi-fournisseurs** : Accéder à des modèles provenant de diverses sources pour trouver des solutions optimales en périphérie  
- **Développement Local** : Tester avec ONNX et Ollama pour un développement hors ligne et respectueux de la vie privée  
- **Prêt pour la Production** : Générer du code prêt pour la production et intégrer avec des outils externes via MCP  
- **Évaluation Complète** : Utiliser des métriques intégrées et personnalisées pour valider les performances de l'IA en périphérie  

Alors que l'IA continue de se diriger vers des scénarios de déploiement en périphérie, AI Toolkit pour VS Code fournit l'environnement de développement et le flux de travail nécessaires pour concevoir, tester et optimiser des applications intelligentes pour des environnements à ressources limitées. Que vous développiez des solutions IoT, des applications mobiles d'IA ou des systèmes d'intelligence embarquée, l'ensemble complet de fonctionnalités et le flux de travail intégré du toolkit soutiennent tout le cycle de vie du développement d'IA en périphérie.  

Avec un développement continu et une communauté active (plus de 1,8k étoiles sur GitHub), AI Toolkit reste à la pointe des outils de développement d'IA, évoluant constamment pour répondre aux besoins des développeurs modernes d'IA construisant pour des scénarios de déploiement en périphérie.  

[Next Foundry Local](./foundrylocal.md)  

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.