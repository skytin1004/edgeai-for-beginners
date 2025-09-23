<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-22T22:41:06+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "ms"
}
-->
# Sesi 5 Contoh: Orkestrasi Multi-Ejen

Contoh ini menunjukkan corak penyelaras + pakar menggunakan endpoint Foundry Local yang serasi dengan OpenAI.

## Jalankan (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Sahkan
```cmd
curl http://localhost:8000/v1/models
```

## Penyelesaian Masalah
- Jika VS Code menandakan `import specialists` tidak dapat diselesaikan dalam `coordinator.py`, pastikan anda menjalankan sebagai modul dan interpreter menunjuk kepada `Module08/.venv`:
	- Jalankan: `python -m samples.05.agents.coordinator`
	- Pilih interpreter: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Rujukan
- Foundry Local (Belajar): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Gambaran keseluruhan Azure AI Agents: https://learn.microsoft.com/azure/ai-services/agents/overview
- Contoh pemanggilan fungsi (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

