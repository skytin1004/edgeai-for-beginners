<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-25T00:44:03+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "ms"
}
-->
# Changelog

Semua perubahan penting pada EdgeAI untuk Pemula didokumentasikan di sini. Projek ini menggunakan entri berdasarkan tarikh dan gaya Keep a Changelog (Ditambah, Diubah, Diperbaiki, Dihapus, Dokumentasi, Dipindahkan).

## 2025-09-23

### Diubah - Pemodenan Utama Modul 08
- **Penyelarasan menyeluruh dengan corak repositori Microsoft Foundry-Local**
  - Dikemas kini semua contoh kod untuk menggunakan `FoundryLocalManager` moden dan integrasi SDK OpenAI
  - Menggantikan panggilan manual `requests` yang usang dengan penggunaan SDK yang betul
  - Menyelaraskan corak pelaksanaan dengan dokumentasi rasmi Microsoft dan sampel

- **Pemodenan 05.AIPoweredAgents.md**:
  - Dikemas kini orkestrasi multi-agen untuk menggunakan corak SDK moden
  - Meningkatkan pelaksanaan penyelaras dengan ciri-ciri canggih (gelung maklum balas, pemantauan prestasi)
  - Menambah pengendalian ralat yang menyeluruh dan pemeriksaan kesihatan perkhidmatan
  - Mengintegrasikan rujukan yang betul kepada sampel tempatan (`samples/05/multi_agent_orchestration.ipynb`)
  - Dikemas kini contoh panggilan fungsi untuk menggunakan parameter `tools` moden dan bukannya `functions` yang usang
  - Menambah corak sedia pengeluaran dengan pemantauan dan penjejakan statistik

- **Penulisan semula lengkap 06.ModelsAsTools.md**:
  - Menggantikan pendaftaran alat asas dengan pelaksanaan penghala model pintar
  - Menambah pemilihan model berdasarkan kata kunci untuk jenis tugas yang berbeza (umum, penaakulan, kod, kreatif)
  - Mengintegrasikan konfigurasi berdasarkan persekitaran dengan penugasan model yang fleksibel
  - Ditingkatkan dengan pemantauan kesihatan perkhidmatan yang menyeluruh dan pengendalian ralat
  - Menambah corak pengeluaran dengan pemantauan permintaan dan penjejakan prestasi
  - Diselaraskan dengan pelaksanaan tempatan dalam `samples/06/router.py` dan `samples/06/model_router.ipynb`

- **Penambahbaikan struktur dokumentasi**:
  - Menambah bahagian gambaran keseluruhan yang menonjolkan pemodenan dan penyelarasan SDK
  - Ditingkatkan dengan emoji dan format yang lebih baik untuk meningkatkan kebolehbacaan
  - Menambah rujukan yang betul kepada fail sampel tempatan di seluruh dokumentasi
  - Termasuk panduan pelaksanaan sedia pengeluaran dan amalan terbaik

### Ditambah
- Bahagian gambaran keseluruhan yang menyeluruh dalam fail Modul 08 yang menonjolkan integrasi SDK moden
- Sorotan seni bina yang mempamerkan ciri-ciri canggih (sistem multi-agen, penghala pintar)
- Rujukan langsung kepada pelaksanaan sampel tempatan untuk pengalaman langsung
- Panduan pengeluaran dengan corak pemantauan dan pengendalian ralat
- Contoh Jupyter notebook interaktif dengan ciri-ciri canggih dan penanda aras

### Diperbaiki
- Ketidaksejajaran antara dokumentasi dan pelaksanaan sampel sebenar
- Corak penggunaan SDK yang usang di seluruh Modul 08
- Rujukan yang hilang kepada perpustakaan sampel tempatan yang menyeluruh
- Pendekatan pelaksanaan yang tidak konsisten di bahagian yang berbeza

---

## 2025-09-18

### Ditambah
- Modul 08: Microsoft Foundry Local – Toolkit Pembangun Lengkap
  - Enam sesi: persediaan, integrasi Azure AI Foundry, model sumber terbuka, demo terkini, agen, dan model-sebagai-alat
  - Sampel boleh dijalankan di bawah `Module08/samples/01`–`06` dengan arahan cmd Windows
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart dengan OpenAI/Foundry Local dan sokongan Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orkestrasi multi-agen (`python -m samples.05.agents.coordinator`)
    - `06` Penghala Model-sebagai-Alat (`router.py`)
- Sokongan Azure OpenAI dalam sampel SDK Sesi 2 dengan konfigurasi pemboleh ubah persekitaran
- `.vscode/settings.json` untuk menunjuk kepada `Module08/.venv` dan meningkatkan resolusi analisis Python
- `.env` dengan petunjuk `PYTHONPATH` untuk kesedaran VS Code/Pylance

### Diubah
- Model lalai dikemas kini kepada `phi-4-mini` di seluruh dokumen dan sampel Modul 08; menghapuskan sebutan `phi-3.5` yang tinggal dalam Modul 08
- Penambahbaikan penghala (`Module08/samples/06/router.py`):
  - Penemuan titik akhir melalui `foundry service status` dengan parsing regex
  - Pemeriksaan kesihatan `/v1/models` semasa permulaan
  - Pendaftaran model yang boleh dikonfigurasi persekitaran (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Keperluan dikemas kini: `Module08/requirements.txt` kini termasuk `openai` (bersama `requests`, `chainlit`)
- Panduan sampel Chainlit diperjelaskan dan penyelesaian masalah ditambah; resolusi import melalui tetapan ruang kerja

### Diperbaiki
- Isu import diselesaikan:
  - Penghala tidak lagi bergantung pada modul `utils` yang tidak wujud; fungsi dimasukkan secara langsung
  - Penyelaras menggunakan import relatif (`from .specialists import ...`) dan dipanggil melalui laluan modul
  - Konfigurasi VS Code/Pylance untuk menyelesaikan import `chainlit` dan pakej
- Pembetulan typo kecil dalam `STUDY_GUIDE.md` dan liputan Modul 08 ditambah

### Dihapus
- Menghapuskan `Module08/infra/obs.py` yang tidak digunakan dan menghapuskan direktori `infra/` yang kosong; corak pemerhatian dikekalkan sebagai pilihan dalam dokumentasi

### Dipindahkan
- Demo Modul 08 disatukan di bawah `Module08/samples` dengan folder bernombor sesi
  - Aplikasi Chainlit dipindahkan ke `samples/04`
  - Agen dipindahkan ke `samples/05` dan fail `__init__.py` ditambah untuk resolusi pakej

### Dokumentasi
- Dokumentasi sesi Modul 08 dan semua README sampel diperkaya dengan rujukan Microsoft Learn dan vendor yang dipercayai
- `Module08/README.md` dikemas kini dengan Gambaran Keseluruhan Sampel, konfigurasi penghala, dan petua pengesahan
- `Module07/README.md` bahagian Windows Foundry Local disahkan terhadap dokumen Learn
- `STUDY_GUIDE.md` dikemas kini:
  - Modul 08 ditambah ke gambaran keseluruhan, jadual, penjejak kemajuan
  - Bahagian Rujukan yang menyeluruh ditambah (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Sejarah (ringkasan)
- Seni bina kursus dan modul ditubuhkan (Modul 01–07)
- Pemodenan kandungan secara iteratif, penyeragaman format, dan penambahan kajian kes
- Liputan rangka kerja pengoptimuman diperluaskan (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Belum Dikeluarkan / Tertunda (cadangan)
- Ujian asap pilihan per sampel untuk mengesahkan ketersediaan Foundry Local
- Semak terjemahan untuk menyelaraskan rujukan model (contohnya, `phi-4-mini`) di mana sesuai
- Tambah konfigurasi pyright minimum jika pasukan lebih suka ketegasan seluruh ruang kerja

---

