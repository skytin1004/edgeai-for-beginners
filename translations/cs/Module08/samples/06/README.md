<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-23T01:19:18+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "cs"
}
-->
# Ukázka ze 6. lekce: Modely jako nástroje

Tato ukázka implementuje minimální router + registr nástrojů, který vybírá model na základě uživatelského dotazu a volá OpenAI-kompatibilní endpoint Foundry Local.

## Soubory
- `router.py`: jednoduchý registr a heuristické směrování; objevování endpointů + kontrola stavu.

## Spuštění (cmd.exe)
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
- Router používá jednoduché heuristiky na základě klíčových slov k výběru mezi nástroji `general`, `reasoning` a `code` a při spuštění vypisuje `/v1/models`.
- Konfigurace prostřednictvím proměnných prostředí:
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

## Odkazy
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integrace s inference SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

