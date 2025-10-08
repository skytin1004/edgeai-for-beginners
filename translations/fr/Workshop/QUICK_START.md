<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20ef6223850f0ab7b6e546a6df0d7d68",
  "translation_date": "2025-10-08T19:07:53+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "fr"
}
-->
# Guide de démarrage rapide pour l'atelier

## Prérequis

### 1. Installer Foundry Local

Suivez le guide d'installation officiel :  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Installer les dépendances Python

Depuis le répertoire de l'atelier :

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Exécution des exemples de l'atelier

### Session 01 : Chat de base

```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What are the benefits of local AI?"
```

**Variables d'environnement :**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Session 02 : Pipeline RAG

```bash
cd Workshop/samples/session02
python rag_pipeline.py
```

**Variables d'environnement :**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Session 02 : Évaluation RAG (Ragas)

```bash
python rag_eval_ragas.py
```

**Remarque** : Nécessite des dépendances supplémentaires installées via `requirements.txt`

### Session 03 : Benchmarking

```bash
cd Workshop/samples/session03
python benchmark_oss_models.py
```

**Variables d'environnement :**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Sortie** : JSON avec des métriques de latence, de débit et de premier token

### Session 04 : Comparaison de modèles

```bash
cd Workshop/samples/session04
python model_compare.py
```

**Variables d'environnement :**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Session 05 : Orchestration multi-agents

```bash
cd Workshop/samples/session05
python agents_orchestrator.py
```

**Variables d'environnement :**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Session 06 : Routeur de modèles

```bash
cd Workshop/samples/session06
python models_router.py
```

**Teste la logique de routage** avec plusieurs intentions (code, résumé, classification)

### Session 06 : Pipeline

```bash
python models_pipeline.py
```

**Pipeline complexe en plusieurs étapes** avec planification, exécution et affinage

## Scripts

### Exporter un rapport de benchmark

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Sortie** : Tableau Markdown + métriques JSON

### Linter pour les modèles CLI Markdown

```bash
python lint_markdown_cli.py --verbose
```

**Objectif** : Détecter les modèles CLI obsolètes dans la documentation

## Tests

### Tests de fumée

```bash
cd Workshop
python -m tests.smoke
```

**Tests** : Fonctionnalité de base des exemples clés

## Dépannage

### Service non démarré

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Erreurs d'importation de modules

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Erreurs de connexion

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Modèle introuvable

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Référence des variables d'environnement

### Configuration principale
| Variable | Par défaut | Description |
|----------|------------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | Variable | Alias du modèle à utiliser |
| `FOUNDRY_LOCAL_ENDPOINT` | Automatique | Remplacer le point de terminaison du service |
| `SHOW_USAGE` | `0` | Afficher les statistiques d'utilisation des tokens |
| `RETRY_ON_FAIL` | `1` | Activer la logique de réessai |
| `RETRY_BACKOFF` | `1.0` | Délai initial de réessai (en secondes) |

### Spécifique à la session
| Variable | Par défaut | Description |
|----------|------------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Modèle d'embedding |
| `RAG_QUESTION` | Voir exemple | Question de test RAG |
| `BENCH_MODELS` | Variable | Modèles séparés par des virgules |
| `BENCH_ROUNDS` | `3` | Itérations de benchmark |
| `BENCH_PROMPT` | Voir exemple | Prompt de benchmark |
| `BENCH_STREAM` | `0` | Mesurer la latence du premier token |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Modèle principal de l'agent |
| `AGENT_MODEL_EDITOR` | Principal | Modèle éditeur de l'agent |
| `SLM_ALIAS` | `phi-4-mini` | Petit modèle de langage |
| `LLM_ALIAS` | `qwen2.5-7b` | Grand modèle de langage |
| `COMPARE_PROMPT` | Voir exemple | Prompt de comparaison |

## Modèles recommandés

### Développement et tests
- **phi-4-mini** - Qualité et vitesse équilibrées
- **qwen2.5-0.5b** - Très rapide pour la classification
- **gemma-2-2b** - Bonne qualité, vitesse modérée

### Scénarios de production
- **phi-4-mini** - Usage général
- **deepseek-coder-1.3b** - Génération de code
- **qwen2.5-7b** - Réponses de haute qualité

## Documentation SDK

- **Foundry Local** : https://github.com/microsoft/Foundry-Local  
- **SDK Python** : https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Obtenir de l'aide

1. Vérifiez le statut du service : `foundry service status`  
2. Consultez les journaux : Vérifiez les journaux du service Foundry Local  
3. Consultez la documentation SDK : https://github.com/microsoft/Foundry-Local  
4. Examinez le code des exemples : Tous les exemples contiennent des docstrings détaillés

## Prochaines étapes

1. Complétez toutes les sessions de l'atelier dans l'ordre  
2. Expérimentez avec différents modèles  
3. Modifiez les exemples pour vos cas d'utilisation  
4. Consultez `SDK_MIGRATION_NOTES.md` pour des modèles avancés  

---

**Dernière mise à jour** : 08/01/2025  
**Version de l'atelier** : Dernière  
**SDK** : Foundry Local Python SDK  

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.