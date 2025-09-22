<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-22T12:28:49+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "fr"
}
-->
# Foundry Local sur Windows (Validé)

Ce guide vous aide à installer, exécuter et intégrer Microsoft Foundry Local sur Windows. Toutes les étapes et commandes ont été validées selon la documentation Microsoft Learn.

- Commencer : https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architecture : https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Référence CLI : https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Intégrer les SDKs : https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Compiler des modèles HF (BYOM) : https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI : Local vs Cloud : https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Installer / Mettre à jour sur Windows

- Installer :
```cmd
winget install Microsoft.FoundryLocal
```
- Mettre à jour :
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Vérifier la version :
```cmd
foundry --version
```

## 2) Bases de la CLI (Trois catégories)

- Modèle :
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Service :
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Cache :
```cmd
foundry cache --help
foundry cache list
```

Notes :
- Le service expose une API REST compatible OpenAI. Le port de l'endpoint est attribué dynamiquement ; utilisez `foundry service status` pour le découvrir.
- Utilisez les SDKs pour plus de commodité ; ils gèrent automatiquement la découverte des endpoints là où c'est pris en charge.

## 3) Découvrir l'endpoint local (Port dynamique)

Foundry Local attribue un port dynamique à chaque démarrage du service :
```cmd
foundry service status
```
Utilisez l'URL signalée `http://localhost:<PORT>` comme votre `base_url` avec les chemins compatibles OpenAI (par exemple, `/v1/chat/completions`).

## 4) Test rapide via le SDK Python OpenAI

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
Références :
- Intégration SDK : https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Apportez votre propre modèle (Compiler avec Olive)

Si vous avez besoin d'un modèle qui n'est pas dans le catalogue, compilez-le en ONNX pour Foundry Local en utilisant Olive.

Flux général (voir la documentation pour les étapes) :
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Docs :
- Compilation BYOM : https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Résolution des problèmes

- Vérifiez le statut du service et les journaux :
```cmd
foundry service status
foundry service diag
```
- Effacer ou déplacer le cache :
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Mettre à jour vers la dernière version preview :
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Expérience de développement liée à Windows

- Choix entre AI local et cloud sur Windows, y compris Foundry Local et Windows ML :
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- Toolkit AI de VS Code avec Foundry Local (utilisez `foundry service status` pour obtenir l'URL de l'endpoint de chat) :
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

