<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T12:19:47+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "fr"
}
-->
# Journal des modifications

Tous les changements notables apportés à EdgeAI for Beginners sont documentés ici. Ce projet utilise des entrées basées sur les dates et le style Keep a Changelog (Ajouté, Modifié, Corrigé, Supprimé, Documentation, Déplacé).

## 2025-09-18

### Ajouté
- Module 08 : Microsoft Foundry Local – Kit complet pour développeurs
  - Six sessions : configuration, intégration Azure AI Foundry, modèles open source, démonstrations de pointe, agents et modèles comme outils
  - Exemples exécutables sous `Module08/samples/01`–`06` avec instructions pour cmd Windows
    - `01` Chat rapide REST (`chat_quickstart.py`)
    - `02` Démarrage rapide SDK avec OpenAI/Foundry Local et support Azure OpenAI (`sdk_quickstart.py`)
    - `03` Liste et benchmark CLI (`list_and_bench.cmd`)
    - `04` Démo Chainlit (`app.py`)
    - `05` Orchestration multi-agents (`python -m samples.05.agents.coordinator`)
    - `06` Routeur pour modèles comme outils (`router.py`)
- Support Azure OpenAI dans l'exemple SDK de la session 2 avec configuration via variables d'environnement
- `.vscode/settings.json` pour pointer vers `Module08/.venv` et améliorer la résolution de l'analyse Python
- `.env` avec un indice `PYTHONPATH` pour la reconnaissance par VS Code/Pylance

### Modifié
- Modèle par défaut mis à jour en `phi-4-mini` dans les documents et exemples du Module 08 ; mentions restantes de `phi-3.5` supprimées dans le Module 08
- Améliorations du routeur (`Module08/samples/06/router.py`) :
  - Découverte des points de terminaison via `foundry service status` avec analyse regex
  - Vérification de santé `/v1/models` au démarrage
  - Registre de modèles configurable via environnement (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Exigences mises à jour : `Module08/requirements.txt` inclut désormais `openai` (en plus de `requests`, `chainlit`)
- Clarification des instructions pour l'exemple Chainlit et ajout de conseils de dépannage ; résolution des imports via les paramètres de l'espace de travail

### Corrigé
- Problèmes d'importation résolus :
  - Le routeur ne dépend plus d'un module `utils` inexistant ; les fonctions sont intégrées
  - Le coordinateur utilise un import relatif (`from .specialists import ...`) et est invoqué via le chemin du module
  - Configuration de VS Code/Pylance pour résoudre `chainlit` et les imports de packages
- Correction d'une faute de frappe mineure dans `STUDY_GUIDE.md` et ajout de la couverture du Module 08

### Supprimé
- Suppression de `Module08/infra/obs.py` inutilisé et du répertoire vide `infra/` ; les modèles d'observabilité sont conservés comme optionnels dans la documentation

### Déplacé
- Consolidation des démonstrations du Module 08 sous `Module08/samples` avec des dossiers numérotés par session
  - Déplacement de l'application Chainlit vers `samples/04`
  - Déplacement des agents vers `samples/05` et ajout de fichiers `__init__.py` pour la résolution des packages

### Documentation
- Documentation des sessions du Module 08 et enrichissement de tous les README des exemples avec des références Microsoft Learn et des fournisseurs de confiance
- Mise à jour de `Module08/README.md` avec une vue d'ensemble des exemples, la configuration du routeur et des conseils de validation
- Validation de la section Windows Foundry Local dans `Module07/README.md` par rapport aux documents Learn
- Mise à jour de `STUDY_GUIDE.md` :
  - Ajout du Module 08 à l'aperçu, aux plannings et au suivi des progrès
  - Ajout d'une section Références complète (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historique (résumé)
- Architecture du cours et modules établis (Modules 01–07)
- Modernisation itérative du contenu, standardisation du formatage et ajout d'études de cas
- Extension de la couverture des frameworks d'optimisation (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Non publié / En attente (propositions)
- Tests de validation optionnels par exemple pour vérifier la disponibilité de Foundry Local
- Revoir les traductions pour aligner les références des modèles (par ex. `phi-4-mini`) si nécessaire
- Ajouter une configuration minimale pyright si les équipes préfèrent une rigueur à l'échelle de l'espace de travail

---

