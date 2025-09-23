<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-23T01:20:18+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "sr"
}
-->
# Сесија 4 Пример: Chainlit RAG Демо

Покрените минималну Chainlit апликацију уз Foundry Local.

## Предуслови
- Windows 11, Python 3.10+
- Инсталиран Foundry Local и доступан модел (нпр. `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Покретање (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Валидација
```cmd
curl http://localhost:8000/v1/models
```

## Решавање проблема
- Ако VS Code приказује "chainlit could not be resolved":
	- Изаберите интерпретер `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Уверите се да су зависности инсталиране: `pip install -r Module08\requirements.txt`

## Референце
- Упутство за Open WebUI (чет апликација са Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

