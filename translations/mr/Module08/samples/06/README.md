<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T17:47:45+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "mr"
}
-->
# सत्र 6 नमुना: साधन म्हणून मॉडेल्स

हा नमुना एक साधा राउटर + टूल रजिस्ट्रेशन अंमलात आणतो जो वापरकर्त्याच्या प्रॉम्प्टवर आधारित मॉडेल निवडतो आणि Foundry Local च्या OpenAI-सुसंगत एन्डपॉइंटला कॉल करतो.

## फाइल्स
- `router.py`: साधा रजिस्ट्रेशन आणि ह्युरिस्टिक राउटिंग; एन्डपॉइंट शोध + हेल्थ चेक.

## चालवा (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## टीप
- राउटर साध्या कीवर्ड ह्युरिस्टिक्सचा वापर करून `general`, `reasoning`, आणि `code` साधनांमध्ये निवड करतो आणि सुरुवातीला `/v1/models` प्रिंट करतो.
- पर्यावरणीय व्हेरिएबल्सद्वारे कॉन्फिगर करा:
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
- Foundry Local (शिका): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- इनफरन्स SDKs सह एकत्रीकरण: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

