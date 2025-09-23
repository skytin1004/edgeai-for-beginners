<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-23T01:19:38+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "sl"
}
-->
# Seansa 6 Vzorec: Modeli kot Orodja

Ta vzorec implementira minimalni usmerjevalnik + register orodij, ki izbere model na podlagi uporabniškega poziva in pokliče OpenAI-kompatibilno končno točko Foundry Local.

## Datoteke
- `router.py`: preprost register in usmerjanje na podlagi heuristike; odkrivanje končnih točk + preverjanje stanja.

## Zagon (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Opombe
- Usmerjevalnik uporablja preproste ključne besede za izbiro med orodji `general`, `reasoning` in `code` ter ob zagonu izpiše `/v1/models`.
- Konfiguracija preko okoljskih spremenljivk:
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

## Reference
- Foundry Local (Učenje): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integracija z SDK-ji za sklepanje: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

