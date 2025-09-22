<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T22:41:21+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "tl"
}
-->
# Session 6 Sample: Mga Modelo bilang Mga Kasangkapan

Ang sample na ito ay nagpatupad ng isang minimal na router + tool registry na pumipili ng modelo batay sa prompt ng user at tumatawag sa Foundry Local’s OpenAI-compatible endpoint.

## Mga File
- `router.py`: simpleng registry at heuristic routing; endpoint discovery + health check.

## Pagpapatakbo (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Mga Tala
- Ginagamit ng router ang simpleng keyword heuristics upang pumili sa pagitan ng `general`, `reasoning`, at `code` tools at nagpi-print ng `/v1/models` sa simula.
- I-configure gamit ang mga environment variables:
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

## Mga Sanggunian
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integrasyon sa inference SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

