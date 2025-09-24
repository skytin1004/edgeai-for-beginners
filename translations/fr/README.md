<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ff006cd813df4152f5036e7b2bc5ed32",
  "translation_date": "2025-09-24T10:14:39+00:00",
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

1. **Forkez le dépôt** : Cliquez [![Forks GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
2. **Clonez le dépôt** : `git clone https://github.com/microsoft/edgeai-for-beginners.git`  
3. [**Rejoignez le Discord Azure AI Foundry et rencontrez des experts et développeurs**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 Support Multilingue

#### Supporté via GitHub Action (Automatisé & Toujours à jour)

[Arabe](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgare](../bg/README.md) | [Birman (Myanmar)](../my/README.md) | [Chinois (Simplifié)](../zh/README.md) | [Chinois (Traditionnel, Hong Kong)](../hk/README.md) | [Chinois (Traditionnel, Macao)](../mo/README.md) | [Chinois (Traditionnel, Taïwan)](../tw/README.md) | [Croate](../hr/README.md) | [Tchèque](../cs/README.md) | [Danois](../da/README.md) | [Néerlandais](../nl/README.md) | [Finnois](../fi/README.md) | [Français](./README.md) | [Allemand](../de/README.md) | [Grec](../el/README.md) | [Hébreu](../he/README.md) | [Hindi](../hi/README.md) | [Hongrois](../hu/README.md) | [Indonésien](../id/README.md) | [Italien](../it/README.md) | [Japonais](../ja/README.md) | [Coréen](../ko/README.md) | [Malais](../ms/README.md) | [Marathi](../mr/README.md) | [Népalais](../ne/README.md) | [Norvégien](../no/README.md) | [Persan (Farsi)](../fa/README.md) | [Polonais](../pl/README.md) | [Portugais (Brésil)](../br/README.md) | [Portugais (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Roumain](../ro/README.md) | [Russe](../ru/README.md) | [Serbe (Cyrillique)](../sr/README.md) | [Slovaque](../sk/README.md) | [Slovène](../sl/README.md) | [Espagnol](../es/README.md) | [Swahili](../sw/README.md) | [Suédois](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Thaï](../th/README.md) | [Turc](../tr/README.md) | [Ukrainien](../uk/README.md) | [Ourdou](../ur/README.md) | [Vietnamien](../vi/README.md)

**Si vous souhaitez ajouter des langues supplémentaires, les langues supportées sont listées [ici](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Introduction

Bienvenue dans **EdgeAI pour les Débutants** – votre parcours complet dans le monde transformateur de l'Intelligence Artificielle en périphérie. Ce cours relie les capacités puissantes de l'IA à des déploiements pratiques et réels sur des appareils en périphérie, vous permettant de tirer parti du potentiel de l'IA directement là où les données sont générées et où les décisions doivent être prises.

### Ce que vous allez maîtriser

Ce cours vous guide des concepts fondamentaux aux implémentations prêtes pour la production, couvrant :
- **Modèles de Langage Réduits (SLMs)** optimisés pour le déploiement en périphérie
- **Optimisation adaptée au matériel** sur diverses plateformes
- **Inférence en temps réel** avec des capacités de préservation de la vie privée
- **Stratégies de déploiement en production** pour des applications d'entreprise

### Pourquoi EdgeAI est important

Edge AI représente un changement de paradigme qui répond à des défis modernes critiques :
- **Confidentialité & Sécurité** : Traitez les données sensibles localement sans les exposer au cloud
- **Performance en temps réel** : Éliminez la latence réseau pour les applications critiques
- **Efficacité des coûts** : Réduisez les dépenses de bande passante et de calcul dans le cloud
- **Opérations résilientes** : Maintenez la fonctionnalité en cas de panne réseau
- **Conformité réglementaire** : Respectez les exigences de souveraineté des données

### Edge AI

Edge AI désigne l'exécution d'algorithmes d'IA et de modèles de langage localement sur du matériel, près de l'endroit où les données sont générées, sans dépendre des ressources cloud pour l'inférence. Cela réduit la latence, améliore la confidentialité et permet une prise de décision en temps réel.

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

## Modules du cours & Navigation

| Module | Sujet | Domaine d'intérêt | Contenu clé | Niveau | Durée |
|--------|-------|-------------------|-------------|--------|-------|
| [📚 01](../../Module01) | [Fondamentaux de EdgeAI](./Module01/README.md) | Comparaison Cloud vs Edge AI | Fondamentaux de EdgeAI • Études de cas réels • Guide d'implémentation • Déploiement en périphérie | Débutant | 3-4 h |
| [🧠 02](../../Module02) | [Fondations des modèles SLM](./Module02/README.md) | Familles de modèles & architecture | Famille Phi • Famille Qwen • Famille Gemma • BitNET • μModel • Phi-Silica | Débutant | 4-5 h |
| [🚀 03](../../Module03) | [Pratique de déploiement SLM](./Module03/README.md) | Déploiement local & cloud | Apprentissage avancé • Environnement local • Déploiement cloud | Intermédiaire | 4-5 h |
| [⚙️ 04](../../Module04) | [Kit d'optimisation des modèles](./Module04/README.md) | Optimisation multiplateforme | Introduction • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Synthèse de workflow | Intermédiaire | 5-6 h |
| [🔧 05](../../Module05) | [SLMOps Production](./Module05/README.md) | Opérations de production | Introduction à SLMOps • Distillation de modèles • Ajustement fin • Déploiement en production | Avancé | 5-6 h |
| [🤖 06](../../Module06) | [Agents IA & Appels de fonctions](./Module06/README.md) | Cadres d'agents & MCP | Introduction aux agents • Appels de fonctions • Protocole de contexte de modèle | Avancé | 4-5 h |
| [💻 07](../../Module07) | [Implémentation sur plateforme](./Module07/README.md) | Échantillons multiplateformes | Kit d'outils IA • Foundry Local • Développement Windows | Avancé | 3-4 h |
| [🏭 08](../../Module08) | [Kit d'outils Foundry Local](./Module08/README.md) | Échantillons prêts pour la production | Applications d'exemple (voir détails ci-dessous) | Expert | 8-10 h |

### 🏭 **Module 08 : Applications d'exemple**

- [01 : Démarrage rapide REST Chat](./Module08/samples/01/README.md)  
- [02 : Intégration SDK OpenAI](./Module08/samples/02/README.md)  
- [03 : Découverte & Benchmarking de modèles](./Module08/samples/03/README.md)  
- [04 : Application Chainlit RAG](./Module08/samples/04/README.md)  
- [05 : Orchestration multi-agents](./Module08/samples/05/README.md)  
- [06 : Routeur Models-as-Tools](./Module08/samples/06/README.md)  
- [07 : Client API direct](./Module08/samples/07/README.md)  
- [08 : Application Chat Windows 11](./Module08/samples/08/README.md)  
- [09 : Système multi-agents avancé](./Module08/samples/09/README.md)  
- [10 : Cadre d'outils Foundry](./Module08/samples/10/README.md)  

### 📊 **Résumé du parcours d'apprentissage**
- **Durée totale** : 36-45 heures  
- **Parcours Débutant** : Modules 01-02 (7-9 heures)  
- **Parcours Intermédiaire** : Modules 03-04 (9-11 heures)  
- **Parcours Avancé** : Modules 05-07 (12-15 heures)  
- **Parcours Expert** : Module 08 (8-10 heures)  

## Ce que vous allez construire

### 🎯 Compétences clés
- **Architecture Edge AI** : Concevoir des systèmes IA locaux avec intégration cloud  
- **Optimisation de modèles** : Quantifier et compresser les modèles pour le déploiement en périphérie (85 % de gain de vitesse, 75 % de réduction de taille)  
- **Déploiement multiplateforme** : Windows, mobile, embarqué, et systèmes hybrides cloud-périphérie  
- **Opérations de production** : Surveillance, mise à l'échelle et maintenance de l'IA en périphérie en production  

### 🏗️ Projets pratiques
- **Applications de chat Foundry Local** : Application native Windows 11 avec changement de modèle  
- **Systèmes multi-agents** : Coordinateur avec agents spécialisés pour des workflows complexes  
- **Applications RAG** : Traitement local de documents avec recherche vectorielle  
- **Routeurs de modèles** : Sélection intelligente entre modèles selon l'analyse des tâches  
- **Cadres API** : Clients prêts pour la production avec streaming et surveillance de la santé  
- **Outils multiplateformes** : Modèles d'intégration LangChain/Semantic Kernel  

### 🏢 Applications industrielles
**Fabrication** • **Santé** • **Véhicules autonomes** • **Villes intelligentes** • **Applications mobiles**

## Démarrage rapide

**Parcours d'apprentissage recommandé** (20-30 heures au total) :

1. **📚 Fondations** (Modules 01-02) : Concepts EdgeAI + familles de modèles SLM  
2. **⚙️ Optimisation** (Modules 03-04) : Déploiement + cadres de quantification  
3. **🚀 Production** (Modules 05-06) : SLMOps + agents IA + appels de fonctions  
4. **💻 Implémentation** (Modules 07-08) : Échantillons de plateforme + kit d'outils Foundry Local  

Chaque module inclut théorie, exercices pratiques et échantillons de code prêts pour la production.

## Impact sur la carrière
**Rôles techniques** : Architecte de solutions EdgeAI • Ingénieur ML (Edge) • Développeur IoT AI • Développeur Mobile AI

**Secteurs d'industrie** : Industrie 4.0 • Technologies de la santé • Systèmes autonomes • FinTech • Électronique grand public

**Projets de portfolio** : Systèmes multi-agents • Applications RAG en production • Déploiement multiplateforme • Optimisation des performances

## Structure du dépôt

```
edgeai-for-beginners/
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## Points forts du cours

✅ **Apprentissage progressif** : Théorie → Pratique → Déploiement en production  
✅ **Études de cas réelles** : Microsoft, Japan Airlines, implémentations en entreprise  
✅ **Exemples pratiques** : Plus de 50 exemples, 10 démonstrations complètes Foundry Local  
✅ **Focus sur les performances** : Améliorations de vitesse de 85 %, réductions de taille de 75 %  
✅ **Multiplateforme** : Windows, mobile, embarqué, hybride cloud-edge  
✅ **Prêt pour la production** : Surveillance, mise à l'échelle, sécurité, cadres de conformité

📖 **[Guide d'étude disponible](STUDY_GUIDE.md)** : Parcours d'apprentissage structuré de 20 heures avec des conseils sur la gestion du temps et des outils d'auto-évaluation.

---

**EdgeAI représente l'avenir du déploiement de l'IA** : local d'abord, respectueux de la vie privée et efficace. Maîtrisez ces compétences pour créer la prochaine génération d'applications intelligentes.

## Autres cours

Notre équipe propose d'autres cours ! Découvrez :

- [MCP pour débutants](https://github.com/microsoft/mcp-for-beginners)  
- [Agents IA pour débutants](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [IA générative pour débutants avec .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
- [IA générative pour débutants avec JavaScript](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)  
- [IA générative pour débutants](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [ML pour débutants](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
- [Science des données pour débutants](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
- [IA pour débutants](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
- [Cybersécurité pour débutants](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)  
- [Développement web pour débutants](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
- [IoT pour débutants](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
- [Développement XR pour débutants](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [Maîtriser GitHub Copilot pour la programmation assistée par IA](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
- [Maîtriser GitHub Copilot pour les développeurs C#/.NET](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
- [Choisissez votre propre aventure Copilot](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  

---

