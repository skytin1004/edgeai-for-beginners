<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c0cb9f7bcff2bc170532d8870a891f38",
  "translation_date": "2025-09-18T14:33:29+00:00",
  "source_file": "Module04/README.md",
  "language_code": "ms"
}
-->
# Bab 04: Penukaran Format Model dan Kuantisasi - Gambaran Bab

Kemunculan EdgeAI telah menjadikan penukaran format model dan kuantisasi sebagai teknologi penting untuk melaksanakan keupayaan pembelajaran mesin yang canggih pada peranti dengan sumber yang terhad. Bab yang komprehensif ini menyediakan panduan lengkap untuk memahami, melaksanakan, dan mengoptimumkan model bagi senario pelaksanaan di peranti tepi.

## 📚 Struktur Bab dan Laluan Pembelajaran

Bab ini disusun dalam enam bahagian progresif, setiap satu membina pemahaman yang lebih mendalam tentang pengoptimuman model untuk pengkomputeran tepi:

---

## [Bahagian 1: Asas Penukaran Format Model dan Kuantisasi](./01.Introduce.md)

### 🎯 Gambaran
Bahagian asas ini menetapkan kerangka teori untuk pengoptimuman model dalam persekitaran pengkomputeran tepi, merangkumi sempadan kuantisasi dari tahap ketepatan 1-bit hingga 8-bit serta strategi penukaran format utama.

**Topik Utama:**
- Kerangka klasifikasi ketepatan (ultra-rendah, rendah, sederhana)
- Kelebihan dan kegunaan format GGUF dan ONNX
- Manfaat kuantisasi untuk kecekapan operasi dan fleksibiliti pelaksanaan
- Penanda aras prestasi dan perbandingan jejak memori

**Hasil Pembelajaran:**
- Memahami sempadan dan klasifikasi kuantisasi
- Mengenal pasti teknik penukaran format yang sesuai
- Mempelajari strategi pengoptimuman lanjutan untuk pelaksanaan di peranti tepi

---

## [Bahagian 2: Panduan Pelaksanaan Llama.cpp](./02.Llamacpp.md)

### 🎯 Gambaran
Tutorial komprehensif untuk melaksanakan Llama.cpp, kerangka C++ yang berkuasa untuk inferens Model Bahasa Besar dengan persediaan minimum merentasi konfigurasi perkakasan yang pelbagai.

**Topik Utama:**
- Pemasangan di platform Windows, macOS, dan Linux
- Penukaran format GGUF dan pelbagai tahap kuantisasi (Q2_K hingga Q8_0)
- Pecutan perkakasan dengan CUDA, Metal, OpenCL, dan Vulkan
- Integrasi Python dan strategi pelaksanaan pengeluaran

**Hasil Pembelajaran:**
- Menguasai pemasangan merentas platform dan binaan dari sumber
- Melaksanakan teknik kuantisasi dan pengoptimuman model
- Melaksanakan model dalam mod pelayan dengan integrasi REST API

---

## [Bahagian 3: Microsoft Olive Optimization Suite](./03.MicrosoftOlive.md)

### 🎯 Gambaran
Penerokaan Microsoft Olive, alat pengoptimuman model yang peka terhadap perkakasan dengan lebih daripada 40 komponen pengoptimuman terbina, direka untuk pelaksanaan model bertaraf perusahaan merentasi platform perkakasan yang pelbagai.

**Topik Utama:**
- Ciri auto-pengoptimuman dengan kuantisasi dinamik dan statik
- Kecerdasan peka perkakasan untuk pelaksanaan CPU, GPU, dan NPU
- Sokongan model popular (Llama, Phi, Qwen, Gemma) secara langsung
- Integrasi perusahaan dengan Azure ML dan aliran kerja pengeluaran

**Hasil Pembelajaran:**
- Memanfaatkan pengoptimuman automatik untuk pelbagai seni bina model
- Melaksanakan strategi pelaksanaan merentas platform
- Menubuhkan saluran pengoptimuman yang bersedia untuk perusahaan

---

## [Bahagian 4: OpenVINO Toolkit Optimization Suite](./04.openvino.md)

### 🎯 Gambaran
Penerokaan komprehensif alat OpenVINO Intel, platform sumber terbuka untuk melaksanakan penyelesaian AI yang berprestasi tinggi merentasi awan, premis, dan persekitaran tepi dengan keupayaan rangka kerja pemampatan rangkaian neural (NNCF) yang canggih.

**Topik Utama:**
- Pelaksanaan merentas platform dengan pecutan perkakasan (CPU, GPU, VPU, pemecut AI)
- Rangka kerja pemampatan rangkaian neural (NNCF) untuk kuantisasi dan pemangkasan lanjutan
- OpenVINO GenAI untuk pengoptimuman dan pelaksanaan model bahasa besar
- Keupayaan pelayan model bertaraf perusahaan dan strategi pelaksanaan yang boleh diskalakan

**Hasil Pembelajaran:**
- Menguasai aliran kerja penukaran dan pengoptimuman model OpenVINO
- Melaksanakan teknik kuantisasi lanjutan dengan NNCF
- Melaksanakan model yang dioptimumkan merentasi platform perkakasan yang pelbagai dengan Pelayan Model

---

## [Bahagian 5: Apple MLX Framework Deep Dive](./05.AppleMLX.md)

### 🎯 Gambaran
Liputan komprehensif Apple MLX, kerangka revolusioner yang direka khusus untuk pembelajaran mesin yang cekap pada Apple Silicon, dengan penekanan pada keupayaan Model Bahasa Besar dan pelaksanaan tempatan.

**Topik Utama:**
- Kelebihan seni bina memori bersatu dan Metal Performance Shaders
- Sokongan untuk model LLaMA, Mistral, Phi-3, Qwen, dan Code Llama
- Penalaan LoRA untuk penyesuaian model yang cekap
- Integrasi Hugging Face dan sokongan kuantisasi (4-bit dan 8-bit)

**Hasil Pembelajaran:**
- Menguasai pengoptimuman Apple Silicon untuk pelaksanaan LLM
- Melaksanakan teknik penalaan dan penyesuaian model
- Membina aplikasi AI perusahaan dengan ciri privasi yang dipertingkatkan

---

## [Bahagian 6: Sintesis Aliran Kerja Pembangunan Edge AI](./06.workflow-synthesis.md)

### 🎯 Gambaran
Sintesis komprehensif semua rangka kerja pengoptimuman ke dalam aliran kerja bersatu, matriks keputusan, dan amalan terbaik untuk pelaksanaan Edge AI yang bersedia untuk pengeluaran merentasi platform dan kegunaan yang pelbagai.

**Topik Utama:**
- Seni bina aliran kerja bersatu yang mengintegrasikan pelbagai rangka kerja pengoptimuman
- Pokok keputusan pemilihan rangka kerja dan analisis kompromi prestasi
- Pengesahan kesediaan pengeluaran dan strategi pelaksanaan yang komprehensif
- Strategi masa depan untuk perkakasan dan seni bina model yang muncul

**Hasil Pembelajaran:**
- Menguasai pemilihan rangka kerja yang sistematik berdasarkan keperluan dan kekangan
- Melaksanakan saluran Edge AI bertaraf pengeluaran dengan pemantauan yang komprehensif
- Merancang aliran kerja yang boleh disesuaikan dengan teknologi dan keperluan yang berkembang

---

## 🎯 Hasil Pembelajaran Bab

Setelah menyelesaikan bab yang komprehensif ini, pembaca akan mencapai:

### **Penguasaan Teknikal**
- Pemahaman mendalam tentang sempadan kuantisasi dan aplikasi praktikal
- Pengalaman langsung dengan pelbagai rangka kerja pengoptimuman
- Kemahiran pelaksanaan pengeluaran untuk persekitaran pengkomputeran tepi

### **Pemahaman Strategik**
- Keupayaan pemilihan pengoptimuman yang peka terhadap perkakasan
- Pembuatan keputusan yang berinformasi tentang kompromi prestasi
- Strategi pelaksanaan dan pemantauan yang bersedia untuk perusahaan

### **Penanda Aras Prestasi**

| Rangka Kerja | Kuantisasi | Penggunaan Memori | Peningkatan Kelajuan | Kegunaan |
|--------------|------------|-------------------|----------------------|----------|
| Llama.cpp    | Q4_K_M     | ~4GB             | 2-3x                | Pelaksanaan merentas platform |
| Olive        | INT4       | Pengurangan 60-75%| 2-6x                | Aliran kerja perusahaan |
| OpenVINO     | INT8/INT4  | Pengurangan 50-75%| 2-5x                | Pengoptimuman perkakasan Intel |
| MLX          | 4-bit      | ~4GB             | 2-4x                | Pengoptimuman Apple Silicon |

## 🚀 Langkah Seterusnya dan Aplikasi Lanjutan

Bab ini menyediakan asas lengkap untuk:
- Pembangunan model tersuai untuk domain tertentu
- Penyelidikan dalam pengoptimuman Edge AI
- Pembangunan aplikasi AI komersial
- Pelaksanaan Edge AI perusahaan berskala besar

Pengetahuan dari enam bahagian ini menawarkan alat komprehensif untuk menavigasi landskap pengoptimuman dan pelaksanaan model Edge AI yang berkembang pesat.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.