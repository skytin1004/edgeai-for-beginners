<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0f8da2fde263594c60dab5c40e0fffc",
  "translation_date": "2025-07-22T07:49:58+00:00",
  "source_file": "README.md",
  "language_code": "fr"
}
-->
# EdgeAI pour Débutants

Un parcours éducatif approfondi à travers les technologies Edge AI, structuré en trois modules complets : Fondamentaux de l'EdgeAI, Bases des Petits Modèles de Langage, et Stratégies de Déploiement Pratiques. Ce cours guide les apprenants des concepts de base aux implémentations avancées, avec des études de cas réels, des exercices pratiques et des exemples de déploiement qui montrent comment exécuter efficacement des modèles d'IA directement sur des appareils en périphérie pour une meilleure confidentialité, une latence réduite et une efficacité accrue.

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
1. **Forkez le Répertoire** : Cliquez [![Forks GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/mcp-for-beginners/fork)  
2. **Clonez le Répertoire** : `git clone https://github.com/microsoft/edgeai-for-beginners.git`  
3. [**Rejoignez le Discord Azure AI Foundry pour rencontrer des experts et d'autres développeurs**](https://discord.com/invite/ByRwuEEgH4)  

### 🌐 Support Multilingue

#### Pris en charge via GitHub Action (Automatisé et Toujours à Jour)

[Français](./README.md) | [Espagnol](../es/README.md) | [Chinois (Simplifié)](../zh/README.md) | [Chinois (Traditionnel, Macao)](../mo/README.md) | [Chinois (Traditionnel, Hong Kong)](../hk/README.md) | [Chinois (Traditionnel, Taïwan)](../tw/README.md) | [Japonais](../ja/README.md) | [Coréen](../ko/README.md) |  

Bienvenue dans EdgeAI pour Débutants, où la puissance des modèles de langage rencontre l'efficacité des appareils locaux. Ce cours introduit comment de petits modèles de langage optimisés (SLMs) peuvent fonctionner directement sur du matériel en périphérie—smartphones, cartes IoT et serveurs compacts—sans nécessiter d'accès au cloud. Vous découvrirez comment l'inférence en temps réel, respectueuse de la vie privée, révolutionne les maisons intelligentes, la surveillance industrielle et les applications hors ligne, grâce à des déploiements légers conçus pour la rapidité, la sécurité et la modularité.

**Edge AI**

L'Edge AI consiste à exécuter des algorithmes d'IA et des modèles de langage localement sur du matériel—près de l'endroit où les données sont générées—sans dépendre des ressources cloud pour l'inférence. Cela réduit la latence, améliore la confidentialité et permet une prise de décision en temps réel.

Principes de base :  
- Inférence sur appareil : Les modèles d'IA s'exécutent sur des appareils en périphérie (téléphones, routeurs, microcontrôleurs, PC industriels).  
- Fonctionnement hors ligne : Fonctionne sans connexion internet permanente.  
- Faible latence : Réponses immédiates adaptées aux systèmes en temps réel.  
- Souveraineté des données : Les données sensibles restent locales, améliorant la sécurité et la conformité.  

**Petits Modèles de Langage (SLMs)**  
Les SLMs comme Phi-4, Mistral-7B ou Gemma sont des versions optimisées de grands modèles de langage (LLMs)—entraînées ou distillées pour :  
- Réduire l'empreinte mémoire  
- Diminuer les besoins en calcul  
- Accélérer les temps de démarrage  

Ils offrent de puissantes capacités de traitement du langage naturel tout en respectant les contraintes de :  
- Systèmes embarqués  
- Appareils mobiles  
- Appareils IoT  
- Serveurs en périphérie avec GPU limité  
- Ordinateurs personnels  

## Architecture du Cours

### [Module 01 : Fondamentaux et Transformation de l'EdgeAI](./Module01/README.md)  
**Thème** : La transformation apportée par le déploiement de l'Edge AI  

#### Structure des Chapitres :  
- [**Section 1 : Fondamentaux de l'EdgeAI**](./Module01/01.EdgeAIFundamentals.md)  
  - Comparaison entre l'IA cloud traditionnelle et l'Edge AI  
  - Défis et contraintes de l'informatique en périphérie  
  - Technologies clés : quantification des modèles, optimisation par compression, Petits Modèles de Langage (SLMs)  
  - Accélération matérielle : NPUs, optimisation GPU, optimisation CPU  
  - Avantages : sécurité de la confidentialité, faible latence, capacités hors ligne, efficacité des coûts  

- [**Section 2 : Études de Cas Réels**](./Module01/02.RealWorldCaseStudies.md)  
  - Écosystème de modèles Microsoft Phi & Mu  
    - Phi Silica : intégration IA pour Windows  
    - Modèles Mu : micro-modèles de langage spécifiques à des tâches  
  - Étude de cas sur le système de rapport IA de Japan Airlines  
  - Impact sur le marché et orientations futures  
  - Considérations et meilleures pratiques pour le déploiement  

- [**Section 3 : Guide Pratique d'Implémentation**](./Module01/03.PracticalImplementationGuide.md)  
  - Configuration de l'environnement de développement (Python 3.10+, .NET 8+)  
  - Exigences matérielles et configurations recommandées  
  - Ressources des familles de modèles principaux  
  - Outils de quantification et d'optimisation (Llama.cpp, Microsoft Olive, Apple MLX)  
  - Liste de vérification pour l'évaluation et la validation  

- [**Section 4 : Plateformes Matérielles pour le Déploiement de l'Edge AI**](./Module01/04.EdgeDeployment.md)  
  - Considérations et exigences pour le déploiement de l'Edge AI  
  - Matériel Edge AI d'Intel et techniques d'optimisation  
  - Solutions AI de Qualcomm pour les systèmes mobiles et embarqués  
  - Plateformes NVIDIA Jetson et informatique en périphérie  
  - Plateformes PC Windows AI avec accélération NPU  
  - Stratégies d'optimisation spécifiques au matériel  

---

### [Module 02 : Bases des Petits Modèles de Langage](./Module02/README.md)  
**Thème** : Principes théoriques des SLMs, stratégies d'implémentation et déploiement en production  

#### Structure des Chapitres :  
- [**Section 1 : Fondamentaux de la Famille de Modèles Microsoft Phi**](./Module02/01.PhiFamily.md)  
  - Évolution de la philosophie de conception (Phi-1 à Phi-4)  
  - Conception architecturale axée sur l'efficacité  
  - Capacités spécialisées (raisonnement, multimodal, déploiement en périphérie)  

- [**Section 2 : Fondamentaux de la Famille Qwen**](./Module02/02.QwenFamily.md)  
  - Excellence open source (Qwen 1.0 à Qwen3) - disponible via Hugging Face  
  - Architecture avancée de raisonnement avec capacités de mode réflexion  
  - Options de déploiement évolutives (0.5B-235B paramètres)  

- [**Section 3 : Fondamentaux de la Famille Gemma**](./Module02/03.GemmaFamily.md)  
  - Innovation axée sur la recherche (Gemma 3 & 3n)  
  - Excellence multimodale  
  - Architecture mobile-first  

- [**Section 4 : Fondamentaux de la Famille BitNET**](./Module02/04.BitNETFamily.md)  
  - Technologie révolutionnaire de quantification (1.58-bit)  
  - Cadre d'inférence spécialisé depuis https://github.com/microsoft/BitNet  
  - Leadership en IA durable grâce à une efficacité extrême  

- [**Section 5 : Fondamentaux des Modèles Microsoft Mu**](./Module02/05.mumodel.md)  
  - Architecture axée sur les appareils intégrée à Windows 11  
  - Intégration système avec les Paramètres de Windows 11  
  - Fonctionnement hors ligne respectueux de la vie privée  

- [**Section 6 : Fondamentaux de Phi-Silica**](./Module02/06.phisilica.md)  
  - Architecture optimisée pour NPU intégrée aux PC Windows 11 Copilot+  
  - Efficacité exceptionnelle (650 tokens/seconde à 1.5W)  
  - Intégration pour développeurs avec le SDK Windows App  

---  

### [Module 03 : Déploiement des Petits Modèles de Langage](./Module03/README.md)  
**Thème** : Cycle complet de déploiement des SLMs, de la théorie à l'environnement de production  

#### Structure des Chapitres :  
- [**Section 1 : Apprentissage Avancé des SLMs**](./Module03/01.SLMAdvancedLearning.md)  
  - Cadre de classification des paramètres (Micro SLM 100M-1.4B, Medium SLM 14B-30B)  
  - Techniques d'optimisation avancées (méthodes de quantification, quantification 1-bit BitNET)  
  - Stratégies d'acquisition de modèles (Azure AI Foundry pour les modèles Phi, Hugging Face pour certains modèles)  

- [**Section 2 : Déploiement en Environnement Local**](./Module03/02.DeployingSLMinLocalEnv.md)  
  - Déploiement universel sur la plateforme Ollama  
  - Solutions locales de niveau entreprise avec Microsoft Foundry  
  - Analyse comparative des cadres  

- [**Section 3 : Déploiement Cloud Conteneurisé**](./Module03/03.DeployingSLMinCloud.md)  
  - Déploiement d'inférence haute performance avec vLLM  
  - Orchestration de conteneurs Ollama  
  - Implémentation optimisée pour l'edge avec ONNX Runtime  

---  

### [Module 04 : Conversion de Format et Quantification des Modèles](./Module04/README.md)  
**Thème** : Boîte à outils complète pour l'optimisation des modèles pour le déploiement en périphérie sur différentes plateformes  

#### Structure des Chapitres :  
- [**Section 1 : Bases de la Conversion de Format et de la Quantification des Modèles**](./Module04/01.Introduce.md)  
  - Cadre de classification des précisions (ultra-faible, faible, moyenne précision)  
  - Avantages et cas d'utilisation des formats GGUF et ONNX  
  - Bénéfices de la quantification pour l'efficacité opérationnelle  
  - Comparaisons des performances et empreintes mémoire  

- [**Section 2 : Guide d'Implémentation de Llama.cpp**](./Module04/02.Llamacpp.md)  
  - Installation multiplateforme (Windows, macOS, Linux)  
  - Conversion au format GGUF et niveaux de quantification (Q2_K à Q8_0)  
  - Accélération matérielle (CUDA, Metal, OpenCL, Vulkan)  
  - Intégration Python et déploiement REST API  

- [**Section 3 : Suite d'Optimisation Microsoft Olive**](./Module04/03.MicrosoftOlive.md)  
  - Optimisation des modèles adaptée au matériel avec plus de 40 composants intégrés  
  - Auto-optimisation avec quantification dynamique et statique  
  - Intégration en entreprise avec les workflows Azure ML  
  - Support des modèles populaires (Llama, Phi, certains modèles Qwen, Gemma)  

- [**Section 4 : Exploration Approfondie du Framework Apple MLX**](./Module04/04.AppleMLX.md)  
  - Architecture mémoire unifiée pour Apple Silicon  
  - Support pour LLaMA, Mistral, Phi-3, certains modèles Qwen  
  - Fine-tuning LoRA et personnalisation des modèles  
  - Intégration Hugging Face avec quantification 4-bit/8-bit  

---  

### [Module 05 : SLMOps - Opérations sur les Petits Modèles de Langage](./Module05/README.md)  
**Thème** : Cycle complet des opérations sur les SLMs, de la distillation au déploiement en production  

#### Structure des Chapitres :  
- [**Section 1 : Introduction au SLMOps**](./Module05/01.IntroduceSLMOps.md)  
  - Changement de paradigme du SLMOps dans les opérations d'IA  
  - Architecture axée sur l'efficacité des coûts et la confidentialité  
  - Impact stratégique sur les entreprises et avantages concurrentiels  
  - Défis et solutions pour les implémentations réelles  

- [**Section 2 : Distillation des Modèles - De la Théorie à la Pratique**](./Module05/02.SLMOps-Distillation.md)  
  - Transfert de connaissances des modèles enseignants aux modèles étudiants  
  - Implémentation du processus de distillation en deux étapes  
  - Workflows de distillation Azure ML avec exemples pratiques  
  - Réduction de 85 % du temps d'inférence avec une rétention de précision de 92 %  

- [**Section 3 : Fine-Tuning - Personnalisation des Modèles pour des Tâches Spécifiques**](./Module05/03.SLMOps-Finetuing.md)  
  - Techniques de fine-tuning efficaces en paramètres (PEFT)  
  - Méthodes avancées LoRA et QLoRA  
  - Implémentation de fine-tuning avec Microsoft Olive  
  - Entraînement multi-adaptateurs et optimisation des hyperparamètres  

- [**Section 4 : Déploiement - Implémentation Prête pour la Production**](./Module05/04.SLMOps.Deployment.md)  
  - Conversion et quantification des modèles pour la production  
  - Configuration de déploiement Foundry Local  
  - Validation de la qualité et benchmarking des performances  
  - Réduction de 75 % de la taille avec surveillance en production  

---  

### [Module 06 : Systèmes Agentiques SLM - Agents IA et Appels de Fonction](./Module06/README.md)  
**Thème** : Implémentation des systèmes agentiques SLM, des bases aux appels de fonction avancés et à l'intégration du Protocole de Contexte de Modèle (MCP)  

#### Structure des Chapitres :  
- [**Section 1 : Fondations des Agents IA et des Petits Modèles de Langage**](./Module06/01.IntroduceAgent.md)  
- Cadre de classification des agents (réflexe, basé sur un modèle, basé sur des objectifs, agents d'apprentissage)
- Fondamentaux des SLM et stratégies d'optimisation (GGUF, quantification, frameworks edge)
- Analyse des compromis entre SLM et LLM (réduction des coûts de 10 à 30×, efficacité des tâches de 70 à 80 %)
- Déploiement pratique avec Ollama, VLLM et solutions Microsoft edge

- [**Section 2 : Appels de fonctions dans les Small Language Models**](./Module06/02.FunctionCalling.md)
  - Mise en œuvre systématique du workflow (détection d'intention, sortie JSON, exécution externe)
  - Implémentations spécifiques aux plateformes (Phi-4-mini, modèles Qwen sélectionnés, Microsoft Foundry Local)
  - Exemples avancés (collaboration multi-agents, sélection dynamique d'outils)
  - Considérations pour la production (limitation de débit, journalisation d'audit, mesures de sécurité)

- [**Section 3 : Intégration du protocole de contexte de modèle (MCP)**](./Module06/03.IntroduceMCP.md)
  - Architecture du protocole et conception de système en couches
  - Support multi-backend (Ollama pour le développement, vLLM pour la production)
  - Protocoles de connexion (modes STDIO et SSE)
  - Applications concrètes (automatisation web, traitement de données, intégration API)

---

### [Module 07 : Échantillons d'implémentation EdgeAI](./Module07/README.md)
**Thème** : Implémentations complètes d'EdgeAI sur diverses plateformes et frameworks

#### Structure des chapitres :
- [**EdgeAI sur NVIDIA Jetson Orin Nano**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - Performance IA de 67 TOPS dans un format de la taille d'une carte de crédit
  - Support des modèles d'IA générative (transformateurs de vision, LLMs, modèles vision-langage)
  - Applications en robotique, drones, caméras intelligentes, dispositifs autonomes
  - Plateforme abordable à 249 $ pour un développement d'IA démocratisé

- [**EdgeAI dans les applications mobiles avec .NET MAUI et ONNX Runtime GenAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - IA mobile multiplateforme avec un code C# unique
  - Support de l'accélération matérielle (CPU, GPU, processeurs IA mobiles)
  - Optimisations spécifiques aux plateformes (CoreML pour iOS, NNAPI pour Android)
  - Implémentation complète de la boucle d'IA générative

- [**EdgeAI sur Azure avec le moteur Small Language Models**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - Architecture de déploiement hybride cloud-edge
  - Intégration des services Azure AI avec ONNX Runtime
  - Déploiement à l'échelle de l'entreprise et gestion continue des modèles
  - Workflows hybrides d'IA pour le traitement intelligent de documents

- [**EdgeAI avec Windows ML**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Fondation Windows AI Foundry pour une inférence performante sur appareil
  - Support matériel universel (AMD, Intel, NVIDIA, Qualcomm)
  - Abstraction et optimisation matérielle automatique
  - Framework unifié pour un écosystème matériel diversifié sous Windows

- [**EdgeAI avec les applications Foundry Local**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - Implémentation RAG axée sur la confidentialité avec des ressources locales
  - Intégration du modèle de langage Phi-3 avec recherche sémantique (modèles Phi uniquement)
  - Support des bases de données vectorielles locales (SQLite, Qdrant)
  - Capacités de souveraineté des données et fonctionnement hors ligne

## Aperçu des résultats d'apprentissage

### Résultats d'apprentissage du Module 01 :
- Comprendre les différences fondamentales entre les architectures cloud et edge AI
- Maîtriser les techniques d'optimisation de base pour le déploiement edge
- Reconnaître les applications concrètes et les histoires de réussite
- Acquérir des compétences pratiques pour implémenter des solutions EdgeAI

### Résultats d'apprentissage du Module 02 :
- Compréhension approfondie des différentes philosophies de conception des SLM et de leurs implications de déploiement
- Maîtriser les capacités de prise de décision stratégique basées sur les contraintes computationnelles et les exigences de performance
- Comprendre les compromis de flexibilité de déploiement
- Posséder des perspectives prêtes pour l'avenir sur les architectures d'IA efficaces

### Résultats d'apprentissage du Module 03 :
- Capacités stratégiques de sélection de modèles
- Maîtrise des techniques d'optimisation
- Maîtrise de la flexibilité de déploiement
- Capacités de configuration prêtes pour la production

### Résultats d'apprentissage du Module 04 :
- Compréhension approfondie des limites de quantification et des applications pratiques
- Expérience pratique avec plusieurs frameworks d'optimisation (Llama.cpp, Olive, MLX)
- Capacités de sélection d'optimisation adaptées au matériel
- Compétences de déploiement en production pour des environnements edge multiplateformes

### Résultats d'apprentissage du Module 05 :
- Maîtriser le paradigme SLMOps et les principes opérationnels
- Implémenter la distillation de modèles pour le transfert de connaissances et l'optimisation de l'efficacité
- Appliquer des techniques de fine-tuning pour la personnalisation de modèles spécifiques au domaine
- Déployer des solutions SLM prêtes pour la production avec des stratégies de surveillance et de maintenance

### Résultats d'apprentissage du Module 06 :
- Comprendre les concepts fondamentaux des agents IA et de l'architecture des Small Language Models
- Maîtriser l'implémentation des appels de fonctions sur plusieurs plateformes et frameworks
- Intégrer le protocole de contexte de modèle (MCP) pour une interaction standardisée avec des outils externes
- Construire des systèmes agentiques sophistiqués nécessitant une intervention humaine minimale

### Résultats d'apprentissage du Module 07 :
- Acquérir une expérience pratique avec diverses plateformes EdgeAI et stratégies d'implémentation
- Maîtriser les techniques d'optimisation spécifiques au matériel sur les plateformes NVIDIA, mobiles, Azure et Windows
- Comprendre les compromis de déploiement entre performance, coût et exigences de confidentialité
- Développer des compétences pratiques pour construire des applications EdgeAI concrètes dans différents écosystèmes

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
- **Benchmarks de performance** : Comparaisons détaillées de la vitesse d'inférence, de l'utilisation de la mémoire et des exigences en ressources
- **Considérations de niveau entreprise** : Pratiques de sécurité, cadres de conformité et stratégies de protection des données

## Démarrage

Chemin d'apprentissage recommandé :
1. Commencez par **Module01** pour construire une compréhension fondamentale de l'EdgeAI
2. Passez à **Module02** pour comprendre en profondeur les différentes familles de modèles SLM
3. Apprenez **Module03** pour maîtriser les compétences pratiques de déploiement
4. Continuez avec **Module04** pour une optimisation avancée des modèles et conversion de formats
5. Complétez **Module05** pour maîtriser SLMOps pour des implémentations prêtes pour la production
6. Explorez **Module06** pour comprendre les systèmes agentiques SLM et les capacités d'appel de fonctions
7. Terminez avec **Module07** pour acquérir une expérience pratique avec des échantillons d'implémentation EdgeAI diversifiés

Chaque module est conçu pour être complet indépendamment, mais un apprentissage séquentiel offrira les meilleurs résultats.

## Guide d'étude

Un [Guide d'étude](STUDY_GUIDE.md) complet est disponible pour vous aider à maximiser votre expérience d'apprentissage. Le guide d'étude fournit :

- **Chemins d'apprentissage structurés** : Calendriers optimisés pour compléter le cours en 20 heures
- **Conseils sur l'allocation du temps** : Recommandations spécifiques pour équilibrer lecture, exercices et projets
- **Focus sur les concepts clés** : Objectifs d'apprentissage prioritaires pour chaque module
- **Outils d'auto-évaluation** : Questions et exercices pour tester votre compréhension
- **Idées de mini-projets** : Applications pratiques pour renforcer votre apprentissage

Le guide d'étude est conçu pour s'adapter à un apprentissage intensif (1 semaine) ou à un apprentissage à temps partiel (3 semaines), avec des indications claires sur la façon d'allouer votre temps efficacement même si vous ne pouvez consacrer que 10 heures au cours.

---

**L'avenir de l'EdgeAI repose sur l'amélioration continue des architectures de modèles, des techniques de quantification et des stratégies de déploiement qui privilégient l'efficacité et la spécialisation plutôt que les capacités généralistes. Les organisations qui adoptent ce changement de paradigme seront bien positionnées pour exploiter le potentiel transformateur de l'IA tout en gardant le contrôle sur leurs données et leurs opérations.**

## Autres cours

Notre équipe propose d'autres cours ! Découvrez :

- [MCP pour les débutants](https://github.com/microsoft/mcp-for-beginners)
- [Agents IA pour les débutants](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [IA générative pour les débutants avec .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [IA générative pour les débutants avec JavaScript](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [IA générative pour les débutants](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [ML pour les débutants](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [Data Science pour les débutants](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [IA pour les débutants](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [Cybersécurité pour les débutants](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [Développement web pour les débutants](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [IoT pour les débutants](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [Développement XR pour les débutants](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Maîtriser GitHub Copilot pour la programmation assistée par IA](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [Maîtriser GitHub Copilot pour les développeurs C#/.NET](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [Choisissez votre propre aventure Copilot](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.