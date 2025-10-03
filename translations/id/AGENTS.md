<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:40:03+00:00",
  "source_file": "AGENTS.md",
  "language_code": "id"
}
-->
# AGENTS.md

## Gambaran Proyek

EdgeAI for Beginners adalah repositori edukasi yang komprehensif yang mengajarkan pengembangan Edge AI dengan Small Language Models (SLMs). Kursus ini mencakup dasar-dasar EdgeAI, penerapan model, teknik optimasi, dan implementasi siap produksi menggunakan Microsoft Foundry Local serta berbagai kerangka kerja AI.

**Teknologi Utama:**
- Python 3.8+ (bahasa utama untuk contoh AI/ML)
- .NET C# (contoh AI/ML)
- JavaScript/Node.js dengan Electron (untuk aplikasi desktop)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Kerangka Kerja AI: LangChain, Semantic Kernel, Chainlit
- Optimasi Model: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Jenis Repositori:** Repositori konten edukasi dengan 8 modul dan 10 aplikasi contoh yang komprehensif

**Arsitektur:** Jalur pembelajaran multi-modul dengan contoh praktis yang menunjukkan pola penerapan Edge AI

## Struktur Repositori

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Perintah Pengaturan

### Pengaturan Repositori

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Pengaturan Contoh Python (Modul08 dan contoh Python)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Pengaturan Contoh Node.js (Contoh 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Pengaturan Foundry Local

Foundry Local diperlukan untuk menjalankan contoh Modul08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Alur Kerja Pengembangan

### Pengembangan Konten

Repositori ini terutama berisi **konten edukasi dalam format Markdown**. Saat melakukan perubahan:

1. Edit file `.md` di direktori modul yang sesuai
2. Ikuti pola format yang sudah ada
3. Pastikan contoh kode akurat dan telah diuji
4. Perbarui konten terjemahan yang sesuai jika diperlukan (atau biarkan otomatisasi menangani)

### Pengembangan Aplikasi Contoh

Untuk contoh Python (contoh 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Untuk contoh Electron (contoh 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Pengujian Aplikasi Contoh

Contoh Python tidak memiliki pengujian otomatis tetapi dapat divalidasi dengan menjalankannya:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Contoh Electron memiliki infrastruktur pengujian:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Instruksi Pengujian

### Validasi Konten

Repositori ini menggunakan alur kerja terjemahan otomatis. Tidak diperlukan pengujian manual untuk terjemahan.

**Validasi manual untuk perubahan konten:**
1. Tinjau rendering Markdown dengan melihat pratinjau file `.md`
2. Verifikasi semua tautan mengarah ke target yang valid
3. Uji cuplikan kode yang disertakan dalam dokumentasi
4. Periksa apakah gambar dimuat dengan benar

### Pengujian Aplikasi Contoh

**Modul08/contoh/08 (aplikasi Electron) memiliki pengujian yang komprehensif:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Contoh Python harus diuji secara manual:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Panduan Gaya Kode

### Konten Markdown

- Gunakan hierarki judul yang konsisten (# untuk judul, ## untuk bagian utama, ### untuk subbagian)
- Sertakan blok kode dengan spesifikasi bahasa: ```python, ```bash, ```javascript
- Ikuti format yang sudah ada untuk tabel, daftar, dan penekanan
- Jaga agar baris mudah dibaca (usahakan ~80-100 karakter, tetapi tidak ketat)
- Gunakan tautan relatif untuk referensi internal

### Gaya Kode Python

- Ikuti konvensi PEP 8
- Gunakan petunjuk tipe jika sesuai
- Sertakan docstring untuk fungsi dan kelas
- Gunakan nama variabel yang bermakna
- Jaga agar fungsi fokus dan ringkas

### Gaya Kode JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Konvensi utama:**
- Konfigurasi ESLint disediakan dalam contoh 08
- Prettier untuk format kode
- Gunakan sintaks modern ES6+
- Ikuti pola yang sudah ada dalam basis kode

## Panduan Pull Request

### Format Judul
```
[ModuleXX] Brief description of change
```
atau
```
[Module08/samples/XX] Description for sample changes
```

### Sebelum Mengirimkan

**Untuk perubahan konten:**
- Pratinjau semua file Markdown yang dimodifikasi
- Verifikasi tautan dan gambar berfungsi
- Periksa kesalahan ketik dan tata bahasa

**Untuk perubahan kode contoh (Modul08/contoh/08):**
```bash
npm run lint
npm test
```

**Untuk perubahan contoh Python:**
- Uji contoh berjalan dengan sukses
- Verifikasi penanganan kesalahan berfungsi
- Periksa kompatibilitas dengan Foundry Local

### Proses Peninjauan

- Perubahan konten edukasi ditinjau untuk akurasi dan kejelasan
- Contoh kode diuji untuk fungsionalitas
- Pembaruan terjemahan ditangani secara otomatis oleh GitHub Actions

## Sistem Terjemahan

**PENTING:** Repositori ini menggunakan terjemahan otomatis melalui GitHub Actions.

- Terjemahan berada di direktori `/translations/` (50+ bahasa)
- Otomatis melalui alur kerja `co-op-translator.yml`
- **JANGAN mengedit file terjemahan secara manual** - file tersebut akan ditimpa
- Hanya edit file sumber bahasa Inggris di direktori root dan modul
- Terjemahan secara otomatis dihasilkan saat push ke cabang `main`

## Integrasi Foundry Local

Sebagian besar contoh Modul08 memerlukan Microsoft Foundry Local untuk dijalankan:

### Memulai Foundry Local
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### Memverifikasi Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Variabel Lingkungan untuk Contoh

Sebagian besar contoh menggunakan variabel lingkungan berikut:
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Pembangunan dan Penerapan

### Penerapan Konten

Repositori ini terutama berisi dokumentasi - tidak diperlukan proses pembangunan untuk konten.

### Pembangunan Aplikasi Contoh

**Aplikasi Electron (Modul08/contoh/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Contoh Python:**
Tidak ada proses pembangunan - contoh dijalankan langsung dengan interpreter Python.

## Masalah Umum dan Pemecahan Masalah

### Foundry Local Tidak Berjalan
**Masalah:** Contoh gagal dengan kesalahan koneksi

**Solusi:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Masalah Lingkungan Virtual Python
**Masalah:** Kesalahan impor modul

**Solusi:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Masalah Pembangunan Electron
**Masalah:** npm install atau kegagalan pembangunan

**Solusi:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Konflik Alur Kerja Terjemahan
**Masalah:** PR terjemahan konflik dengan perubahan Anda

**Solusi:**
- Hanya edit file sumber bahasa Inggris
- Biarkan alur kerja terjemahan otomatis menangani terjemahan
- Jika konflik terjadi, gabungkan `main` ke cabang Anda setelah terjemahan digabungkan

## Sumber Daya Tambahan

### Jalur Pembelajaran
- **Jalur Pemula:** Modul 01-02 (7-9 jam)
- **Jalur Menengah:** Modul 03-04 (9-11 jam)
- **Jalur Lanjutan:** Modul 05-07 (12-15 jam)
- **Jalur Ahli:** Modul 08 (8-10 jam)

### Konten Modul Utama
- **Modul01:** Dasar-dasar EdgeAI dan studi kasus dunia nyata
- **Modul02:** Keluarga dan arsitektur Small Language Model (SLM)
- **Modul03:** Strategi penerapan lokal dan cloud
- **Modul04:** Optimasi model dengan berbagai kerangka kerja
- **Modul05:** SLMOps - operasi produksi
- **Modul06:** Agen AI dan pemanggilan fungsi
- **Modul07:** Implementasi spesifik platform
- **Modul08:** Toolkit Foundry Local dengan 10 contoh komprehensif

### Ketergantungan Eksternal
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Runtime model AI lokal
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Kerangka kerja optimasi
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Toolkit optimasi model
- [OpenVINO](https://docs.openvino.ai/) - Toolkit optimasi dari Intel

## Catatan Khusus Proyek

### Aplikasi Contoh Modul08

Repositori ini mencakup 10 aplikasi contoh yang komprehensif:

1. **01-REST Chat Quickstart** - Integrasi dasar OpenAI SDK
2. **02-OpenAI SDK Integration** - Fitur SDK lanjutan
3. **03-Model Discovery & Benchmarking** - Alat perbandingan model
4. **04-Chainlit RAG Application** - Generasi berbasis pengambilan
5. **05-Multi-Agent Orchestration** - Koordinasi agen dasar
6. **06-Models-as-Tools Router** - Perutean model cerdas
7. **07-Direct API Client** - Integrasi API tingkat rendah
8. **08-Windows 11 Chat App** - Aplikasi desktop Electron native
9. **09-Advanced Multi-Agent System** - Orkestrasi agen yang kompleks
10. **10-Foundry Tools Framework** - Integrasi LangChain/Semantic Kernel

Setiap contoh menunjukkan aspek berbeda dari pengembangan Edge AI dengan Foundry Local.

### Pertimbangan Performa

- SLM dioptimalkan untuk penerapan edge (2-16GB RAM)
- Inferensi lokal memberikan waktu respons 50-500ms
- Teknik kuantisasi mencapai pengurangan ukuran 75% dengan retensi performa 85%
- Kemampuan percakapan real-time dengan model lokal

### Keamanan dan Privasi

- Semua pemrosesan dilakukan secara lokal - tidak ada data yang dikirim ke cloud
- Cocok untuk aplikasi yang sensitif terhadap privasi (kesehatan, keuangan)
- Memenuhi persyaratan kedaulatan data
- Foundry Local berjalan sepenuhnya di perangkat keras lokal

---

**Ini adalah repositori edukasi yang berfokus pada pengajaran pengembangan Edge AI. Pola kontribusi utama adalah meningkatkan konten edukasi dan menambahkan/meningkatkan aplikasi contoh yang menunjukkan konsep Edge AI.**

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.