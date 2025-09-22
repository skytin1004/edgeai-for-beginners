<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T19:23:20+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "sv"
}
-->
# Session 6 Exempel: Modeller som Verktyg

Detta exempel implementerar en minimal router + verktygsregister som väljer en modell baserat på användarens prompt och anropar Foundry Locals OpenAI-kompatibla endpoint.

## Filer
- `router.py`: enkelt register och heuristisk routing; endpoint-upptäckt + hälsokontroll.

## Kör (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Anteckningar
- Routern använder enkla nyckelordsheuristik för att välja mellan `general`, `reasoning` och `code` verktyg och skriver ut `/v1/models` vid start.
- Konfigurera via miljövariabler:
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

## Referenser
- Foundry Local (Lär dig): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integrera med inferens-SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

