<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3c232b8e9dac492a43b9c189f4cb04df",
  "translation_date": "2025-09-15T15:33:31+00:00",
  "source_file": "README.md",
  "language_code": "fr"
}
-->
# EdgeAI pour les Débutants

![Image de couverture du cours](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.fr.png)

[![Contributeurs GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)  
[![Problèmes GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)  
[![Pull-requests GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)  
[![PRs Bienvenus](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  

[![Observateurs GitHub](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)  
[![Forks GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
[![Étoiles GitHub](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)  

[![Discord Microsoft Azure AI Foundry](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Suivez ces étapes pour commencer à utiliser ces ressources :

1. **Forkez le dépôt** : Cliquez sur [![Forks GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
2. **Clonez le dépôt** : `git clone https://github.com/microsoft/edgeai-for-beginners.git`  
3. [**Rejoignez le Discord Azure AI Foundry pour rencontrer des experts et d'autres développeurs**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 Support Multilingue

#### Supporté via GitHub Action (Automatisé & Toujours à jour)

[Français](./README.md) | [Espagnol](../es/README.md) | [Chinois (Simplifié)](../zh/README.md) | [Chinois (Traditionnel, Macao)](../mo/README.md) | [Chinois (Traditionnel, Hong Kong)](../hk/README.md) | [Chinois (Traditionnel, Taïwan)](../tw/README.md) | [Japonais](../ja/README.md) | [Coréen](../ko/README.md)  
**Si vous souhaitez ajouter des langues supplémentaires, les langues supportées sont listées [ici](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Introduction

Bienvenue dans **EdgeAI pour les Débutants** – votre parcours complet dans le monde transformateur de l'Intelligence Artificielle en périphérie. Ce cours relie les capacités puissantes de l'IA à des déploiements pratiques et réels sur des appareils en périphérie, vous permettant de tirer parti du potentiel de l'IA directement là où les données sont générées et où les décisions doivent être prises.

### Ce que vous allez maîtriser

Ce cours vous guide des concepts fondamentaux aux implémentations prêtes pour la production, couvrant :
- **Modèles de Langage Réduits (SLMs)** optimisés pour le déploiement en périphérie  
- **Optimisation adaptée au matériel** sur diverses plateformes  
- **Inférence en temps réel** avec des capacités de préservation de la vie privée  
- **Stratégies de déploiement en production** pour des applications d'entreprise  

### Pourquoi l'EdgeAI est important

L'Edge AI représente un changement de paradigme qui répond à des défis modernes critiques :  
- **Confidentialité & Sécurité** : Traitez les données sensibles localement sans exposition au cloud  
- **Performance en temps réel** : Éliminez la latence réseau pour les applications critiques  
- **Efficacité des coûts** : Réduisez les dépenses de bande passante et de calcul dans le cloud  
- **Opérations résilientes** : Maintenez la fonctionnalité en cas de panne réseau  
- **Conformité réglementaire** : Respectez les exigences de souveraineté des données  

### Edge AI

L'Edge AI consiste à exécuter des algorithmes d'IA et des modèles de langage localement sur du matériel – près de l'endroit où les données sont générées – sans dépendre des ressources cloud pour l'inférence. Cela réduit la latence, améliore la confidentialité et permet une prise de décision en temps réel.

### Principes fondamentaux :
- **Inférence sur appareil** : Les modèles d'IA s'exécutent sur des appareils en périphérie (téléphones, routeurs, microcontrôleurs, PC industriels)  
- **Capacité hors ligne** : Fonctionne sans connectivité Internet persistante  
- **Faible latence** : Réponses immédiates adaptées aux systèmes en temps réel  
- **Souveraineté des données** : Conserve les données sensibles localement, améliorant la sécurité et la conformité  

### Modèles de Langage Réduits (SLMs)

Les SLMs comme Phi-4, Mistral-7B et Gemma sont des versions optimisées de grands modèles de langage – entraînés ou distillés pour :  
- **Empreinte mémoire réduite** : Utilisation efficace de la mémoire limitée des appareils en périphérie  
- **Moins de demande de calcul** : Optimisés pour les performances CPU et GPU en périphérie  
- **Temps de démarrage plus rapides** : Initialisation rapide pour des applications réactives  

Ils débloquent des capacités NLP puissantes tout en respectant les contraintes de :  
- **Systèmes embarqués** : Appareils IoT et contrôleurs industriels  
- **Appareils mobiles** : Smartphones et tablettes avec capacités hors ligne  
- **Appareils IoT** : Capteurs et appareils intelligents avec ressources limitées  
- **Serveurs en périphérie** : Unités de traitement locales avec ressources GPU limitées  
- **Ordinateurs personnels** : Scénarios de déploiement sur ordinateurs de bureau et portables  

## Architecture du cours

### [Module 01 : Fondamentaux et Transformation de l'EdgeAI](./Module01/README.md)  
**Thème** : Le changement transformateur du déploiement de l'Edge AI  

#### Structure des chapitres :  
- [**Section 1 : Fondamentaux de l'EdgeAI**](./Module01/01.EdgeAIFundamentals.md)  
  - Comparaison entre l'IA cloud traditionnelle et l'IA en périphérie  
  - Défis et contraintes du calcul en périphérie  
  - Technologies clés : quantification des modèles, optimisation par compression, Modèles de Langage Réduits (SLMs)  
  - Accélération matérielle : NPUs, optimisation GPU, optimisation CPU  
  - Avantages : sécurité de la confidentialité, faible latence, capacités hors ligne, efficacité des coûts  

- [**Section 2 : Études de cas réels**](./Module01/02.RealWorldCaseStudies.md)  
  - Écosystème de modèles Microsoft Phi & Mu  
  - Étude de cas sur le système de reporting AI de Japan Airlines  
  - Impact sur le marché et orientations futures  
  - Considérations de déploiement et meilleures pratiques  

- [**Section 3 : Guide pratique d'implémentation**](./Module01/03.PracticalImplementationGuide.md)  
  - Configuration de l'environnement de développement (Python 3.10+, .NET 8+)  
  - Exigences matérielles et configurations recommandées  
  - Ressources des familles de modèles principaux  
  - Outils de quantification et d'optimisation (Llama.cpp, Microsoft Olive, Apple MLX)  
  - Liste de vérification pour l'évaluation et la vérification  

- [**Section 4 : Plateformes matérielles de déploiement Edge AI**](./Module01/04.EdgeDeployment.md)  
  - Considérations et exigences pour le déploiement de l'Edge AI  
  - Matériel Edge AI Intel et techniques d'optimisation  
  - Solutions AI Qualcomm pour systèmes mobiles et embarqués  
  - Plateformes de calcul en périphérie NVIDIA Jetson  
  - Plateformes PC Windows AI avec accélération NPU  
  - Stratégies d'optimisation spécifiques au matériel  

---

### [Module 02 : Fondations des Modèles de Langage Réduits](./Module02/README.md)  
**Thème** : Principes théoriques des SLMs, stratégies d'implémentation et déploiement en production  

#### Structure des chapitres :  
- [**Section 1 : Fondamentaux de la famille de modèles Microsoft Phi**](./Module02/01.PhiFamily.md)  
  - Évolution de la philosophie de conception (Phi-1 à Phi-4)  
  - Conception axée sur l'efficacité  
  - Capacités spécialisées (raisonnement, multimodal, déploiement en périphérie)  

- [**Section 2 : Fondamentaux de la famille Qwen**](./Module02/02.QwenFamily.md)  
  - Excellence open source (Qwen 1.0 à Qwen3) - disponible via Hugging Face  
  - Architecture avancée de raisonnement avec capacités de mode réflexion  
  - Options de déploiement évolutives (0.5B-235B paramètres)  

- [**Section 3 : Fondamentaux de la famille Gemma**](./Module02/03.GemmaFamily.md)  
  - Innovation axée sur la recherche (Gemma 3 & 3n)  
  - Excellence multimodale  
  - Architecture axée sur le mobile  

- [**Section 4 : Fondamentaux de la famille BitNET**](./Module02/04.BitNETFamily.md)  
  - Technologie révolutionnaire de quantification (1.58-bit)  
  - Cadre d'inférence spécialisé depuis https://github.com/microsoft/BitNet  
  - Leadership en IA durable grâce à une efficacité extrême  

- [**Section 5 : Fondamentaux du modèle Microsoft Mu**](./Module02/05.mumodel.md)  
  - Architecture axée sur les appareils intégrée à Windows 11  
  - Intégration système avec les paramètres de Windows 11  
  - Fonctionnement hors ligne préservant la confidentialité  

- [**Section 6 : Fondamentaux de Phi-Silica**](./Module02/06.phisilica.md)  
  - Architecture optimisée pour NPU intégrée aux PC Windows 11 Copilot+  
  - Efficacité exceptionnelle (650 tokens/seconde à 1.5W)  
  - Intégration pour les développeurs avec Windows App SDK  

---

### [Module 03 : Déploiement des Modèles de Langage Réduits](./Module03/README.md)  
**Thème** : Cycle complet de déploiement des SLMs, de la théorie à l'environnement de production  

#### Structure des chapitres :  
- [**Section 1 : Apprentissage avancé des SLMs**](./Module03/01.SLMAdvancedLearning.md)  
  - Cadre de classification des paramètres (Micro SLM 100M-1.4B, Medium SLM 14B-30B)  
  - Techniques avancées d'optimisation (méthodes de quantification, quantification BitNET 1-bit)  
  - Stratégies d'acquisition de modèles (Azure AI Foundry pour les modèles Phi, Hugging Face pour les modèles sélectionnés)  

- [**Section 2 : Déploiement dans un environnement local**](./Module03/02.DeployingSLMinLocalEnv.md)  
  - Déploiement universel sur la plateforme Ollama  
  - Solutions locales de niveau entreprise Microsoft Foundry  
  - Analyse comparative des cadres  

- [**Section 3 : Déploiement en cloud conteneurisé**](./Module03/03.DeployingSLMinCloud.md)  
  - Déploiement d'inférence haute performance vLLM  
  - Orchestration de conteneurs Ollama  
  - Implémentation optimisée pour la périphérie avec ONNX Runtime  

---

### [Module 04 : Conversion de format et quantification des modèles](./Module04/README.md)  
**Thème** : Boîte à outils complète d'optimisation des modèles pour le déploiement en périphérie sur diverses plateformes  

#### Structure des chapitres :  
- [**Section 1 : Fondations de la conversion de format et de la quantification des modèles**](./Module04/01.Introduce.md)  
  - Cadre de classification de précision (ultra-faible, faible, moyenne précision)  
  - Avantages et cas d'utilisation des formats GGUF et ONNX  
  - Bénéfices de la quantification pour l'efficacité opérationnelle  
  - Comparaisons de performances et empreintes mémoire  

- [**Section 2 : Guide d'implémentation de Llama.cpp**](./Module04/02.Llamacpp.md)  
  - Installation multiplateforme (Windows, macOS, Linux)  
  - Conversion au format GGUF et niveaux de quantification (Q2_K à Q8_0)  
  - Accélération matérielle (CUDA, Metal, OpenCL, Vulkan)  
  - Intégration Python et déploiement API REST  

- [**Section 3 : Suite d'optimisation Microsoft Olive**](./Module04/03.MicrosoftOlive.md)  
  - Optimisation des modèles adaptée au matériel avec plus de 40 composants intégrés  
  - Auto-optimisation avec quantification dynamique et statique  
  - Intégration entreprise avec les workflows Azure ML  
  - Support des modèles populaires (Llama, Phi, modèles Qwen sélectionnés, Gemma)  

- [**Section 4 : Exploration approfondie du framework Apple MLX**](./Module04/04.AppleMLX.md)  
  - Architecture mémoire unifiée pour Apple Silicon  
  - Support pour LLaMA, Mistral, Phi-3, modèles Qwen sélectionnés  
  - Affinage LoRA et personnalisation des modèles  
  - Intégration Hugging Face avec quantification 4-bit/8-bit  

---

### [Module 05 : SLMOps - Opérations des Modèles de Langage Réduits](./Module05/README.md)  
**Thème** : Cycle complet des opérations SLM, de la distillation au déploiement en production  

#### Structure des chapitres :  
- [**Section 1 : Introduction aux SLMOps**](./Module05/01.IntroduceSLMOps.md)  
  - Changement de paradigme des SLMOps dans les opérations IA  
  - Architecture axée sur l'efficacité des coûts et la confidentialité  
  - Impact stratégique sur les entreprises et avantages compétitifs  
  - Défis réels d'implémentation et solutions  

- [**Section 2 : Distillation des modèles - De la théorie à la pratique**](./Module05/02.SLMOps-Distillation.md)  
  - Transfert de connaissances des modèles enseignants aux modèles étudiants  
  - Implémentation du processus de distillation en deux étapes  
  - Workflows de distillation Azure ML avec exemples pratiques  
  - Réduction de 85% du temps d'inférence avec une rétention de précision de 92%  

- [**Section 3 : Affinage - Personnalisation des modèles pour des tâches spécifiques**](./Module05/03.SLMOps-Finetuing.md)  
  - Techniques d'affinage efficaces en paramètres (PEFT)  
  - Méthodes avancées LoRA et QLoRA  
  - Implémentation d'affinage Microsoft Olive  
  - Formation multi-adaptateurs et optimisation des hyperparamètres  
- [**Section 4 : Déploiement - Mise en œuvre prête pour la production**](./Module05/04.SLMOps.Deployment.md)
  - Conversion et quantification des modèles pour la production
  - Configuration de déploiement Foundry Local
  - Benchmarking des performances et validation de la qualité
  - Réduction de taille de 75 % avec surveillance en production

---

### [Module 06 : Systèmes agentiques SLM - Agents IA et appels de fonctions](./Module06/README.md)
**Thème** : Mise en œuvre des systèmes agentiques SLM, des bases aux appels de fonctions avancés et intégration du protocole de contexte de modèle

#### Structure des chapitres :
- [**Section 1 : Fondations des agents IA et des petits modèles de langage**](./Module06/01.IntroduceAgent.md)
  - Cadre de classification des agents (réflexes, basés sur des modèles, orientés objectifs, agents apprenants)
  - Fondamentaux des SLM et stratégies d'optimisation (GGUF, quantification, frameworks edge)
  - Analyse des compromis entre SLM et LLM (réduction des coûts de 10 à 30×, efficacité des tâches de 70 à 80 %)
  - Déploiement pratique avec Ollama, VLLM et solutions Microsoft edge

- [**Section 2 : Appels de fonctions dans les petits modèles de langage**](./Module06/02.FunctionCalling.md)
  - Mise en œuvre de workflows systématiques (détection d'intention, sortie JSON, exécution externe)
  - Implémentations spécifiques aux plateformes (Phi-4-mini, modèles Qwen sélectionnés, Microsoft Foundry Local)
  - Exemples avancés (collaboration multi-agents, sélection dynamique d'outils)
  - Considérations pour la production (limitation de débit, journalisation d'audit, mesures de sécurité)

- [**Section 3 : Intégration du protocole de contexte de modèle (MCP)**](./Module06/03.IntroduceMCP.md)
  - Architecture du protocole et conception de systèmes en couches
  - Support multi-backend (Ollama pour le développement, vLLM pour la production)
  - Protocoles de connexion (modes STDIO et SSE)
  - Applications réelles (automatisation web, traitement de données, intégration API)

---

### [Module 07 : Exemples d'implémentation EdgeAI](./Module07/README.md)
**Thème** : Implémentations EdgeAI complètes sur diverses plateformes et frameworks

#### Structure des chapitres :
- [**EdgeAI sur NVIDIA Jetson Orin Nano**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - Performance IA de 67 TOPS dans un format de la taille d'une carte de crédit
  - Support des modèles d'IA générative (transformateurs de vision, LLM, modèles vision-langage)
  - Applications en robotique, drones, caméras intelligentes, dispositifs autonomes
  - Plateforme abordable à 249 $ pour un développement IA démocratisé

- [**EdgeAI dans les applications mobiles avec .NET MAUI et ONNX Runtime GenAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - IA mobile multiplateforme avec un code C# unique
  - Support de l'accélération matérielle (CPU, GPU, processeurs IA mobiles)
  - Optimisations spécifiques aux plateformes (CoreML pour iOS, NNAPI pour Android)
  - Implémentation complète de la boucle d'IA générative

- [**EdgeAI sur Azure avec le moteur des petits modèles de langage**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - Architecture de déploiement hybride cloud-edge
  - Intégration des services Azure AI avec ONNX Runtime
  - Déploiement à l'échelle de l'entreprise et gestion continue des modèles
  - Workflows IA hybrides pour le traitement intelligent de documents

- [**EdgeAI avec Windows ML**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Fondation Windows AI Foundry pour une inférence performante sur appareil
  - Support matériel universel (AMD, Intel, NVIDIA, Qualcomm)
  - Abstraction et optimisation matérielle automatiques
  - Framework unifié pour un écosystème matériel Windows diversifié

- [**EdgeAI avec les applications Foundry Local**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - Implémentation RAG axée sur la confidentialité avec des ressources locales
  - Intégration du modèle de langage Phi-3 avec recherche sémantique (modèles Phi uniquement)
  - Support des bases de données vectorielles locales (SQLite, Qdrant)
  - Capacités de souveraineté des données et fonctionnement hors ligne

## Objectifs d'apprentissage du cours

En complétant ce cours complet sur EdgeAI, vous développerez l'expertise nécessaire pour concevoir, implémenter et déployer des solutions EdgeAI prêtes pour la production. Notre approche structurée garantit que vous maîtriserez à la fois les bases théoriques et les compétences pratiques.

### Compétences techniques

**Connaissances de base**
- Comprendre les différences fondamentales entre les architectures IA basées sur le cloud et celles basées sur le edge
- Maîtriser les principes de quantification, compression et optimisation des modèles pour des environnements contraints en ressources
- Comprendre les options d'accélération matérielle (NPUs, GPUs, CPUs) et leurs implications de déploiement

**Compétences en implémentation**
- Déployer des petits modèles de langage sur diverses plateformes edge (mobile, embarqué, IoT, serveurs edge)
- Appliquer des frameworks d'optimisation tels que Llama.cpp, Microsoft Olive, ONNX Runtime et Apple MLX
- Implémenter des systèmes d'inférence en temps réel avec des exigences de réponse sous la seconde

**Expertise en production**
- Concevoir des architectures EdgeAI évolutives pour des applications d'entreprise
- Implémenter des stratégies de surveillance, maintenance et mise à jour pour les systèmes déployés
- Appliquer les meilleures pratiques de sécurité pour des implémentations EdgeAI respectueuses de la vie privée

### Capacités stratégiques

**Cadre de prise de décision**
- Évaluer les opportunités EdgeAI et identifier les cas d'utilisation adaptés aux applications commerciales
- Analyser les compromis entre précision du modèle, vitesse d'inférence, consommation d'énergie et coûts matériels
- Sélectionner les familles SLM et configurations appropriées en fonction des contraintes de déploiement spécifiques

**Architecture système**
- Concevoir des solutions EdgeAI de bout en bout intégrées à l'infrastructure existante
- Planifier des architectures hybrides edge-cloud pour une performance et une efficacité des coûts optimales
- Implémenter des flux de données et des pipelines de traitement pour des applications IA en temps réel

### Applications industrielles

**Scénarios de déploiement pratiques**
- **Fabrication** : Systèmes de contrôle qualité, maintenance prédictive et optimisation des processus
- **Santé** : Outils de diagnostic respectueux de la vie privée et systèmes de surveillance des patients
- **Transport** : Prise de décision pour véhicules autonomes et gestion du trafic
- **Villes intelligentes** : Infrastructure intelligente et systèmes de gestion des ressources
- **Électronique grand public** : Applications mobiles alimentées par l'IA et dispositifs domestiques intelligents

## Aperçu des résultats d'apprentissage

### Résultats d'apprentissage du Module 01 :
- Comprendre les différences fondamentales entre les architectures IA cloud et edge
- Maîtriser les techniques d'optimisation de base pour le déploiement edge
- Reconnaître les applications réelles et les succès
- Acquérir des compétences pratiques pour implémenter des solutions EdgeAI

### Résultats d'apprentissage du Module 02 :
- Compréhension approfondie des différentes philosophies de conception SLM et leurs implications de déploiement
- Maîtriser les capacités de prise de décision stratégique basées sur les contraintes computationnelles et les exigences de performance
- Comprendre les compromis de flexibilité de déploiement
- Posséder des perspectives prêtes pour l'avenir sur des architectures IA efficaces

### Résultats d'apprentissage du Module 03 :
- Capacités stratégiques de sélection de modèles
- Maîtrise des techniques d'optimisation
- Maîtrise de la flexibilité de déploiement
- Capacités de configuration prêtes pour la production

### Résultats d'apprentissage du Module 04 :
- Compréhension approfondie des limites de quantification et des applications pratiques
- Expérience pratique avec plusieurs frameworks d'optimisation (Llama.cpp, Olive, MLX)
- Capacités de sélection d'optimisation matérielle
- Compétences de déploiement en production pour des environnements edge multiplateformes

### Résultats d'apprentissage du Module 05 :
- Maîtriser le paradigme SLMOps et les principes opérationnels
- Implémenter la distillation de modèles pour le transfert de connaissances et l'optimisation de l'efficacité
- Appliquer des techniques de fine-tuning pour la personnalisation de modèles spécifiques au domaine
- Déployer des solutions SLM prêtes pour la production avec des stratégies de surveillance et de maintenance

### Résultats d'apprentissage du Module 06 :
- Comprendre les concepts fondamentaux des agents IA et de l'architecture des petits modèles de langage
- Maîtriser l'implémentation des appels de fonctions sur plusieurs plateformes et frameworks
- Intégrer le protocole de contexte de modèle (MCP) pour une interaction standardisée avec des outils externes
- Construire des systèmes agentiques sophistiqués nécessitant une intervention humaine minimale

### Résultats d'apprentissage du Module 07 :
- Acquérir une expérience pratique avec diverses plateformes EdgeAI et stratégies d'implémentation
- Maîtriser les techniques d'optimisation spécifiques au matériel sur les plateformes NVIDIA, mobiles, Azure et Windows
- Comprendre les compromis de déploiement entre performance, coût et exigences de confidentialité
- Développer des compétences pratiques pour construire des applications EdgeAI réelles dans différents écosystèmes

## Résultats attendus du cours

À l'issue de ce cours, vous serez équipé des connaissances, compétences et confiance nécessaires pour diriger des initiatives EdgeAI dans des environnements professionnels.

### Préparation professionnelle

**Leadership technique**
- **Architecture de solution** : Concevoir des systèmes EdgeAI complets répondant aux exigences d'entreprise
- **Optimisation des performances** : Atteindre un équilibre optimal entre précision, vitesse et consommation de ressources
- **Déploiement multiplateforme** : Implémenter des solutions sur Windows, Linux, mobile et plateformes embarquées
- **Opérations de production** : Maintenir et faire évoluer des systèmes EdgeAI avec une fiabilité de niveau entreprise

**Expertise industrielle**
- **Évaluation technologique** : Évaluer et recommander des solutions EdgeAI pour des défis commerciaux spécifiques
- **Planification d'implémentation** : Développer des calendriers réalistes et des besoins en ressources pour des projets EdgeAI
- **Gestion des risques** : Identifier et atténuer les risques techniques et opérationnels dans les déploiements EdgeAI
- **Optimisation du ROI** : Démontrer une valeur commerciale mesurable grâce aux implémentations EdgeAI

### Opportunités d'avancement professionnel

**Rôles professionnels**
- Architecte de solutions EdgeAI
- Ingénieur en apprentissage automatique (spécialisation Edge)
- Développeur IA IoT
- Développeur d'applications mobiles IA
- Consultant IA d'entreprise

**Secteurs industriels**
- Fabrication intelligente et industrie 4.0
- Véhicules autonomes et transport
- Technologie de santé et dispositifs médicaux
- Technologie financière et sécurité
- Électronique grand public et applications mobiles

### Certification et validation

**Développement de portefeuille**
- Compléter des projets EdgeAI de bout en bout démontrant une compétence pratique
- Déployer des solutions prêtes pour la production sur plusieurs plateformes matérielles
- Documenter les stratégies d'optimisation et les améliorations de performance obtenues

**Chemin d'apprentissage continu**
- Base pour des spécialisations avancées en IA
- Préparation aux architectures hybrides cloud-edge
- Porte d'entrée vers les technologies et frameworks IA émergents

Ce cours vous positionne à l'avant-garde du déploiement de la technologie IA, où des capacités intelligentes sont intégrées de manière transparente dans les dispositifs et systèmes qui alimentent la vie moderne.

## Diagramme de structure de fichier

```
edgeai-for-beginners/
├── imgs/
│   └── cover.png
├── Module01/ (EdgeAI Fundamentals and Transformation)
│   ├── 01.EdgeAIFundamentals.md
│   ├── 02.RealWorldCaseStudies.md
│   ├── 03.PracticalImplementationGuide.md
│   ├── 04.EdgeDeployment.md
│   └── README.md
├── Module02/ (Small Language Model Foundations)
│   ├── 01.PhiFamily.md
│   ├── 02.QwenFamily.md
│   ├── 03.GemmaFamily.md
│   ├── 04.BitNETFamily.md
│   ├── 05.mumodel.md
│   ├── 06.phisilica.md
│   └── README.md
├── Module03/ (SLM Deployment Practice)
│   ├── 01.SLMAdvancedLearning.md
│   ├── 02.DeployingSLMinLocalEnv.md
│   ├── 03.DeployingSLMinCloud.md
│   └── README.md
├── Module04/ (Model Format Conversion and Quantization)
│   ├── 01.Introduce.md
│   ├── 02.Llamacpp.md
│   ├── 03.MicrosoftOlive.md
│   ├── 04.AppleMLX.md
│   └── README.md
├── Module05/ (SLMOps - Small Language Model Operations)
│   ├── 01.IntroduceSLMOps.md
│   ├── 02.SLMOps-Distillation.md
│   ├── 03.SLMOps-Finetuing.md
│   ├── 04.SLMOps.Deployment.md
│   └── README.md
├── Module06/ (SLM Agentic Systems)
│   ├── 01.IntroduceAgent.md
│   ├── 02.FunctionCalling.md
│   ├── 03.IntroduceMCP.md
│   └── README.md
├── Module07/ (EdgeAI Implementation Samples)
│   └── README.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md (This file)
├── SECURITY.md
├── STUDY_GUIDE.md
└── SUPPORT.md
```

## Caractéristiques du cours

- **Apprentissage progressif** : Avancez progressivement des concepts de base au déploiement avancé
- **Intégration théorie et pratique** : Chaque module contient des bases théoriques et des opérations pratiques
- **Études de cas réelles** : Basées sur des cas réels de Microsoft, Alibaba, Google et autres
- **Pratique concrète** : Fichiers de configuration complets, procédures de test API et scripts de déploiement
- **Benchmarks de performance** : Comparaisons détaillées de vitesse d'inférence, utilisation mémoire et exigences en ressources
- **Considérations de niveau entreprise** : Pratiques de sécurité, cadres de conformité et stratégies de protection des données

## Premiers pas

Chemin d'apprentissage recommandé :
1. Commencez par **Module01** pour construire une compréhension fondamentale de EdgeAI
2. Passez à **Module02** pour comprendre en profondeur les différentes familles de modèles SLM
3. Apprenez **Module03** pour maîtriser les compétences pratiques de déploiement
4. Continuez avec **Module04** pour l'optimisation avancée des modèles et la conversion de formats
5. Complétez **Module05** pour maîtriser SLMOps pour des implémentations prêtes pour la production
6. Explorez **Module06** pour comprendre les systèmes agentiques SLM et les capacités d'appel de fonctions
7. Terminez avec **Module07** pour acquérir une expérience pratique avec des exemples d'implémentation EdgeAI diversifiés

Chaque module est conçu pour être complet indépendamment, mais un apprentissage séquentiel fournira les meilleurs résultats.

## Guide d'étude

Un [Guide d'étude](STUDY_GUIDE.md) complet est disponible pour vous aider à maximiser votre expérience d'apprentissage. Le guide d'étude fournit :

- **Chemins d'apprentissage structurés** : Calendriers optimisés pour compléter le cours en 20 heures
- **Conseils d'allocation de temps** : Recommandations spécifiques pour équilibrer lecture, exercices et projets
- **Focus sur les concepts clés** : Objectifs d'apprentissage prioritaires pour chaque module
- **Outils d'auto-évaluation** : Questions et exercices pour tester votre compréhension
- **Idées de mini-projets** : Applications pratiques pour renforcer votre apprentissage

Le guide d'étude est conçu pour s'adapter à un apprentissage intensif (1 semaine) ou à un apprentissage à temps partiel (3 semaines), avec des indications claires sur la manière de répartir votre temps efficacement, même si vous ne pouvez consacrer que 10 heures au cours.

---

**L'avenir de EdgeAI réside dans l'amélioration continue des architectures de modèles, des techniques de quantification et des stratégies de déploiement qui privilégient l'efficacité et la spécialisation plutôt que les capacités généralistes. Les organisations qui adoptent ce changement de paradigme seront bien positionnées pour exploiter le potentiel transformateur de l'IA tout en gardant le contrôle sur leurs données et leurs opérations.**

## Autres cours

Notre équipe propose d'autres cours ! Découvrez :

- [MCP pour débutants](https://github.com/microsoft/mcp-for-beginners)
- [Agents IA pour débutants](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [IA générative pour débutants avec .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [IA générative pour débutants avec JavaScript](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [IA générative pour débutants](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [ML pour débutants](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [Data Science pour débutants](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [IA pour débutants](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [Cybersécurité pour débutants](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [Développement web pour débutants](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [IoT pour les débutants](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
- [Développement XR pour les débutants](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [Maîtriser GitHub Copilot pour la programmation assistée par IA](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
- [Maîtriser GitHub Copilot pour les développeurs C#/.NET](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
- [Choisissez votre propre aventure avec Copilot](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction professionnelle humaine. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.