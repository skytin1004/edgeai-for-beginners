<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T12:28:21+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "fr"
}
-->
# Session 4 Exemple : Démo Chainlit RAG

Exécutez l'application Chainlit minimale avec Foundry Local.

## Prérequis
- Windows 11, Python 3.10+
- Foundry Local installé et un modèle disponible (par exemple, `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Exécution (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Validation
```cmd
curl http://localhost:8000/v1/models
```

## Résolution des problèmes
- Si VS Code affiche "chainlit could not be resolved" :
	- Sélectionnez l'interpréteur `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Assurez-vous que les dépendances sont installées : `pip install -r Module08\requirements.txt`

## Références
- Guide Open WebUI (application de chat avec Open WebUI) : https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Apprendre) : https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

