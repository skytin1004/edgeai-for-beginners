<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-23T01:19:50+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "lt"
}
-->
# 6 sesijos pavyzdys: Modeliai kaip įrankiai

Šiame pavyzdyje įgyvendinamas minimalus maršrutizatorius + įrankių registras, kuris parenka modelį pagal vartotojo užklausą ir naudoja Foundry Local OpenAI suderinamą galinį tašką.

## Failai
- `router.py`: paprastas registras ir euristinis maršrutizavimas; galinio taško aptikimas + sveikatos patikrinimas.

## Paleidimas (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Pastabos
- Maršrutizatorius naudoja paprastas raktažodžių euristikas, kad pasirinktų tarp `general`, `reasoning` ir `code` įrankių, ir paleidimo metu atspausdina `/v1/models`.
- Konfigūruojama per aplinkos kintamuosius:
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

## Nuorodos
- Foundry Local (mokymasis): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integracija su inferencijos SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

