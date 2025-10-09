<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T19:02:26+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "ms"
}
-->
# Log Perubahan

Semua perubahan penting pada EdgeAI untuk Pemula didokumentasikan di sini. Projek ini menggunakan entri berdasarkan tarikh dan gaya Keep a Changelog (Ditambah, Diubah, Diperbaiki, Dihapus, Dokumentasi, Dipindahkan).

## 2025-10-08

### Ditambah - Kemas Kini Komprehensif Bengkel
- **Penulisan semula lengkap README.md Bengkel**:
  - Ditambah pengenalan komprehensif yang menerangkan nilai Edge AI (privasi, prestasi, kos)
  - Dicipta 6 objektif pembelajaran utama dengan kompetensi terperinci
  - Ditambah jadual hasil pembelajaran dengan hasil dan matriks kompetensi
  - Termasuk bahagian kemahiran bersedia untuk kerjaya bagi relevansi industri
  - Ditambah panduan permulaan pantas dengan prasyarat dan persediaan 3 langkah
  - Dicipta jadual sumber untuk sampel Python (8 fail dengan masa jalan)
  - Ditambah jadual Jupyter notebooks (8 notebooks dengan penilaian kesukaran)
  - Dicipta jadual dokumentasi (7 dokumen utama dengan panduan "Gunakan Bila")
  - Ditambah cadangan laluan pembelajaran untuk tahap kemahiran yang berbeza

- **Infrastruktur pengesahan dan ujian Bengkel**:
  - Dicipta `scripts/validate_samples.py` - Alat pengesahan komprehensif untuk sintaks, import, dan amalan terbaik
  - Dicipta `scripts/test_samples.py` - Pelari ujian pantas untuk semua sampel Python
  - Ditambah dokumentasi pengesahan ke `scripts/README.md`

- **Dokumentasi komprehensif**:
  - Dicipta `SAMPLES_UPDATE_SUMMARY.md` - Panduan terperinci 400+ baris yang merangkumi semua penambahbaikan
  - Dicipta `UPDATE_COMPLETE.md` - Ringkasan eksekutif tentang penyelesaian kemas kini
  - Dicipta `QUICK_REFERENCE.md` - Kad rujukan pantas untuk Bengkel

### Diubah - Pemodenan Sampel Python Bengkel
- **Semua 8 sampel Python dikemas kini dengan amalan terbaik**:
  - Meningkatkan pengendalian ralat dengan blok try-except di sekitar semua operasi I/O
  - Ditambah petunjuk jenis dan docstring komprehensif
  - Melaksanakan corak log konsisten [INFO]/[ERROR]/[RESULT]
  - Melindungi import pilihan dengan petunjuk pemasangan
  - Meningkatkan maklum balas pengguna di semua sampel

- **session01/chat_bootstrap.py**:
  - Meningkatkan inisialisasi klien dengan mesej ralat komprehensif
  - Memperbaiki pengendalian ralat penstriman dengan pengesahan chunk
  - Ditambah pengendalian pengecualian yang lebih baik untuk ketidaktersediaan perkhidmatan

- **session02/rag_pipeline.py**:
  - Ditambah pengawal import untuk sentence-transformers dengan petunjuk pemasangan
  - Meningkatkan pengendalian ralat untuk operasi embedding dan generasi
  - Memperbaiki pemformatan output dengan hasil yang terstruktur

- **session02/rag_eval_ragas.py**:
  - Melindungi import pilihan (ragas, datasets) dengan mesej ralat mesra pengguna
  - Ditambah pengendalian ralat untuk metrik penilaian
  - Memperbaiki pemformatan output untuk hasil penilaian

- **session03/benchmark_oss_models.py**:
  - Melaksanakan degradasi yang anggun (teruskan pada kegagalan model)
  - Ditambah pelaporan kemajuan terperinci dan pengendalian ralat per-model
  - Meningkatkan pengiraan statistik dengan pemulihan ralat komprehensif

- **session04/model_compare.py**:
  - Ditambah petunjuk jenis (Jenis Tuple)
  - Memperbaiki pemformatan output dengan hasil JSON terstruktur
  - Melaksanakan pengendalian ralat per-model dengan pemulihan

- **session05/agents_orchestrator.py**:
  - Meningkatkan Agent.act() dengan docstring komprehensif
  - Ditambah pengendalian ralat pipeline dengan log peringkat demi peringkat
  - Memperbaiki pengurusan memori dan penjejakan keadaan

- **session06/models_router.py**:
  - Meningkatkan dokumentasi fungsi untuk semua komponen penghalaan
  - Ditambah log terperinci dalam fungsi route()
  - Memperbaiki output ujian dengan hasil terstruktur

- **session06/models_pipeline.py**:
  - Ditambah pengendalian ralat pada fungsi pembantu chat()
  - Meningkatkan pipeline() dengan log peringkat dan pelaporan kemajuan
  - Memperbaiki main() dengan pemulihan ralat komprehensif

### Dokumentasi - Penambahbaikan Dokumentasi Bengkel
- Dikemas kini README.md utama dengan bahagian Bengkel yang menonjolkan laluan pembelajaran praktikal
- Meningkatkan STUDY_GUIDE.md dengan bahagian Bengkel komprehensif termasuk:
  - Objektif pembelajaran dan fokus kajian
  - Soalan penilaian kendiri
  - Latihan praktikal dengan anggaran masa
  - Peruntukan masa untuk kajian intensif dan separuh masa
  - Ditambah Bengkel ke templat penjejakan kemajuan
- Dikemas kini panduan peruntukan masa dari 20 jam ke 30 jam (termasuk Bengkel)
- Ditambah penerangan sampel Bengkel dan hasil pembelajaran ke README

### Diperbaiki
- Menyelesaikan corak pengendalian ralat yang tidak konsisten di seluruh sampel Bengkel
- Memperbaiki ralat import kebergantungan pilihan dengan pengawal yang betul
- Membetulkan petunjuk jenis yang hilang dalam fungsi kritikal
- Menangani maklum balas pengguna yang tidak mencukupi dalam senario ralat
- Memperbaiki isu pengesahan dengan infrastruktur ujian komprehensif

---

## 2025-09-23

### Diubah - Pemodenan Modul 08 Utama
- **Penyelarasan komprehensif dengan corak repositori Microsoft Foundry-Local**:
  - Dikemas kini semua contoh kod untuk menggunakan `FoundryLocalManager` moden dan integrasi SDK OpenAI
  - Menggantikan panggilan manual `requests` yang usang dengan penggunaan SDK yang betul
  - Menyelaraskan corak pelaksanaan dengan dokumentasi rasmi Microsoft dan sampel

- **Pemodenan 05.AIPoweredAgents.md**:
  - Dikemas kini orkestrasi multi-agen untuk menggunakan corak SDK moden
  - Meningkatkan pelaksanaan penyelaras dengan ciri-ciri canggih (gelung maklum balas, pemantauan prestasi)
  - Ditambah pengendalian ralat komprehensif dan pemeriksaan kesihatan perkhidmatan
  - Mengintegrasikan rujukan yang betul kepada sampel tempatan (`samples/05/multi_agent_orchestration.ipynb`)
  - Dikemas kini contoh panggilan fungsi untuk menggunakan parameter `tools` moden dan bukannya `functions` yang usang
  - Ditambah corak bersedia untuk pengeluaran dengan pemantauan dan penjejakan statistik

- **Penulisan semula lengkap 06.ModelsAsTools.md**:
  - Menggantikan pendaftaran alat asas dengan pelaksanaan penghala model pintar
  - Ditambah pemilihan model berdasarkan kata kunci untuk jenis tugas yang berbeza (umum, penaakulan, kod, kreatif)
  - Mengintegrasikan konfigurasi berdasarkan persekitaran dengan penugasan model yang fleksibel
  - Meningkatkan dengan pemantauan kesihatan perkhidmatan komprehensif dan pengendalian ralat
  - Ditambah corak pengeluaran dengan pemantauan permintaan dan penjejakan prestasi
  - Menyelaraskan dengan pelaksanaan tempatan dalam `samples/06/router.py` dan `samples/06/model_router.ipynb`

- **Penambahbaikan struktur dokumentasi**:
  - Ditambah bahagian gambaran keseluruhan yang menonjolkan pemodenan dan penyelarasan SDK
  - Meningkatkan dengan emoji dan pemformatan yang lebih baik untuk meningkatkan kebolehbacaan
  - Ditambah rujukan yang betul kepada fail sampel tempatan di seluruh dokumentasi
  - Termasuk panduan pelaksanaan bersedia untuk pengeluaran dan amalan terbaik

### Ditambah
- Bahagian gambaran keseluruhan komprehensif dalam fail Modul 08 yang menonjolkan integrasi SDK moden
- Sorotan seni bina yang mempamerkan ciri-ciri canggih (sistem multi-agen, penghala pintar)
- Rujukan langsung kepada pelaksanaan sampel tempatan untuk pengalaman praktikal
- Panduan pengeluaran dengan corak pemantauan dan pengendalian ralat
- Contoh Jupyter notebook interaktif dengan ciri-ciri canggih dan penanda aras

### Diperbaiki
- Ketidaksejajaran penyelarasan antara dokumentasi dan pelaksanaan sampel sebenar
- Corak penggunaan SDK yang usang di seluruh Modul 08
- Rujukan yang hilang kepada perpustakaan sampel tempatan yang komprehensif
- Pendekatan pelaksanaan yang tidak konsisten di seluruh bahagian yang berbeza

---

## 2025-09-18

### Ditambah
- Modul 08: Microsoft Foundry Local – Toolkit Pembangun Lengkap
  - Enam sesi: persediaan, integrasi Azure AI Foundry, model sumber terbuka, demo canggih, agen, dan model-sebagai-alat
  - Sampel boleh dijalankan di bawah `Module08/samples/01`–`06` dengan arahan cmd Windows
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart dengan sokongan OpenAI/Foundry Local dan Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orkestrasi multi-agen (`python -m samples.05.agents.coordinator`)
    - `06` Penghala Model-sebagai-Alat (`router.py`)
- Sokongan Azure OpenAI dalam sampel SDK Sesi 2 dengan konfigurasi pembolehubah persekitaran
- `.vscode/settings.json` untuk menunjuk ke `Module08/.venv` dan meningkatkan resolusi analisis Python
- `.env` dengan petunjuk `PYTHONPATH` untuk kesedaran VS Code/Pylance

### Diubah
- Model lalai dikemas kini ke `phi-4-mini` di seluruh dokumen dan sampel Modul 08; menghapuskan sebutan `phi-3.5` yang tinggal dalam Modul 08
- Penambahbaikan penghala (`Module08/samples/06/router.py`):
  - Penemuan titik akhir melalui `foundry service status` dengan parsing regex
  - Pemeriksaan kesihatan `/v1/models` semasa permulaan
  - Pendaftaran model yang boleh dikonfigurasi persekitaran (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Keperluan dikemas kini: `Module08/requirements.txt` kini termasuk `openai` (bersama `requests`, `chainlit`)
- Panduan sampel Chainlit diperjelaskan dan penyelesaian masalah ditambah; resolusi import melalui tetapan ruang kerja

### Diperbaiki
- Menyelesaikan isu import:
  - Penghala tidak lagi bergantung pada modul `utils` yang tidak wujud; fungsi diintegrasikan
  - Penyelaras menggunakan import relatif (`from .specialists import ...`) dan dipanggil melalui laluan modul
  - Konfigurasi VS Code/Pylance untuk menyelesaikan `chainlit` dan import pakej
- Membetulkan typo kecil dalam `STUDY_GUIDE.md` dan menambah liputan Modul 08

### Dihapus
- Menghapuskan `Module08/infra/obs.py` yang tidak digunakan dan menghapuskan direktori `infra/` yang kosong; corak pemerhatian dikekalkan sebagai pilihan dalam dokumen

### Dipindahkan
- Menyatukan demo Modul 08 di bawah `Module08/samples` dengan folder bernombor sesi
  - Memindahkan aplikasi Chainlit ke `samples/04`
  - Memindahkan agen ke `samples/05` dan menambah fail `__init__.py` untuk resolusi pakej

### Dokumentasi
- Dokumen sesi Modul 08 dan semua README sampel diperkaya dengan rujukan Microsoft Learn dan vendor yang dipercayai
- `Module08/README.md` dikemas kini dengan Gambaran Keseluruhan Sampel, konfigurasi penghala, dan petua pengesahan
- Bahagian Windows Foundry Local `Module07/README.md` disahkan terhadap dokumen Learn
- `STUDY_GUIDE.md` dikemas kini:
  - Ditambah Modul 08 ke gambaran keseluruhan, jadual, penjejak kemajuan
  - Ditambah bahagian Rujukan komprehensif (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Sejarah (ringkasan)
- Seni bina kursus dan modul ditubuhkan (Modul 01–07)
- Pemodenan kandungan secara iteratif, penyeragaman format, dan penambahan kajian kes
- Liputan rangka kerja pengoptimuman diperluaskan (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Belum Dikeluarkan / Senarai Tertunggak (cadangan)
- Ujian pantas pilihan per-sampel untuk mengesahkan ketersediaan Foundry Local
- Semak terjemahan untuk menyelaraskan rujukan model (contoh: `phi-4-mini`) di mana sesuai
- Tambah konfigurasi pyright minimum jika pasukan lebih suka ketegasan seluruh ruang kerja

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.