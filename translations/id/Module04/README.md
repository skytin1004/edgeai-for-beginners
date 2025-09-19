<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c0cb9f7bcff2bc170532d8870a891f38",
  "translation_date": "2025-09-18T14:33:01+00:00",
  "source_file": "Module04/README.md",
  "language_code": "id"
}
-->
# Bab 04: Konversi Format Model dan Kuantisasi - Ikhtisar Bab

Kemunculan EdgeAI telah menjadikan konversi format model dan kuantisasi sebagai teknologi penting untuk menerapkan kemampuan pembelajaran mesin canggih pada perangkat dengan sumber daya terbatas. Bab ini memberikan panduan lengkap untuk memahami, mengimplementasikan, dan mengoptimalkan model untuk skenario penerapan di edge.

## 📚 Struktur Bab dan Jalur Pembelajaran

Bab ini disusun dalam enam bagian progresif, masing-masing membangun pemahaman yang lebih mendalam tentang optimasi model untuk komputasi edge:

---

## [Bagian 1: Dasar-Dasar Konversi Format Model dan Kuantisasi](./01.Introduce.md)

### 🎯 Ikhtisar
Bagian dasar ini menetapkan kerangka teori untuk optimasi model dalam lingkungan komputasi edge, mencakup batas kuantisasi dari presisi 1-bit hingga 8-bit dan strategi utama konversi format.

**Topik Utama:**
- Kerangka klasifikasi presisi (ultra-rendah, rendah, presisi sedang)
- Keunggulan dan kasus penggunaan format GGUF dan ONNX
- Manfaat kuantisasi untuk efisiensi operasional dan fleksibilitas penerapan
- Perbandingan kinerja dan jejak memori

**Hasil Pembelajaran:**
- Memahami batas kuantisasi dan klasifikasi
- Mengidentifikasi teknik konversi format yang sesuai
- Mempelajari strategi optimasi lanjutan untuk penerapan di edge

---

## [Bagian 2: Panduan Implementasi Llama.cpp](./02.Llamacpp.md)

### 🎯 Ikhtisar
Tutorial lengkap untuk mengimplementasikan Llama.cpp, kerangka kerja C++ yang kuat untuk inferensi Model Bahasa Besar dengan pengaturan minimal di berbagai konfigurasi perangkat keras.

**Topik Utama:**
- Instalasi di platform Windows, macOS, dan Linux
- Konversi format GGUF dan berbagai tingkat kuantisasi (Q2_K hingga Q8_0)
- Akselerasi perangkat keras dengan CUDA, Metal, OpenCL, dan Vulkan
- Integrasi Python dan strategi penerapan produksi

**Hasil Pembelajaran:**
- Menguasai instalasi lintas platform dan pembangunan dari sumber
- Mengimplementasikan teknik kuantisasi dan optimasi model
- Menerapkan model dalam mode server dengan integrasi REST API

---

## [Bagian 3: Microsoft Olive Optimization Suite](./03.MicrosoftOlive.md)

### 🎯 Ikhtisar
Eksplorasi Microsoft Olive, toolkit optimasi model yang sadar perangkat keras dengan lebih dari 40 komponen optimasi bawaan, dirancang untuk penerapan model tingkat perusahaan di berbagai platform perangkat keras.

**Topik Utama:**
- Fitur auto-optimasi dengan kuantisasi dinamis dan statis
- Intelijen yang sadar perangkat keras untuk penerapan di CPU, GPU, dan NPU
- Dukungan model populer (Llama, Phi, Qwen, Gemma) secara langsung
- Integrasi perusahaan dengan Azure ML dan alur kerja produksi

**Hasil Pembelajaran:**
- Memanfaatkan optimasi otomatis untuk berbagai arsitektur model
- Mengimplementasikan strategi penerapan lintas platform
- Membangun pipeline optimasi yang siap untuk tingkat perusahaan

---

## [Bagian 4: OpenVINO Toolkit Optimization Suite](./04.openvino.md)

### 🎯 Ikhtisar
Eksplorasi menyeluruh tentang toolkit OpenVINO dari Intel, platform open-source untuk menerapkan solusi AI yang berkinerja tinggi di cloud, on-premises, dan lingkungan edge dengan kemampuan Neural Network Compression Framework (NNCF) yang canggih.

**Topik Utama:**
- Penerapan lintas platform dengan akselerasi perangkat keras (CPU, GPU, VPU, akselerator AI)
- Neural Network Compression Framework (NNCF) untuk kuantisasi dan pruning tingkat lanjut
- OpenVINO GenAI untuk optimasi dan penerapan model bahasa besar
- Kemampuan server model tingkat perusahaan dan strategi penerapan yang skalabel

**Hasil Pembelajaran:**
- Menguasai alur kerja konversi dan optimasi model OpenVINO
- Mengimplementasikan teknik kuantisasi tingkat lanjut dengan NNCF
- Menerapkan model yang dioptimalkan di berbagai platform perangkat keras dengan Model Server

---

## [Bagian 5: Pendalaman Kerangka Apple MLX](./05.AppleMLX.md)

### 🎯 Ikhtisar
Cakupan menyeluruh tentang Apple MLX, kerangka kerja revolusioner yang dirancang khusus untuk pembelajaran mesin yang efisien di Apple Silicon, dengan penekanan pada kemampuan Model Bahasa Besar dan penerapan lokal.

**Topik Utama:**
- Keunggulan arsitektur memori terpadu dan Metal Performance Shaders
- Dukungan untuk model LLaMA, Mistral, Phi-3, Qwen, dan Code Llama
- Fine-tuning LoRA untuk kustomisasi model yang efisien
- Integrasi Hugging Face dan dukungan kuantisasi (4-bit dan 8-bit)

**Hasil Pembelajaran:**
- Menguasai optimasi Apple Silicon untuk penerapan LLM
- Mengimplementasikan teknik fine-tuning dan kustomisasi model
- Membangun aplikasi AI tingkat perusahaan dengan fitur privasi yang ditingkatkan

---

## [Bagian 6: Sintesis Alur Kerja Pengembangan Edge AI](./06.workflow-synthesis.md)

### 🎯 Ikhtisar
Sintesis menyeluruh dari semua kerangka optimasi ke dalam alur kerja terpadu, matriks keputusan, dan praktik terbaik untuk penerapan Edge AI yang siap produksi di berbagai platform dan kasus penggunaan.

**Topik Utama:**
- Arsitektur alur kerja terpadu yang mengintegrasikan berbagai kerangka optimasi
- Pohon keputusan pemilihan kerangka kerja dan analisis trade-off kinerja
- Validasi kesiapan produksi dan strategi penerapan yang komprehensif
- Strategi untuk masa depan menghadapi perangkat keras dan arsitektur model yang muncul

**Hasil Pembelajaran:**
- Menguasai pemilihan kerangka kerja secara sistematis berdasarkan kebutuhan dan kendala
- Mengimplementasikan pipeline Edge AI yang siap produksi dengan pemantauan yang komprehensif
- Merancang alur kerja yang dapat beradaptasi dengan teknologi dan kebutuhan yang terus berkembang

---

## 🎯 Hasil Pembelajaran Bab

Setelah menyelesaikan bab ini, pembaca akan mencapai:

### **Penguasaan Teknis**
- Pemahaman mendalam tentang batas kuantisasi dan aplikasi praktisnya
- Pengalaman langsung dengan berbagai kerangka optimasi
- Keterampilan penerapan produksi untuk lingkungan komputasi edge

### **Pemahaman Strategis**
- Kemampuan memilih optimasi yang sadar perangkat keras
- Pengambilan keputusan yang terinformasi tentang trade-off kinerja
- Strategi penerapan dan pemantauan yang siap untuk tingkat perusahaan

### **Benchmark Kinerja**

| Kerangka Kerja | Kuantisasi | Penggunaan Memori | Peningkatan Kecepatan | Kasus Penggunaan |
|----------------|------------|-------------------|-----------------------|------------------|
| Llama.cpp      | Q4_K_M     | ~4GB             | 2-3x                 | Penerapan lintas platform |
| Olive          | INT4       | Pengurangan 60-75% | 2-6x                 | Alur kerja perusahaan |
| OpenVINO       | INT8/INT4  | Pengurangan 50-75% | 2-5x                 | Optimasi perangkat keras Intel |
| MLX            | 4-bit      | ~4GB             | 2-4x                 | Optimasi Apple Silicon |

## 🚀 Langkah Selanjutnya dan Aplikasi Lanjutan

Bab ini memberikan dasar lengkap untuk:
- Pengembangan model kustom untuk domain spesifik
- Penelitian dalam optimasi Edge AI
- Pengembangan aplikasi AI komersial
- Penerapan Edge AI tingkat perusahaan dalam skala besar

Pengetahuan dari enam bagian ini menawarkan toolkit yang komprehensif untuk menavigasi lanskap yang terus berkembang dalam optimasi dan penerapan model Edge AI.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.