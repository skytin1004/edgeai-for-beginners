<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T12:20:30+00:00",
  "source_file": "Module08/README.md",
  "language_code": "fr"
}
-->
# Module 08 : Prise en main de Microsoft Foundry Local - Kit complet pour développeurs

## Vue d'ensemble

Microsoft Foundry Local représente la nouvelle génération de développement IA en périphérie, offrant aux développeurs des outils puissants pour créer, déployer et étendre des applications IA localement tout en assurant une intégration fluide avec Azure AI Foundry. Ce module couvre en détail Foundry Local, de l'installation au développement avancé d'agents.

**Technologies clés :**
- CLI et SDK Microsoft Foundry Local
- Intégration avec Azure AI Foundry
- Inférence de modèles sur appareil
- Mise en cache et optimisation des modèles locaux
- Architectures basées sur des agents

## Objectifs d'apprentissage du module

En complétant ce module, vous serez capable de :

- **Maîtriser la configuration de Foundry Local** : Installer, configurer et optimiser Foundry Local pour le développement sous Windows 11
- **Déployer divers modèles** : Exécuter localement les modèles phi, qwen, deepseek et GPT-OSS-20B via des commandes CLI
- **Créer des solutions de production** : Développer des applications IA avec ingénierie avancée des prompts et intégration des données
- **Exploiter l'écosystème open-source** : Intégrer des modèles Hugging Face et des contributions communautaires
- **Comparer les architectures IA** : Comprendre les compromis entre LLMs et SLMs et les stratégies de déploiement
- **Développer des agents IA** : Construire des agents intelligents en utilisant l'architecture et les capacités de Foundry Local
- **Implémenter des modèles comme outils** : Créer des solutions IA modulaires et personnalisables pour les applications d'entreprise

## Structure des sessions

### [1 : Prise en main de Foundry Local](./01.FoundryLocalSetup.md)
**Focus** : Installation, configuration CLI, mise en cache des modèles et accélération matérielle

**Ce que vous apprendrez :**
- Installation complète de Foundry Local sous Windows 11
- Configuration CLI et structure des commandes
- Stratégies de mise en cache des modèles pour des performances optimales
- Configuration et optimisation de l'accélération matérielle
- Déploiement pratique des modèles phi, qwen, deepseek et GPT-OSS-20B

**Durée** : 2-3 heures  
**Prérequis** : Windows 11, connaissances de base en ligne de commande

---

### [2 : Construire des solutions IA avec Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Focus** : Ingénierie avancée des prompts, intégration des données et tâches exploitables

**Ce que vous apprendrez :**
- Techniques avancées d'ingénierie des prompts
- Modèles d'intégration des données et meilleures pratiques
- Création de tâches IA exploitables avec Foundry Local
- Flux de travail d'intégration fluide avec Azure AI Foundry
- Optimisation des performances et surveillance

**Durée** : 2-3 heures  
**Prérequis** : Session 1 terminée, compte Azure (optionnel)

---

### [3 : Modèles open-source avec Foundry Local](./03.OpenSourceModels.md)
**Focus** : Intégration Hugging Face, stratégies de sélection de modèles et ajouts communautaires

**Ce que vous apprendrez :**
- Intégration des modèles Hugging Face avec Foundry Local
- Stratégies et implémentation "Bring-your-own-model" (BYOM)
- Aperçus de la série Model Mondays et contributions communautaires
- Déploiement et optimisation de modèles personnalisés
- Critères d'évaluation et de sélection des modèles communautaires

**Durée** : 2-3 heures  
**Prérequis** : Sessions 1-2 terminées, compte Hugging Face

---

### [4 : Explorer les modèles de pointe - LLMs, SLMs et inférence sur appareil](./04.CuttingEdgeModels.md)
**Focus** : Comparaison des modèles, EdgeAI avec Phi et ONNX Runtime, démonstrations avancées

**Ce que vous apprendrez :**
- Comparaison complète entre LLMs et SLMs et cas d'utilisation
- Compromis entre inférence locale et cloud et cadres décisionnels
- Implémentation EdgeAI avec Phi et ONNX Runtime
- Développement et déploiement de l'application Chainlit RAG Chat
- Techniques d'optimisation de l'inférence WebGPU
- Intégration et capacités du SDK AI PC

**Durée** : 3-4 heures  
**Prérequis** : Sessions 1-3 terminées, compréhension des concepts d'inférence

---

### [5 : Construire rapidement des agents IA avec Foundry Local](./05.AIPoweredAgents.md)
**Focus** : Développement rapide d'applications GenAI, prompts système, grounding et architectures d'agents

**Ce que vous apprendrez :**
- Architecture et modèles de conception des agents Foundry Local
- Ingénierie des prompts système pour le comportement des agents
- Techniques de grounding pour des réponses fiables des agents
- Flux de travail de développement rapide d'applications GenAI
- Orchestration des agents et systèmes multi-agents
- Stratégies de déploiement en production pour les agents IA

**Durée** : 3-4 heures  
**Prérequis** : Sessions 1-4 terminées, compréhension de base des agents IA

---

### [6 : Foundry Local - Modèles comme outils](./06.ModelsAsTools.md)
**Focus** : Solutions IA modulaires, déploiement sur appareil et mise à l'échelle en entreprise

**Ce que vous apprendrez :**
- Considérer les modèles IA comme des outils modulaires et personnalisables
- Déploiement sur appareil sans dépendance au cloud
- Inférence à faible latence, économique et respectueuse de la vie privée
- Modèles d'intégration SDK, API et CLI
- Personnalisation des modèles pour des cas d'utilisation spécifiques
- Stratégies de mise à l'échelle de local à Azure AI Foundry
- Architectures d'applications IA prêtes pour l'entreprise

**Durée** : 3-4 heures  
**Prérequis** : Toutes les sessions précédentes, expérience en développement d'entreprise utile

## Prérequis

### Configuration système
- **Système d'exploitation** : Windows 11 (22H2 ou version ultérieure)
- **Mémoire** : 16 Go de RAM (32 Go recommandés pour les modèles volumineux)
- **Stockage** : 50 Go d'espace libre pour la mise en cache des modèles
- **Matériel** : Appareil avec NPU recommandé (PC Copilot+), GPU optionnel
- **Réseau** : Internet haut débit pour le téléchargement initial des modèles

### Environnement de développement
- Visual Studio Code avec extension AI Toolkit
- Python 3.10+ et pip
- Git pour le contrôle de version
- PowerShell ou Command Prompt
- Azure CLI (optionnel pour l'intégration cloud)

### Connaissances requises
- Compréhension de base des concepts IA/ML
- Familiarité avec la ligne de commande
- Bases de la programmation Python
- Concepts REST API
- Connaissances de base sur les prompts et l'inférence des modèles

## Chronologie du module

**Temps total estimé** : 15-20 heures

| Session | Domaine d'étude | Temps | Complexité |
|---------|-----------------|-------|------------|
|  1 | Configuration & Bases | 2-3 heures | Débutant |
|  2 | Solutions IA | 2-3 heures | Intermédiaire |
|  3 | Open Source | 2-3 heures | Intermédiaire |
|  4 | Modèles avancés | 3-4 heures | Avancé |
|  5 | Agents IA | 3-4 heures | Avancé |
|  6 | Outils d'entreprise | 3-4 heures | Expert |

## Ressources clés

### Documentation principale
- [GitHub Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local)
- [Documentation Azure AI Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Série Model Mondays](https://aka.ms/model-mondays)

### Ressources communautaires
- [Discussions communautaires Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Exemples Azure AI Foundry](https://github.com/Azure-Samples/ai-foundry)
- [Communauté des développeurs IA Microsoft](https://techcommunity.microsoft.com/category/artificialintelligence)

## Résultats d'apprentissage

En complétant ce module, vous serez capable de :

### Maîtrise technique
- **Déployer et gérer** : Installations Foundry Local dans des environnements de développement et de production
- **Intégrer des modèles** : Travailler sans effort avec des familles de modèles variées de Microsoft, Hugging Face et sources communautaires
- **Créer des applications** : Développer des applications IA prêtes pour la production avec des fonctionnalités avancées et des optimisations
- **Développer des agents** : Implémenter des agents IA sophistiqués avec grounding, raisonnement et intégration d'outils

### Compréhension stratégique
- **Décisions architecturales** : Faire des choix éclairés entre déploiement local et cloud
- **Optimisation des performances** : Optimiser les performances d'inférence sur différentes configurations matérielles
- **Mise à l'échelle en entreprise** : Concevoir des applications évolutives, des prototypes locaux aux déploiements en entreprise
- **Confidentialité et sécurité** : Implémenter des solutions IA respectueuses de la vie privée avec inférence locale

### Capacités d'innovation
- **Prototypage rapide** : Construire et tester rapidement des concepts d'application IA
- **Intégration communautaire** : Exploiter des modèles open-source et contribuer à l'écosystème
- **Modèles avancés** : Implémenter des modèles IA de pointe, y compris RAG, agents et intégration d'outils
- **Développement prêt pour l'avenir** : Créer des applications prêtes pour les technologies et modèles IA émergents

## Prise en main

1. **Préparez votre environnement** : Assurez-vous d'avoir Windows 11 avec les spécifications matérielles recommandées
2. **Installez les prérequis** : Configurez les outils de développement et les dépendances
3. **Commencez par la session 1** : Débutez avec l'installation et la configuration de Foundry Local
4. **Progressez séquentiellement** : Complétez les sessions dans l'ordre pour une progression optimale
5. **Pratiquez continuellement** : Appliquez les concepts via des exercices pratiques et des projets

## Indicateurs de réussite

Suivez votre progression dans le module :

- [ ] Installer et configurer Foundry Local avec succès
- [ ] Déployer et exécuter au moins 4 familles de modèles différentes
- [ ] Construire une solution IA complète avec intégration des données
- [ ] Intégrer au moins 2 modèles open-source
- [ ] Créer une application de chat RAG fonctionnelle
- [ ] Développer et déployer un agent IA
- [ ] Implémenter une architecture "modèles comme outils"

## Démarrage rapide pour les exemples

### 1) Configuration de l'environnement (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Démarrer un modèle local (nouveau terminal)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Exécuter la démo Chainlit (Session 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Exécuter le coordinateur multi-agents (Session 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Si vous voyez des erreurs de connexion, validez Foundry Local :
```cmd
curl http://localhost:8000/v1/models
```

### Configuration du routeur (Session 6)
Le routeur effectue une vérification rapide de l'état et prend en charge la configuration basée sur l'environnement :
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Ce module représente l'avant-garde du développement IA en périphérie, combinant les outils de qualité entreprise de Microsoft avec la flexibilité et l'innovation de l'écosystème open-source. En maîtrisant Foundry Local, vous serez positionné à la pointe du développement d'applications IA.

Pour Azure OpenAI (Session 2), consultez le README des exemples pour les variables d'environnement requises et les paramètres de version API.

## Aperçu des exemples

- `samples/01` : Chat REST rapide avec Foundry Local (`chat_quickstart.py`).
- `samples/02` : Intégration SDK OpenAI (`sdk_quickstart.py`).
- `samples/03` : Découverte de modèles + benchmark rapide (`list_and_bench.cmd`).
- `samples/04` : Démo Chainlit RAG (`app.py`).
- `samples/05` : Orchestration multi-agents (`python -m samples.05.agents.coordinator`).
- `samples/06` : Routeur "Modèles comme outils" (`python samples\06\router.py`).

---

