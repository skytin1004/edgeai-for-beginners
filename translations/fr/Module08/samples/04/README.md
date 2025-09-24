<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "562ac0eae12d808c9f45fbb77eb5c84f",
  "translation_date": "2025-09-24T10:21:19+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "fr"
}
-->
# Exemple 04 : Applications de Chat en Production avec Chainlit

Un exemple complet démontrant plusieurs approches pour créer des applications de chat prêtes pour la production en utilisant Microsoft Foundry Local, avec des interfaces web modernes, des réponses en streaming et des technologies de navigateur de pointe.

## Contenu Inclus

- **🚀 Application de Chat Chainlit** (`app.py`) : Application de chat prête pour la production avec streaming
- **🌐 Démo WebGPU** (`webgpu-demo/`) : Inférence IA basée sur le navigateur avec accélération matérielle
- **🎨 Intégration Open WebUI** (`open-webui-guide.md`) : Interface professionnelle similaire à ChatGPT
- **📚 Notebook Éducatif** (`chainlit_app.ipynb`) : Matériel d'apprentissage interactif

## Démarrage Rapide

### 1. Application de Chat Chainlit

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Accessible à : `http://localhost:8080`

### 2. Démo WebGPU dans le Navigateur

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Accessible à : `http://localhost:5173`

### 3. Configuration Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Accessible à : `http://localhost:3000`

## Modèles d'Architecture

### Matrice de Décision Local vs Cloud

| Scénario | Recommandation | Raison |
|----------|----------------|--------|
| **Données Sensibles** | 🏠 Local (Foundry) | Les données ne quittent jamais l'appareil |
| **Raisonnement Complexe** | ☁️ Cloud (Azure OpenAI) | Accès à des modèles plus grands |
| **Chat en Temps Réel** | 🏠 Local (Foundry) | Latence réduite, réponses plus rapides |
| **Analyse de Documents** | 🔄 Hybride | Extraction locale, analyse dans le cloud |
| **Génération de Code** | 🏠 Local (Foundry) | Confidentialité + modèles spécialisés |
| **Tâches de Recherche** | ☁️ Cloud (Azure OpenAI) | Base de connaissances étendue nécessaire |

### Comparaison des Technologies

| Technologie | Cas d'Utilisation | Avantages | Inconvénients |
|-------------|-------------------|-----------|---------------|
| **Chainlit** | Développeurs Python, prototypage rapide | Configuration facile, support du streaming | Limité à Python |
| **WebGPU** | Confidentialité maximale, scénarios hors ligne | Natif au navigateur, pas besoin de serveur | Taille de modèle limitée |
| **Open WebUI** | Déploiement en production, équipes | Interface professionnelle, gestion des utilisateurs | Nécessite Docker |

## Prérequis

- **Foundry Local** : Installé et en cours d'exécution ([Télécharger](https://aka.ms/foundry-local-installer))
- **Python** : Version 3.10+ avec environnement virtuel
- **Modèle** : Au moins un modèle chargé (`foundry model run phi-4-mini`)
- **Navigateur** : Chrome/Edge avec support WebGPU pour les démos
- **Docker** : Pour Open WebUI (optionnel)

## Installation & Configuration

### 1. Configuration de l'Environnement Python

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration de Foundry Local

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Applications Exemple

### Application de Chat Chainlit

**Caractéristiques :**
- 🚀 **Streaming en Temps Réel** : Les tokens apparaissent au fur et à mesure de leur génération
- 🛡️ **Gestion des Erreurs Robuste** : Dégradation et récupération en douceur
- 🎨 **Interface Moderne** : Interface de chat professionnelle prête à l'emploi
- 🔧 **Configuration Flexible** : Variables d'environnement et détection automatique
- 📱 **Design Adaptatif** : Fonctionne sur ordinateurs et appareils mobiles

**Démarrage Rapide :**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b-instruct
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### Démo WebGPU dans le Navigateur

**Caractéristiques :**
- 🌐 **IA Natif au Navigateur** : Pas besoin de serveur, fonctionne entièrement dans le navigateur
- ⚡ **Accélération WebGPU** : Accélération matérielle lorsque disponible
- 🔒 **Confidentialité Maximale** : Les données ne quittent jamais votre appareil
- 🎯 **Installation Zéro** : Fonctionne dans tout navigateur compatible
- 🔄 **Fallback en Douceur** : Bascule sur le CPU si WebGPU n'est pas disponible

**Exécution :**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Intégration Open WebUI

**Caractéristiques :**
- 🎨 **Interface Similaire à ChatGPT** : UI professionnelle et familière
- 👥 **Support Multi-utilisateurs** : Comptes utilisateurs et historique des conversations
- 📁 **Traitement de Fichiers** : Téléchargement et analyse de documents
- 🔄 **Changement de Modèle** : Commutation facile entre différents modèles
- 🐳 **Déploiement Docker** : Configuration prête pour la production en conteneur

**Configuration Rapide :**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Référence de Configuration

### Variables d'Environnement

| Variable | Description | Valeur par Défaut | Exemple |
|----------|-------------|-------------------|---------|
| `MODEL` | Alias du modèle à utiliser | `phi-4-mini` | `qwen2.5-7b-instruct` |
| `BASE_URL` | Point de terminaison Foundry Local | Détecté automatiquement | `http://localhost:51211` |
| `API_KEY` | Clé API (optionnelle pour local) | `""` | `your-api-key` |

## Résolution des Problèmes

### Problèmes Courants

**Application Chainlit :**

1. **Service non disponible :**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Conflits de port :**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Problèmes d'environnement Python :**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**Démo WebGPU :**

1. **WebGPU non supporté :**
   - Mettre à jour vers Chrome/Edge 113+
   - Activer WebGPU : `chrome://flags/#enable-unsafe-webgpu`
   - Vérifier le statut GPU : `chrome://gpu`
   - La démo basculera automatiquement sur le CPU

2. **Erreurs de chargement de modèle :**
   - Vérifier la connexion internet pour le téléchargement du modèle
   - Consulter la console du navigateur pour les erreurs CORS
   - Vérifier que vous servez via HTTP (pas file://)

**Open WebUI :**

1. **Connexion refusée :**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modèles non visibles :**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Liste de Validation

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## Utilisation Avancée

### Optimisation des Performances

**Chainlit :**
- Utiliser le streaming pour une meilleure perception des performances
- Implémenter le pooling de connexions pour une haute concurrence
- Mettre en cache les réponses des modèles pour les requêtes répétées
- Surveiller l'utilisation de la mémoire avec des historiques de conversation volumineux

**WebGPU :**
- Utiliser WebGPU pour une confidentialité et une vitesse maximales
- Implémenter la quantification des modèles pour des modèles plus petits
- Utiliser les Web Workers pour le traitement en arrière-plan
- Mettre en cache les modèles compilés dans le stockage du navigateur

**Open WebUI :**
- Utiliser des volumes persistants pour l'historique des conversations
- Configurer des limites de ressources pour le conteneur Docker
- Implémenter des stratégies de sauvegarde pour les données utilisateur
- Configurer un proxy inverse pour la terminaison SSL

### Modèles d'Intégration

**Hybride Local/Cloud :**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**Pipeline Multi-modal :**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## Déploiement en Production

### Considérations de Sécurité

- **Clés API** : Utiliser des variables d'environnement, ne jamais les coder en dur
- **Réseau** : Utiliser HTTPS en production, envisager un VPN pour l'accès en équipe
- **Contrôle d'Accès** : Implémenter l'authentification pour Open WebUI
- **Confidentialité des Données** : Auditer les données locales vs celles envoyées au cloud
- **Mises à Jour** : Maintenir Foundry Local et les conteneurs à jour

### Surveillance et Maintenance

- **Vérifications de Santé** : Implémenter la surveillance des points de terminaison
- **Journalisation** : Centraliser les journaux de tous les composants
- **Métriques** : Suivre les temps de réponse, taux d'erreur, utilisation des ressources
- **Sauvegarde** : Sauvegarde régulière des données de conversation et des configurations

## Références et Ressources

### Documentation
- [Documentation Chainlit](https://docs.chainlit.io/) - Guide complet du framework
- [Documentation Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Documentation officielle de Microsoft
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - Intégration WebGPU
- [Documentation Open WebUI](https://docs.openwebui.com/) - Configuration avancée

### Fichiers Exemple
- [`app.py`](../../../../../Module08/samples/04/app.py) - Application Chainlit en production
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Notebook éducatif
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Inférence IA basée sur le navigateur
- [`open-webui-guide.md`](./open-webui-guide.md) - Configuration complète Open WebUI

### Exemples Connexes
- [Documentation Session 4](../../04.CuttingEdgeModels.md) - Guide complet de la session
- [Exemples Foundry Local](https://github.com/microsoft/foundry-local/tree/main/samples) - Exemples officiels

---

