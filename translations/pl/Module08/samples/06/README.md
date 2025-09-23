<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T13:41:00+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "pl"
}
-->
# Sesja 6 Przykład: Modele jako narzędzia

Ten przykład implementuje minimalny router + rejestr narzędzi, który wybiera model na podstawie zapytania użytkownika i wywołuje zgodny z OpenAI punkt końcowy Foundry Local.

## Pliki
- `router.py`: prosty rejestr i heurystyczne trasowanie; odkrywanie punktów końcowych + sprawdzanie ich stanu.

## Uruchom (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Uwagi
- Router używa prostych heurystyk opartych na słowach kluczowych, aby wybrać między narzędziami `general`, `reasoning` i `code`, i drukuje `/v1/models` przy uruchomieniu.
- Konfiguracja za pomocą zmiennych środowiskowych:
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

## Odnośniki
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integracja z SDK inferencji: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

