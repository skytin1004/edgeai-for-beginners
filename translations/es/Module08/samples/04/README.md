<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T12:58:21+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "es"
}
-->
# Sesión 4 Ejemplo: Demostración de Chainlit RAG

Ejecuta la aplicación mínima de Chainlit contra Foundry Local.

## Requisitos previos
- Windows 11, Python 3.10+
- Foundry Local instalado y un modelo disponible (por ejemplo, `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Ejecutar (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Validar
```cmd
curl http://localhost:8000/v1/models
```

## Solución de problemas
- Si VS Code muestra "chainlit could not be resolved":
	- Selecciona el intérprete `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Asegúrate de que las dependencias estén instaladas: `pip install -r Module08\requirements.txt`

## Referencias
- Cómo abrir WebUI (aplicación de chat con Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Aprender): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

