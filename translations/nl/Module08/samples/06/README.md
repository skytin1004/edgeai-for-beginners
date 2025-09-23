<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T21:53:45+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "nl"
}
-->
# Sessie 6 Voorbeeld: Modellen als Tools

Dit voorbeeld implementeert een minimale router + toolregister die een model selecteert op basis van de gebruikersprompt en Foundry Local's OpenAI-compatibele endpoint aanroept.

## Bestanden
- `router.py`: eenvoudig register en heuristische routering; endpointdetectie + gezondheidscontrole.

## Uitvoeren (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Opmerkingen
- De router gebruikt eenvoudige sleutelwoordheuristieken om te kiezen tussen `general`, `reasoning` en `code` tools en print `/v1/models` bij het starten.
- Configureren via omgevingsvariabelen:
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

## Referenties
- Foundry Local (Leer): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integreren met inference SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

