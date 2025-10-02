<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "65a22ed38b95f334dd8a893bf2c55806",
  "translation_date": "2025-10-02T13:40:47+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "id"
}
-->
# Panduan Pengembangan Edge AI dengan AI Toolkit untuk Visual Studio Code

## Pendahuluan

Selamat datang di panduan lengkap untuk menggunakan AI Toolkit di Visual Studio Code dalam pengembangan Edge AI. Seiring dengan pergeseran kecerdasan buatan dari komputasi cloud terpusat ke perangkat edge yang terdistribusi, pengembang membutuhkan alat yang kuat dan terintegrasi untuk menangani tantangan unik dalam penerapan edge—mulai dari keterbatasan sumber daya hingga kebutuhan operasi offline.

AI Toolkit untuk Visual Studio Code menjembatani kesenjangan ini dengan menyediakan lingkungan pengembangan lengkap yang dirancang khusus untuk membangun, menguji, dan mengoptimalkan aplikasi AI yang berjalan efisien di perangkat edge. Baik Anda mengembangkan untuk sensor IoT, perangkat seluler, sistem tertanam, atau server edge, toolkit ini menyederhanakan seluruh alur kerja pengembangan Anda dalam lingkungan VS Code yang sudah familiar.

Panduan ini akan membawa Anda melalui konsep-konsep penting, alat-alat, dan praktik terbaik untuk memanfaatkan AI Toolkit dalam proyek Edge AI Anda, mulai dari pemilihan model awal hingga penerapan produksi.

## Ikhtisar

AI Toolkit untuk Visual Studio Code adalah ekstensi yang kuat yang menyederhanakan pengembangan agen dan pembuatan aplikasi AI. Toolkit ini menyediakan kemampuan komprehensif untuk menjelajahi, mengevaluasi, dan menerapkan model AI dari berbagai penyedia—termasuk Anthropic, OpenAI, GitHub, Google—serta mendukung eksekusi model lokal menggunakan ONNX dan Ollama.

Yang membedakan AI Toolkit adalah pendekatannya yang menyeluruh terhadap seluruh siklus pengembangan AI. Berbeda dengan alat pengembangan AI tradisional yang hanya berfokus pada aspek tertentu, AI Toolkit menyediakan lingkungan terintegrasi yang mencakup penemuan model, eksperimen, pengembangan agen, evaluasi, dan penerapan—semuanya dalam lingkungan VS Code yang sudah dikenal.

Platform ini dirancang khusus untuk prototipe cepat dan penerapan produksi, dengan fitur seperti pembuatan prompt, starter cepat, integrasi alat MCP (Model Context Protocol) yang mulus, dan kemampuan evaluasi yang luas. Untuk pengembangan Edge AI, ini berarti Anda dapat dengan efisien mengembangkan, menguji, dan mengoptimalkan aplikasi AI untuk skenario penerapan edge sambil mempertahankan alur kerja pengembangan penuh dalam VS Code.

## Tujuan Pembelajaran

Pada akhir panduan ini, Anda akan dapat:

### Kompetensi Inti
- **Menginstal dan mengonfigurasi** AI Toolkit untuk Visual Studio Code untuk alur kerja pengembangan Edge AI
- **Menavigasi dan memanfaatkan** antarmuka AI Toolkit, termasuk Model Catalog, Playground, dan Agent Builder
- **Memilih dan mengevaluasi** model AI yang cocok untuk penerapan edge berdasarkan kinerja dan keterbatasan sumber daya
- **Mengonversi dan mengoptimalkan** model menggunakan format ONNX dan teknik kuantisasi untuk perangkat edge

### Keterampilan Pengembangan Edge AI
- **Merancang dan mengimplementasikan** aplikasi Edge AI menggunakan lingkungan pengembangan terintegrasi
- **Melakukan pengujian model** dalam kondisi mirip edge menggunakan inferensi lokal dan pemantauan sumber daya
- **Membuat dan menyesuaikan** agen AI yang dioptimalkan untuk skenario penerapan edge
- **Mengevaluasi kinerja model** menggunakan metrik yang relevan untuk komputasi edge (latensi, penggunaan memori, akurasi)

### Optimasi dan Penerapan
- **Menerapkan teknik kuantisasi dan pruning** untuk mengurangi ukuran model sambil mempertahankan kinerja yang dapat diterima
- **Mengoptimalkan model** untuk platform perangkat keras edge tertentu termasuk akselerasi CPU, GPU, dan NPU
- **Menerapkan praktik terbaik** untuk pengembangan Edge AI termasuk manajemen sumber daya dan strategi cadangan
- **Menyiapkan model dan aplikasi** untuk penerapan produksi di perangkat edge

### Konsep Edge AI Lanjutan
- **Mengintegrasikan dengan kerangka kerja Edge AI** termasuk ONNX Runtime, Windows ML, dan TensorFlow Lite
- **Mengimplementasikan arsitektur multi-model** dan skenario pembelajaran federasi untuk lingkungan edge
- **Memecahkan masalah umum Edge AI** termasuk keterbatasan memori, kecepatan inferensi, dan kompatibilitas perangkat keras
- **Merancang strategi pemantauan dan logging** untuk aplikasi Edge AI dalam produksi

### Aplikasi Praktis
- **Membangun solusi Edge AI end-to-end** dari pemilihan model hingga penerapan
- **Menunjukkan kemahiran** dalam alur kerja pengembangan dan teknik optimasi khusus edge
- **Menerapkan konsep yang dipelajari** ke kasus penggunaan Edge AI dunia nyata termasuk IoT, seluler, dan aplikasi tertanam
- **Mengevaluasi dan membandingkan** berbagai strategi penerapan Edge AI dan komprominya

## Fitur Utama untuk Pengembangan Edge AI

### 1. Model Catalog dan Penemuan
- **Dukungan Multi-Penyedia**: Jelajahi dan akses model AI dari Anthropic, OpenAI, GitHub, Google, dan penyedia lainnya
- **Integrasi Model Lokal**: Penemuan model ONNX dan Ollama yang disederhanakan untuk penerapan edge
- **Model GitHub**: Integrasi langsung dengan hosting model GitHub untuk akses yang lebih mudah
- **Perbandingan Model**: Bandingkan model secara berdampingan untuk menemukan keseimbangan optimal untuk keterbatasan perangkat edge

### 2. Playground Interaktif
- **Lingkungan Pengujian Interaktif**: Eksperimen cepat dengan kemampuan model dalam lingkungan yang terkendali
- **Dukungan Multi-modal**: Uji dengan gambar, teks, dan input lainnya yang umum dalam skenario edge
- **Eksperimen Real-time**: Umpan balik langsung tentang respons dan kinerja model
- **Optimasi Parameter**: Sesuaikan parameter model untuk kebutuhan penerapan edge

### 3. Prompt (Agent) Builder
- **Generasi Bahasa Alami**: Buat prompt awal menggunakan deskripsi bahasa alami
- **Penyempurnaan Iteratif**: Tingkatkan prompt berdasarkan respons dan kinerja model
- **Dekonstruksi Tugas**: Pecah tugas kompleks dengan chaining prompt dan output terstruktur
- **Dukungan Variabel**: Gunakan variabel dalam prompt untuk perilaku agen yang dinamis
- **Generasi Kode Produksi**: Hasilkan kode siap produksi untuk pengembangan aplikasi yang cepat

### 4. Bulk Run dan Evaluasi
- **Pengujian Multi-Model**: Jalankan beberapa prompt di berbagai model yang dipilih secara bersamaan
- **Pengujian Skala Efisien**: Uji berbagai input dan konfigurasi dengan efisien
- **Kasus Uji Kustom**: Jalankan agen dengan kasus uji untuk memvalidasi fungsionalitas
- **Perbandingan Kinerja**: Bandingkan hasil di berbagai model dan konfigurasi

### 5. Evaluasi Model dengan Dataset
- **Metrik Standar**: Uji model AI menggunakan evaluator bawaan (F1 score, relevansi, kesamaan, koherensi)
- **Evaluator Kustom**: Buat metrik evaluasi Anda sendiri untuk kasus penggunaan tertentu
- **Integrasi Dataset**: Uji model terhadap dataset yang komprehensif
- **Pengukuran Kinerja**: Kuantifikasi kinerja model untuk keputusan penerapan edge

### 6. Kemampuan Fine-tuning
- **Kustomisasi Model**: Sesuaikan model untuk kasus penggunaan dan domain tertentu
- **Adaptasi Khusus**: Sesuaikan model untuk domain dan kebutuhan khusus
- **Optimasi Edge**: Fine-tuning model khusus untuk keterbatasan penerapan edge
- **Pelatihan Domain-Specific**: Buat model yang disesuaikan untuk kasus penggunaan edge tertentu

### 7. Integrasi Alat MCP
- **Konektivitas Alat Eksternal**: Hubungkan agen ke alat eksternal melalui server Model Context Protocol
- **Tindakan Dunia Nyata**: Aktifkan agen untuk melakukan query database, mengakses API, atau menjalankan logika kustom
- **Server MCP yang Ada**: Gunakan alat dari protokol command (stdio) atau HTTP (server-sent event)
- **Pengembangan MCP Kustom**: Bangun dan buat kerangka server MCP baru dengan pengujian di Agent Builder

### 8. Pengembangan dan Pengujian Agen
- **Dukungan Pemanggilan Fungsi**: Aktifkan agen untuk memanggil fungsi eksternal secara dinamis
- **Pengujian Integrasi Real-time**: Uji integrasi dengan run real-time dan penggunaan alat
- **Versi Agen**: Kontrol versi untuk agen dengan kemampuan perbandingan hasil evaluasi
- **Debugging dan Tracing**: Kemampuan tracing dan debugging lokal untuk pengembangan agen

## Alur Kerja Pengembangan Edge AI

### Fase 1: Penemuan dan Pemilihan Model
1. **Jelajahi Model Catalog**: Gunakan katalog model untuk menemukan model yang cocok untuk penerapan edge
2. **Bandingkan Kinerja**: Evaluasi model berdasarkan ukuran, akurasi, dan kecepatan inferensi
3. **Uji Secara Lokal**: Gunakan model Ollama atau ONNX untuk pengujian lokal sebelum penerapan edge
4. **Tentukan Kebutuhan Sumber Daya**: Tentukan kebutuhan memori dan komputasi untuk perangkat edge target

### Fase 2: Optimasi Model
1. **Konversi ke ONNX**: Konversi model yang dipilih ke format ONNX untuk kompatibilitas edge
2. **Terapkan Kuantisasi**: Kurangi ukuran model melalui kuantisasi INT8 atau INT4
3. **Optimasi Perangkat Keras**: Optimalkan untuk perangkat keras edge target (ARM, x86, akselerator khusus)
4. **Validasi Kinerja**: Validasi model yang dioptimalkan tetap mempertahankan akurasi yang dapat diterima

### Fase 3: Pengembangan Aplikasi
1. **Desain Agen**: Gunakan Agent Builder untuk membuat agen AI yang dioptimalkan untuk edge
2. **Rekayasa Prompt**: Kembangkan prompt yang bekerja efektif dengan model edge yang lebih kecil
3. **Pengujian Integrasi**: Uji agen dalam kondisi simulasi edge
4. **Generasi Kode**: Hasilkan kode produksi yang dioptimalkan untuk penerapan edge

### Fase 4: Evaluasi dan Pengujian
1. **Evaluasi Batch**: Uji beberapa konfigurasi untuk menemukan pengaturan edge yang optimal
2. **Profiling Kinerja**: Analisis kecepatan inferensi, penggunaan memori, dan akurasi
3. **Simulasi Edge**: Uji dalam kondisi yang mirip dengan lingkungan penerapan edge target
4. **Pengujian Beban**: Evaluasi kinerja di bawah berbagai kondisi beban

### Fase 5: Persiapan Penerapan
1. **Optimasi Akhir**: Terapkan optimasi akhir berdasarkan hasil pengujian
2. **Pengemasan Penerapan**: Paketkan model dan kode untuk penerapan edge
3. **Dokumentasi**: Dokumentasikan kebutuhan dan konfigurasi penerapan
4. **Persiapan Pemantauan**: Siapkan pemantauan dan logging untuk penerapan edge

## Target Audiens untuk Pengembangan Edge AI

### Pengembang Edge AI
- Pengembang aplikasi yang membangun perangkat edge dan solusi IoT berbasis AI
- Pengembang sistem tertanam yang mengintegrasikan kemampuan AI ke perangkat dengan keterbatasan sumber daya
- Pengembang seluler yang membuat aplikasi AI di perangkat

### Insinyur Edge AI
- Insinyur AI yang mengoptimalkan model untuk penerapan edge dan mengelola pipeline inferensi
- Insinyur DevOps yang menerapkan dan mengelola model AI di infrastruktur edge yang terdistribusi
- Insinyur kinerja yang mengoptimalkan beban kerja AI untuk keterbatasan perangkat keras edge

### Peneliti dan Pendidik
- Peneliti AI yang mengembangkan model dan algoritma efisien untuk komputasi edge
- Pendidik yang mengajarkan konsep Edge AI dan mendemonstrasikan teknik optimasi
- Mahasiswa yang mempelajari tantangan dan solusi dalam penerapan Edge AI

## Kasus Penggunaan Edge AI

### Perangkat IoT Cerdas
- **Pengenalan Gambar Real-time**: Terapkan model visi komputer pada kamera dan sensor IoT
- **Pemrosesan Suara**: Implementasikan pengenalan suara dan pemrosesan bahasa alami pada speaker pintar
- **Pemeliharaan Prediktif**: Jalankan model deteksi anomali pada perangkat edge industri
- **Pemantauan Lingkungan**: Terapkan model analisis data sensor untuk aplikasi lingkungan

### Aplikasi Seluler dan Tertanam
- **Terjemahan di Perangkat**: Implementasikan model terjemahan bahasa yang bekerja offline
- **Augmented Reality**: Terapkan pengenalan objek real-time dan pelacakan untuk aplikasi AR
- **Pemantauan Kesehatan**: Jalankan model analisis kesehatan pada perangkat wearable dan peralatan medis
- **Sistem Otonom**: Implementasikan model pengambilan keputusan untuk drone, robot, dan kendaraan

### Infrastruktur Komputasi Edge
- **Pusat Data Edge**: Terapkan model AI di pusat data edge untuk aplikasi latensi rendah
- **Integrasi CDN**: Integrasikan kemampuan pemrosesan AI ke dalam jaringan pengiriman konten
- **Edge 5G**: Manfaatkan komputasi edge 5G untuk aplikasi berbasis AI
- **Fog Computing**: Implementasikan pemrosesan AI di lingkungan fog computing

## Instalasi dan Pengaturan

### Instalasi Ekstensi
Instal ekstensi AI Toolkit langsung dari Visual Studio Code Marketplace:

**ID Ekstensi**: `ms-windows-ai-studio.windows-ai-studio`

**Metode Instalasi**:
1. **VS Code Marketplace**: Cari "AI Toolkit" di tampilan Extensions
2. **Command Line**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Instalasi Langsung**: Unduh dari [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Prasyarat untuk Pengembangan Edge AI
- **Visual Studio Code**: Versi terbaru direkomendasikan
- **Lingkungan Python**: Python 3.8+ dengan pustaka AI yang diperlukan
- **ONNX Runtime** (Opsional): Untuk inferensi model ONNX
- **Ollama** (Opsional): Untuk penyajian model lokal
- **Alat Akselerasi Perangkat Keras**: CUDA, OpenVINO, atau akselerator khusus platform

### Konfigurasi Awal
1. **Aktivasi Ekstensi**: Buka VS Code dan verifikasi AI Toolkit muncul di Activity Bar
2. **Pengaturan Penyedia Model**: Konfigurasikan akses ke GitHub, OpenAI, Anthropic, atau penyedia model lainnya
3. **Lingkungan Lokal**: Siapkan lingkungan Python dan instal paket yang diperlukan
4. **Akselerasi Perangkat Keras**: Konfigurasikan akselerasi GPU/NPU jika tersedia
5. **Integrasi MCP**: Siapkan server Model Context Protocol jika diperlukan

### Daftar Periksa Pengaturan Awal
- [ ] Ekstensi AI Toolkit terinstal dan diaktifkan
- [ ] Katalog model dapat diakses dan model dapat ditemukan
- [ ] Playground berfungsi untuk pengujian model
- [ ] Agent Builder dapat diakses untuk pengembangan prompt
- [ ] Lingkungan pengembangan lokal dikonfigurasi
- [ ] Akselerasi perangkat keras (jika tersedia) dikonfigurasi dengan benar

## Memulai dengan AI Toolkit

### Panduan Memulai Cepat

Kami merekomendasikan memulai dengan model yang di-host oleh GitHub untuk pengalaman yang paling lancar:

1. **Instalasi**: Ikuti [panduan instalasi](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) untuk menyiapkan AI Toolkit di perangkat Anda
2. **Penemuan Model**: Dari tampilan pohon ekstensi, pilih **CATALOG > Models** untuk menjelajahi model yang tersedia
3. **Model GitHub**: Mulailah dengan model yang di-host oleh GitHub untuk integrasi yang optimal
4. **Pengujian Playground**: Dari kartu model mana pun, pilih **Try in Playground** untuk mulai bereksperimen dengan kemampuan model

### Langkah-Langkah Pengembangan Edge AI

#### Langkah 1: Penjelajahan dan Pemilihan Model
1. Buka tampilan AI Toolkit di Activity Bar VS Code
2. Jelajahi Model Catalog untuk model yang cocok untuk penerapan edge
3. Filter berdasarkan penyedia (GitHub, ONNX, Ollama) sesuai kebutuhan edge Anda
4. Gunakan **Try in Playground** untuk segera menguji kemampuan model

#### Langkah 2: Pengembangan Agen
1. Gunakan **Prompt (Agent) Builder** untuk membuat agen AI yang dioptimalkan untuk edge
2. Buat prompt awal menggunakan deskripsi bahasa alami  
3. Iterasi dan perbaiki prompt berdasarkan respons model  
4. Integrasikan alat MCP untuk meningkatkan kemampuan agen  

#### Langkah 3: Pengujian dan Evaluasi  
1. Gunakan **Bulk Run** untuk menguji beberapa prompt pada model yang dipilih  
2. Jalankan agen dengan kasus uji untuk memvalidasi fungsionalitas  
3. Evaluasi akurasi dan kinerja menggunakan metrik bawaan atau kustom  
4. Bandingkan berbagai model dan konfigurasi  

#### Langkah 4: Penyesuaian dan Optimasi  
1. Sesuaikan model untuk kasus penggunaan spesifik  
2. Terapkan penyesuaian khusus domain  
3. Optimalkan untuk kendala penerapan di edge  
4. Versi dan bandingkan konfigurasi agen yang berbeda  

#### Langkah 5: Persiapan Penerapan  
1. Hasilkan kode siap produksi menggunakan Agent Builder  
2. Siapkan koneksi server MCP untuk penggunaan produksi  
3. Persiapkan paket penerapan untuk perangkat edge  
4. Konfigurasikan metrik pemantauan dan evaluasi  

## Praktik Terbaik untuk Pengembangan AI Edge  

### Pemilihan Model  
- **Kendala Ukuran**: Pilih model yang sesuai dengan batas memori perangkat target  
- **Kecepatan Inferensi**: Prioritaskan model dengan waktu inferensi cepat untuk aplikasi real-time  
- **Kompromi Akurasi**: Seimbangkan akurasi model dengan kendala sumber daya  
- **Kompatibilitas Format**: Pilih format seperti ONNX atau yang dioptimalkan untuk perangkat keras edge  

### Teknik Optimasi  
- **Kuantisasi**: Gunakan kuantisasi INT8 atau INT4 untuk mengurangi ukuran model dan meningkatkan kecepatan  
- **Pruning**: Hapus parameter model yang tidak diperlukan untuk mengurangi kebutuhan komputasi  
- **Distilasi Pengetahuan**: Buat model yang lebih kecil dengan tetap mempertahankan kinerja model yang lebih besar  
- **Akselerasi Perangkat Keras**: Manfaatkan NPU, GPU, atau akselerator khusus jika tersedia  

### Alur Kerja Pengembangan  
- **Pengujian Iteratif**: Uji secara berkala dalam kondisi mirip edge selama pengembangan  
- **Pemantauan Kinerja**: Pantau penggunaan sumber daya dan kecepatan inferensi secara terus-menerus  
- **Kontrol Versi**: Lacak versi model dan pengaturan optimasi  
- **Dokumentasi**: Dokumentasikan semua keputusan optimasi dan kompromi kinerja  

### Pertimbangan Penerapan  
- **Pemantauan Sumber Daya**: Pantau penggunaan memori, CPU, dan daya dalam produksi  
- **Strategi Cadangan**: Implementasikan mekanisme cadangan untuk kegagalan model  
- **Mekanisme Pembaruan**: Rencanakan pembaruan model dan manajemen versi  
- **Keamanan**: Terapkan langkah-langkah keamanan yang sesuai untuk aplikasi AI edge  

## Integrasi dengan Kerangka Kerja AI Edge  

### ONNX Runtime  
- **Penerapan Lintas Platform**: Terapkan model ONNX di berbagai platform edge  
- **Optimasi Perangkat Keras**: Manfaatkan optimasi spesifik perangkat keras dari ONNX Runtime  
- **Dukungan Mobile**: Gunakan ONNX Runtime Mobile untuk aplikasi smartphone dan tablet  
- **Integrasi IoT**: Terapkan pada perangkat IoT menggunakan distribusi ringan ONNX Runtime  

### Windows ML  
- **Perangkat Windows**: Optimalkan untuk perangkat edge berbasis Windows dan PC  
- **Akselerasi NPU**: Manfaatkan Neural Processing Units pada perangkat Windows  
- **DirectML**: Gunakan DirectML untuk akselerasi GPU di platform Windows  
- **Integrasi UWP**: Integrasikan dengan aplikasi Universal Windows Platform  

### TensorFlow Lite  
- **Optimasi Mobile**: Terapkan model TensorFlow Lite pada perangkat mobile dan embedded  
- **Delegasi Perangkat Keras**: Gunakan delegasi perangkat keras khusus untuk akselerasi  
- **Mikrokontroler**: Terapkan pada mikrokontroler menggunakan TensorFlow Lite Micro  
- **Dukungan Lintas Platform**: Terapkan di Android, iOS, dan sistem Linux embedded  

### Azure IoT Edge  
- **Hybrid Cloud-Edge**: Gabungkan pelatihan cloud dengan inferensi edge  
- **Penerapan Modul**: Terapkan model AI sebagai modul IoT Edge  
- **Manajemen Perangkat**: Kelola perangkat edge dan pembaruan model secara remote  
- **Telemetri**: Kumpulkan data kinerja dan metrik model dari penerapan edge  

## Skenario AI Edge Lanjutan  

### Penerapan Multi-Model  
- **Ensemble Model**: Terapkan beberapa model untuk meningkatkan akurasi atau redundansi  
- **Pengujian A/B**: Uji berbagai model secara bersamaan pada perangkat edge  
- **Seleksi Dinamis**: Pilih model berdasarkan kondisi perangkat saat ini  
- **Berbagi Sumber Daya**: Optimalkan penggunaan sumber daya di antara beberapa model yang diterapkan  

### Federated Learning  
- **Pelatihan Terdistribusi**: Latih model di beberapa perangkat edge  
- **Preservasi Privasi**: Simpan data pelatihan secara lokal sambil berbagi peningkatan model  
- **Pembelajaran Kolaboratif**: Biarkan perangkat belajar dari pengalaman kolektif  
- **Koordinasi Edge-Cloud**: Koordinasikan pembelajaran antara perangkat edge dan infrastruktur cloud  

### Pemrosesan Real-time  
- **Pemrosesan Stream**: Proses data stream secara kontinu pada perangkat edge  
- **Inferensi Latensi Rendah**: Optimalkan untuk latensi inferensi minimal  
- **Pemrosesan Batch**: Proses batch data secara efisien pada perangkat edge  
- **Pemrosesan Adaptif**: Sesuaikan pemrosesan berdasarkan kemampuan perangkat saat ini  

## Pemecahan Masalah Pengembangan AI Edge  

### Masalah Umum  
- **Kendala Memori**: Model terlalu besar untuk memori perangkat target  
- **Kecepatan Inferensi**: Inferensi model terlalu lambat untuk kebutuhan real-time  
- **Degradasi Akurasi**: Optimasi mengurangi akurasi model secara tidak dapat diterima  
- **Kompatibilitas Perangkat Keras**: Model tidak kompatibel dengan perangkat keras target  

### Strategi Debugging  
- **Profiling Kinerja**: Gunakan fitur tracing AI Toolkit untuk mengidentifikasi hambatan  
- **Pemantauan Sumber Daya**: Pantau penggunaan memori dan CPU selama pengembangan  
- **Pengujian Inkremental**: Uji optimasi secara bertahap untuk mengisolasi masalah  
- **Simulasi Perangkat Keras**: Gunakan alat pengembangan untuk mensimulasikan perangkat keras target  

### Solusi Optimasi  
- **Kuantisasi Lebih Lanjut**: Terapkan teknik kuantisasi yang lebih agresif  
- **Arsitektur Model**: Pertimbangkan arsitektur model yang dioptimalkan untuk edge  
- **Optimasi Pra-pemrosesan**: Optimalkan pra-pemrosesan data untuk kendala edge  
- **Optimasi Inferensi**: Gunakan optimasi inferensi spesifik perangkat keras  

## Sumber Daya dan Langkah Selanjutnya  

### Dokumentasi Resmi  
- [Dokumentasi Pengembang AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Panduan Instalasi dan Pengaturan](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Dokumentasi Aplikasi Cerdas VS Code](https://code.visualstudio.com/docs/intelligentapps)  
- [Dokumentasi Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Komunitas dan Dukungan  
- [Repositori GitHub AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [Masalah GitHub dan Permintaan Fitur](https://aka.ms/AIToolkit/feedback)  
- [Komunitas Discord Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Marketplace Ekstensi VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Sumber Daya Teknis  
- [Dokumentasi ONNX Runtime](https://onnxruntime.ai/)  
- [Dokumentasi Ollama](https://ollama.ai/)  
- [Dokumentasi Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Dokumentasi Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Jalur Pembelajaran  
- [Kursus Dasar AI Edge](../Module01/README.md)  
- [Panduan Model Bahasa Kecil](../Module02/README.md)  
- [Strategi Penerapan Edge](../Module03/README.md)  
- [Pengembangan AI Edge Windows](./windowdeveloper.md)  

### Sumber Daya Tambahan  
- **Statistik Repositori**: 1.8k+ bintang, 150+ fork, 18+ kontributor  
- **Lisensi**: Lisensi MIT  
- **Keamanan**: Kebijakan keamanan Microsoft berlaku  
- **Telemetri**: Menghormati pengaturan telemetri VS Code  

## Kesimpulan  

AI Toolkit untuk Visual Studio Code merupakan platform komprehensif untuk pengembangan AI modern, menyediakan kemampuan pengembangan agen yang efisien yang sangat berharga untuk aplikasi AI Edge. Dengan katalog model yang luas yang mendukung penyedia seperti Anthropic, OpenAI, GitHub, dan Google, ditambah eksekusi lokal melalui ONNX dan Ollama, toolkit ini menawarkan fleksibilitas yang diperlukan untuk berbagai skenario penerapan edge.

Kekuatan toolkit ini terletak pada pendekatan terintegrasi—dari penemuan dan eksperimen model di Playground hingga pengembangan agen yang canggih dengan Prompt Builder, kemampuan evaluasi yang komprehensif, dan integrasi alat MCP yang mulus. Bagi pengembang AI Edge, ini berarti prototipe dan pengujian agen AI yang cepat sebelum penerapan edge, dengan kemampuan untuk iterasi cepat dan optimasi untuk lingkungan dengan sumber daya terbatas.

Keuntungan utama untuk pengembangan AI Edge meliputi:  
- **Eksperimen Cepat**: Uji model dan agen dengan cepat sebelum berkomitmen pada penerapan edge  
- **Fleksibilitas Multi-Penyedia**: Akses model dari berbagai sumber untuk menemukan solusi edge yang optimal  
- **Pengembangan Lokal**: Uji dengan ONNX dan Ollama untuk pengembangan offline dan yang menjaga privasi  
- **Kesiapan Produksi**: Hasilkan kode siap produksi dan integrasikan dengan alat eksternal melalui MCP  
- **Evaluasi Komprehensif**: Gunakan metrik bawaan dan kustom untuk memvalidasi kinerja AI edge  

Seiring AI terus bergerak menuju skenario penerapan edge, AI Toolkit untuk VS Code menyediakan lingkungan pengembangan dan alur kerja yang diperlukan untuk membangun, menguji, dan mengoptimalkan aplikasi cerdas untuk lingkungan dengan sumber daya terbatas. Baik Anda mengembangkan solusi IoT, aplikasi AI mobile, atau sistem kecerdasan tertanam, fitur lengkap toolkit ini dan alur kerja terintegrasi mendukung seluruh siklus pengembangan AI edge.

Dengan pengembangan yang berkelanjutan dan komunitas yang aktif (1.8k+ bintang GitHub), AI Toolkit tetap berada di garis depan alat pengembangan AI, terus berkembang untuk memenuhi kebutuhan pengembang AI modern yang membangun untuk skenario penerapan edge.

[Next Foundry Local](./foundrylocal.md)  

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.