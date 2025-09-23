<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T14:26:03+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "ur"
}
-->
# سیشن 6 نمونہ: ماڈلز بطور اوزار

یہ نمونہ ایک سادہ روٹر + ٹول رجسٹری کو نافذ کرتا ہے جو صارف کے پرامپٹ کی بنیاد پر ماڈل منتخب کرتا ہے اور Foundry Local کے OpenAI-compatible endpoint کو کال کرتا ہے۔

## فائلیں
- `router.py`: سادہ رجسٹری اور ہیورسٹک روٹنگ؛ اینڈ پوائنٹ دریافت + صحت کی جانچ۔

## چلائیں (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## نوٹس
- روٹر سادہ کلیدی الفاظ کے ہیورسٹکس استعمال کرتا ہے تاکہ `general`, `reasoning`, اور `code` ٹولز کے درمیان انتخاب کرے اور شروع میں `/v1/models` پرنٹ کرے۔
- ماحول کے متغیرات کے ذریعے ترتیب دیں:
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

## حوالہ جات
- Foundry Local (سیکھیں): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- انفرنس SDKs کے ساتھ انضمام کریں: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

