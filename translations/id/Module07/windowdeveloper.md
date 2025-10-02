<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77bb931ce93583c081cf7861f43d9662",
  "translation_date": "2025-10-02T13:44:06+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "id"
}
-->
# Panduan Pengembangan AI Edge Windows

## Pendahuluan

Selamat datang di Pengembangan AI Edge Windows - panduan lengkap untuk membangun aplikasi cerdas yang memanfaatkan kekuatan AI di perangkat menggunakan platform Windows AI Foundry dari Microsoft. Panduan ini dirancang khusus untuk pengembang Windows yang ingin mengintegrasikan kemampuan AI Edge terkini ke dalam aplikasi mereka sambil memanfaatkan akselerasi perangkat keras Windows secara maksimal.

### Keunggulan AI Windows

Windows AI Foundry adalah platform yang terpadu, andal, dan aman yang mendukung seluruh siklus hidup pengembang AI - mulai dari pemilihan dan penyempurnaan model hingga optimasi dan penerapan di arsitektur CPU, GPU, NPU, dan cloud hybrid. Platform ini mendemokratisasi pengembangan AI dengan menyediakan:

- **Abstraksi Perangkat Keras**: Penerapan yang mulus di silikon AMD, Intel, NVIDIA, dan Qualcomm
- **Kecerdasan di Perangkat**: AI yang menjaga privasi dan berjalan sepenuhnya di perangkat lokal
- **Performa yang Dioptimalkan**: Model yang telah dioptimalkan untuk konfigurasi perangkat keras Windows
- **Siap untuk Perusahaan**: Fitur keamanan dan kepatuhan tingkat produksi

### Mengapa Windows untuk AI Edge?

**Dukungan Perangkat Keras Universal**  
Windows ML menyediakan optimasi perangkat keras otomatis di seluruh ekosistem Windows, memastikan aplikasi AI Anda bekerja secara optimal terlepas dari arsitektur silikon yang mendasarinya.

**Runtime AI Terintegrasi**  
Mesin inferensi Windows ML bawaan menghilangkan kebutuhan pengaturan yang kompleks, memungkinkan pengembang untuk fokus pada logika aplikasi daripada masalah infrastruktur.

**Optimasi PC Copilot+**  
API yang dirancang khusus untuk perangkat Windows generasi berikutnya dengan Neural Processing Units (NPUs) yang memberikan performa luar biasa per watt.

**Ekosistem Pengembang**  
Alat yang kaya termasuk integrasi Visual Studio, dokumentasi yang komprehensif, dan aplikasi contoh yang mempercepat siklus pengembangan.

## Tujuan Pembelajaran

Dengan menyelesaikan panduan pengembangan AI Edge Windows ini, Anda akan menguasai keterampilan penting untuk membangun aplikasi AI siap produksi di platform Windows.

### Kompetensi Teknis Inti

**Penguasaan Windows AI Foundry**  
- Memahami arsitektur dan komponen platform Windows AI Foundry  
- Menavigasi seluruh siklus pengembangan AI dalam ekosistem Windows  
- Menerapkan praktik terbaik keamanan untuk aplikasi AI di perangkat  
- Mengoptimalkan aplikasi untuk berbagai konfigurasi perangkat keras Windows  

**Keahlian Integrasi API**  
- Menguasai API Windows AI untuk aplikasi teks, visi, dan multimodal  
- Menerapkan integrasi model bahasa Phi Silica untuk generasi teks dan penalaran  
- Menerapkan kemampuan visi komputer menggunakan API pemrosesan gambar bawaan  
- Menyesuaikan model yang telah dilatih menggunakan teknik LoRA (Low-Rank Adaptation)  

**Implementasi Lokal Foundry**  
- Menjelajahi, mengevaluasi, dan menerapkan model bahasa sumber terbuka menggunakan Foundry Local CLI  
- Memahami optimasi model dan kuantisasi untuk penerapan lokal  
- Menerapkan kemampuan AI offline yang berfungsi tanpa konektivitas internet  
- Mengelola siklus hidup model dan pembaruan di lingkungan produksi  

**Penerapan Windows ML**  
- Membawa model ONNX kustom ke aplikasi Windows menggunakan Windows ML  
- Memanfaatkan akselerasi perangkat keras otomatis di arsitektur CPU, GPU, dan NPU  
- Menerapkan inferensi waktu nyata dengan pemanfaatan sumber daya yang optimal  
- Merancang aplikasi AI yang skalabel untuk berbagai kategori perangkat Windows  

### Keterampilan Pengembangan Aplikasi

**Pengembangan Windows Lintas Platform**  
- Membangun aplikasi bertenaga AI menggunakan .NET MAUI untuk penerapan Windows universal  
- Mengintegrasikan kemampuan AI ke dalam aplikasi Win32, UWP, dan Progressive Web Applications  
- Menerapkan desain UI responsif yang beradaptasi dengan status pemrosesan AI  
- Menangani operasi AI asinkron dengan pola pengalaman pengguna yang tepat  

**Optimasi Performa**  
- Memprofilkan dan mengoptimalkan performa inferensi AI di berbagai konfigurasi perangkat keras  
- Menerapkan manajemen memori yang efisien untuk model bahasa besar  
- Merancang aplikasi yang secara elegan menyesuaikan berdasarkan kemampuan perangkat keras yang tersedia  
- Menerapkan strategi caching untuk operasi AI yang sering digunakan  

**Kesiapan Produksi**  
- Menerapkan penanganan kesalahan yang komprehensif dan mekanisme cadangan  
- Merancang telemetri dan pemantauan untuk performa aplikasi AI  
- Menerapkan praktik terbaik keamanan untuk penyimpanan dan eksekusi model AI lokal  
- Merencanakan strategi penerapan untuk aplikasi perusahaan dan konsumen  

### Pemahaman Bisnis dan Strategis

**Arsitektur Aplikasi AI**  
- Merancang arsitektur hybrid yang mengoptimalkan antara pemrosesan AI lokal dan cloud  
- Mengevaluasi trade-off antara ukuran model, akurasi, dan kecepatan inferensi  
- Merencanakan arsitektur aliran data yang menjaga privasi sambil memungkinkan kecerdasan  
- Menerapkan solusi AI yang hemat biaya dan skalabel sesuai permintaan pengguna  

**Posisi Pasar**  
- Memahami keunggulan kompetitif aplikasi AI asli Windows  
- Mengidentifikasi kasus penggunaan di mana AI di perangkat memberikan pengalaman pengguna yang unggul  
- Mengembangkan strategi go-to-market untuk aplikasi Windows yang ditingkatkan AI  
- Memposisikan aplikasi untuk memanfaatkan manfaat ekosistem Windows  

## Contoh SDK Aplikasi Windows AI

Windows App SDK menyediakan contoh lengkap yang menunjukkan integrasi AI di berbagai kerangka kerja dan skenario penerapan. Contoh ini adalah referensi penting untuk memahami pola pengembangan AI Windows.

### Contoh Windows AI Foundry

| Contoh | Kerangka Kerja | Area Fokus | Fitur Utama |
|--------|----------------|------------|-------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integrasi API Windows AI | Aplikasi WinUI lengkap yang menunjukkan API Windows AI, optimasi ARM64, penerapan paket |

**Teknologi Utama:**  
- API Windows AI  
- Kerangka kerja WinUI 3  
- Optimasi platform ARM64  
- Kompatibilitas PC Copilot+  
- Penerapan aplikasi paket  

**Prasyarat:**  
- Windows 11 dengan PC Copilot+ direkomendasikan  
- Visual Studio 2022  
- Konfigurasi build ARM64  
- Windows App SDK 1.8.1+  

### Contoh Windows ML

#### Contoh C++

| Contoh | Jenis | Area Fokus | Fitur Utama |
|--------|-------|------------|-------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplikasi Konsol | Windows ML Dasar | Penemuan EP, opsi baris perintah, kompilasi model |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplikasi Konsol | Penerapan Kerangka Kerja | Runtime bersama, jejak penerapan lebih kecil |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplikasi Konsol | Penerapan Mandiri | Penerapan mandiri, tanpa dependensi runtime |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Penggunaan Perpustakaan | WindowsML dalam perpustakaan bersama, manajemen memori |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | Tutorial ResNet | Konversi model, kompilasi EP, tutorial Build 2025 |

#### Contoh C#

**Aplikasi Konsol**

| Contoh | Jenis | Area Fokus | Fitur Utama |
|--------|-------|------------|-------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Aplikasi Konsol | Integrasi C# Dasar | Penggunaan helper bersama, antarmuka baris perintah |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | Tutorial ResNet | Konversi model, kompilasi EP, tutorial Build 2025 |

**Aplikasi GUI**

| Contoh | Kerangka Kerja | Area Fokus | Fitur Utama |
|--------|----------------|------------|-------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | GUI Desktop | Klasifikasi gambar dengan antarmuka WPF |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | GUI Tradisional | Klasifikasi gambar dengan Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | GUI Modern | Klasifikasi gambar dengan antarmuka WinUI 3 |

#### Contoh Python

| Contoh | Bahasa | Area Fokus | Fitur Utama |
|--------|--------|------------|-------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Klasifikasi Gambar | Binding Python WinML, pemrosesan gambar batch |

### Prasyarat Contoh

**Persyaratan Sistem:**  
- PC Windows 11 yang menjalankan versi 24H2 (build 26100) atau lebih tinggi  
- Visual Studio 2022 dengan beban kerja C++ dan .NET  
- Windows App SDK 1.8.1 atau lebih baru  
- Python 3.10-3.13 untuk contoh Python di perangkat x64 dan ARM64  

**Spesifik Windows AI Foundry:**  
- PC Copilot+ direkomendasikan untuk performa optimal  
- Konfigurasi build ARM64 untuk contoh Windows AI  
- Identitas paket diperlukan (aplikasi yang tidak dikemas tidak lagi didukung)  

### Alur Kerja Contoh Umum

Sebagian besar contoh Windows ML mengikuti pola standar ini:

1. **Inisialisasi Lingkungan** - Membuat lingkungan ONNX Runtime  
2. **Mendaftarkan Penyedia Eksekusi** - Menemukan dan mendaftarkan akselerator perangkat keras yang tersedia (CPU, GPU, NPU)  
3. **Memuat Model** - Memuat model ONNX, opsional dikompilasi untuk perangkat keras target  
4. **Pra-pemrosesan Input** - Mengonversi gambar/data ke format input model  
5. **Menjalankan Inferensi** - Menjalankan model dan mendapatkan prediksi  
6. **Memproses Hasil** - Menerapkan softmax dan menampilkan prediksi teratas  

### File Model yang Digunakan

| Model | Tujuan | Termasuk | Catatan |
|-------|--------|----------|---------|
| SqueezeNet | Klasifikasi gambar ringan | ✅ Termasuk | Telah dilatih sebelumnya, siap digunakan |
| ResNet-50 | Klasifikasi gambar dengan akurasi tinggi | ❌ Membutuhkan konversi | Gunakan [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) untuk konversi |

### Dukungan Perangkat Keras

Semua contoh secara otomatis mendeteksi dan memanfaatkan perangkat keras yang tersedia:  
- **CPU** - Dukungan universal di semua perangkat Windows  
- **GPU** - Deteksi dan optimasi otomatis untuk perangkat keras grafis yang tersedia  
- **NPU** - Memanfaatkan Neural Processing Units di perangkat yang didukung (PC Copilot+)  

## Komponen Platform Windows AI Foundry

### 1. API Windows AI

API Windows AI menyediakan kemampuan AI siap pakai yang didukung oleh model di perangkat, dioptimalkan untuk efisiensi dan performa pada perangkat PC Copilot+ dengan pengaturan minimal yang diperlukan.

#### Kategori API Inti

**Model Bahasa Phi Silica**  
- Model bahasa kecil namun kuat untuk generasi teks dan penalaran  
- Dioptimalkan untuk inferensi waktu nyata dengan konsumsi daya minimal  
- Dukungan untuk penyempurnaan kustom menggunakan teknik LoRA  
- Integrasi dengan pencarian semantik Windows dan pengambilan pengetahuan  

**API Visi Komputer**  
- **Pengenalan Teks (OCR)**: Mengekstrak teks dari gambar dengan akurasi tinggi  
- **Super Resolusi Gambar**: Meningkatkan resolusi gambar menggunakan model AI lokal  
- **Segmentasi Gambar**: Mengidentifikasi dan mengisolasi objek tertentu dalam gambar  
- **Deskripsi Gambar**: Menghasilkan deskripsi teks rinci untuk konten visual  
- **Penghapusan Objek**: Menghapus objek yang tidak diinginkan dari gambar dengan inpainting berbasis AI  

**Kemampuan Multimodal**  
- **Integrasi Visi-Bahasa**: Menggabungkan pemahaman teks dan gambar  
- **Pencarian Semantik**: Memungkinkan kueri bahasa alami di konten multimedia  
- **Pengambilan Pengetahuan**: Membangun pengalaman pencarian cerdas dengan data lokal  

### 2. Foundry Local

Foundry Local memberikan pengembang akses cepat ke model bahasa sumber terbuka yang siap digunakan di Windows Silicon, menawarkan kemampuan untuk menjelajahi, menguji, berinteraksi, dan menerapkan model dalam aplikasi lokal.

#### Aplikasi Contoh Foundry Local

Repositori [Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples) menyediakan contoh lengkap di berbagai bahasa pemrograman dan kerangka kerja, menunjukkan berbagai pola integrasi dan kasus penggunaan.

| Contoh | Bahasa/Kerangka Kerja | Area Fokus | Fitur Utama |
|--------|------------------------|------------|-------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Implementasi RAG | Integrasi Kernel Semantik, penyimpanan vektor Qdrant, embedding JINA, pengambilan dokumen, obrolan streaming |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Aplikasi Obrolan Desktop | Obrolan lintas platform, pengalihan model lokal/cloud, integrasi SDK OpenAI, streaming waktu nyata |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Integrasi Dasar | Penggunaan SDK sederhana, inisialisasi model, fungsionalitas obrolan dasar |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Integrasi Dasar | Penggunaan SDK Python, respons streaming, API kompatibel OpenAI |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Integrasi Sistem | Penggunaan SDK tingkat rendah, operasi asinkron, klien HTTP reqwest |

#### Kategori Contoh Berdasarkan Kasus Penggunaan

**RAG (Retrieval-Augmented Generation)**  
- **dotNET/rag**: Implementasi RAG lengkap menggunakan Kernel Semantik, database vektor Qdrant, dan embedding JINA  
- **Arsitektur**: Pengambilan dokumen → Pemotongan teks → Embedding vektor → Pencarian kesamaan → Respons berbasis konteks  
- **Teknologi**: Microsoft.SemanticKernel, Qdrant.Client, embedding BERT ONNX, penyelesaian obrolan streaming  

**Aplikasi Desktop**  
- **electron/foundry-chat**: Aplikasi obrolan siap produksi dengan pengalihan model lokal/cloud  
- **Fitur**: Pemilih model, respons streaming, penanganan kesalahan, penerapan lintas platform  
- **Arsitektur**: Proses utama Electron, komunikasi IPC, skrip preload yang aman  

**Contoh Integrasi SDK**  
- **JavaScript (Node.js)**: Interaksi model dasar dan respons streaming  
- **Python**: Penggunaan API kompatibel OpenAI dengan streaming asinkron  
- **Rust**: Integrasi tingkat rendah dengan reqwest dan tokio untuk operasi asinkron  

#### Prasyarat untuk Sampel Foundry Lokal  

**Persyaratan Sistem:**  
- Windows 11 dengan Foundry Lokal terinstal  
- Node.js v16+ untuk sampel JavaScript/Electron  
- .NET 8.0+ untuk sampel C#  
- Python 3.10+ untuk sampel Python  
- Rust 1.70+ untuk sampel Rust  

**Instalasi:**  
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```
  

#### Pengaturan Khusus Sampel  

**Sampel dotNET RAG:**  
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```
  
**Sampel Obrolan Electron:**  
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```
  
**Sampel JavaScript/Python/Rust:**  
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```
  

#### Fitur Utama  

**Katalog Model**  
- Koleksi lengkap model open-source yang telah dioptimalkan  
- Model dioptimalkan untuk CPU, GPU, dan NPU untuk penerapan langsung  
- Dukungan untuk keluarga model populer seperti Llama, Mistral, Phi, dan model khusus domain  

**Integrasi CLI**  
- Antarmuka baris perintah untuk pengelolaan dan penerapan model  
- Alur kerja otomatis untuk optimasi dan kuantisasi  
- Integrasi dengan lingkungan pengembangan populer dan pipeline CI/CD  

**Penerapan Lokal**  
- Operasi offline sepenuhnya tanpa ketergantungan cloud  
- Dukungan untuk format dan konfigurasi model khusus  
- Penyajian model yang efisien dengan optimasi perangkat keras otomatis  

### 3. Windows ML  

Windows ML berfungsi sebagai platform AI inti dan runtime inferensi terintegrasi di Windows, memungkinkan pengembang untuk menerapkan model khusus secara efisien di ekosistem perangkat keras Windows yang luas.  

#### Manfaat Arsitektur  

**Dukungan Perangkat Keras Universal**  
- Optimasi otomatis untuk silikon AMD, Intel, NVIDIA, dan Qualcomm  
- Dukungan eksekusi CPU, GPU, dan NPU dengan pengalihan transparan  
- Abstraksi perangkat keras yang menghilangkan pekerjaan optimasi spesifik platform  

**Fleksibilitas Model**  
- Dukungan untuk format model ONNX dengan konversi otomatis dari kerangka kerja populer  
- Penerapan model khusus dengan kinerja tingkat produksi  
- Integrasi dengan arsitektur aplikasi Windows yang ada  

**Integrasi Perusahaan**  
- Kompatibel dengan kerangka kerja keamanan dan kepatuhan Windows  
- Dukungan untuk alat penerapan dan pengelolaan perusahaan  
- Integrasi dengan sistem pengelolaan dan pemantauan perangkat Windows  

## Alur Kerja Pengembangan  

### Fase 1: Persiapan Lingkungan dan Konfigurasi Alat  

**Persiapan Lingkungan Pengembangan**  
1. Instal Visual Studio 2022 dengan beban kerja C++ dan .NET  
2. Instal Windows App SDK 1.8.1 atau yang lebih baru  
3. Konfigurasikan alat CLI Windows AI Foundry  
4. Siapkan ekstensi AI Toolkit untuk Visual Studio Code  
5. Pasang alat pemantauan dan profil kinerja  
6. Pastikan konfigurasi build ARM64 untuk optimasi Copilot+ PC  

**Pengaturan Repositori Sampel**  
1. Clone [repositori sampel Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)  
2. Navigasikan ke `Samples/WindowsAIFoundry/cs-winui` untuk contoh API Windows AI  
3. Navigasikan ke `Samples/WindowsML` untuk contoh Windows ML yang komprehensif  
4. Tinjau [persyaratan build](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) untuk platform target Anda  

**Eksplorasi Galeri Pengembang AI**  
- Jelajahi aplikasi sampel dan implementasi referensi  
- Uji API Windows AI dengan demonstrasi interaktif  
- Tinjau kode sumber untuk praktik terbaik dan pola  
- Identifikasi sampel yang relevan untuk kasus penggunaan spesifik Anda  

### Fase 2: Pemilihan dan Integrasi Model  

**Analisis Persyaratan**  
- Tentukan persyaratan fungsional untuk kemampuan AI  
- Tetapkan batasan kinerja dan target optimasi  
- Evaluasi persyaratan privasi dan keamanan  
- Rencanakan arsitektur penerapan dan strategi skalabilitas  

**Evaluasi Model**  
- Gunakan Foundry Lokal untuk menguji model open-source untuk kasus penggunaan Anda  
- Benchmark API Windows AI terhadap persyaratan model khusus  
- Evaluasi trade-off antara ukuran model, akurasi, dan kecepatan inferensi  
- Prototipe pendekatan integrasi dengan model yang dipilih  

### Fase 3: Pengembangan Aplikasi  

**Integrasi Inti**  
- Implementasikan integrasi API Windows AI dengan penanganan kesalahan yang tepat  
- Desain antarmuka pengguna yang mengakomodasi alur kerja pemrosesan AI  
- Terapkan strategi caching dan optimasi untuk inferensi model  
- Tambahkan telemetri dan pemantauan untuk kinerja operasi AI  

**Pengujian dan Validasi**  
- Uji aplikasi di berbagai konfigurasi perangkat keras Windows  
- Validasi metrik kinerja di bawah berbagai kondisi beban  
- Implementasikan pengujian otomatis untuk keandalan fungsi AI  
- Lakukan pengujian pengalaman pengguna dengan fitur yang ditingkatkan AI  

### Fase 4: Optimasi dan Penerapan  

**Optimasi Kinerja**  
- Profil kinerja aplikasi di berbagai konfigurasi perangkat keras target  
- Optimalkan penggunaan memori dan strategi pemuatan model  
- Implementasikan perilaku adaptif berdasarkan kemampuan perangkat keras yang tersedia  
- Sesuaikan pengalaman pengguna untuk berbagai skenario kinerja  

**Penerapan Produksi**  
- Paket aplikasi dengan dependensi model AI yang tepat  
- Implementasikan mekanisme pembaruan untuk model dan logika aplikasi  
- Konfigurasikan pemantauan dan analitik untuk lingkungan produksi  
- Rencanakan strategi peluncuran untuk penerapan perusahaan dan konsumen  

## Contoh Implementasi Praktis  

### Contoh 1: Aplikasi Pemrosesan Dokumen Cerdas  

Bangun aplikasi Windows yang memproses dokumen menggunakan berbagai kemampuan AI:  

**Teknologi yang Digunakan:**  
- Phi Silica untuk ringkasan dokumen dan menjawab pertanyaan  
- API OCR untuk ekstraksi teks dari dokumen yang dipindai  
- API Deskripsi Gambar untuk analisis grafik dan diagram  
- Model ONNX khusus untuk klasifikasi dokumen  

**Pendekatan Implementasi:**  
- Desain arsitektur modular dengan komponen AI yang dapat dipasang  
- Implementasikan pemrosesan asinkron untuk batch dokumen besar  
- Tambahkan indikator kemajuan dan dukungan pembatalan untuk operasi yang berjalan lama  
- Sertakan kemampuan offline untuk pemrosesan dokumen sensitif  

### Contoh 2: Sistem Manajemen Inventaris Ritel  

Buat sistem inventaris bertenaga AI untuk aplikasi ritel:  

**Teknologi yang Digunakan:**  
- Segmentasi Gambar untuk identifikasi produk  
- Model visi khusus untuk klasifikasi merek dan kategori  
- Penerapan Foundry Lokal model bahasa khusus ritel  
- Integrasi dengan sistem POS dan inventaris yang ada  

**Pendekatan Implementasi:**  
- Bangun integrasi kamera untuk pemindaian produk secara real-time  
- Implementasikan pengenalan produk melalui barcode dan visual  
- Tambahkan kueri inventaris berbasis bahasa alami menggunakan model bahasa lokal  
- Desain arsitektur yang dapat diskalakan untuk penerapan multi-toko  

### Contoh 3: Asisten Dokumentasi Kesehatan  

Kembangkan alat dokumentasi kesehatan yang menjaga privasi:  

**Teknologi yang Digunakan:**  
- Phi Silica untuk pembuatan catatan medis dan dukungan keputusan klinis  
- OCR untuk mendigitalkan catatan medis tulisan tangan  
- Model bahasa medis khusus yang diterapkan melalui Windows ML  
- Penyimpanan vektor lokal untuk pengambilan pengetahuan medis  

**Pendekatan Implementasi:**  
- Pastikan operasi offline sepenuhnya untuk privasi pasien  
- Implementasikan validasi dan saran terminologi medis  
- Tambahkan pencatatan audit untuk kepatuhan regulasi  
- Desain integrasi dengan sistem Rekam Medis Elektronik yang ada  

## Strategi Optimasi Kinerja  

### Pengembangan yang Sadar Perangkat Keras  

**Optimasi NPU**  
- Desain aplikasi untuk memanfaatkan kemampuan NPU di PC Copilot+  
- Implementasikan fallback yang mulus ke GPU/CPU pada perangkat tanpa NPU  
- Optimalkan format model untuk akselerasi spesifik NPU  
- Pantau pemanfaatan NPU dan karakteristik termal  

**Manajemen Memori**  
- Implementasikan strategi pemuatan dan caching model yang efisien  
- Gunakan pemetaan memori untuk model besar guna mengurangi waktu startup  
- Desain aplikasi yang hemat memori untuk perangkat dengan sumber daya terbatas  
- Terapkan kuantisasi model untuk optimasi memori  

**Efisiensi Baterai**  
- Optimalkan operasi AI untuk konsumsi daya minimal  
- Implementasikan pemrosesan adaptif berdasarkan status baterai  
- Desain pemrosesan latar belakang yang efisien untuk operasi AI berkelanjutan  
- Gunakan alat profil daya untuk mengoptimalkan penggunaan energi  

### Pertimbangan Skalabilitas  

**Multi-Threading**  
- Desain operasi AI yang aman untuk pemrosesan bersamaan  
- Implementasikan distribusi kerja yang efisien di seluruh inti yang tersedia  
- Gunakan pola async/await untuk operasi AI yang tidak memblokir  
- Rencanakan optimasi thread pool untuk konfigurasi perangkat keras yang berbeda  

**Strategi Caching**  
- Implementasikan caching cerdas untuk operasi AI yang sering digunakan  
- Desain strategi invalidasi cache untuk pembaruan model  
- Gunakan caching persisten untuk operasi pra-pemrosesan yang mahal  
- Implementasikan caching terdistribusi untuk skenario multi-pengguna  

## Praktik Terbaik Keamanan dan Privasi  

### Perlindungan Data  

**Pemrosesan Lokal**  
- Pastikan data sensitif tidak pernah meninggalkan perangkat lokal  
- Implementasikan penyimpanan aman untuk model AI dan data sementara  
- Gunakan fitur keamanan Windows untuk sandboxing aplikasi  
- Terapkan enkripsi untuk model yang disimpan dan hasil pemrosesan sementara  

**Keamanan Model**  
- Validasi integritas model sebelum pemuatan dan eksekusi  
- Implementasikan mekanisme pembaruan model yang aman  
- Gunakan model yang ditandatangani untuk mencegah manipulasi  
- Terapkan kontrol akses untuk file model dan konfigurasi  

### Pertimbangan Kepatuhan  

**Kesesuaian Regulasi**  
- Desain aplikasi untuk memenuhi persyaratan GDPR, HIPAA, dan regulasi lainnya  
- Implementasikan pencatatan audit untuk proses pengambilan keputusan AI  
- Sediakan fitur transparansi untuk hasil yang dihasilkan AI  
- Aktifkan kontrol pengguna atas pemrosesan data AI  

**Keamanan Perusahaan**  
- Integrasi dengan kebijakan keamanan perusahaan Windows  
- Dukungan penerapan yang dikelola melalui alat pengelolaan perusahaan  
- Implementasikan kontrol akses berbasis peran untuk fitur AI  
- Sediakan kontrol administratif untuk fungsi AI  

## Pemecahan Masalah dan Debugging  

### Tantangan Pengembangan Umum  

**Masalah Konfigurasi Build**  
- Pastikan konfigurasi platform ARM64 untuk sampel API Windows AI  
- Verifikasi kompatibilitas versi Windows App SDK (1.8.1+ diperlukan)  
- Periksa bahwa identitas paket dikonfigurasi dengan benar (diperlukan untuk API Windows AI)  
- Validasi bahwa alat build mendukung versi kerangka kerja target  

**Masalah Pemuatan Model**  
- Validasi kompatibilitas model ONNX dengan Windows ML  
- Periksa integritas file model dan persyaratan format  
- Verifikasi persyaratan kemampuan perangkat keras untuk model tertentu  
- Debug masalah alokasi memori selama pemuatan model  
- Pastikan pendaftaran penyedia eksekusi untuk akselerasi perangkat keras  

**Pertimbangan Mode Penerapan**  
- **Mode Mandiri**: Didukung sepenuhnya dengan ukuran penerapan yang lebih besar  
- **Mode Bergantung Kerangka Kerja**: Jejak lebih kecil tetapi membutuhkan runtime bersama  
- **Aplikasi Tanpa Paket**: Tidak lagi didukung untuk API Windows AI  
- Gunakan `dotnet run -p:Platform=ARM64 -p:SelfContained=true` untuk penerapan ARM64 mandiri  

**Masalah Kinerja**  
- Profil kinerja aplikasi di berbagai konfigurasi perangkat keras  
- Identifikasi hambatan dalam pipeline pemrosesan AI  
- Optimalkan operasi pra-pemrosesan dan pasca-pemrosesan data  
- Implementasikan pemantauan kinerja dan peringatan  

**Kesulitan Integrasi**  
- Debug masalah integrasi API dengan penanganan kesalahan yang tepat  
- Validasi format data input dan persyaratan pra-pemrosesan  
- Uji kasus tepi dan kondisi kesalahan secara menyeluruh  
- Implementasikan pencatatan yang komprehensif untuk debugging masalah produksi  

### Alat dan Teknik Debugging  

**Integrasi Visual Studio**  
- Gunakan debugger AI Toolkit untuk analisis eksekusi model  
- Implementasikan profil kinerja untuk operasi AI  
- Debug operasi AI asinkron dengan penanganan pengecualian yang tepat  
- Gunakan alat profil memori untuk optimasi  

**Alat Windows AI Foundry**  
- Manfaatkan CLI Foundry Lokal untuk pengujian dan validasi model  
- Gunakan alat pengujian API Windows AI untuk verifikasi integrasi  
- Implementasikan pencatatan khusus untuk pemantauan operasi AI  
- Buat pengujian otomatis untuk keandalan fungsi AI  

## Mempersiapkan Aplikasi Anda untuk Masa Depan  

### Teknologi yang Muncul  

**Perangkat Keras Generasi Berikutnya**  
- Desain aplikasi untuk memanfaatkan kemampuan NPU di masa depan  
- Rencanakan untuk ukuran dan kompleksitas model yang meningkat  
- Implementasikan arsitektur adaptif untuk perangkat keras yang berkembang  
- Pertimbangkan algoritma yang siap kuantum untuk kompatibilitas masa depan  

**Kemampuan AI Lanjutan**  
- Persiapkan integrasi AI multimodal di lebih banyak jenis data  
- Rencanakan kolaborasi AI real-time antara beberapa perangkat  
- Desain untuk kemampuan pembelajaran federasi  
- Pertimbangkan arsitektur kecerdasan hibrid edge-cloud  

### Pembelajaran dan Adaptasi Berkelanjutan  

**Pembaruan Model**  
- Implementasikan mekanisme pembaruan model yang mulus  
- Desain aplikasi untuk beradaptasi dengan kemampuan model yang ditingkatkan  
- Rencanakan kompatibilitas mundur dengan model yang ada  
- Implementasikan pengujian A/B untuk evaluasi kinerja model  

**Evolusi Fitur**  
- Desain arsitektur modular yang mengakomodasi kemampuan AI baru  
- Rencanakan integrasi API Windows AI yang muncul  
- Implementasikan flag fitur untuk peluncuran kemampuan secara bertahap  
- Desain antarmuka pengguna yang beradaptasi dengan fitur AI yang ditingkatkan  

## Kesimpulan  

Pengembangan Windows Edge AI mewakili konvergensi kemampuan AI yang kuat dengan platform Windows yang tangguh, aman, dan skalabel. Dengan menguasai ekosistem Windows AI Foundry, pengembang dapat menciptakan aplikasi cerdas yang memberikan pengalaman pengguna yang luar biasa sambil mempertahankan standar privasi, keamanan, dan kinerja tertinggi.  

Kombinasi API Windows AI, Foundry Lokal, dan Windows ML menyediakan fondasi yang tak tertandingi untuk membangun generasi berikutnya dari aplikasi Windows yang cerdas. Seiring AI terus berkembang, platform Windows memastikan bahwa aplikasi Anda akan berkembang dengan teknologi yang muncul sambil mempertahankan kompatibilitas dan kinerja di seluruh ekosistem perangkat keras Windows yang beragam.  

Apakah Anda sedang membangun aplikasi konsumen, solusi perusahaan, atau alat industri khusus, pengembangan Windows Edge AI memberdayakan Anda untuk menciptakan pengalaman yang cerdas, responsif, dan terintegrasi secara mendalam yang memanfaatkan potensi penuh perangkat Windows modern.  

## Sumber Daya Tambahan  

### Dokumentasi dan Pembelajaran  
- [Dokumentasi Windows AI Foundry](https://learn.microsoft.com/windows/ai/)  
- [Referensi API Windows AI](https://learn.microsoft.com/windows/ai/apis/)  
- [Mulai membangun aplikasi dengan API Windows AI](https://learn.microsoft.com/windows/ai/apis/model-setup)  
- [Panduan Memulai Foundry Lokal](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)  
- [Ikhtisar Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)  
- [Persyaratan Sistem Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)  
- [Pengaturan Lingkungan Pengembangan Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)  

### Repositori Sampel dan Kode  
- [Sampel Windows App SDK - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)  
- [Sampel Windows App SDK - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)  
- [Contoh Inferensi ONNX Runtime](https://github.com/microsoft/onnxruntime-inference-examples)  
- [Repositori Contoh Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Alat Pengembangan
- [AI Toolkit untuk Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [Galeri Pengembang AI](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Contoh Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Alat Konversi Model](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Dukungan Teknis
- [Dokumentasi Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Dokumentasi ONNX Runtime](https://onnxruntime.ai/docs/)
- [Dokumentasi Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Laporkan Masalah - Contoh Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Komunitas dan Dukungan
- [Komunitas Pengembang Windows](https://developer.microsoft.com/en-us/windows/)
- [Blog Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Pelatihan AI Microsoft Learn](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Panduan ini dirancang untuk berkembang seiring dengan ekosistem Windows AI yang terus maju. Pembaruan rutin memastikan keselarasan dengan kemampuan platform terbaru dan praktik terbaik pengembangan.*

[08. Praktik Langsung dengan Microsoft Foundry Local - Toolkit Pengembang Lengkap](../Module08/README.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.