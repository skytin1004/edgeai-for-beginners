<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T22:34:15+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "ms"
}
-->
# Changelog

Semua perubahan penting pada EdgeAI untuk Pemula didokumentasikan di sini. Projek ini menggunakan entri berdasarkan tarikh dan gaya Keep a Changelog (Ditambah, Diubah, Diperbaiki, Dihapus, Dokumentasi, Dipindahkan).

## 2025-09-18

### Ditambah
- Modul 08: Microsoft Foundry Local – Toolkit Pembangun Lengkap
  - Enam sesi: persediaan, integrasi Azure AI Foundry, model sumber terbuka, demo terkini, agen, dan model sebagai alat
  - Sampel boleh dijalankan di bawah `Module08/samples/01`–`06` dengan arahan cmd Windows
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart dengan sokongan OpenAI/Foundry Local dan Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orkestrasi multi-agen (`python -m samples.05.agents.coordinator`)
    - `06` Router model sebagai alat (`router.py`)
- Sokongan Azure OpenAI dalam sampel SDK Sesi 2 dengan konfigurasi pembolehubah persekitaran
- `.vscode/settings.json` untuk menunjuk ke `Module08/.venv` dan meningkatkan resolusi analisis Python
- `.env` dengan petunjuk `PYTHONPATH` untuk kesedaran VS Code/Pylance

### Diubah
- Model lalai dikemas kini kepada `phi-4-mini` di seluruh dokumen dan sampel Modul 08; semua sebutan `phi-3.5` yang tinggal dalam Modul 08 telah dihapuskan
- Penambahbaikan Router (`Module08/samples/06/router.py`):
  - Penemuan endpoint melalui `foundry service status` dengan parsing regex
  - Pemeriksaan kesihatan `/v1/models` semasa permulaan
  - Pendaftaran model yang boleh dikonfigurasi melalui env (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Keperluan dikemas kini: `Module08/requirements.txt` kini termasuk `openai` (bersama `requests`, `chainlit`)
- Panduan sampel Chainlit diperjelaskan dan penyelesaian masalah ditambah; resolusi import melalui tetapan ruang kerja

### Diperbaiki
- Masalah import diselesaikan:
  - Router tidak lagi bergantung pada modul `utils` yang tidak wujud; fungsi telah disatukan
  - Koordinator menggunakan import relatif (`from .specialists import ...`) dan dipanggil melalui laluan modul
  - Konfigurasi VS Code/Pylance untuk menyelesaikan import `chainlit` dan pakej
- Pembetulan typo kecil dalam `STUDY_GUIDE.md` dan liputan Modul 08 ditambah

### Dihapus
- `Module08/infra/obs.py` yang tidak digunakan telah dihapuskan dan direktori `infra/` yang kosong telah dibuang; corak pemerhatian dikekalkan sebagai pilihan dalam dokumen

### Dipindahkan
- Demo Modul 08 disatukan di bawah `Module08/samples` dengan folder bernombor sesi
  - Aplikasi Chainlit dipindahkan ke `samples/04`
  - Agen dipindahkan ke `samples/05` dan fail `__init__.py` ditambah untuk resolusi pakej

### Dokumentasi
- Dokumen sesi Modul 08 dan semua README sampel diperkaya dengan rujukan Microsoft Learn dan vendor yang dipercayai
- `Module08/README.md` dikemas kini dengan Gambaran Keseluruhan Sampel, konfigurasi router, dan petua pengesahan
- Bahagian Windows Foundry Local dalam `Module07/README.md` disahkan terhadap dokumen Learn
- `STUDY_GUIDE.md` dikemas kini:
  - Modul 08 ditambah ke gambaran keseluruhan, jadual, penjejak kemajuan
  - Bahagian Rujukan yang komprehensif ditambah (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Sejarah (ringkasan)
- Arkitektur kursus dan modul ditubuhkan (Modul 01–07)
- Pemodenan kandungan secara iteratif, penyeragaman format, dan kajian kes ditambah
- Liputan rangka kerja pengoptimuman diperluaskan (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Belum Dikeluarkan / Tertunda (cadangan)
- Ujian asap pilihan per sampel untuk mengesahkan ketersediaan Foundry Local
- Semak terjemahan untuk menyelaraskan rujukan model (contohnya, `phi-4-mini`) di mana sesuai
- Tambah konfigurasi pyright minimum jika pasukan lebih suka ketegasan seluruh ruang kerja

---

