<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T22:34:05+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "id"
}
-->
# Changelog

Semua perubahan penting pada EdgeAI untuk Pemula didokumentasikan di sini. Proyek ini menggunakan entri berbasis tanggal dan gaya Keep a Changelog (Added, Changed, Fixed, Removed, Docs, Moved).

## 2025-09-18

### Added
- Modul 08: Microsoft Foundry Local – Toolkit Pengembang Lengkap
  - Enam sesi: pengaturan, integrasi Azure AI Foundry, model open-source, demo terbaru, agen, dan model sebagai alat
  - Contoh yang dapat dijalankan di bawah `Module08/samples/01`–`06` dengan instruksi cmd Windows
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart dengan OpenAI/Foundry Local dan dukungan Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orkestrasi multi-agen (`python -m samples.05.agents.coordinator`)
    - `06` Router model sebagai alat (`router.py`)
- Dukungan Azure OpenAI dalam contoh SDK Sesi 2 dengan konfigurasi variabel lingkungan
- `.vscode/settings.json` diarahkan ke `Module08/.venv` untuk meningkatkan resolusi analisis Python
- `.env` dengan petunjuk `PYTHONPATH` untuk kesadaran VS Code/Pylance

### Changed
- Model default diperbarui ke `phi-4-mini` di seluruh dokumen dan contoh Modul 08; menghapus sisa referensi `phi-3.5` dalam Modul 08
- Peningkatan Router (`Module08/samples/06/router.py`):
  - Penemuan endpoint melalui `foundry service status` dengan parsing regex
  - Pemeriksaan kesehatan `/v1/models` saat startup
  - Registri model yang dapat dikonfigurasi melalui lingkungan (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Persyaratan diperbarui: `Module08/requirements.txt` sekarang mencakup `openai` (bersama dengan `requests`, `chainlit`)
- Panduan contoh Chainlit diperjelas dan troubleshooting ditambahkan; resolusi impor melalui pengaturan workspace

### Fixed
- Masalah impor diselesaikan:
  - Router tidak lagi bergantung pada modul `utils` yang tidak ada; fungsi diintegrasikan langsung
  - Koordinator menggunakan impor relatif (`from .specialists import ...`) dan dijalankan melalui jalur modul
  - Konfigurasi VS Code/Pylance untuk menyelesaikan impor `chainlit` dan paket
- Typo kecil diperbaiki di `STUDY_GUIDE.md` dan cakupan Modul 08 ditambahkan

### Removed
- Menghapus `Module08/infra/obs.py` yang tidak digunakan dan menghapus direktori kosong `infra/`; pola observabilitas tetap sebagai opsional dalam dokumen

### Moved
- Demo Modul 08 dikonsolidasikan di bawah `Module08/samples` dengan folder bernomor sesi
  - Memindahkan aplikasi Chainlit ke `samples/04`
  - Memindahkan agen ke `samples/05` dan menambahkan file `__init__.py` untuk resolusi paket

### Docs
- Dokumen sesi Modul 08 dan semua README contoh diperkaya dengan referensi Microsoft Learn dan vendor terpercaya
- `Module08/README.md` diperbarui dengan Ikhtisar Contoh, konfigurasi router, dan tips validasi
- Bagian Windows Foundry Local di `Module07/README.md` divalidasi terhadap dokumen Learn
- `STUDY_GUIDE.md` diperbarui:
  - Menambahkan Modul 08 ke ikhtisar, jadwal, pelacak kemajuan
  - Menambahkan bagian Referensi yang komprehensif (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historical (ringkasan)
- Arsitektur kursus dan modul ditetapkan (Modul 01–07)
- Modernisasi konten secara iteratif, standarisasi format, dan penambahan studi kasus
- Perluasan cakupan kerangka kerja optimasi (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Unreleased / Backlog (usulan)
- Tes smoke opsional per contoh untuk memvalidasi ketersediaan Foundry Local
- Tinjau terjemahan untuk menyelaraskan referensi model (misalnya, `phi-4-mini`) jika sesuai
- Tambahkan konfigurasi pyright minimal jika tim lebih memilih keketatan di seluruh workspace

---

