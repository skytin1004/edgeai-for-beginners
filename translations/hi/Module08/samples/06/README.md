<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T13:41:05+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "hi"
}
-->
# सत्र 6 नमूना: उपकरणों के रूप में मॉडल

यह नमूना एक न्यूनतम राउटर + टूल रजिस्ट्री को लागू करता है, जो उपयोगकर्ता के प्रॉम्प्ट के आधार पर एक मॉडल का चयन करता है और Foundry Local के OpenAI-संगत एंडपॉइंट को कॉल करता है।

## फाइलें
- `router.py`: सरल रजिस्ट्री और हीयुरिस्टिक रूटिंग; एंडपॉइंट खोज + स्वास्थ्य जांच।

## चलाएं (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## नोट्स
- राउटर सरल कीवर्ड हीयुरिस्टिक्स का उपयोग करता है ताकि `general`, `reasoning`, और `code` उपकरणों के बीच चयन कर सके और स्टार्ट पर `/v1/models` प्रिंट करता है।
- पर्यावरण वेरिएबल्स के माध्यम से कॉन्फ़िगर करें:
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

## संदर्भ
- Foundry Local (सीखें): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- इन्फेरेंस SDKs के साथ एकीकृत करें: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

