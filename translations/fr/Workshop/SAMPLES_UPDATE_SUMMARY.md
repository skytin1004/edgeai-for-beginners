<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-08T19:26:50+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "fr"
}
-->
# Échantillons de l'atelier - Résumé de la mise à jour du SDK local Foundry

## Aperçu

Tous les exemples Python dans le répertoire `Workshop/samples` ont été mis à jour pour suivre les meilleures pratiques du SDK local Foundry et garantir une cohérence dans l'atelier.

**Date** : 8 octobre 2025  
**Portée** : 9 fichiers Python répartis sur 6 sessions d'atelier  
**Objectif principal** : Gestion des erreurs, documentation, modèles SDK, expérience utilisateur

---

## Fichiers mis à jour

### Session 01 : Premiers pas
- ✅ `chat_bootstrap.py` - Exemples de base de chat et de streaming

### Session 02 : Solutions RAG
- ✅ `rag_pipeline.py` - Implémentation RAG avec embeddings
- ✅ `rag_eval_ragas.py` - Évaluation RAG avec les métriques RAGAS

### Session 03 : Modèles open source
- ✅ `benchmark_oss_models.py` - Benchmarking multi-modèles

### Session 04 : Modèles de pointe
- ✅ `model_compare.py` - Comparaison SLM vs LLM

### Session 05 : Agents alimentés par l'IA
- ✅ `agents_orchestrator.py` - Coordination multi-agents

### Session 06 : Modèles comme outils
- ✅ `models_router.py` - Routage basé sur l'intention
- ✅ `models_pipeline.py` - Pipeline multi-étapes routé

### Infrastructure de support
- ✅ `workshop_utils.py` - Déjà conforme aux meilleures pratiques (aucun changement nécessaire)

---

## Améliorations clés

### 1. Gestion des erreurs améliorée

**Avant :**
```python
manager, client, model_id = get_client(alias)
```

**Après :**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Avantages :**
- Gestion des erreurs fluide avec des messages clairs
- Indications de dépannage exploitables
- Codes de sortie appropriés pour les scripts

### 2. Meilleure gestion des imports

**Avant :**
```python
from sentence_transformers import SentenceTransformer
```

**Après :**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Avantages :**
- Instructions claires lorsque des dépendances manquent
- Évite les erreurs d'importation cryptiques
- Instructions d'installation conviviales

### 3. Documentation complète

**Ajoutée à tous les exemples :**
- Documentation des variables d'environnement dans les docstrings
- Liens de référence SDK
- Exemples d'utilisation
- Documentation détaillée des fonctions/paramètres
- Indications de type pour un meilleur support IDE

**Exemple :**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. Meilleur retour utilisateur

**Ajout de journaux informatifs :**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Indicateurs de progression :**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Sortie structurée :**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Benchmarking robuste

**Améliorations de la session 03 :**
- Gestion des erreurs par modèle (continue en cas d'échec)
- Rapport de progression détaillé
- Exécution correcte des tours de préchauffage
- Prise en charge de la mesure de latence du premier jeton
- Séparation claire des étapes

### 6. Indications de type cohérentes

**Ajoutées partout :**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Avantages :**
- Meilleure autocomplétion IDE
- Détection précoce des erreurs
- Code auto-documenté

### 7. Routeur de modèles amélioré

**Améliorations de la session 06 :**
- Documentation complète de la détection d'intention
- Explication de l'algorithme de sélection de modèles
- Journaux détaillés de routage
- Formatage des résultats de test
- Récupération des erreurs dans les tests par lot

### 8. Orchestration multi-agents

**Améliorations de la session 05 :**
- Rapport de progression étape par étape
- Gestion des erreurs par agent
- Structure claire du pipeline
- Documentation améliorée de la gestion de la mémoire

---

## Liste de contrôle des tests

### Prérequis
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Tester chaque exemple

#### Session 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

#### Session 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```

#### Session 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```

#### Session 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```

#### Session 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```

#### Session 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```

---

## Référence des variables d'environnement

### Globales (tous les exemples)
| Variable | Description | Valeur par défaut |
|----------|-------------|-------------------|
| `FOUNDRY_LOCAL_ALIAS` | Alias du modèle à utiliser | Variable selon l'exemple |
| `FOUNDRY_LOCAL_ENDPOINT` | Remplacer le point de service | Détecté automatiquement |
| `SHOW_USAGE` | Afficher l'utilisation des jetons | `0` |
| `RETRY_ON_FAIL` | Activer la logique de reprise | `1` |
| `RETRY_BACKOFF` | Délai initial de reprise | `1.0` |

### Spécifiques aux exemples
| Variable | Utilisée par | Description |
|----------|-------------|-------------|
| `EMBED_MODEL` | Session 02 | Nom du modèle d'embedding |
| `RAG_QUESTION` | Session 02 | Question de test pour RAG |
| `BENCH_MODELS` | Session 03 | Modèles à tester, séparés par des virgules |
| `BENCH_ROUNDS` | Session 03 | Nombre de tours de benchmark |
| `BENCH_PROMPT` | Session 03 | Prompt de test pour les benchmarks |
| `BENCH_STREAM` | Session 03 | Mesurer la latence du premier jeton |
| `SLM_ALIAS` | Session 04 | Modèle de petite taille |
| `LLM_ALIAS` | Session 04 | Modèle de grande taille |
| `COMPARE_PROMPT` | Session 04 | Prompt de test pour la comparaison |
| `AGENT_MODEL_PRIMARY` | Session 05 | Modèle d'agent principal |
| `AGENT_MODEL_EDITOR` | Session 05 | Modèle d'agent éditeur |
| `AGENT_QUESTION` | Session 05 | Question de test pour les agents |
| `PIPELINE_TASK` | Session 06 | Tâche pour le pipeline |

---

## Changements majeurs

**Aucun** - Tous les changements sont rétrocompatibles.

Les scripts existants continueront de fonctionner. Les nouvelles fonctionnalités sont :
- Variables d'environnement optionnelles
- Messages d'erreur améliorés (ne cassent pas la fonctionnalité)
- Journaux supplémentaires (peuvent être supprimés)
- Indications de type améliorées (aucun impact à l'exécution)

---

## Meilleures pratiques mises en œuvre

### 1. Toujours utiliser Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Modèle de gestion des erreurs approprié
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Journaux informatifs
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Indications de type
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Docstrings complètes
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. Prise en charge des variables d'environnement
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Dégradation progressive
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## Problèmes courants et solutions

### Problème : Erreurs d'importation
**Solution :** Installer les dépendances manquantes  
```bash
pip install sentence-transformers ragas datasets numpy
```

### Problème : Erreurs de connexion
**Solution :** Vérifier que Foundry Local est en cours d'exécution  
```bash
foundry service status
foundry model run phi-4-mini
```

### Problème : Modèle introuvable
**Solution :** Vérifier les modèles disponibles  
```bash
foundry model ls
foundry model download <alias>
```

### Problème : Performances lentes
**Solution :** Utiliser des modèles plus petits ou ajuster les paramètres  
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Prochaines étapes

### 1. Tester tous les exemples
Suivre la liste de contrôle des tests ci-dessus pour vérifier que tous les exemples fonctionnent correctement.

### 2. Mettre à jour la documentation
- Mettre à jour les fichiers markdown des sessions avec les nouveaux exemples
- Ajouter une section de dépannage au README principal
- Créer un guide de référence rapide

### 3. Créer des tests d'intégration
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Ajouter des benchmarks de performance
Suivre les améliorations de performance liées aux améliorations de gestion des erreurs.

### 5. Retour utilisateur
Collecter les retours des participants à l'atelier sur :
- Clarté des messages d'erreur
- Exhaustivité de la documentation
- Facilité d'utilisation

---

## Ressources

- **SDK local Foundry** : https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Référence rapide** : `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Notes de migration** : `Workshop/SDK_MIGRATION_NOTES.md`
- **Répertoire principal** : https://github.com/microsoft/Foundry-Local

---

## Maintenance

### Ajout de nouveaux exemples
Suivre ces modèles lors de la création de nouveaux exemples :

1. Utiliser `workshop_utils` pour la gestion des clients
2. Ajouter une gestion complète des erreurs
3. Inclure la prise en charge des variables d'environnement
4. Ajouter des indications de type et des docstrings
5. Fournir des journaux informatifs
6. Inclure des exemples d'utilisation dans les docstrings
7. Lier à la documentation SDK

### Révision des mises à jour
Lors de la révision des mises à jour des exemples, vérifier :
- [ ] Gestion des erreurs sur toutes les opérations d'E/S
- [ ] Indications de type sur les fonctions publiques
- [ ] Docstrings complètes
- [ ] Documentation des variables d'environnement
- [ ] Retour utilisateur informatif
- [ ] Liens de référence SDK
- [ ] Style de code cohérent

---

**Résumé** : Tous les exemples Python de l'atelier suivent désormais les meilleures pratiques du SDK local Foundry avec une gestion des erreurs améliorée, une documentation complète et une expérience utilisateur optimisée. Aucun changement majeur - toutes les fonctionnalités existantes sont préservées et améliorées.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.