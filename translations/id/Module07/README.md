<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e9e31a2b5ff0f6a682a258fa859a8ff5",
  "translation_date": "2025-09-26T19:39:38+00:00",
  "source_file": "Module07/README.md",
  "language_code": "id"
}
-->
# Bab 07: Contoh EdgeAI

Edge AI adalah perpaduan antara kecerdasan buatan dan komputasi edge, memungkinkan pemrosesan cerdas langsung pada perangkat tanpa bergantung pada konektivitas cloud. Bab ini membahas lima implementasi EdgeAI yang berbeda di berbagai platform dan kerangka kerja, menunjukkan fleksibilitas dan kekuatan menjalankan model AI di edge.

## 1. EdgeAI pada NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano merupakan terobosan dalam komputasi AI edge yang terjangkau, memberikan performa AI hingga 67 TOPS dalam bentuk yang kecil seukuran kartu kredit. Platform AI edge yang kuat ini mendemokratisasi pengembangan AI generatif untuk para hobiis, pelajar, dan pengembang profesional.

### Fitur Utama
- Memberikan performa AI hingga 67 TOPS—peningkatan 1,7X dibandingkan pendahulunya
- 1024 CUDA core dan hingga 32 Tensor Core untuk pemrosesan AI
- CPU Arm Cortex-A78AE v8.2 64-bit 6-core dengan frekuensi maksimum 1,5 GHz
- Harga hanya $249, menyediakan platform yang paling terjangkau dan mudah diakses bagi pengembang, pelajar, dan pembuat

### Aplikasi
Jetson Orin Nano unggul dalam menjalankan model AI generatif modern termasuk vision transformers, model bahasa besar, dan model vision-language. Dirancang khusus untuk kasus penggunaan GenAI, kini Anda dapat menjalankan beberapa LLM di perangkat seukuran telapak tangan. Kasus penggunaan populer meliputi robotika berbasis AI, drone pintar, kamera cerdas, dan perangkat edge otonom.

**Pelajari Lebih Lanjut**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI pada Aplikasi Mobile dengan .NET MAUI dan ONNX Runtime GenAI

Solusi ini menunjukkan cara mengintegrasikan AI Generatif dan Model Bahasa Besar (LLM) ke dalam aplikasi mobile lintas platform menggunakan .NET MAUI (Multi-platform App UI) dan ONNX Runtime GenAI. Pendekatan ini memungkinkan pengembang .NET membangun aplikasi mobile berbasis AI yang canggih yang berjalan secara native di perangkat Android dan iOS.

### Fitur Utama
- Dibangun di atas kerangka kerja .NET MAUI, menyediakan satu basis kode untuk aplikasi Android dan iOS
- Integrasi ONNX Runtime GenAI memungkinkan menjalankan model AI generatif langsung di perangkat mobile
- Mendukung berbagai akselerator perangkat keras yang disesuaikan untuk perangkat mobile, termasuk CPU, GPU, dan prosesor AI khusus
- Optimasi spesifik platform seperti CoreML untuk iOS dan NNAPI untuk Android melalui ONNX Runtime
- Mengimplementasikan seluruh loop AI generatif termasuk pra dan pasca pemrosesan, inferensi, pemrosesan logits, pencarian dan sampling, serta manajemen cache KV

### Manfaat Pengembangan
Pendekatan .NET MAUI memungkinkan pengembang memanfaatkan keterampilan C# dan .NET yang sudah ada sambil membangun aplikasi AI lintas platform. Kerangka kerja ONNX Runtime GenAI mendukung berbagai arsitektur model termasuk Llama, Mistral, Phi, Gemma, dan lainnya. Kernel ARM64 yang dioptimalkan mempercepat perkalian matriks INT4 yang terkuantisasi, memastikan performa yang efisien pada perangkat keras mobile sambil mempertahankan pengalaman pengembangan .NET yang familiar.

### Kasus Penggunaan
Solusi ini ideal bagi pengembang yang ingin membangun aplikasi mobile berbasis AI menggunakan teknologi .NET, termasuk chatbot cerdas, aplikasi pengenalan gambar, alat penerjemahan bahasa, dan sistem rekomendasi yang dipersonalisasi yang berjalan sepenuhnya di perangkat untuk meningkatkan privasi dan kemampuan offline.

**Pelajari Lebih Lanjut**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI di Azure dengan Small Language Models Engine

Solusi EdgeAI berbasis Azure dari Microsoft berfokus pada penerapan Small Language Models (SLM) secara efisien di lingkungan hybrid cloud-edge. Pendekatan ini menjembatani kesenjangan antara layanan AI skala cloud dan kebutuhan penerapan di edge.

### Keunggulan Arsitektur
- Integrasi mulus dengan layanan Azure AI
- Menjalankan SLM/LLM dan model multi-modal di perangkat dan di cloud dengan ONNX Runtime
- Dioptimalkan untuk penerapan skala perusahaan
- Mendukung pembaruan dan manajemen model secara berkelanjutan

### Kasus Penggunaan
Implementasi Azure EdgeAI unggul dalam skenario yang membutuhkan penerapan AI tingkat perusahaan dengan kemampuan manajemen cloud. Ini mencakup pemrosesan dokumen cerdas, analitik waktu nyata, dan alur kerja AI hybrid yang memanfaatkan sumber daya komputasi cloud dan edge.

**Pelajari Lebih Lanjut**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI dengan Windows ML](./windowdeveloper.md)

Windows ML adalah runtime canggih dari Microsoft yang dioptimalkan untuk inferensi model di perangkat dan penerapan yang disederhanakan, menjadi dasar dari Windows AI Foundry. Platform ini memungkinkan pengembang menciptakan aplikasi Windows berbasis AI yang memanfaatkan seluruh spektrum perangkat keras PC.

### Kemampuan Platform
- Berfungsi di semua PC Windows 11 yang menjalankan versi 24H2 (build 26100) atau lebih tinggi
- Berfungsi di semua perangkat keras PC x64 dan ARM64, bahkan PC yang tidak memiliki NPU atau GPU
- Memungkinkan pengembang membawa model mereka sendiri dan menerapkannya secara efisien di ekosistem mitra silikon termasuk AMD, Intel, NVIDIA, dan Qualcomm yang mencakup CPU, GPU, NPU
- Dengan memanfaatkan API infrastruktur, pengembang tidak perlu lagi membuat beberapa build aplikasi mereka untuk menargetkan silikon yang berbeda

### Manfaat bagi Pengembang
Windows ML mengabstraksi perangkat keras dan penyedia eksekusi, sehingga Anda dapat fokus menulis kode Anda. Selain itu, Windows ML secara otomatis diperbarui untuk mendukung NPU, GPU, dan CPU terbaru saat dirilis. Platform ini menyediakan kerangka kerja terpadu untuk pengembangan AI di ekosistem perangkat keras Windows yang beragam.

**Pelajari Lebih Lanjut**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](./windowdeveloper.md) - Panduan komprehensif untuk pengembangan Windows Edge AI

## [5. EdgeAI dengan Foundry Local Applications](./foundrylocal.md)

Foundry Local memungkinkan pengembang Windows dan Mac membangun aplikasi Retrieval Augmented Generation (RAG) menggunakan sumber daya lokal di .NET, menggabungkan model bahasa lokal dengan kemampuan pencarian semantik. Pendekatan ini menyediakan solusi AI yang berfokus pada privasi yang beroperasi sepenuhnya di infrastruktur lokal.

### Arsitektur Teknis
- Menggabungkan model bahasa Phi, Local Embeddings, dan Semantic Kernel untuk menciptakan skenario RAG
- Menggunakan embeddings sebagai vektor (array) nilai floating-point yang mewakili konten dan makna semantiknya
- Semantic Kernel bertindak sebagai pengatur utama, mengintegrasikan Phi dan Komponen Cerdas untuk menciptakan pipeline RAG yang mulus
- Mendukung basis data vektor lokal termasuk SQLite dan Qdrant

### Manfaat Implementasi
RAG, atau Retrieval Augmented Generation, adalah cara cerdas untuk "mencari informasi dan memasukkannya ke dalam prompt". Implementasi lokal ini memastikan privasi data sambil memberikan respons cerdas yang didasarkan pada basis pengetahuan khusus. Pendekatan ini sangat berharga untuk skenario perusahaan yang membutuhkan kedaulatan data dan kemampuan operasi offline.

**Pelajari Lebih Lanjut**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local menyediakan server REST yang kompatibel dengan OpenAI yang didukung oleh ONNX Runtime untuk menjalankan model secara lokal di Windows. Berikut adalah ringkasan cepat yang telah divalidasi; lihat dokumen resmi untuk detail lengkap.

- Memulai: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arsitektur: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Referensi CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Panduan lengkap Windows di repo ini: [foundrylocal.md](./foundrylocal.md)

Instal atau tingkatkan di Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Jelajahi kategori CLI:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Jalankan model dan temukan endpoint dinamis:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Cek REST cepat untuk daftar model (ganti PORT dari status):
```cmd
curl -s http://localhost:PORT/v1/models
```

Tips:
- Integrasi SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Bawa model Anda sendiri (kompilasi): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Sumber Daya Pengembangan Windows EdgeAI

Untuk pengembang yang secara khusus menargetkan platform Windows, kami telah membuat panduan komprehensif yang mencakup ekosistem Windows EdgeAI secara lengkap. Sumber daya ini menyediakan informasi mendetail tentang Windows AI Foundry, termasuk API, alat, dan praktik terbaik untuk pengembangan EdgeAI di Windows.

### Platform Windows AI Foundry
Platform Windows AI Foundry menyediakan rangkaian alat dan API yang komprehensif yang dirancang khusus untuk pengembangan AI Edge di perangkat Windows. Ini mencakup dukungan khusus untuk perangkat keras yang dipercepat NPU, integrasi Windows ML, dan teknik optimasi spesifik platform.

**Panduan Komprehensif**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

Panduan ini mencakup:
- Ikhtisar platform Windows AI Foundry dan komponennya
- API Phi Silica untuk inferensi yang efisien pada perangkat keras NPU
- API Computer Vision untuk pemrosesan gambar dan OCR
- Integrasi dan optimasi runtime Windows ML
- CLI Foundry Local untuk pengembangan dan pengujian lokal
- Strategi optimasi perangkat keras untuk perangkat Windows
- Contoh implementasi praktis dan praktik terbaik

### [AI Toolkit untuk Pengembangan Edge AI](./aitoolkit.md)
Untuk pengembang yang menggunakan Visual Studio Code, ekstensi AI Toolkit menyediakan lingkungan pengembangan yang komprehensif yang dirancang khusus untuk membangun, menguji, dan menerapkan aplikasi Edge AI. Toolkit ini menyederhanakan seluruh alur kerja pengembangan Edge AI dalam VS Code.

**Panduan Pengembangan**: [AI Toolkit untuk Pengembangan Edge AI](./aitoolkit.md)

Panduan AI Toolkit mencakup:
- Penemuan dan pemilihan model untuk penerapan di edge
- Alur kerja pengujian dan optimasi lokal
- Integrasi ONNX dan Ollama untuk model edge
- Teknik konversi dan kuantisasi model
- Pengembangan agen untuk skenario edge
- Evaluasi performa dan pemantauan
- Persiapan penerapan dan praktik terbaik

## Kesimpulan

Kelima implementasi EdgeAI ini menunjukkan kematangan dan keragaman solusi AI edge yang tersedia saat ini. Dari perangkat edge yang dipercepat perangkat keras seperti Jetson Orin Nano hingga kerangka kerja perangkat lunak seperti ONNX Runtime GenAI dan Windows ML, pengembang memiliki opsi yang belum pernah ada sebelumnya untuk menerapkan aplikasi cerdas di edge.

Benang merah di semua platform ini adalah demokratisasi kemampuan AI, membuat pembelajaran mesin yang canggih dapat diakses oleh pengembang di berbagai tingkat keterampilan dan kasus penggunaan. Baik membangun aplikasi mobile, perangkat lunak desktop, atau sistem tertanam, solusi EdgeAI ini menyediakan fondasi untuk generasi berikutnya dari aplikasi cerdas yang beroperasi secara efisien dan privat di edge.

Setiap platform menawarkan keunggulan unik: Jetson Orin Nano untuk komputasi edge yang dipercepat perangkat keras, ONNX Runtime GenAI untuk pengembangan mobile lintas platform, Azure EdgeAI untuk integrasi cloud-edge tingkat perusahaan, Windows ML untuk aplikasi native Windows, dan Foundry Local untuk implementasi RAG yang berfokus pada privasi. Bersama-sama, mereka mewakili ekosistem yang komprehensif untuk pengembangan EdgeAI.

---

