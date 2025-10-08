<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T19:06:48+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "fr"
}
-->
# Mises à jour du SDK Local Foundry

## Vue d'ensemble

Mise à jour des notebooks et des utilitaires du Workshop pour utiliser correctement le **SDK Python officiel de Foundry Local**, en suivant les modèles de :
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Fichiers modifiés

### 1. `Workshop/samples/workshop_utils.py`

**Modifications :**
- ✅ Ajout de la gestion des erreurs d'importation pour le package `foundry-local-sdk`
- ✅ Amélioration de la documentation avec les modèles officiels du SDK
- ✅ Amélioration des journaux avec des symboles Unicode (✓, ✗, ⚠)
- ✅ Ajout de docstrings détaillées avec des exemples
- ✅ Meilleurs messages d'erreur faisant référence aux commandes CLI
- ✅ Mise à jour des commentaires pour correspondre à la documentation officielle du SDK

**Améliorations clés :**

#### Gestion des erreurs d'importation
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Fonction améliorée `get_client()`
- Ajout d'une documentation détaillée sur le modèle d'initialisation du SDK
- Précision que `FoundryLocalManager` démarre automatiquement le service
- Explication de la résolution des alias de modèles vers des variantes optimisées pour le matériel
- Amélioration des journaux avec des informations sur les points de terminaison
- Meilleurs messages d'erreur suggérant des étapes de dépannage

#### Fonction améliorée `chat_once()`
- Ajout d'une docstring complète avec des exemples d'utilisation
- Clarification de la compatibilité avec le SDK OpenAI
- Documentation du support de streaming (via kwargs)
- Amélioration des messages d'erreur avec des suggestions de commandes CLI
- Ajout de notes sur la vérification de la disponibilité des modèles

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Modifications :**
- ✅ Mise à jour de toutes les cellules markdown avec des références au SDK
- ✅ Amélioration des commentaires de code avec des explications sur les modèles du SDK
- ✅ Amélioration de la documentation et des explications des cellules
- ✅ Ajout de conseils de dépannage
- ✅ Mise à jour du catalogue de modèles (remplacement de 'gpt-oss-20b' par 'phi-3.5-mini')
- ✅ Meilleur formatage des sorties avec des indicateurs visuels
- ✅ Ajout de liens et de références au SDK tout au long du document

**Mises à jour cellule par cellule :**

#### Cellule 1 (Titre)
- Ajout de liens vers la documentation du SDK
- Références aux dépôts GitHub officiels

#### Cellule 2 (Scénario)
- Reformulation avec des étapes numérotées
- Clarification du modèle de routage basé sur l'intention
- Mise en avant des avantages de l'exécution locale

#### Cellule 3 (Installation des dépendances)
- Ajout d'une explication sur ce que chaque package fournit
- Documentation des capacités du SDK (résolution des alias, optimisation matérielle)

#### Cellule 4 (Configuration de l'environnement)
- Amélioration des docstrings des fonctions
- Ajout de commentaires en ligne expliquant les modèles du SDK
- Documentation de la structure du catalogue de modèles
- Clarification de la correspondance des priorités/capacités

#### Cellule 5 (Vérification du catalogue)
- Ajout de coches visuelles (✓)
- Meilleur formatage des sorties

#### Cellule 6 (Test de détection d'intention)
- Reformulation des sorties sous forme de tableau
- Affichage des intentions et des modèles sélectionnés

#### Cellule 7 (Fonction de routage)
- Explication complète du modèle du SDK
- Documentation du flux d'initialisation
- Liste de toutes les fonctionnalités (reprise, suivi, erreurs)
- Ajout d'un lien de référence au SDK

#### Cellule 8 (Démonstration par lot)
- Explication améliorée de ce à quoi s'attendre
- Ajout d'une section de dépannage
- Inclusion de commandes CLI pour le débogage
- Meilleur formatage de l'affichage des sorties

### 3. `Workshop/notebooks/session06_README.md` (Nouveau fichier)

**Création d'une documentation complète couvrant :**

1. **Vue d'ensemble** : Diagramme d'architecture et explication des composants
2. **Intégration du SDK** : Exemples de code suivant les modèles officiels
3. **Prérequis** : Instructions étape par étape pour la configuration
4. **Utilisation** : Comment exécuter et personnaliser le notebook
5. **Alias de modèles** : Explication des variantes optimisées pour le matériel
6. **Dépannage** : Problèmes courants et solutions
7. **Extension** : Comment ajouter des intentions, des modèles et une logique personnalisée
8. **Conseils de performance** : Bonnes pratiques pour une utilisation en production
9. **Ressources** : Liens vers la documentation officielle et la communauté

## Mise en œuvre des modèles du SDK

### Modèle officiel (tiré des documents de Foundry Local)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### Notre mise en œuvre (dans workshop_utils)

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**Avantages de notre approche :**
- ✅ Suit exactement le modèle officiel du SDK
- ✅ Ajoute une mise en cache pour éviter les initialisations répétées
- ✅ Inclut une logique de reprise pour une robustesse en production
- ✅ Prend en charge le suivi de l'utilisation des jetons
- ✅ Fournit de meilleurs messages d'erreur
- ✅ Reste compatible avec les exemples officiels

## Modifications du catalogue de modèles

### Avant
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Après
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Raison :** Remplacement de 'gpt-oss-20b' (alias non standard) par 'phi-3.5-mini' (alias officiel de Foundry Local).

## Dépendances

### Fichier requirements.txt mis à jour

Le fichier requirements.txt du Workshop inclut déjà :
```
foundry-local-sdk
openai>=1.30.0
```

Ce sont les seuls packages nécessaires pour l'intégration avec Foundry Local.

## Test des mises à jour

### 1. Vérifiez que Foundry Local est en cours d'exécution

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Vérifiez les modèles disponibles

```bash
foundry model ls
```

Assurez-vous que ces modèles sont disponibles ou seront téléchargés automatiquement :
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Exécutez le notebook

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Ou ouvrez-le dans VS Code et exécutez toutes les cellules.

### 4. Comportement attendu

**Cellule 1 (Installation) :** Installation des packages réussie  
**Cellule 2 (Configuration) :** Pas d'erreurs, les imports fonctionnent  
**Cellule 3 (Vérification) :** Affiche ✓ avec la liste des modèles  
**Cellule 4 (Test d'intention) :** Affiche les résultats de détection d'intention  
**Cellule 5 (Routeur) :** Affiche ✓ Fonction de routage prête  
**Cellule 6 (Exécution) :** Route les invites vers les modèles, affiche les résultats  

### 5. Dépannage des erreurs de connexion

Si vous voyez `APIConnectionError: Connection error` :

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Variables d'environnement

Les variables d'environnement suivantes sont prises en charge :

| Variable | Par défaut | Description |
|----------|------------|-------------|
| `SHOW_USAGE` | `0` | Mettre à `1` pour afficher l'utilisation des jetons |
| `RETRY_ON_FAIL` | `1` | Activer la logique de reprise |
| `RETRY_BACKOFF` | `1.0` | Délai initial de reprise (en secondes) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Remplacer le point de terminaison du service |

### Exemples d'utilisation

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migration depuis l'ancien modèle

Si vous avez un code existant utilisant des appels API directs, voici comment migrer :

### Avant (API directe)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### Après (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### Avantages de la migration
- ✅ Gestion automatique du service
- ✅ Résolution des alias de modèles
- ✅ Sélection d'optimisation matérielle
- ✅ Meilleure gestion des erreurs
- ✅ Compatibilité avec le SDK OpenAI
- ✅ Support du streaming

## Références

### Documentation officielle
- **GitHub Foundry Local** : https://github.com/microsoft/Foundry-Local  
- **Source SDK Python** : https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  
- **Référence CLI** : https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **API REST** : https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md  
- **Dépannage** : https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md  

### Ressources du Workshop
- **Session 06 README** : `Workshop/notebooks/session06_README.md`  
- **Workshop Utils** : `Workshop/samples/workshop_utils.py`  
- **Notebook Exemple** : `Workshop/notebooks/session06_models_router.ipynb`  

### Communauté
- **Discord** : https://aka.ms/foundry-local-discord  
- **Problèmes GitHub** : https://github.com/microsoft/Foundry-Local/issues  

## Prochaines étapes

1. **Revoir les modifications** : Lisez les fichiers mis à jour  
2. **Tester le notebook** : Exécutez session06_models_router.ipynb  
3. **Vérifier le SDK** : Assurez-vous que foundry-local-sdk est installé  
4. **Vérifier le service** : Confirmez que Foundry Local est en cours d'exécution  
5. **Explorer la documentation** : Lisez le nouveau session06_README.md  

## Résumé

Ces mises à jour garantissent que les supports du Workshop suivent exactement les **modèles officiels du SDK Foundry Local** tels que documentés dans le dépôt GitHub. Tous les exemples de code, la documentation et les utilitaires sont désormais alignés sur les meilleures pratiques recommandées par Microsoft pour le déploiement local de modèles d'IA.

Les modifications améliorent :
- ✅ **Exactitude** : Utilisation des modèles officiels du SDK  
- ✅ **Documentation** : Explications et exemples complets  
- ✅ **Gestion des erreurs** : Meilleurs messages et conseils de dépannage  
- ✅ **Maintenabilité** : Conformité aux conventions officielles  
- ✅ **Expérience utilisateur** : Instructions plus claires et aide au débogage  

---

**Mise à jour :** 8 octobre 2025  
**Version du SDK :** foundry-local-sdk (dernière version)  
**Branche du Workshop :** Reactor

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.