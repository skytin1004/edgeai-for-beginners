<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T18:34:08+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "pa"
}
-->
# ਸੈਸ਼ਨ 1 ਨਮੂਨਾ: REST ਰਾਹੀਂ ਤੇਜ਼ ਗੱਲਬਾਤ

Python `requests` ਦੀ ਵਰਤੋਂ ਕਰਕੇ Foundry Local ਨਾਲ ਘੱਟੋ-ਘੱਟ ਗੱਲਬਾਤ ਦੀ ਬੇਨਤੀ ਚਲਾਓ।

## ਪੂਰਵ ਸ਼ਰਤਾਂ
- Foundry Local ਸੇਵਾ ਜੋ ਮਾਡਲ ਚਲਾ ਰਹੀ ਹੈ (ਜਿਵੇਂ ਕਿ `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## ਚਲਾਓ (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## ਸੰਦਰਭ
- Foundry Local (ਸਿੱਖੋ): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI-ਅਨੁਕੂਲ API ਝਲਕ: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

