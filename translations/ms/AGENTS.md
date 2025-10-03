<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:40:37+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ms"
}
-->
# AGENTS.md

## Gambaran Projek

EdgeAI untuk Pemula adalah repositori pendidikan yang komprehensif yang mengajar pembangunan Edge AI menggunakan Model Bahasa Kecil (SLM). Kursus ini merangkumi asas EdgeAI, penyebaran model, teknik pengoptimuman, dan pelaksanaan siap produksi menggunakan Microsoft Foundry Local dan pelbagai rangka kerja AI.

**Teknologi Utama:**
- Python 3.8+ (bahasa utama untuk sampel AI/ML)
- .NET C# (Sampel AI/ML)
- JavaScript/Node.js dengan Electron (untuk aplikasi desktop)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Rangka Kerja AI: LangChain, Semantic Kernel, Chainlit
- Pengoptimuman Model: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Jenis Repositori:** Repositori kandungan pendidikan dengan 8 modul dan 10 aplikasi sampel yang komprehensif

**Arkitektur:** Laluan pembelajaran pelbagai modul dengan sampel praktikal yang menunjukkan corak penyebaran Edge AI

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

## Perintah Persediaan

### Persediaan Repositori

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Persediaan Sampel Python (Modul08 dan sampel Python)

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

### Persediaan Sampel Node.js (Sampel 08 - Aplikasi Chat Windows)

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

### Persediaan Foundry Local

Foundry Local diperlukan untuk menjalankan sampel Modul08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Aliran Kerja Pembangunan

### Pembangunan Kandungan

Repositori ini terutamanya mengandungi **kandungan pendidikan dalam Markdown**. Apabila membuat perubahan:

1. Edit fail `.md` dalam direktori modul yang sesuai
2. Ikuti corak format yang sedia ada
3. Pastikan contoh kod adalah tepat dan telah diuji
4. Kemas kini kandungan terjemahan yang sepadan jika perlu (atau biarkan automasi mengendalikannya)

### Pembangunan Aplikasi Sampel

Untuk sampel Python (sampel 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Untuk sampel Electron (sampel 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Ujian Aplikasi Sampel

Sampel Python tidak mempunyai ujian automatik tetapi boleh disahkan dengan menjalankannya:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Sampel Electron mempunyai infrastruktur ujian:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Arahan Pengujian

### Pengesahan Kandungan

Repositori menggunakan aliran kerja terjemahan automatik. Tiada ujian manual diperlukan untuk terjemahan.

**Pengesahan manual untuk perubahan kandungan:**
1. Semak rendering Markdown dengan pratonton fail `.md`
2. Pastikan semua pautan menuju ke sasaran yang sah
3. Uji sebarang petikan kod yang disertakan dalam dokumentasi
4. Periksa bahawa imej dimuatkan dengan betul

### Pengujian Aplikasi Sampel

**Modul08/sampel/08 (aplikasi Electron) mempunyai ujian yang komprehensif:**
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

**Sampel Python perlu diuji secara manual:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Garis Panduan Gaya Kod

### Kandungan Markdown

- Gunakan hierarki tajuk yang konsisten (# untuk tajuk, ## untuk bahagian utama, ### untuk subbahagian)
- Sertakan blok kod dengan penentu bahasa: ```python, ```bash, ```javascript
- Ikuti format sedia ada untuk jadual, senarai, dan penekanan
- Pastikan baris mudah dibaca (sasaran ~80-100 aksara, tetapi tidak ketat)
- Gunakan pautan relatif untuk rujukan dalaman

### Gaya Kod Python

- Ikuti konvensyen PEP 8
- Gunakan petunjuk jenis di mana sesuai
- Sertakan docstring untuk fungsi dan kelas
- Gunakan nama pemboleh ubah yang bermakna
- Pastikan fungsi fokus dan ringkas

### Gaya Kod JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Konvensyen utama:**
- Konfigurasi ESLint disediakan dalam sampel 08
- Prettier untuk format kod
- Gunakan sintaks ES6+ moden
- Ikuti corak sedia ada dalam pangkalan kod

## Garis Panduan Permintaan Tarik

### Format Tajuk
```
[ModuleXX] Brief description of change
```
atau
```
[Module08/samples/XX] Description for sample changes
```

### Sebelum Menghantar

**Untuk perubahan kandungan:**
- Pratonton semua fail Markdown yang diubah
- Pastikan pautan dan imej berfungsi
- Periksa kesalahan ejaan dan tatabahasa

**Untuk perubahan kod sampel (Modul08/sampel/08):**
```bash
npm run lint
npm test
```

**Untuk perubahan sampel Python:**
- Uji sampel berjalan dengan berjaya
- Pastikan pengendalian ralat berfungsi
- Periksa keserasian dengan Foundry Local

### Proses Semakan

- Perubahan kandungan pendidikan disemak untuk ketepatan dan kejelasan
- Sampel kod diuji untuk fungsi
- Kemas kini terjemahan dikendalikan secara automatik oleh GitHub Actions

## Sistem Terjemahan

**PENTING:** Repositori ini menggunakan terjemahan automatik melalui GitHub Actions.

- Terjemahan berada dalam direktori `/translations/` (50+ bahasa)
- Automatik melalui aliran kerja `co-op-translator.yml`
- **JANGAN edit fail terjemahan secara manual** - ia akan ditulis semula
- Edit hanya fail sumber bahasa Inggeris dalam direktori root dan modul
- Terjemahan dijana secara automatik apabila ditolak ke cawangan `main`

## Integrasi Foundry Local

Kebanyakan sampel Modul08 memerlukan Microsoft Foundry Local untuk dijalankan:

### Memulakan Foundry Local
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

### Mengesahkan Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Pembolehubah Persekitaran untuk Sampel

Kebanyakan sampel menggunakan pembolehubah persekitaran ini:
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

## Pembinaan dan Penyebaran

### Penyebaran Kandungan

Repositori ini terutamanya dokumentasi - tiada proses pembinaan diperlukan untuk kandungan.

### Pembinaan Aplikasi Sampel

**Aplikasi Electron (Modul08/sampel/08):**
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

**Sampel Python:**
Tiada proses pembinaan - sampel dijalankan terus dengan interpreter Python.

## Masalah Biasa dan Penyelesaian

### Foundry Local Tidak Berjalan
**Masalah:** Sampel gagal dengan ralat sambungan

**Penyelesaian:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Masalah Persekitaran Maya Python
**Masalah:** Ralat import modul

**Penyelesaian:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Masalah Pembinaan Electron
**Masalah:** Kegagalan pemasangan npm atau pembinaan

**Penyelesaian:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Konflik Aliran Kerja Terjemahan
**Masalah:** PR terjemahan bertentangan dengan perubahan anda

**Penyelesaian:**
- Edit hanya fail sumber bahasa Inggeris
- Biarkan aliran kerja terjemahan automatik mengendalikan terjemahan
- Jika konflik berlaku, gabungkan `main` ke dalam cawangan anda selepas terjemahan digabungkan

## Sumber Tambahan

### Laluan Pembelajaran
- **Laluan Pemula:** Modul 01-02 (7-9 jam)
- **Laluan Pertengahan:** Modul 03-04 (9-11 jam)
- **Laluan Lanjutan:** Modul 05-07 (12-15 jam)
- **Laluan Pakar:** Modul 08 (8-10 jam)

### Kandungan Modul Utama
- **Modul01:** Asas EdgeAI dan kajian kes dunia sebenar
- **Modul02:** Keluarga dan seni bina Model Bahasa Kecil (SLM)
- **Modul03:** Strategi penyebaran tempatan dan awan
- **Modul04:** Pengoptimuman model dengan pelbagai rangka kerja
- **Modul05:** SLMOps - operasi produksi
- **Modul06:** Ejen AI dan pemanggilan fungsi
- **Modul07:** Pelaksanaan khusus platform
- **Modul08:** Alat Foundry Local dengan 10 sampel komprehensif

### Kebergantungan Luaran
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Runtime model AI tempatan
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Rangka kerja pengoptimuman
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Alat pengoptimuman model
- [OpenVINO](https://docs.openvino.ai/) - Alat pengoptimuman Intel

## Nota Khusus Projek

### Aplikasi Sampel Modul08

Repositori ini termasuk 10 aplikasi sampel komprehensif:

1. **01-REST Chat Quickstart** - Integrasi asas OpenAI SDK
2. **02-OpenAI SDK Integration** - Ciri SDK lanjutan
3. **03-Model Discovery & Benchmarking** - Alat perbandingan model
4. **04-Chainlit RAG Application** - Penjanaan yang diperkaya dengan pengambilan
5. **05-Multi-Agent Orchestration** - Koordinasi ejen asas
6. **06-Models-as-Tools Router** - Penghalaan model pintar
7. **07-Direct API Client** - Integrasi API tahap rendah
8. **08-Windows 11 Chat App** - Aplikasi desktop Electron asli
9. **09-Advanced Multi-Agent System** - Orkestrasi ejen kompleks
10. **10-Foundry Tools Framework** - Integrasi LangChain/Semantic Kernel

Setiap sampel menunjukkan aspek pembangunan Edge AI yang berbeza dengan Foundry Local.

### Pertimbangan Prestasi

- SLM dioptimumkan untuk penyebaran edge (2-16GB RAM)
- Inferens tempatan memberikan masa tindak balas 50-500ms
- Teknik kuantisasi mencapai pengurangan saiz 75% dengan pengekalan prestasi 85%
- Keupayaan perbualan masa nyata dengan model tempatan

### Keselamatan dan Privasi

- Semua pemprosesan berlaku secara tempatan - tiada data dihantar ke awan
- Sesuai untuk aplikasi sensitif privasi (kesihatan, kewangan)
- Memenuhi keperluan kedaulatan data
- Foundry Local berjalan sepenuhnya pada perkakasan tempatan

---

**Ini adalah repositori pendidikan yang fokus pada pengajaran pembangunan Edge AI. Corak sumbangan utama adalah meningkatkan kandungan pendidikan dan menambah/memperbaiki aplikasi sampel yang menunjukkan konsep Edge AI.**

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.