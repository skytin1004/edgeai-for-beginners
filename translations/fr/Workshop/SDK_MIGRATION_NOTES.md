<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec281a7cf06deda1f29140a2959ef0d2",
  "translation_date": "2025-10-08T19:28:37+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "fr"
}
-->
# Notes de Migration du SDK Local Foundry

## Vue d'ensemble

Tous les fichiers Python dans le dossier Workshop ont été mis à jour pour suivre les derniers modèles du [SDK Python Local Foundry officiel](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Résumé des Changements

### Infrastructure Principale (`workshop_utils.py`)

#### Fonctionnalités Améliorées :
- **Support de la Redéfinition des Points de Terminaison** : Ajout du support de la variable d'environnement `FOUNDRY_LOCAL_ENDPOINT`
- **Gestion des Erreurs Améliorée** : Meilleure gestion des exceptions avec des messages d'erreur détaillés
- **Cache Amélioré** : Les clés de cache incluent désormais le point de terminaison pour les scénarios multi-points de terminaison
- **Reprise avec Retard Exponentiel** : La logique de reprise utilise maintenant un retard exponentiel pour une meilleure fiabilité
- **Annotations de Type** : Ajout d'annotations de type complètes pour un meilleur support des IDE

#### Nouvelles Capacités :
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Applications Exemple

#### Session 01 : Initialisation du Chat (`chat_bootstrap.py`)
- Modèle par défaut mis à jour de `phi-3.5-mini` à `phi-4-mini`
- Ajout du support de la redéfinition des points de terminaison
- Documentation enrichie avec des références au SDK

#### Session 02 : Pipeline RAG (`rag_pipeline.py`)
- Mis à jour pour utiliser `phi-4-mini` comme modèle par défaut
- Ajout du support de la redéfinition des points de terminaison
- Documentation améliorée avec des détails sur les variables d'environnement

#### Session 02 : Évaluation RAG (`rag_eval_ragas.py`)
- Modèles par défaut mis à jour
- Ajout de la configuration des points de terminaison
- Gestion des erreurs améliorée

#### Session 03 : Benchmarking (`benchmark_oss_models.py`)
- Liste des modèles par défaut mise à jour pour inclure `phi-4-mini`
- Documentation complète des variables d'environnement ajoutée
- Documentation des fonctions améliorée
- Ajout du support de la redéfinition des points de terminaison

#### Session 04 : Comparaison des Modèles (`model_compare.py`)
- Modèle LLM par défaut mis à jour de `gpt-oss-20b` à `qwen2.5-7b`
- Ajout de la configuration des points de terminaison
- Documentation enrichie

#### Session 05 : Orchestration Multi-Agent (`agents_orchestrator.py`)
- Ajout d'annotations de type (changement de `str | None` à `Optional[str]`)
- Documentation de la classe Agent enrichie
- Ajout du support de la redéfinition des points de terminaison
- Modèle d'initialisation amélioré

#### Session 06 : Routeur de Modèles (`models_router.py`)
- Ajout de la configuration des points de terminaison
- Documentation enrichie sur la détection d'intention
- Documentation améliorée de la logique de routage

#### Session 06 : Pipeline (`models_pipeline.py`)
- Documentation complète des fonctions ajoutée
- Documentation étape par étape améliorée
- Gestion des erreurs enrichie

### Scripts

#### Exportation de Benchmark (`export_benchmark_markdown.py`)
- Ajout du support de la redéfinition des points de terminaison
- Modèles par défaut mis à jour
- Documentation des fonctions enrichie
- Gestion des erreurs améliorée

#### Linter CLI (`lint_markdown_cli.py`)
- Ajout de liens de référence au SDK
- Documentation d'utilisation améliorée

### Tests

#### Tests de Fumée (`smoke.py`)
- Ajout du support de la redéfinition des points de terminaison
- Documentation enrichie
- Documentation des cas de test améliorée
- Meilleur rapport d'erreurs

## Variables d'Environnement

Tous les exemples supportent désormais ces variables d'environnement :

### Configuration Principale
- `FOUNDRY_LOCAL_ALIAS` - Alias du modèle à utiliser (par défaut variable selon l'exemple)
- `FOUNDRY_LOCAL_ENDPOINT` - Redéfinir le point de terminaison du service (optionnel)
- `SHOW_USAGE` - Afficher les statistiques d'utilisation des jetons (par défaut : "0")
- `RETRY_ON_FAIL` - Activer la logique de reprise (par défaut : "1")
- `RETRY_BACKOFF` - Délai initial de reprise en secondes (par défaut : "1.0")

### Spécifique à l'Exemple
- `EMBED_MODEL` - Modèle d'intégration pour les exemples RAG
- `BENCH_MODELS` - Modèles séparés par des virgules pour le benchmarking
- `BENCH_ROUNDS` - Nombre de tours de benchmarking
- `BENCH_PROMPT` - Prompt de test pour les benchmarks
- `BENCH_STREAM` - Mesurer la latence du premier jeton
- `RAG_QUESTION` - Question de test pour les exemples RAG
- `AGENT_MODEL_PRIMARY` - Modèle principal de l'agent
- `AGENT_MODEL_EDITOR` - Modèle éditeur de l'agent
- `SLM_ALIAS` - Alias du petit modèle de langage
- `LLM_ALIAS` - Alias du grand modèle de langage

## Meilleures Pratiques du SDK Implémentées

### 1. Initialisation Correcte du Client
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. Récupération des Informations sur le Modèle
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Gestion des Erreurs
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Logique de Reprise avec Retard Exponentiel
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. Support du Streaming
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## Guide de Migration pour les Exemples Personnalisés

Si vous créez de nouveaux exemples ou mettez à jour des exemples existants :

1. **Utilisez les helpers de `workshop_utils.py`** :
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Supportez la redéfinition des points de terminaison** :
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Ajoutez une documentation complète** :
   - Variables d'environnement dans les docstrings
   - Lien de référence au SDK
   - Exemples d'utilisation

4. **Utilisez des annotations de type** :
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implémentez une gestion correcte des erreurs** :
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Tests

Tous les exemples peuvent être testés avec :

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
python Workshop/samples/session01/chat_bootstrap.py "Test question"
python Workshop/samples/session02/rag_pipeline.py

# Run benchmark
python Workshop/samples/session03/benchmark_oss_models.py

# Run smoke tests
python -m Workshop.tests.smoke
```

## Références de Documentation du SDK

- **Répertoire Principal** : https://github.com/microsoft/Foundry-Local
- **SDK Python** : https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Documentation API** : Consultez le répertoire SDK pour les dernières docs API

## Changements Importants

### Aucun Attendu
Tous les changements sont rétrocompatibles. Les mises à jour visent principalement à :
- Ajouter de nouvelles fonctionnalités optionnelles (redéfinition des points de terminaison)
- Améliorer la gestion des erreurs
- Enrichir la documentation
- Mettre à jour les noms des modèles par défaut selon les recommandations actuelles

### Améliorations Optionnelles
Vous pourriez vouloir mettre à jour votre code pour utiliser :
- `FOUNDRY_LOCAL_ENDPOINT` pour un contrôle explicite des points de terminaison
- `SHOW_USAGE=1` pour la visibilité de l'utilisation des jetons
- Modèles par défaut mis à jour (`phi-4-mini` au lieu de `phi-3.5-mini`)

## Problèmes Courants & Solutions

### Problème : "Échec de l'initialisation du client"
**Solution** : Assurez-vous que le service Foundry Local est en cours d'exécution :
```bash
foundry service start
foundry model run phi-4-mini
```

### Problème : "Modèle introuvable"
**Solution** : Vérifiez les modèles disponibles :
```bash
foundry model list
```

### Problème : Erreurs de connexion au point de terminaison
**Solution** : Vérifiez le point de terminaison :
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Prochaines Étapes

1. **Mettre à jour les exemples du Module08** : Appliquer des modèles similaires aux exemples du Module08
2. **Ajouter des tests d'intégration** : Créer une suite de tests complète
3. **Benchmarking des performances** : Comparer les performances avant/après
4. **Mises à jour de la documentation** : Mettre à jour le README principal avec les nouveaux modèles

## Directives de Contribution

Lors de l'ajout de nouveaux exemples :
1. Utilisez `workshop_utils.py` pour la cohérence
2. Suivez le modèle des exemples existants
3. Ajoutez des docstrings complètes
4. Incluez des liens de référence au SDK
5. Supportez la redéfinition des points de terminaison
6. Ajoutez des annotations de type appropriées
7. Incluez des exemples d'utilisation dans les docstrings

## Compatibilité des Versions

Ces mises à jour sont compatibles avec :
- `foundry-local-sdk` (dernière version)
- `openai>=1.30.0`
- Python 3.8+

---

**Dernière Mise à Jour** : 08/01/2025  
**Responsable** : Équipe EdgeAI Workshop  
**Version du SDK** : Foundry Local SDK (dernière 0.7.117+67073234e7)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.