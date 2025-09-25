<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-25T00:37:57+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "id"
}
-->
# Catatan Perubahan

Semua perubahan penting pada EdgeAI untuk Pemula didokumentasikan di sini. Proyek ini menggunakan entri berbasis tanggal dan gaya Keep a Changelog (Ditambahkan, Diubah, Diperbaiki, Dihapus, Dokumentasi, Dipindahkan).

## 2025-09-23

### Diubah - Modernisasi Utama Modul 08
- **Penyelarasan menyeluruh dengan pola repositori Microsoft Foundry-Local**
  - Memperbarui semua contoh kode untuk menggunakan `FoundryLocalManager` modern dan integrasi OpenAI SDK
  - Mengganti panggilan manual `requests` yang sudah usang dengan penggunaan SDK yang tepat
  - Menyelaraskan pola implementasi dengan dokumentasi resmi Microsoft dan contoh-contoh

- **Modernisasi 05.AIPoweredAgents.md**:
  - Memperbarui orkestrasi multi-agen untuk menggunakan pola SDK modern
  - Meningkatkan implementasi koordinator dengan fitur canggih (loop umpan balik, pemantauan kinerja)
  - Menambahkan penanganan kesalahan yang komprehensif dan pemeriksaan kesehatan layanan
  - Mengintegrasikan referensi yang tepat ke contoh lokal (`samples/05/multi_agent_orchestration.ipynb`)
  - Memperbarui contoh pemanggilan fungsi untuk menggunakan parameter `tools` modern alih-alih `functions` yang sudah usang
  - Menambahkan pola siap produksi dengan pemantauan dan pelacakan statistik

- **Penulisan ulang lengkap 06.ModelsAsTools.md**:
  - Mengganti registri alat dasar dengan implementasi router model cerdas
  - Menambahkan pemilihan model berbasis kata kunci untuk berbagai jenis tugas (umum, penalaran, kode, kreatif)
  - Mengintegrasikan konfigurasi berbasis lingkungan dengan penugasan model yang fleksibel
  - Ditingkatkan dengan pemantauan kesehatan layanan yang komprehensif dan penanganan kesalahan
  - Menambahkan pola penerapan produksi dengan pemantauan permintaan dan pelacakan kinerja
  - Diselaraskan dengan implementasi lokal di `samples/06/router.py` dan `samples/06/model_router.ipynb`

- **Peningkatan struktur dokumentasi**:
  - Menambahkan bagian ikhtisar yang menyoroti modernisasi dan penyelarasan SDK
  - Ditingkatkan dengan emoji dan format yang lebih baik untuk meningkatkan keterbacaan
  - Menambahkan referensi yang tepat ke file contoh lokal di seluruh dokumentasi
  - Menyertakan panduan implementasi siap produksi dan praktik terbaik

### Ditambahkan
- Bagian ikhtisar komprehensif dalam file Modul 08 yang menyoroti integrasi SDK modern
- Sorotan arsitektur yang menunjukkan fitur canggih (sistem multi-agen, routing cerdas)
- Referensi langsung ke implementasi contoh lokal untuk pengalaman langsung
- Panduan penerapan produksi dengan pola pemantauan dan penanganan kesalahan
- Contoh notebook Jupyter interaktif dengan fitur canggih dan tolok ukur

### Diperbaiki
- Ketidaksesuaian penyelarasan antara dokumentasi dan implementasi contoh aktual
- Pola penggunaan SDK yang sudah usang di seluruh Modul 08
- Referensi yang hilang ke pustaka contoh lokal yang komprehensif
- Pendekatan implementasi yang tidak konsisten di berbagai bagian

---

## 2025-09-18

### Ditambahkan
- Modul 08: Microsoft Foundry Local – Toolkit Pengembang Lengkap
  - Enam sesi: pengaturan, integrasi Azure AI Foundry, model open-source, demo mutakhir, agen, dan model-sebagai-alat
  - Contoh yang dapat dijalankan di bawah `Module08/samples/01`–`06` dengan instruksi cmd Windows
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart dengan OpenAI/Foundry Local dan dukungan Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orkestrasi multi-agen (`python -m samples.05.agents.coordinator`)
    - `06` Router Models-as-Tools (`router.py`)
- Dukungan Azure OpenAI dalam contoh SDK Sesi 2 dengan konfigurasi variabel lingkungan
- `.vscode/settings.json` untuk menunjuk ke `Module08/.venv` dan meningkatkan resolusi analisis Python
- `.env` dengan petunjuk `PYTHONPATH` untuk kesadaran VS Code/Pylance

### Diubah
- Model default diperbarui ke `phi-4-mini` di seluruh dokumen dan contoh Modul 08; menghapus sisa penyebutan `phi-3.5` dalam Modul 08
- Peningkatan Router (`Module08/samples/06/router.py`):
  - Penemuan endpoint melalui `foundry service status` dengan parsing regex
  - Pemeriksaan kesehatan `/v1/models` saat startup
  - Registri model yang dapat dikonfigurasi lingkungan (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Persyaratan diperbarui: `Module08/requirements.txt` sekarang menyertakan `openai` (bersama dengan `requests`, `chainlit`)
- Panduan contoh Chainlit diperjelas dan penanganan masalah ditambahkan; resolusi impor melalui pengaturan ruang kerja

### Diperbaiki
- Masalah impor diselesaikan:
  - Router tidak lagi bergantung pada modul `utils` yang tidak ada; fungsi diintegrasikan langsung
  - Koordinator menggunakan impor relatif (`from .specialists import ...`) dan dipanggil melalui jalur modul
  - Konfigurasi VS Code/Pylance untuk menyelesaikan impor `chainlit` dan paket
- Typo kecil diperbaiki dalam `STUDY_GUIDE.md` dan cakupan Modul 08 ditambahkan

### Dihapus
- Menghapus `Module08/infra/obs.py` yang tidak digunakan dan menghapus direktori `infra/` kosong; pola observabilitas dipertahankan sebagai opsional dalam dokumentasi

### Dipindahkan
- Konsolidasi demo Modul 08 di bawah `Module08/samples` dengan folder bernomor sesi
  - Memindahkan aplikasi Chainlit ke `samples/04`
  - Memindahkan agen ke `samples/05` dan menambahkan file `__init__.py` untuk resolusi paket

### Dokumentasi
- Dokumentasi sesi Modul 08 dan semua README contoh diperkaya dengan referensi Microsoft Learn dan vendor terpercaya
- `Module08/README.md` diperbarui dengan Ikhtisar Contoh, konfigurasi router, dan tips validasi
- Bagian Windows Foundry Local di `Module07/README.md` divalidasi terhadap dokumen Learn
- `STUDY_GUIDE.md` diperbarui:
  - Menambahkan Modul 08 ke ikhtisar, jadwal, pelacak kemajuan
  - Menambahkan bagian Referensi yang komprehensif (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Sejarah (ringkasan)
- Arsitektur kursus dan modul ditetapkan (Modul 01–07)
- Modernisasi konten secara iteratif, standarisasi format, dan penambahan studi kasus
- Perluasan cakupan kerangka kerja optimasi (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Belum Dirilis / Backlog (usulan)
- Tes smoke opsional per contoh untuk memvalidasi ketersediaan Foundry Local
- Tinjau terjemahan untuk menyelaraskan referensi model (misalnya, `phi-4-mini`) jika sesuai
- Menambahkan konfigurasi pyright minimal jika tim lebih memilih keketatan di seluruh ruang kerja

---

