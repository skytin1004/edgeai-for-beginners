<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T17:47:17+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "bn"
}
-->
# সেশন ১ উদাহরণ: REST এর মাধ্যমে দ্রুত চ্যাট

Python `requests` ব্যবহার করে Foundry Local-এ একটি ন্যূনতম চ্যাট অনুরোধ চালান।

## পূর্বশর্ত
- Foundry Local সার্ভিস একটি মডেল চালাচ্ছে (যেমন, `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## চালান (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## রেফারেন্স
- Foundry Local (শিখুন): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI-সামঞ্জস্যপূর্ণ API ওভারভিউ: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

