<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T12:28:10+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "fr"
}
-->
# Exemple de la session 6 : Les modèles comme outils

Cet exemple implémente un routeur minimal + un registre d'outils qui sélectionne un modèle en fonction de l'invite utilisateur et appelle l'endpoint compatible OpenAI de Foundry Local.

## Fichiers
- `router.py` : registre simple et routage heuristique ; découverte des endpoints + vérification de l'état.

## Exécution (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Remarques
- Le routeur utilise des heuristiques simples basées sur des mots-clés pour choisir entre les outils `general`, `reasoning` et `code`, et affiche `/v1/models` au démarrage.
- Configuration via des variables d'environnement :
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-distill-qwen-7b"},"code":{"model":"qwen2.5-7b-instruct"}}
```

## Références
- Foundry Local (Apprendre) : https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Intégration avec les SDK d'inférence : https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

