<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T10:17:17+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "fr"
}
-->
# Journal des modifications

Tous les changements notables apportés à EdgeAI pour les débutants sont documentés ici. Ce projet utilise des entrées basées sur les dates et le style Keep a Changelog (Ajouté, Modifié, Corrigé, Supprimé, Documentation, Déplacé).

## 2025-09-23

### Modifié - Modernisation majeure du Module 08
- **Alignement complet avec les modèles de dépôt Microsoft Foundry-Local**
  - Mise à jour de tous les exemples de code pour utiliser `FoundryLocalManager` et l'intégration SDK OpenAI modernes
  - Remplacement des appels manuels obsolètes `requests` par une utilisation correcte du SDK
  - Alignement des modèles d'implémentation avec la documentation officielle de Microsoft et les exemples

- **Modernisation de 05.AIPoweredAgents.md** :
  - Mise à jour de l'orchestration multi-agents pour utiliser les modèles SDK modernes
  - Amélioration de l'implémentation du coordinateur avec des fonctionnalités avancées (boucles de rétroaction, surveillance des performances)
  - Ajout d'une gestion complète des erreurs et de la vérification de la santé des services
  - Intégration de références appropriées aux exemples locaux (`samples/05/multi_agent_orchestration.ipynb`)
  - Mise à jour des exemples d'appels de fonctions pour utiliser le paramètre moderne `tools` au lieu de `functions` obsolètes
  - Ajout de modèles prêts pour la production avec surveillance et suivi des statistiques

- **Réécriture complète de 06.ModelsAsTools.md** :
  - Remplacement du registre d'outils basique par une implémentation de routage de modèles intelligente
  - Ajout de la sélection de modèles basée sur des mots-clés pour différents types de tâches (général, raisonnement, code, créatif)
  - Intégration d'une configuration basée sur l'environnement avec une attribution flexible des modèles
  - Amélioration avec une surveillance complète de la santé des services et une gestion des erreurs
  - Ajout de modèles de déploiement en production avec surveillance des requêtes et suivi des performances
  - Alignement avec l'implémentation locale dans `samples/06/router.py` et `samples/06/model_router.ipynb`

- **Améliorations de la structure de la documentation** :
  - Ajout de sections d'aperçu mettant en avant la modernisation et l'alignement SDK
  - Amélioration avec des emojis et un meilleur formatage pour une lisibilité accrue
  - Ajout de références appropriées aux fichiers d'exemples locaux dans toute la documentation
  - Inclusion de conseils d'implémentation prêts pour la production et de bonnes pratiques

### Ajouté
- Sections d'aperçu complètes dans les fichiers du Module 08 mettant en avant l'intégration SDK moderne
- Points forts de l'architecture présentant des fonctionnalités avancées (systèmes multi-agents, routage intelligent)
- Références directes aux implémentations d'exemples locaux pour une expérience pratique
- Conseils de déploiement en production avec des modèles de surveillance et de gestion des erreurs
- Exemples interactifs de notebooks Jupyter avec des fonctionnalités avancées et des benchmarks

### Corrigé
- Disparités d'alignement entre la documentation et les implémentations d'exemples réels
- Modèles d'utilisation SDK obsolètes dans tout le Module 08
- Références manquantes à la bibliothèque d'exemples locaux complète
- Approches d'implémentation incohérentes dans différentes sections

---

## 2025-09-18

### Ajouté
- Module 08 : Microsoft Foundry Local – Kit de développement complet
  - Six sessions : configuration, intégration Azure AI Foundry, modèles open-source, démonstrations de pointe, agents et modèles comme outils
  - Exemples exécutables sous `Module08/samples/01`–`06` avec instructions cmd Windows
    - `01` Chat rapide REST (`chat_quickstart.py`)
    - `02` Démarrage rapide SDK avec OpenAI/Foundry Local et support Azure OpenAI (`sdk_quickstart.py`)
    - `03` Liste et benchmark CLI (`list_and_bench.cmd`)
    - `04` Démo Chainlit (`app.py`)
    - `05` Orchestration multi-agents (`python -m samples.05.agents.coordinator`)
    - `06` Routeur de modèles comme outils (`router.py`)
- Support Azure OpenAI dans l'exemple SDK de la session 2 avec configuration des variables d'environnement
- `.vscode/settings.json` pointant vers `Module08/.venv` pour améliorer la résolution de l'analyse Python
- `.env` avec un indice `PYTHONPATH` pour la prise en charge de VS Code/Pylance

### Modifié
- Modèle par défaut mis à jour vers `phi-4-mini` dans les documents et exemples du Module 08 ; suppression des mentions restantes de `phi-3.5` dans le Module 08
- Améliorations du routeur (`Module08/samples/06/router.py`) :
  - Découverte des points de terminaison via `foundry service status` avec analyse regex
  - Vérification de la santé `/v1/models` au démarrage
  - Registre de modèles configurable via l'environnement (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Exigences mises à jour : `Module08/requirements.txt` inclut désormais `openai` (en plus de `requests`, `chainlit`)
- Conseils clarifiés pour l'exemple Chainlit et ajout de dépannage ; résolution des imports via les paramètres de l'espace de travail

### Corrigé
- Résolution des problèmes d'importation :
  - Le routeur ne dépend plus d'un module `utils` inexistant ; les fonctions sont intégrées
  - Le coordinateur utilise une importation relative (`from .specialists import ...`) et est invoqué via le chemin du module
  - Configuration VS Code/Pylance pour résoudre les imports `chainlit` et de packages
- Correction d'une petite faute de frappe dans `STUDY_GUIDE.md` et ajout de la couverture du Module 08

### Supprimé
- Suppression de `Module08/infra/obs.py` inutilisé et du répertoire vide `infra/` ; les modèles d'observabilité sont conservés comme optionnels dans la documentation

### Déplacé
- Regroupement des démonstrations du Module 08 sous `Module08/samples` avec des dossiers numérotés par session
  - Déplacement de l'application Chainlit vers `samples/04`
  - Déplacement des agents vers `samples/05` et ajout de fichiers `__init__.py` pour la résolution des packages

### Documentation
- Documentation des sessions du Module 08 et tous les fichiers README des exemples enrichis avec des références Microsoft Learn et des fournisseurs de confiance
- `Module08/README.md` mis à jour avec un aperçu des exemples, configuration du routeur et conseils de validation
- Section Windows Foundry Local de `Module07/README.md` validée par rapport aux documents Learn
- `STUDY_GUIDE.md` mis à jour :
  - Ajout du Module 08 à l'aperçu, aux calendriers, au suivi des progrès
  - Ajout d'une section Références complète (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historique (résumé)
- Architecture du cours et modules établis (Modules 01–07)
- Modernisation itérative du contenu, standardisation du formatage et ajout d'études de cas
- Couverture élargie des cadres d'optimisation (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Non publié / En attente (propositions)
- Tests de validation optionnels par exemple pour vérifier la disponibilité de Foundry Local
- Revoir les traductions pour aligner les références de modèles (par ex., `phi-4-mini`) si nécessaire
- Ajouter une configuration pyright minimale si les équipes préfèrent une rigueur à l'échelle de l'espace de travail

---

