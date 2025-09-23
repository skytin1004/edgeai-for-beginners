<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-23T01:19:11+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "sw"
}
-->
# Kipindi cha 6 Mfano: Miundo kama Zana

Mfano huu unatekeleza router ndogo + usajili wa zana ambao huchagua mfano kulingana na maelezo ya mtumiaji na kuita endpoint ya Foundry Local inayolingana na OpenAI.

## Faili
- `router.py`: usajili rahisi na njia ya kielelezo; ugunduzi wa endpoint + ukaguzi wa afya.

## Endesha (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Maelezo
- Router hutumia kielelezo rahisi cha maneno muhimu kuchagua kati ya zana za `general`, `reasoning`, na `code` na kuchapisha `/v1/models` mwanzoni.
- Sanidi kupitia vigezo vya mazingira:
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

## Marejeleo
- Foundry Local (Jifunze): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Jumuisha na SDK za inference: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

