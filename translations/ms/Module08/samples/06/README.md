<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T22:41:17+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "ms"
}
-->
# Sesi 6 Contoh: Model sebagai Alat

Contoh ini melaksanakan router + pendaftaran alat yang minimal, yang memilih model berdasarkan arahan pengguna dan memanggil endpoint Foundry Local yang serasi dengan OpenAI.

## Fail
- `router.py`: pendaftaran ringkas dan penghalaan heuristik; penemuan endpoint + pemeriksaan kesihatan.

## Jalankan (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Nota
- Router menggunakan heuristik kata kunci ringkas untuk memilih antara alat `general`, `reasoning`, dan `code` serta mencetak `/v1/models` semasa permulaan.
- Konfigurasi melalui pembolehubah persekitaran:
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

## Rujukan
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integrasi dengan SDK inferens: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

