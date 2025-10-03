<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:20:59+00:00",
  "source_file": "AGENTS.md",
  "language_code": "fr"
}
-->
# AGENTS.md

## Aperçu du projet

EdgeAI for Beginners est un dépôt éducatif complet qui enseigne le développement de l'IA Edge avec des modèles de langage réduits (SLMs). Le cours couvre les fondamentaux de l'EdgeAI, le déploiement de modèles, les techniques d'optimisation et les implémentations prêtes pour la production en utilisant Microsoft Foundry Local et divers frameworks d'IA.

**Technologies clés :**
- Python 3.8+ (langage principal pour les exemples d'IA/ML)
- .NET C# (exemples d'IA/ML)
- JavaScript/Node.js avec Electron (pour les applications de bureau)
- SDK Microsoft Foundry Local
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Frameworks d'IA : LangChain, Semantic Kernel, Chainlit
- Optimisation de modèles : Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Type de dépôt :** Contenu éducatif avec 8 modules et 10 applications d'exemple complètes

**Architecture :** Parcours d'apprentissage multi-modules avec des exemples pratiques démontrant les modèles de déploiement de l'IA Edge

## Structure du dépôt

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Commandes d'installation

### Configuration du dépôt

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Configuration des exemples Python (Module08 et exemples Python)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Configuration des exemples Node.js (Exemple 08 - Application de chat Windows)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Configuration de Foundry Local

Foundry Local est requis pour exécuter les exemples du Module08 :

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Flux de travail de développement

### Développement de contenu

Ce dépôt contient principalement du **contenu éducatif en Markdown**. Lors de modifications :

1. Modifiez les fichiers `.md` dans les répertoires de modules appropriés
2. Suivez les modèles de formatage existants
3. Assurez-vous que les exemples de code sont précis et testés
4. Mettez à jour le contenu traduit correspondant si nécessaire (ou laissez l'automatisation s'en charger)

### Développement des applications d'exemple

Pour les exemples Python (exemples 01-07, 09-10) :
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Pour l'exemple Electron (exemple 08) :
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Test des applications d'exemple

Les exemples Python n'ont pas de tests automatisés mais peuvent être validés en les exécutant :
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

L'exemple Electron dispose d'une infrastructure de test :
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Instructions de test

### Validation du contenu

Le dépôt utilise des flux de travail de traduction automatisés. Aucun test manuel requis pour les traductions.

**Validation manuelle des modifications de contenu :**
1. Prévisualisez le rendu Markdown des fichiers `.md` modifiés
2. Vérifiez que tous les liens pointent vers des cibles valides
3. Testez les extraits de code inclus dans la documentation
4. Vérifiez que les images se chargent correctement

### Test des applications d'exemple

**Module08/samples/08 (application Electron) dispose de tests complets :**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Les exemples Python doivent être testés manuellement :**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Directives de style de code

### Contenu Markdown

- Utilisez une hiérarchie cohérente des titres (# pour le titre, ## pour les sections principales, ### pour les sous-sections)
- Incluez des blocs de code avec des spécificateurs de langage : ```python, ```bash, ```javascript
- Suivez le formatage existant pour les tableaux, listes et emphases
- Gardez les lignes lisibles (visez ~80-100 caractères, mais sans contrainte stricte)
- Utilisez des liens relatifs pour les références internes

### Style de code Python

- Suivez les conventions PEP 8
- Utilisez des annotations de type lorsque c'est approprié
- Incluez des docstrings pour les fonctions et classes
- Utilisez des noms de variables significatifs
- Gardez les fonctions ciblées et concises

### Style de code JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Conventions clés :**
- Configuration ESLint fournie dans l'exemple 08
- Prettier pour le formatage du code
- Utilisez la syntaxe moderne ES6+
- Suivez les modèles existants dans la base de code

## Directives pour les pull requests

### Format du titre
```
[ModuleXX] Brief description of change
```
ou
```
[Module08/samples/XX] Description for sample changes
```

### Avant de soumettre

**Pour les modifications de contenu :**
- Prévisualisez tous les fichiers Markdown modifiés
- Vérifiez que les liens et les images fonctionnent
- Recherchez les fautes de frappe et les erreurs grammaticales

**Pour les modifications de code des exemples (Module08/samples/08) :**
```bash
npm run lint
npm test
```

**Pour les modifications des exemples Python :**
- Testez que l'exemple s'exécute correctement
- Vérifiez que la gestion des erreurs fonctionne
- Assurez la compatibilité avec Foundry Local

### Processus de révision

- Les modifications de contenu éducatif sont examinées pour leur précision et leur clarté
- Les exemples de code sont testés pour leur fonctionnalité
- Les mises à jour de traduction sont gérées automatiquement par GitHub Actions

## Système de traduction

**IMPORTANT :** Ce dépôt utilise une traduction automatisée via GitHub Actions.

- Les traductions se trouvent dans le répertoire `/translations/` (50+ langues)
- Automatisé via le workflow `co-op-translator.yml`
- **NE PAS modifier manuellement les fichiers de traduction** - ils seront écrasés
- Modifiez uniquement les fichiers sources en anglais dans les répertoires racine et de modules
- Les traductions sont générées automatiquement lors des pushs vers la branche `main`

## Intégration de Foundry Local

La plupart des exemples du Module08 nécessitent que Microsoft Foundry Local soit en cours d'exécution :

### Démarrage de Foundry Local
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### Vérification de Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Variables d'environnement pour les exemples

La plupart des exemples utilisent ces variables d'environnement :
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Construction et déploiement

### Déploiement de contenu

Ce dépôt est principalement de la documentation - aucun processus de construction requis pour le contenu.

### Construction des applications d'exemple

**Application Electron (Module08/samples/08) :**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Exemples Python :**
Pas de processus de construction - les exemples sont exécutés directement avec l'interpréteur Python.

## Problèmes courants et dépannage

### Foundry Local non démarré
**Problème :** Les exemples échouent avec des erreurs de connexion

**Solution :**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Problèmes avec l'environnement virtuel Python
**Problème :** Erreurs d'importation de module

**Solution :**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Problèmes de construction Electron
**Problème :** Échecs lors de l'installation ou de la construction avec npm

**Solution :**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Conflits dans le workflow de traduction
**Problème :** Les PR de traduction entrent en conflit avec vos modifications

**Solution :**
- Modifiez uniquement les fichiers sources en anglais
- Laissez le workflow de traduction automatisé gérer les traductions
- En cas de conflit, fusionnez `main` dans votre branche après la fusion des traductions

## Ressources supplémentaires

### Parcours d'apprentissage
- **Parcours débutant :** Modules 01-02 (7-9 heures)
- **Parcours intermédiaire :** Modules 03-04 (9-11 heures)
- **Parcours avancé :** Modules 05-07 (12-15 heures)
- **Parcours expert :** Module 08 (8-10 heures)

### Contenu clé des modules
- **Module01 :** Fondamentaux de l'EdgeAI et études de cas réels
- **Module02 :** Familles et architectures des modèles de langage réduits (SLM)
- **Module03 :** Stratégies de déploiement local et cloud
- **Module04 :** Optimisation de modèles avec plusieurs frameworks
- **Module05 :** SLMOps - opérations en production
- **Module06 :** Agents d'IA et appels de fonctions
- **Module07 :** Implémentations spécifiques à la plateforme
- **Module08 :** Outils Foundry Local avec 10 exemples complets

### Dépendances externes
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Runtime local pour modèles d'IA
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Framework d'optimisation
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Outil d'optimisation de modèles
- [OpenVINO](https://docs.openvino.ai/) - Toolkit d'optimisation d'Intel

## Notes spécifiques au projet

### Applications d'exemple du Module08

Le dépôt inclut 10 applications d'exemple complètes :

1. **01-REST Chat Quickstart** - Intégration basique du SDK OpenAI
2. **02-OpenAI SDK Integration** - Fonctionnalités avancées du SDK
3. **03-Model Discovery & Benchmarking** - Outils de comparaison de modèles
4. **04-Chainlit RAG Application** - Génération augmentée par récupération
5. **05-Multi-Agent Orchestration** - Coordination basique des agents
6. **06-Models-as-Tools Router** - Routage intelligent des modèles
7. **07-Direct API Client** - Intégration API bas-niveau
8. **08-Windows 11 Chat App** - Application de bureau native Electron
9. **09-Advanced Multi-Agent System** - Orchestration complexe des agents
10. **10-Foundry Tools Framework** - Intégration LangChain/Semantic Kernel

Chaque exemple démontre différents aspects du développement de l'IA Edge avec Foundry Local.

### Considérations de performance

- Les SLMs sont optimisés pour le déploiement Edge (2-16GB RAM)
- L'inférence locale offre des temps de réponse de 50-500ms
- Les techniques de quantification réduisent la taille de 75% tout en conservant 85% des performances
- Capacités de conversation en temps réel avec des modèles locaux

### Sécurité et confidentialité

- Tout le traitement se fait localement - aucune donnée n'est envoyée au cloud
- Convient aux applications sensibles à la confidentialité (santé, finance)
- Répond aux exigences de souveraineté des données
- Foundry Local fonctionne entièrement sur du matériel local

---

**Ce dépôt éducatif est axé sur l'enseignement du développement de l'IA Edge. Le modèle de contribution principal consiste à améliorer le contenu éducatif et à ajouter/améliorer les applications d'exemple qui démontrent les concepts de l'IA Edge.**

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.