<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T17:47:50+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "ne"
}
-->
# सत्र ६ नमूना: उपकरणको रूपमा मोडेलहरू

यो नमूनाले न्यूनतम राउटर + उपकरण रजिस्ट्री कार्यान्वयन गर्दछ जसले प्रयोगकर्ताको प्रम्प्टको आधारमा मोडेल चयन गर्छ र Foundry Local को OpenAI-संगत अन्त बिन्दुमा कल गर्छ।

## फाइलहरू
- `router.py`: साधारण रजिस्ट्री र ह्युरिस्टिक राउटिङ; अन्त बिन्दु पत्ता लगाउने + स्वास्थ्य जाँच।

## चलाउनुहोस् (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## नोटहरू
- राउटरले साधारण कीवर्ड ह्युरिस्टिक्स प्रयोग गरेर `general`, `reasoning`, र `code` उपकरणहरू बीच चयन गर्छ र सुरुमा `/v1/models` प्रिन्ट गर्छ।
- वातावरण चरहरू मार्फत कन्फिगर गर्नुहोस्:
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

## सन्दर्भहरू
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- अनुमान SDKs सँग एकीकृत गर्नुहोस्: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

