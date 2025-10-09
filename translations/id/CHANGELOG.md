<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T18:57:57+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "id"
}
-->
# Catatan Perubahan

Semua perubahan penting pada EdgeAI untuk Pemula didokumentasikan di sini. Proyek ini menggunakan entri berbasis tanggal dan gaya Keep a Changelog (Ditambahkan, Diubah, Diperbaiki, Dihapus, Dokumentasi, Dipindahkan).

## 2025-10-08

### Ditambahkan - Pembaruan Komprehensif Workshop
- **Penulisan ulang lengkap README.md Workshop**:
  - Ditambahkan pengantar komprehensif yang menjelaskan nilai Edge AI (privasi, performa, biaya)
  - Dibuat 6 tujuan pembelajaran inti dengan kompetensi yang terperinci
  - Ditambahkan tabel hasil pembelajaran dengan deliverables dan matriks kompetensi
  - Disertakan bagian keterampilan siap kerja untuk relevansi industri
  - Ditambahkan panduan mulai cepat dengan prasyarat dan pengaturan 3 langkah
  - Dibuat tabel sumber daya untuk sampel Python (8 file dengan waktu eksekusi)
  - Ditambahkan tabel Jupyter notebooks (8 notebook dengan tingkat kesulitan)
  - Dibuat tabel dokumentasi (7 dokumen utama dengan panduan "Gunakan Saat")
  - Ditambahkan rekomendasi jalur pembelajaran untuk berbagai tingkat keterampilan

- **Infrastruktur validasi dan pengujian Workshop**:
  - Dibuat `scripts/validate_samples.py` - Alat validasi komprehensif untuk sintaks, impor, dan praktik terbaik
  - Dibuat `scripts/test_samples.py` - Penguji cepat untuk semua sampel Python
  - Ditambahkan dokumentasi validasi ke `scripts/README.md`

- **Dokumentasi komprehensif**:
  - Dibuat `SAMPLES_UPDATE_SUMMARY.md` - Panduan terperinci lebih dari 400 baris yang mencakup semua peningkatan
  - Dibuat `UPDATE_COMPLETE.md` - Ringkasan eksekutif dari penyelesaian pembaruan
  - Dibuat `QUICK_REFERENCE.md` - Kartu referensi cepat untuk Workshop

### Diubah - Modernisasi Sampel Python Workshop
- **Semua 8 sampel Python diperbarui dengan praktik terbaik**:
  - Peningkatan penanganan error dengan blok try-except di semua operasi I/O
  - Ditambahkan petunjuk tipe dan docstring yang komprehensif
  - Diimplementasikan pola logging [INFO]/[ERROR]/[RESULT] yang konsisten
  - Melindungi impor opsional dengan petunjuk instalasi
  - Peningkatan umpan balik pengguna di semua sampel

- **session01/chat_bootstrap.py**:
  - Peningkatan inisialisasi klien dengan pesan error yang komprehensif
  - Peningkatan penanganan error streaming dengan validasi chunk
  - Ditambahkan penanganan pengecualian yang lebih baik untuk ketidaktersediaan layanan

- **session02/rag_pipeline.py**:
  - Ditambahkan pengamanan impor untuk sentence-transformers dengan petunjuk instalasi
  - Peningkatan penanganan error untuk operasi embedding dan generasi
  - Peningkatan format output dengan hasil yang terstruktur

- **session02/rag_eval_ragas.py**:
  - Melindungi impor opsional (ragas, datasets) dengan pesan error yang ramah pengguna
  - Ditambahkan penanganan error untuk metrik evaluasi
  - Peningkatan format output untuk hasil evaluasi

- **session03/benchmark_oss_models.py**:
  - Diimplementasikan degradasi yang anggun (melanjutkan pada kegagalan model)
  - Ditambahkan pelaporan kemajuan yang terperinci dan penanganan error per model
  - Peningkatan perhitungan statistik dengan pemulihan error yang komprehensif

- **session04/model_compare.py**:
  - Ditambahkan petunjuk tipe (jenis pengembalian Tuple)
  - Peningkatan format output dengan hasil JSON yang terstruktur
  - Diimplementasikan penanganan error per model dengan pemulihan

- **session05/agents_orchestrator.py**:
  - Peningkatan Agent.act() dengan docstring yang komprehensif
  - Ditambahkan penanganan error pipeline dengan logging tahap demi tahap
  - Peningkatan manajemen memori dan pelacakan status

- **session06/models_router.py**:
  - Peningkatan dokumentasi fungsi untuk semua komponen routing
  - Ditambahkan logging yang terperinci dalam fungsi route()
  - Peningkatan output pengujian dengan hasil yang terstruktur

- **session06/models_pipeline.py**:
  - Ditambahkan penanganan error ke fungsi pembantu chat()
  - Peningkatan pipeline() dengan logging tahap dan pelaporan kemajuan
  - Peningkatan main() dengan pemulihan error yang komprehensif

### Dokumentasi - Peningkatan Dokumentasi Workshop
- Diperbarui README.md utama dengan bagian Workshop yang menyoroti jalur pembelajaran langsung
- Peningkatan STUDY_GUIDE.md dengan bagian Workshop yang komprehensif termasuk:
  - Tujuan pembelajaran dan area fokus studi
  - Pertanyaan penilaian mandiri
  - Latihan langsung dengan estimasi waktu
  - Alokasi waktu untuk studi intensif dan paruh waktu
  - Ditambahkan Workshop ke template pelacakan kemajuan
- Diperbarui panduan alokasi waktu dari 20 jam menjadi 30 jam (termasuk Workshop)
- Ditambahkan deskripsi sampel Workshop dan hasil pembelajaran ke README

### Diperbaiki
- Diselesaikan pola penanganan error yang tidak konsisten di seluruh sampel Workshop
- Diperbaiki error impor dependensi opsional dengan pengamanan yang tepat
- Dikoreksi petunjuk tipe yang hilang di fungsi-fungsi penting
- Ditangani umpan balik pengguna yang tidak memadai dalam skenario error
- Diperbaiki masalah validasi dengan infrastruktur pengujian yang komprehensif

---

## 2025-09-23

### Diubah - Modernisasi Modul 08 Besar
- **Penyelarasan komprehensif dengan pola repositori Microsoft Foundry-Local**:
  - Diperbarui semua contoh kode untuk menggunakan `FoundryLocalManager` modern dan integrasi SDK OpenAI
  - Diganti panggilan manual `requests` yang usang dengan penggunaan SDK yang tepat
  - Diselaraskan pola implementasi dengan dokumentasi dan sampel resmi Microsoft

- **Modernisasi 05.AIPoweredAgents.md**:
  - Diperbarui orkestrasi multi-agen untuk menggunakan pola SDK modern
  - Peningkatan implementasi koordinator dengan fitur canggih (loop umpan balik, pemantauan performa)
  - Ditambahkan penanganan error yang komprehensif dan pemeriksaan kesehatan layanan
  - Diintegrasikan referensi yang tepat ke sampel lokal (`samples/05/multi_agent_orchestration.ipynb`)
  - Diperbarui contoh pemanggilan fungsi untuk menggunakan parameter `tools` modern alih-alih `functions` yang usang
  - Ditambahkan pola siap produksi dengan pemantauan dan pelacakan statistik

- **Penulisan ulang lengkap 06.ModelsAsTools.md**:
  - Diganti registri alat dasar dengan implementasi router model yang cerdas
  - Ditambahkan pemilihan model berbasis kata kunci untuk berbagai jenis tugas (umum, penalaran, kode, kreatif)
  - Diintegrasikan konfigurasi berbasis lingkungan dengan penugasan model yang fleksibel
  - Ditingkatkan dengan pemantauan kesehatan layanan yang komprehensif dan penanganan error
  - Ditambahkan pola penerapan produksi dengan pemantauan permintaan dan pelacakan performa
  - Diselaraskan dengan implementasi lokal di `samples/06/router.py` dan `samples/06/model_router.ipynb`

- **Peningkatan struktur dokumentasi**:
  - Ditambahkan bagian ikhtisar yang menyoroti modernisasi dan penyelarasan SDK
  - Ditingkatkan dengan emoji dan format yang lebih baik untuk meningkatkan keterbacaan
  - Ditambahkan referensi yang tepat ke file sampel lokal di seluruh dokumentasi
  - Disertakan panduan implementasi siap produksi dan praktik terbaik

### Ditambahkan
- Bagian ikhtisar komprehensif di file Modul 08 yang menyoroti integrasi SDK modern
- Sorotan arsitektur yang menunjukkan fitur canggih (sistem multi-agen, routing cerdas)
- Referensi langsung ke implementasi sampel lokal untuk pengalaman langsung
- Panduan penerapan produksi dengan pola pemantauan dan penanganan error
- Contoh notebook Jupyter interaktif dengan fitur canggih dan benchmark

### Diperbaiki
- Ketidaksesuaian penyelarasan antara dokumentasi dan implementasi sampel aktual
- Pola penggunaan SDK yang usang di seluruh Modul 08
- Referensi yang hilang ke pustaka sampel lokal yang komprehensif
- Pendekatan implementasi yang tidak konsisten di berbagai bagian

---

## 2025-09-18

### Ditambahkan
- Modul 08: Microsoft Foundry Local – Toolkit Pengembang Lengkap
  - Enam sesi: pengaturan, integrasi Azure AI Foundry, model open-source, demo mutakhir, agen, dan model-sebagai-alat
  - Sampel yang dapat dijalankan di bawah `Module08/samples/01`–`06` dengan instruksi cmd Windows
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart dengan OpenAI/Foundry Local dan dukungan Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orkestrasi multi-agen (`python -m samples.05.agents.coordinator`)
    - `06` Router Model-sebagai-Alat (`router.py`)
- Dukungan Azure OpenAI di sampel SDK Sesi 2 dengan konfigurasi variabel lingkungan
- `.vscode/settings.json` untuk menunjuk ke `Module08/.venv` dan meningkatkan resolusi analisis Python
- `.env` dengan petunjuk `PYTHONPATH` untuk kesadaran VS Code/Pylance

### Diubah
- Model default diperbarui ke `phi-4-mini` di seluruh dokumen dan sampel Modul 08; dihapus penyebutan `phi-3.5` yang tersisa dalam Modul 08
- Peningkatan Router (`Module08/samples/06/router.py`):
  - Penemuan endpoint melalui `foundry service status` dengan parsing regex
  - Pemeriksaan kesehatan `/v1/models` saat startup
  - Registri model yang dapat dikonfigurasi lingkungan (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Persyaratan diperbarui: `Module08/requirements.txt` sekarang mencakup `openai` (bersama `requests`, `chainlit`)
- Panduan sampel Chainlit diklarifikasi dan troubleshooting ditambahkan; resolusi impor melalui pengaturan workspace

### Diperbaiki
- Masalah impor diselesaikan:
  - Router tidak lagi bergantung pada modul `utils` yang tidak ada; fungsi-fungsi diintegrasikan
  - Koordinator menggunakan impor relatif (`from .specialists import ...`) dan dipanggil melalui jalur modul
  - Konfigurasi VS Code/Pylance untuk menyelesaikan `chainlit` dan impor paket
- Dikoreksi typo kecil di `STUDY_GUIDE.md` dan ditambahkan cakupan Modul 08

### Dihapus
- Dihapus `Module08/infra/obs.py` yang tidak digunakan dan direktori `infra/` yang kosong; pola observabilitas dipertahankan sebagai opsional dalam dokumentasi

### Dipindahkan
- Demo Modul 08 dikonsolidasikan di bawah `Module08/samples` dengan folder bernomor sesi
  - Aplikasi Chainlit dipindahkan ke `samples/04`
  - Agen dipindahkan ke `samples/05` dan ditambahkan file `__init__.py` untuk resolusi paket

### Dokumentasi
- Dokumentasi sesi Modul 08 dan semua README sampel diperkaya dengan referensi Microsoft Learn dan vendor terpercaya
- `Module08/README.md` diperbarui dengan Ikhtisar Sampel, konfigurasi router, dan tips validasi
- Bagian Windows Foundry Local di `Module07/README.md` divalidasi terhadap dokumen Learn
- `STUDY_GUIDE.md` diperbarui:
  - Ditambahkan Modul 08 ke ikhtisar, jadwal, pelacak kemajuan
  - Ditambahkan bagian Referensi yang komprehensif (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Sejarah (ringkasan)
- Arsitektur kursus dan modul ditetapkan (Modul 01–07)
- Modernisasi konten secara iteratif, standarisasi format, dan penambahan studi kasus
- Perluasan cakupan kerangka kerja optimasi (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Belum Dirilis / Backlog (usulan)
- Pengujian cepat opsional per sampel untuk memvalidasi ketersediaan Foundry Local
- Tinjau terjemahan untuk menyelaraskan referensi model (misalnya, `phi-4-mini`) jika sesuai
- Tambahkan konfigurasi pyright minimal jika tim lebih memilih keketatan di seluruh workspace

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.