<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T12:27:49+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "fr"
}
-->
# Session 1 Exemple : Discussion rapide via REST

Exécutez une requête de chat minimale vers Foundry Local en utilisant Python `requests`.

## Prérequis
- Service Foundry Local exécutant un modèle (par exemple, `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Exécution (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Références
- Foundry Local (Apprendre) : https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Vue d'ensemble de l'API compatible OpenAI : https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

