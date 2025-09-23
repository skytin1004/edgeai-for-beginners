<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-23T01:19:21+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "sk"
}
-->
# Session 6 Ukážka: Modely ako nástroje

Táto ukážka implementuje minimálny router + registráciu nástrojov, ktorý vyberá model na základe používateľského vstupu a volá OpenAI-kompatibilný endpoint Foundry Local.

## Súbory
- `router.py`: jednoduchá registrácia a heuristické smerovanie; objavovanie endpointov + kontrola stavu.

## Spustenie (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Poznámky
- Router používa jednoduché heuristiky na základe kľúčových slov na výber medzi nástrojmi `general`, `reasoning` a `code` a pri štarte vypisuje `/v1/models`.
- Konfigurácia cez environmentálne premenné:
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

## Referencie
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integrácia s inferenčnými SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

