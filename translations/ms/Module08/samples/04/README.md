<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T22:41:27+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "ms"
}
-->
# Sesi 4 Contoh: Demo Chainlit RAG

Jalankan aplikasi Chainlit minimal dengan Foundry Local.

## Prasyarat
- Windows 11, Python 3.10+
- Foundry Local dipasang dan model tersedia (contohnya, `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Jalankan (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Sahkan
```cmd
curl http://localhost:8000/v1/models
```

## Penyelesaian Masalah
- Jika VS Code menunjukkan "chainlit could not be resolved":
	- Pilih interpreter `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Pastikan kebergantungan dipasang: `pip install -r Module08\requirements.txt`

## Rujukan
- Cara membuka WebUI (aplikasi sembang dengan Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Belajar): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

