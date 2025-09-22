<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T22:34:36+00:00",
  "source_file": "Module08/README.md",
  "language_code": "id"
}
-->
# Modul 08: Praktik Langsung dengan Microsoft Foundry Local - Toolkit Pengembang Lengkap

## Ikhtisar

Microsoft Foundry Local adalah generasi terbaru dalam pengembangan AI di edge, memberikan alat yang kuat bagi pengembang untuk membangun, menerapkan, dan mengembangkan aplikasi AI secara lokal sambil tetap terintegrasi dengan Azure AI Foundry. Modul ini mencakup Foundry Local secara menyeluruh, mulai dari instalasi hingga pengembangan agen tingkat lanjut.

**Teknologi Utama:**
- Microsoft Foundry Local CLI dan SDK
- Integrasi Azure AI Foundry
- Inferensi model di perangkat
- Caching dan optimasi model lokal
- Arsitektur berbasis agen

## Tujuan Pembelajaran Modul

Dengan menyelesaikan modul ini, Anda akan:

- **Menguasai Pengaturan Foundry Local**: Instalasi, konfigurasi, dan optimasi Foundry Local untuk pengembangan di Windows 11
- **Menerapkan Berbagai Model**: Menjalankan model phi, qwen, deepseek, dan GPT-OSS-20B secara lokal dengan perintah CLI
- **Membangun Solusi Produksi**: Membuat aplikasi AI dengan teknik prompt engineering tingkat lanjut dan integrasi data
- **Memanfaatkan Ekosistem Open-Source**: Mengintegrasikan model Hugging Face dan kontribusi dari komunitas
- **Membandingkan Arsitektur AI**: Memahami perbandingan LLMs vs SLMs serta strategi penerapannya
- **Mengembangkan Agen AI**: Membangun agen cerdas menggunakan arsitektur dan kemampuan grounding Foundry Local
- **Mengimplementasikan Model sebagai Alat**: Membuat solusi AI modular dan dapat disesuaikan untuk aplikasi perusahaan

## Struktur Sesi

### [1: Memulai dengan Foundry Local](./01.FoundryLocalSetup.md)
**Fokus**: Instalasi, pengaturan CLI, caching model, dan akselerasi perangkat keras

**Apa yang Akan Anda Pelajari:**
- Instalasi Foundry Local lengkap di Windows 11
- Konfigurasi CLI dan struktur perintah
- Strategi caching model untuk kinerja optimal
- Pengaturan dan optimasi akselerasi perangkat keras
- Penerapan langsung model phi, qwen, deepseek, dan GPT-OSS-20B

**Durasi**: 2-3 jam  
**Prasyarat**: Windows 11, pengetahuan dasar tentang command line

---

### [2: Membangun Solusi AI dengan Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Fokus**: Teknik prompt engineering tingkat lanjut, integrasi data, dan tugas yang dapat ditindaklanjuti

**Apa yang Akan Anda Pelajari:**
- Teknik prompt engineering tingkat lanjut
- Pola integrasi data dan praktik terbaik
- Membangun tugas AI yang dapat ditindaklanjuti dengan Foundry Local
- Alur kerja integrasi yang mulus dengan Azure AI Foundry
- Optimasi kinerja dan pemantauan

**Durasi**: 2-3 jam  
**Prasyarat**: Penyelesaian Sesi 1, akun Azure (opsional)

---

### [3: Model Open-Source di Foundry Local](./03.OpenSourceModels.md)
**Fokus**: Integrasi Hugging Face, strategi pemilihan model, dan kontribusi dari komunitas

**Apa yang Akan Anda Pelajari:**
- Integrasi model Hugging Face dengan Foundry Local
- Strategi dan implementasi "Bring-your-own-model" (BYOM)
- Wawasan dari seri Model Mondays dan kontribusi komunitas
- Penerapan dan optimasi model kustom
- Kriteria evaluasi dan pemilihan model komunitas

**Durasi**: 2-3 jam  
**Prasyarat**: Penyelesaian Sesi 1-2, akun Hugging Face

---

### [4: Eksplorasi Model Terkini - LLMs, SLMs, dan Inferensi di Perangkat](./04.CuttingEdgeModels.md)
**Fokus**: Perbandingan model, EdgeAI dengan Phi dan ONNX Runtime, demo tingkat lanjut

**Apa yang Akan Anda Pelajari:**
- Perbandingan komprehensif LLMs vs SLMs dan kasus penggunaannya
- Trade-off inferensi lokal vs cloud dan kerangka keputusan
- Implementasi EdgeAI dengan Phi dan ONNX Runtime
- Pengembangan dan penerapan Chainlit RAG Chat App
- Teknik optimasi inferensi WebGPU
- Integrasi dan kemampuan AI PC SDK

**Durasi**: 3-4 jam  
**Prasyarat**: Penyelesaian Sesi 1-3, pemahaman tentang konsep inferensi

---

### [5: Membangun Agen AI dengan Cepat menggunakan Foundry Local](./05.AIPoweredAgents.md)
**Fokus**: Pengembangan aplikasi GenAI yang cepat, sistem prompt, grounding, dan arsitektur agen

**Apa yang Akan Anda Pelajari:**
- Arsitektur agen Foundry Local dan pola desain
- Teknik prompt sistem untuk perilaku agen
- Teknik grounding untuk respons agen yang andal
- Alur kerja pengembangan aplikasi GenAI yang cepat
- Orkestrasi agen dan sistem multi-agen
- Strategi penerapan produksi untuk agen AI

**Durasi**: 3-4 jam  
**Prasyarat**: Penyelesaian Sesi 1-4, pemahaman dasar tentang agen AI

---

### [6: Foundry Local - Model sebagai Alat](./06.ModelsAsTools.md)
**Fokus**: Solusi AI modular, penerapan di perangkat, dan skala perusahaan

**Apa yang Akan Anda Pelajari:**
- Memperlakukan model AI sebagai alat modular yang dapat disesuaikan
- Penerapan di perangkat tanpa ketergantungan cloud
- Inferensi dengan latensi rendah, hemat biaya, dan menjaga privasi
- Pola integrasi SDK, API, dan CLI
- Kustomisasi model untuk kasus penggunaan spesifik
- Strategi skala dari lokal ke Azure AI Foundry
- Arsitektur aplikasi AI siap perusahaan

**Durasi**: 3-4 jam  
**Prasyarat**: Semua sesi sebelumnya, pengalaman pengembangan perusahaan akan membantu

## Prasyarat

### Persyaratan Sistem
- **Sistem Operasi**: Windows 11 (22H2 atau lebih baru)
- **Memori**: RAM 16GB (32GB direkomendasikan untuk model yang lebih besar)
- **Penyimpanan**: Ruang kosong 50GB untuk caching model
- **Perangkat Keras**: Perangkat dengan NPU direkomendasikan (Copilot+ PC), GPU opsional
- **Jaringan**: Internet berkecepatan tinggi untuk unduhan model awal

### Lingkungan Pengembangan
- Visual Studio Code dengan ekstensi AI Toolkit
- Python 3.10+ dan pip
- Git untuk kontrol versi
- PowerShell atau Command Prompt
- Azure CLI (opsional untuk integrasi cloud)

### Pengetahuan Prasyarat
- Pemahaman dasar tentang konsep AI/ML
- Familiaritas dengan command line
- Dasar-dasar pemrograman Python
- Konsep REST API
- Pengetahuan dasar tentang prompting dan inferensi model

## Garis Waktu Modul

**Total Waktu yang Diperkirakan**: 15-20 jam

| Sesi | Area Fokus | Waktu | Kompleksitas |
|------|------------|-------|--------------|
|  1 | Pengaturan & Dasar | 2-3 jam | Pemula |
|  2 | Solusi AI | 2-3 jam | Menengah |
|  3 | Open Source | 2-3 jam | Menengah |
|  4 | Model Tingkat Lanjut | 3-4 jam | Lanjutan |
|  5 | Agen AI | 3-4 jam | Lanjutan |
|  6 | Alat Perusahaan | 3-4 jam | Ahli |

## Sumber Daya Utama

### Dokumentasi Utama
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Dokumentasi Azure AI Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Seri Model Mondays](https://aka.ms/model-mondays)

### Sumber Daya Komunitas
- [Diskusi Komunitas Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Contoh Azure AI Foundry](https://github.com/Azure-Samples/ai-foundry)
- [Komunitas Pengembang AI Microsoft](https://techcommunity.microsoft.com/category/artificialintelligence)

## Hasil Pembelajaran

Setelah menyelesaikan modul ini, Anda akan mampu:

### Penguasaan Teknis
- **Menerapkan dan Mengelola**: Instalasi Foundry Local di lingkungan pengembangan dan produksi
- **Mengintegrasikan Model**: Bekerja dengan berbagai keluarga model dari Microsoft, Hugging Face, dan sumber komunitas
- **Membangun Aplikasi**: Membuat aplikasi AI siap produksi dengan fitur dan optimasi tingkat lanjut
- **Mengembangkan Agen**: Mengimplementasikan agen AI canggih dengan grounding, penalaran, dan integrasi alat

### Pemahaman Strategis
- **Keputusan Arsitektur**: Membuat pilihan yang tepat antara penerapan lokal vs cloud
- **Optimasi Kinerja**: Mengoptimalkan kinerja inferensi di berbagai konfigurasi perangkat keras
- **Skala Perusahaan**: Merancang aplikasi yang dapat berkembang dari prototipe lokal ke penerapan perusahaan
- **Privasi dan Keamanan**: Mengimplementasikan solusi AI yang menjaga privasi dengan inferensi lokal

### Kemampuan Inovasi
- **Prototipe Cepat**: Dengan cepat membangun dan menguji konsep aplikasi AI
- **Integrasi Komunitas**: Memanfaatkan model open-source dan berkontribusi pada ekosistem
- **Pola Tingkat Lanjut**: Mengimplementasikan pola AI terkini termasuk RAG, agen, dan integrasi alat
- **Pengembangan Siap Masa Depan**: Membuat aplikasi yang siap untuk teknologi dan pola AI yang sedang berkembang

## Memulai

1. **Persiapkan Lingkungan Anda**: Pastikan Windows 11 dengan spesifikasi perangkat keras yang direkomendasikan
2. **Instal Prasyarat**: Siapkan alat pengembangan dan dependensi
3. **Mulai dengan Sesi 1**: Mulai dengan instalasi dan pengaturan dasar Foundry Local
4. **Lanjutkan Secara Berurutan**: Selesaikan sesi secara berurutan untuk kemajuan pembelajaran yang optimal
5. **Latihan Secara Berkelanjutan**: Terapkan konsep melalui latihan langsung dan proyek

## Metrik Keberhasilan

Lacak kemajuan Anda melalui modul ini:

- [ ] Berhasil menginstal dan mengonfigurasi Foundry Local
- [ ] Menerapkan dan menjalankan setidaknya 4 keluarga model yang berbeda
- [ ] Membangun solusi AI lengkap dengan integrasi data
- [ ] Mengintegrasikan setidaknya 2 model open-source
- [ ] Membuat aplikasi chat RAG yang berfungsi
- [ ] Mengembangkan dan menerapkan agen AI
- [ ] Mengimplementasikan arsitektur model sebagai alat

## Panduan Cepat untuk Contoh

### 1) Pengaturan lingkungan (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Memulai model lokal (terminal baru)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Menjalankan demo Chainlit (Sesi 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Menjalankan koordinator multi-agen (Sesi 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Jika Anda melihat kesalahan koneksi, validasi Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Konfigurasi router (Sesi 6)
Router melakukan pemeriksaan kesehatan cepat dan mendukung konfigurasi berbasis lingkungan:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Modul ini mewakili teknologi terkini dalam pengembangan AI di edge, menggabungkan alat kelas perusahaan dari Microsoft dengan fleksibilitas dan inovasi ekosistem open-source. Dengan menguasai Foundry Local, Anda akan berada di garis depan pengembangan aplikasi AI.

Untuk Azure OpenAI (Sesi 2), lihat README contoh untuk variabel lingkungan yang diperlukan dan pengaturan versi API.

## Ikhtisar Contoh

- `samples/01`: Chat REST cepat ke Foundry Local (`chat_quickstart.py`).
- `samples/02`: Integrasi SDK OpenAI (`sdk_quickstart.py`).
- `samples/03`: Penemuan model + uji cepat (`list_and_bench.cmd`).
- `samples/04`: Demo Chainlit RAG (`app.py`).
- `samples/05`: Orkestrasi multi-agen (`python -m samples.05.agents.coordinator`).
- `samples/06`: Router Model sebagai Alat (`python samples\06\router.py`).

---

