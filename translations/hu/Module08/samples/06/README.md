<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-23T01:19:14+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "hu"
}
-->
# 6. munkamenet mintája: Modellek mint eszközök

Ez a minta egy minimális routert és eszközregisztert valósít meg, amely a felhasználói prompt alapján kiválaszt egy modellt, és meghívja a Foundry Local OpenAI-kompatibilis végpontját.

## Fájlok
- `router.py`: egyszerű regiszter és heurisztikus útválasztás; végpont felfedezése + állapotellenőrzés.

## Futtatás (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Megjegyzések
- A router egyszerű kulcsszó-heurisztikát használ, hogy válasszon a `general`, `reasoning` és `code` eszközök között, és a `/v1/models`-t nyomtatja ki indításkor.
- Konfigurálás környezeti változókon keresztül:
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

## Hivatkozások
- Foundry Local (Tanulás): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integráció inference SDK-kkal: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

