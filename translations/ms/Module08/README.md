<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T22:35:02+00:00",
  "source_file": "Module08/README.md",
  "language_code": "ms"
}
-->
# Modul 08: Hands-on Dengan Microsoft Foundry Local - Toolkit Pembangun Lengkap

## Gambaran Umum

Microsoft Foundry Local mewakili generasi baharu pembangunan AI di tepi, memberikan pembangun alat yang berkuasa untuk membina, melancarkan, dan menskalakan aplikasi AI secara tempatan sambil mengekalkan integrasi lancar dengan Azure AI Foundry. Modul ini menyediakan liputan menyeluruh tentang Foundry Local dari pemasangan hingga pembangunan agen yang maju.

**Teknologi Utama:**
- Microsoft Foundry Local CLI dan SDK
- Integrasi Azure AI Foundry
- Inferens model pada peranti
- Cache dan pengoptimuman model tempatan
- Seni bina berasaskan agen

## Objektif Pembelajaran Modul

Dengan melengkapkan modul ini, anda akan:

- **Menguasai Pemasangan Foundry Local**: Pasang, konfigurasikan, dan optimalkan Foundry Local untuk pembangunan Windows 11
- **Melancarkan Pelbagai Model**: Jalankan model phi, qwen, deepseek, dan GPT-OSS-20B secara tempatan dengan arahan CLI
- **Membina Penyelesaian Pengeluaran**: Cipta aplikasi AI dengan kejuruteraan prompt yang maju dan integrasi data
- **Manfaatkan Ekosistem Sumber Terbuka**: Integrasi model Hugging Face dan sumbangan komuniti
- **Bandingkan Seni Bina AI**: Fahami perbandingan LLMs vs SLMs dan strategi pelancaran
- **Membangunkan Agen AI**: Bina agen pintar menggunakan seni bina dan kemampuan grounding Foundry Local
- **Laksanakan Model Sebagai Alat**: Cipta penyelesaian AI modular dan boleh disesuaikan untuk aplikasi perusahaan

## Struktur Sesi

### [1: Memulakan Dengan Foundry Local](./01.FoundryLocalSetup.md)
**Fokus**: Pemasangan, persediaan CLI, cache model, dan pecutan perkakasan

**Apa Yang Akan Anda Pelajari:**
- Pemasangan lengkap Foundry Local pada Windows 11
- Konfigurasi CLI dan struktur arahan
- Strategi cache model untuk prestasi optimum
- Persediaan dan pengoptimuman pecutan perkakasan
- Pelancaran model phi, qwen, deepseek, dan GPT-OSS-20B secara praktikal

**Durasi**: 2-3 jam  
**Prasyarat**: Windows 11, pengetahuan asas baris arahan

---

### [2: Membina Penyelesaian AI Dengan Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Fokus**: Kejuruteraan prompt yang maju, integrasi data, dan tugas yang boleh diambil tindakan

**Apa Yang Akan Anda Pelajari:**
- Teknik kejuruteraan prompt yang maju
- Corak integrasi data dan amalan terbaik
- Membina tugas AI yang boleh diambil tindakan dengan Foundry Local
- Aliran kerja integrasi Azure AI Foundry yang lancar
- Pengoptimuman prestasi dan pemantauan

**Durasi**: 2-3 jam  
**Prasyarat**: Penyelesaian Sesi 1, akaun Azure (pilihan)

---

### [3: Model Sumber Terbuka Foundry Local](./03.OpenSourceModels.md)
**Fokus**: Integrasi Hugging Face, strategi pemilihan model, dan sumbangan komuniti

**Apa Yang Akan Anda Pelajari:**
- Integrasi model Hugging Face dengan Foundry Local
- Strategi dan pelaksanaan bawa model anda sendiri (BYOM)
- Wawasan siri Model Mondays dan sumbangan komuniti
- Pelancaran dan pengoptimuman model tersuai
- Kriteria penilaian dan pemilihan model komuniti

**Durasi**: 2-3 jam  
**Prasyarat**: Penyelesaian Sesi 1-2, akaun Hugging Face

---

### [4: Terokai Model Terkini - LLMs, SLMs, dan Inferens Pada Peranti](./04.CuttingEdgeModels.md)
**Fokus**: Perbandingan model, EdgeAI dengan Phi dan ONNX Runtime, demo yang maju

**Apa Yang Akan Anda Pelajari:**
- Perbandingan menyeluruh LLMs vs SLMs dan kes penggunaan
- Perdagangan inferens tempatan vs awan dan rangka kerja keputusan
- Pelaksanaan EdgeAI dengan Phi dan ONNX Runtime
- Pembangunan dan pelancaran Aplikasi Chat Chainlit RAG
- Teknik pengoptimuman inferens WebGPU
- Integrasi dan kemampuan SDK AI PC

**Durasi**: 3-4 jam  
**Prasyarat**: Penyelesaian Sesi 1-3, pemahaman konsep inferens

---

### [5: Bina Agen Berkuasa AI Dengan Cepat Menggunakan Foundry Local](./05.AIPoweredAgents.md)
**Fokus**: Pembangunan aplikasi GenAI yang pantas, prompt sistem, grounding, dan seni bina agen

**Apa Yang Akan Anda Pelajari:**
- Seni bina dan corak reka bentuk agen Foundry Local
- Kejuruteraan prompt sistem untuk tingkah laku agen
- Teknik grounding untuk respons agen yang boleh dipercayai
- Aliran kerja pembangunan aplikasi GenAI yang pantas
- Orkestrasi agen dan sistem multi-agen
- Strategi pelancaran pengeluaran untuk agen AI

**Durasi**: 3-4 jam  
**Prasyarat**: Penyelesaian Sesi 1-4, pemahaman asas tentang agen AI

---

### [6: Foundry Local - Model Sebagai Alat](./06.ModelsAsTools.md)
**Fokus**: Penyelesaian AI modular, pelancaran pada peranti, dan penskalaan perusahaan

**Apa Yang Akan Anda Pelajari:**
- Menganggap model AI sebagai alat modular dan boleh disesuaikan
- Pelancaran pada peranti tanpa kebergantungan awan
- Inferens yang rendah latensi, kos efisien, dan melindungi privasi
- Corak integrasi SDK, API, dan CLI
- Penyesuaian model untuk kes penggunaan tertentu
- Strategi penskalaan dari tempatan ke Azure AI Foundry
- Seni bina aplikasi AI yang sedia untuk perusahaan

**Durasi**: 3-4 jam  
**Prasyarat**: Semua sesi sebelumnya, pengalaman pembangunan perusahaan berguna

## Prasyarat

### Keperluan Sistem
- **Sistem Operasi**: Windows 11 (22H2 atau lebih baru)
- **Memori**: 16GB RAM (32GB disyorkan untuk model yang lebih besar)
- **Storan**: 50GB ruang kosong untuk cache model
- **Perkakasan**: Peranti dengan NPU disyorkan (Copilot+ PC), GPU pilihan
- **Rangkaian**: Internet berkelajuan tinggi untuk muat turun model awal

### Persekitaran Pembangunan
- Visual Studio Code dengan sambungan AI Toolkit
- Python 3.10+ dan pip
- Git untuk kawalan versi
- PowerShell atau Command Prompt
- Azure CLI (pilihan untuk integrasi awan)

### Pengetahuan Prasyarat
- Pemahaman asas tentang konsep AI/ML
- Familiariti dengan baris arahan
- Asas pengaturcaraan Python
- Konsep REST API
- Pengetahuan asas tentang prompt dan inferens model

## Garis Masa Modul

**Anggaran Masa Keseluruhan**: 15-20 jam

| Sesi | Kawasan Fokus | Masa | Kerumitan |
|------|---------------|------|-----------|
|  1 | Persediaan & Asas | 2-3 jam | Pemula |
|  2 | Penyelesaian AI | 2-3 jam | Pertengahan |
|  3 | Sumber Terbuka | 2-3 jam | Pertengahan |
|  4 | Model Lanjutan | 3-4 jam | Lanjutan |
|  5 | Agen AI | 3-4 jam | Lanjutan |
|  6 | Alat Perusahaan | 3-4 jam | Pakar |

## Sumber Utama

### Dokumentasi Utama
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Dokumentasi Azure AI Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Siri Model Mondays](https://aka.ms/model-mondays)

### Sumber Komuniti
- [Perbincangan Komuniti Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Contoh Azure AI Foundry](https://github.com/Azure-Samples/ai-foundry)
- [Komuniti Pembangun AI Microsoft](https://techcommunity.microsoft.com/category/artificialintelligence)

## Hasil Pembelajaran

Setelah melengkapkan modul ini, anda akan dilengkapi untuk:

### Penguasaan Teknikal
- **Melancarkan dan Mengurus**: Pemasangan Foundry Local di persekitaran pembangunan dan pengeluaran
- **Integrasi Model**: Bekerja dengan keluarga model yang pelbagai dari Microsoft, Hugging Face, dan sumber komuniti
- **Membina Aplikasi**: Cipta aplikasi AI yang sedia untuk pengeluaran dengan ciri dan pengoptimuman yang maju
- **Membangunkan Agen**: Laksanakan agen AI yang canggih dengan grounding, penaakulan, dan integrasi alat

### Pemahaman Strategik
- **Keputusan Seni Bina**: Membuat pilihan yang bijak antara pelancaran tempatan vs awan
- **Pengoptimuman Prestasi**: Mengoptimumkan prestasi inferens di pelbagai konfigurasi perkakasan
- **Penskalaan Perusahaan**: Reka aplikasi yang menskalakan dari prototaip tempatan ke pelancaran perusahaan
- **Privasi dan Keselamatan**: Laksanakan penyelesaian AI yang melindungi privasi dengan inferens tempatan

### Keupayaan Inovasi
- **Prototip Pantas**: Cepat membina dan menguji konsep aplikasi AI
- **Integrasi Komuniti**: Manfaatkan model sumber terbuka dan menyumbang kepada ekosistem
- **Corak Lanjutan**: Laksanakan corak AI terkini termasuk RAG, agen, dan integrasi alat
- **Pembangunan Sedia Masa Depan**: Bina aplikasi yang sedia untuk teknologi dan corak AI yang muncul

## Memulakan

1. **Sediakan Persekitaran Anda**: Pastikan Windows 11 dengan spesifikasi perkakasan yang disyorkan
2. **Pasang Prasyarat**: Sediakan alat pembangunan dan kebergantungan
3. **Mulakan Dengan Sesi 1**: Mulakan dengan pemasangan dan persediaan asas Foundry Local
4. **Teruskan Secara Berurutan**: Lengkapkan sesi mengikut urutan untuk perkembangan pembelajaran yang optimum
5. **Berlatih Secara Berterusan**: Terapkan konsep melalui latihan praktikal dan projek

## Metrik Kejayaan

Jejak kemajuan anda melalui modul:

- [ ] Berjaya memasang dan mengkonfigurasi Foundry Local
- [ ] Melancarkan dan menjalankan sekurang-kurangnya 4 keluarga model yang berbeza
- [ ] Membina penyelesaian AI lengkap dengan integrasi data
- [ ] Mengintegrasi sekurang-kurangnya 2 model sumber terbuka
- [ ] Mencipta aplikasi chat RAG yang berfungsi
- [ ] Membangunkan dan melancarkan agen AI
- [ ] Melaksanakan seni bina model-sebagai-alat

## Permulaan Cepat untuk Contoh

### 1) Persediaan persekitaran (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Mulakan model tempatan (terminal baru)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Jalankan demo Chainlit (Sesi 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Jalankan penyelaras multi-agen (Sesi 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Jika anda melihat ralat sambungan, sahkan Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Konfigurasi router (Sesi 6)
Router melakukan pemeriksaan kesihatan pantas dan menyokong konfigurasi berdasarkan persekitaran:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Modul ini mewakili kemajuan terkini dalam pembangunan AI di tepi, menggabungkan alat Microsoft yang sedia perusahaan dengan fleksibiliti dan inovasi ekosistem sumber terbuka. Dengan menguasai Foundry Local, anda akan berada di barisan hadapan pembangunan aplikasi AI.

Untuk Azure OpenAI (Sesi 2), lihat README contoh untuk pembolehubah persekitaran yang diperlukan dan tetapan versi API.

## Gambaran Umum Contoh

- `samples/01`: Chat REST cepat ke Foundry Local (`chat_quickstart.py`).
- `samples/02`: Integrasi SDK OpenAI (`sdk_quickstart.py`).
- `samples/03`: Penemuan model + bench cepat (`list_and_bench.cmd`).
- `samples/04`: Demo Chainlit RAG (`app.py`).
- `samples/05`: Orkestrasi multi-agen (`python -m samples.05.agents.coordinator`).
- `samples/06`: Router model-sebagai-alat (`python samples\06\router.py`).

---

