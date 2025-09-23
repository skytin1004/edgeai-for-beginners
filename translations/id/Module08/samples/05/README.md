<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-22T22:41:02+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "id"
}
-->
# Sesi 5 Contoh: Orkestrasi Multi-Agen

Contoh ini menunjukkan pola koordinator + spesialis menggunakan endpoint Foundry Local yang kompatibel dengan OpenAI.

## Jalankan (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Validasi
```cmd
curl http://localhost:8000/v1/models
```

## Pemecahan Masalah
- Jika VS Code menandai `import specialists` tidak terselesaikan di `coordinator.py`, pastikan Anda menjalankan sebagai modul dan interpreter mengarah ke `Module08/.venv`:
	- Jalankan: `python -m samples.05.agents.coordinator`
	- Pilih interpreter: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Referensi
- Foundry Local (Pelajari): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Ikhtisar Azure AI Agents: https://learn.microsoft.com/azure/ai-services/agents/overview
- Contoh pemanggilan fungsi (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

