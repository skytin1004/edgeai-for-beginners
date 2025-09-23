<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T22:41:00+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "tl"
}
-->
# Session 1 Sample: Mabilis na Chat gamit ang REST

Magpatakbo ng simpleng chat request sa Foundry Local gamit ang Python `requests`.

## Mga Kinakailangan
- Foundry Local service na tumatakbo gamit ang isang modelo (hal., `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Pagpapatakbo (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Mga Sanggunian
- Foundry Local (Learn): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI-compatible API overview: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

