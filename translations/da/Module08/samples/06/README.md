<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T20:26:08+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "da"
}
-->
# Session 6 Eksempel: Modeller som Værktøjer

Dette eksempel implementerer en minimal router + værktøjsregister, der vælger en model baseret på brugerens prompt og kalder Foundry Locals OpenAI-kompatible endpoint.

## Filer
- `router.py`: simpelt register og heuristisk routing; endpoint-opdagelse + sundhedstjek.

## Kør (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Noter
- Routeren bruger simple nøgleord-heuristikker til at vælge mellem `general`, `reasoning` og `code` værktøjer og udskriver `/v1/models` ved start.
- Konfigurer via miljøvariabler:
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

## Referencer
- Foundry Local (Lær): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integration med inferens-SDK'er: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

