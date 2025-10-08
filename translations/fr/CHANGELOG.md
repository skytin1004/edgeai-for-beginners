<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-08T18:51:21+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "fr"
}
-->
# Journal des modifications

Tous les changements notables apportés à EdgeAI pour les débutants sont documentés ici. Ce projet utilise des entrées basées sur les dates et le style Keep a Changelog (Ajouté, Modifié, Corrigé, Supprimé, Documentation, Déplacé).

## 2025-10-08

### Ajouté - Mise à jour complète de l'atelier
- **Réécriture complète du fichier README.md de l'atelier** :
  - Ajout d'une introduction détaillée expliquant la proposition de valeur de l'IA Edge (confidentialité, performance, coût)
  - Création de 6 objectifs d'apprentissage principaux avec des compétences détaillées
  - Ajout d'un tableau des résultats d'apprentissage avec livrables et matrice de compétences
  - Inclusion d'une section sur les compétences prêtes pour le marché pour une pertinence industrielle
  - Ajout d'un guide de démarrage rapide avec les prérequis et une configuration en 3 étapes
  - Création de tableaux de ressources pour les exemples Python (8 fichiers avec temps d'exécution)
  - Ajout d'un tableau de notebooks Jupyter (8 notebooks avec niveaux de difficulté)
  - Création d'un tableau de documentation (7 documents clés avec des conseils "Utiliser quand")
  - Ajout de recommandations de parcours d'apprentissage pour différents niveaux de compétence

- **Infrastructure de validation et de test de l'atelier** :
  - Création de `scripts/validate_samples.py` - Outil de validation complet pour la syntaxe, les imports et les bonnes pratiques
  - Création de `scripts/test_samples.py` - Exécuteur de tests rapides pour tous les exemples Python
  - Ajout de la documentation de validation au fichier `scripts/README.md`

- **Documentation complète** :
  - Création de `SAMPLES_UPDATE_SUMMARY.md` - Guide détaillé de plus de 400 lignes couvrant toutes les améliorations
  - Création de `UPDATE_COMPLETE.md` - Résumé exécutif de la mise à jour terminée
  - Création de `QUICK_REFERENCE.md` - Carte de référence rapide pour l'atelier

### Modifié - Modernisation des exemples Python de l'atelier
- **Mise à jour des 8 exemples Python avec les meilleures pratiques** :
  - Amélioration de la gestion des erreurs avec des blocs try-except autour de toutes les opérations d'E/S
  - Ajout de types hints et de docstrings détaillées
  - Mise en œuvre d'un modèle de journalisation cohérent [INFO]/[ERROR]/[RESULT]
  - Protection des imports optionnels avec des indications d'installation
  - Amélioration des retours utilisateurs dans tous les exemples

- **session01/chat_bootstrap.py** :
  - Amélioration de l'initialisation du client avec des messages d'erreur détaillés
  - Meilleure gestion des erreurs de streaming avec validation des blocs
  - Ajout d'une gestion améliorée des exceptions pour l'indisponibilité des services

- **session02/rag_pipeline.py** :
  - Ajout de protections d'import pour sentence-transformers avec des indications d'installation
  - Amélioration de la gestion des erreurs pour les opérations d'embedding et de génération
  - Formatage amélioré des résultats avec des structures claires

- **session02/rag_eval_ragas.py** :
  - Protection des imports optionnels (ragas, datasets) avec des messages d'erreur conviviaux
  - Ajout de la gestion des erreurs pour les métriques d'évaluation
  - Formatage amélioré des résultats d'évaluation

- **session03/benchmark_oss_models.py** :
  - Mise en œuvre d'une dégradation progressive (continue en cas d'échec des modèles)
  - Ajout de rapports détaillés sur la progression et de gestion des erreurs par modèle
  - Calcul des statistiques amélioré avec une récupération complète des erreurs

- **session04/model_compare.py** :
  - Ajout de type hints (types Tuple en retour)
  - Formatage amélioré des résultats avec des structures JSON
  - Mise en œuvre de la gestion des erreurs par modèle avec récupération

- **session05/agents_orchestrator.py** :
  - Amélioration de Agent.act() avec des docstrings détaillées
  - Ajout de la gestion des erreurs de pipeline avec journalisation étape par étape
  - Meilleure gestion de la mémoire et suivi de l'état

- **session06/models_router.py** :
  - Documentation des fonctions améliorée pour tous les composants de routage
  - Ajout de journalisation détaillée dans la fonction route()
  - Amélioration des résultats de test avec des structures claires

- **session06/models_pipeline.py** :
  - Ajout de la gestion des erreurs à la fonction d'assistance chat()
  - Amélioration de pipeline() avec journalisation des étapes et rapports de progression
  - Amélioration de main() avec une récupération complète des erreurs

### Documentation - Amélioration de la documentation de l'atelier
- Mise à jour du fichier README.md principal avec une section Atelier mettant en avant le parcours d'apprentissage pratique
- Amélioration de STUDY_GUIDE.md avec une section Atelier complète incluant :
  - Objectifs d'apprentissage et domaines d'étude
  - Questions d'auto-évaluation
  - Exercices pratiques avec estimations de temps
  - Allocation de temps pour étude concentrée et à temps partiel
  - Ajout de l'atelier au modèle de suivi de progression
- Mise à jour du guide d'allocation de temps de 20 heures à 30 heures (incluant l'atelier)
- Ajout de descriptions des exemples de l'atelier et des résultats d'apprentissage au README

### Corrigé
- Résolution des incohérences dans les modèles de gestion des erreurs dans les exemples de l'atelier
- Correction des erreurs d'importation de dépendances optionnelles avec des protections appropriées
- Correction des types hints manquants dans les fonctions critiques
- Résolution des retours insuffisants aux utilisateurs dans les scénarios d'erreur
- Correction des problèmes de validation avec une infrastructure de test complète

---

## 2025-09-23

### Modifié - Modernisation majeure du module 08
- **Alignement complet avec les modèles de dépôt Microsoft Foundry-Local** :
  - Mise à jour de tous les exemples de code pour utiliser le gestionnaire moderne `FoundryLocalManager` et l'intégration SDK OpenAI
  - Remplacement des appels manuels obsolètes `requests` par une utilisation correcte du SDK
  - Alignement des modèles d'implémentation avec la documentation officielle de Microsoft et les exemples

- **Modernisation de 05.AIPoweredAgents.md** :
  - Mise à jour de l'orchestration multi-agents pour utiliser des modèles SDK modernes
  - Amélioration de l'implémentation du coordinateur avec des fonctionnalités avancées (boucles de rétroaction, surveillance des performances)
  - Ajout d'une gestion complète des erreurs et de la vérification de la santé des services
  - Intégration de références appropriées aux exemples locaux (`samples/05/multi_agent_orchestration.ipynb`)
  - Mise à jour des exemples d'appels de fonctions pour utiliser le paramètre moderne `tools` au lieu de `functions` obsolètes
  - Ajout de modèles prêts pour la production avec surveillance et suivi des statistiques

- **Réécriture complète de 06.ModelsAsTools.md** :
  - Remplacement du registre d'outils basique par une implémentation de routage de modèles intelligente
  - Ajout de la sélection de modèles basée sur des mots-clés pour différents types de tâches (général, raisonnement, code, créatif)
  - Intégration d'une configuration basée sur l'environnement avec une affectation flexible des modèles
  - Amélioration avec une surveillance complète de la santé des services et gestion des erreurs
  - Ajout de modèles de déploiement en production avec surveillance des requêtes et suivi des performances
  - Alignement avec l'implémentation locale dans `samples/06/router.py` et `samples/06/model_router.ipynb`

- **Améliorations de la structure de la documentation** :
  - Ajout de sections d'aperçu mettant en avant la modernisation et l'alignement SDK
  - Amélioration avec des emojis et un meilleur formatage pour une lisibilité accrue
  - Ajout de références appropriées aux fichiers d'exemples locaux dans toute la documentation
  - Inclusion de conseils d'implémentation prêts pour la production et des meilleures pratiques

### Ajouté
- Sections d'aperçu complètes dans les fichiers du module 08 mettant en avant l'intégration SDK moderne
- Points forts de l'architecture présentant des fonctionnalités avancées (systèmes multi-agents, routage intelligent)
- Références directes aux implémentations d'exemples locaux pour une expérience pratique
- Conseils de déploiement en production avec modèles de surveillance et gestion des erreurs
- Exemples interactifs de notebooks Jupyter avec fonctionnalités avancées et benchmarks

### Corrigé
- Disparités d'alignement entre la documentation et les implémentations d'exemples réels
- Modèles d'utilisation SDK obsolètes dans tout le module 08
- Références manquantes à la bibliothèque d'exemples locaux complète
- Approches d'implémentation incohérentes dans différentes sections

---

## 2025-09-18

### Ajouté
- Module 08 : Microsoft Foundry Local – Kit complet pour développeurs
  - Six sessions : configuration, intégration Azure AI Foundry, modèles open-source, démonstrations avancées, agents et modèles comme outils
  - Exemples exécutables sous `Module08/samples/01`–`06` avec instructions cmd Windows
    - `01` Chat rapide REST (`chat_quickstart.py`)
    - `02` Démarrage rapide SDK avec OpenAI/Foundry Local et support Azure OpenAI (`sdk_quickstart.py`)
    - `03` Liste et benchmark CLI (`list_and_bench.cmd`)
    - `04` Démo Chainlit (`app.py`)
    - `05` Orchestration multi-agents (`python -m samples.05.agents.coordinator`)
    - `06` Routeur de modèles comme outils (`router.py`)
- Support Azure OpenAI dans l'exemple SDK de la session 2 avec configuration de variables d'environnement
- `.vscode/settings.json` pointant vers `Module08/.venv` pour améliorer la résolution d'analyse Python
- `.env` avec indication `PYTHONPATH` pour la prise en charge de VS Code/Pylance

### Modifié
- Modèle par défaut mis à jour vers `phi-4-mini` dans les documents et exemples du module 08 ; suppression des mentions restantes de `phi-3.5` dans le module 08
- Améliorations du routeur (`Module08/samples/06/router.py`) :
  - Découverte des points de terminaison via `foundry service status` avec analyse regex
  - Vérification de la santé `/v1/models` au démarrage
  - Registre de modèles configurable via environnement (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Exigences mises à jour : `Module08/requirements.txt` inclut désormais `openai` (avec `requests`, `chainlit`)
- Guide d'exemple Chainlit clarifié et dépannage ajouté ; résolution des imports via paramètres de l'espace de travail

### Corrigé
- Résolution des problèmes d'importation :
  - Le routeur ne dépend plus d'un module `utils` inexistant ; les fonctions sont intégrées
  - Le coordinateur utilise un import relatif (`from .specialists import ...`) et est invoqué via le chemin du module
  - Configuration VS Code/Pylance pour résoudre `chainlit` et les imports de packages
- Correction d'une faute de frappe mineure dans `STUDY_GUIDE.md` et ajout de la couverture du module 08

### Supprimé
- Suppression de `Module08/infra/obs.py` inutilisé et du répertoire vide `infra/` ; les modèles d'observabilité sont conservés comme optionnels dans la documentation

### Déplacé
- Consolidation des démonstrations du module 08 sous `Module08/samples` avec des dossiers numérotés par session
  - Déplacement de l'application Chainlit vers `samples/04`
  - Déplacement des agents vers `samples/05` et ajout de fichiers `__init__.py` pour la résolution des packages

### Documentation
- Documentation des sessions du module 08 et tous les fichiers README des exemples enrichis avec des références Microsoft Learn et des fournisseurs de confiance
- Mise à jour de `Module08/README.md` avec aperçu des exemples, configuration du routeur et conseils de validation
- Section Windows Foundry Local de `Module07/README.md` validée par rapport aux documents Learn
- Mise à jour de `STUDY_GUIDE.md` :
  - Ajout du module 08 à l'aperçu, aux plannings, au suivi de progression
  - Ajout d'une section Références complète (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historique (résumé)
- Architecture du cours et modules établis (Modules 01–07)
- Modernisation itérative du contenu, standardisation du formatage et ajout d'études de cas
- Couverture élargie des frameworks d'optimisation (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Non publié / En attente (propositions)
- Tests rapides optionnels par exemple pour valider la disponibilité de Foundry Local
- Revoir les traductions pour aligner les références aux modèles (par ex., `phi-4-mini`) si nécessaire
- Ajouter une configuration pyright minimale si les équipes préfèrent une rigueur stricte à l'échelle de l'espace de travail

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.