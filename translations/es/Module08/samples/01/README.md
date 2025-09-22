<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T12:57:47+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "es"
}
-->
# Sesión 1 Ejemplo: Chat Rápido vía REST

Realiza una solicitud mínima de chat a Foundry Local utilizando Python `requests`.

## Requisitos previos
- Servicio Foundry Local ejecutando un modelo (por ejemplo, `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Ejecución (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Referencias
- Foundry Local (Aprende): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Descripción general de la API compatible con OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

