<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T12:58:09+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "es"
}
-->
# Sesión 6 Ejemplo: Modelos como Herramientas

Este ejemplo implementa un enrutador mínimo + un registro de herramientas que selecciona un modelo basado en el mensaje del usuario y llama al endpoint compatible con OpenAI de Foundry Local.

## Archivos
- `router.py`: registro simple y enrutamiento heurístico; descubrimiento de endpoint + verificación de estado.

## Ejecución (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Notas
- El enrutador utiliza heurísticas simples basadas en palabras clave para elegir entre las herramientas `general`, `reasoning` y `code`, e imprime `/v1/models` al iniciar.
- Configuración mediante variables de entorno:
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

## Referencias
- Foundry Local (Aprender): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integración con SDKs de inferencia: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

