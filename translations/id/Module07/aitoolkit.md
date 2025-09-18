<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-18T15:06:10+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "id"
}
-->
# Panduan Pengembangan Edge AI dengan AI Toolkit untuk Visual Studio Code

## Pendahuluan

Selamat datang di panduan lengkap untuk menggunakan AI Toolkit pada Visual Studio Code dalam pengembangan Edge AI. Seiring dengan pergeseran kecerdasan buatan dari komputasi cloud terpusat ke perangkat edge yang terdistribusi, pengembang membutuhkan alat yang kuat dan terintegrasi untuk menangani tantangan unik dalam penerapan edge - mulai dari keterbatasan sumber daya hingga kebutuhan operasi offline.

AI Toolkit untuk Visual Studio Code menjembatani kesenjangan ini dengan menyediakan lingkungan pengembangan lengkap yang dirancang khusus untuk membangun, menguji, dan mengoptimalkan aplikasi AI yang berjalan secara efisien pada perangkat edge. Baik Anda mengembangkan untuk sensor IoT, perangkat seluler, sistem tertanam, atau server edge, toolkit ini menyederhanakan seluruh alur kerja pengembangan Anda dalam lingkungan VS Code yang sudah familiar.

Panduan ini akan membawa Anda melalui konsep-konsep penting, alat-alat, dan praktik terbaik untuk memanfaatkan AI Toolkit dalam proyek Edge AI Anda, mulai dari pemilihan model awal hingga penerapan produksi.

## Ikhtisar

AI Toolkit menyediakan lingkungan pengembangan terintegrasi untuk seluruh siklus hidup aplikasi Edge AI dalam VS Code. Toolkit ini menawarkan integrasi yang mulus dengan model AI populer dari penyedia seperti OpenAI, Anthropic, Google, dan GitHub, sambil mendukung penerapan model lokal melalui ONNX dan Ollama - kemampuan penting untuk aplikasi Edge AI yang membutuhkan inferensi di perangkat.

Yang membedakan AI Toolkit dalam pengembangan Edge AI adalah fokusnya pada seluruh pipeline penerapan edge. Berbeda dengan alat pengembangan AI tradisional yang terutama menargetkan penerapan cloud, AI Toolkit mencakup fitur khusus untuk optimasi model, pengujian dengan keterbatasan sumber daya, dan evaluasi kinerja spesifik edge. Toolkit ini memahami bahwa pengembangan Edge AI membutuhkan pertimbangan yang berbeda - ukuran model yang lebih kecil, waktu inferensi yang lebih cepat, kemampuan offline, dan optimasi spesifik perangkat keras.

Platform ini mendukung berbagai skenario penerapan, mulai dari inferensi sederhana di perangkat hingga arsitektur edge multi-model yang kompleks. Toolkit ini menyediakan alat untuk konversi model, kuantisasi, dan optimasi yang penting untuk penerapan edge yang sukses, sambil mempertahankan produktivitas pengembang yang dikenal dari VS Code.

## Tujuan Pembelajaran

Pada akhir panduan ini, Anda akan mampu:

### Kompetensi Inti
- **Menginstal dan mengonfigurasi** AI Toolkit untuk alur kerja pengembangan Edge AI
- **Menavigasi dan menggunakan** antarmuka AI Toolkit, termasuk Model Catalog, Playground, dan Agent Builder
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
- **Mempersiapkan model dan aplikasi** untuk penerapan produksi pada perangkat edge

### Konsep Edge AI Lanjutan
- **Mengintegrasikan dengan kerangka kerja Edge AI** termasuk ONNX Runtime, Windows ML, dan TensorFlow Lite
- **Mengimplementasikan arsitektur multi-model** dan skenario pembelajaran federasi untuk lingkungan edge
- **Memecahkan masalah umum Edge AI** termasuk keterbatasan memori, kecepatan inferensi, dan kompatibilitas perangkat keras
- **Merancang strategi pemantauan dan pencatatan** untuk aplikasi Edge AI dalam produksi

### Aplikasi Praktis
- **Membangun solusi Edge AI end-to-end** dari pemilihan model hingga penerapan
- **Menunjukkan kemahiran** dalam alur kerja pengembangan dan teknik optimasi spesifik edge
- **Menerapkan konsep yang dipelajari** pada kasus penggunaan Edge AI dunia nyata termasuk IoT, seluler, dan aplikasi tertanam
- **Mengevaluasi dan membandingkan** berbagai strategi penerapan Edge AI dan komprominya

## Fitur Utama untuk Pengembangan Edge AI

### 1. Katalog dan Penemuan Model
- **Dukungan Model Lokal**: Temukan dan akses model AI yang dioptimalkan khusus untuk penerapan edge
- **Integrasi ONNX**: Akses model dalam format ONNX untuk inferensi edge yang efisien
- **Dukungan Ollama**: Manfaatkan model yang berjalan secara lokal melalui Ollama untuk privasi dan operasi offline
- **Perbandingan Model**: Bandingkan model secara berdampingan untuk menemukan keseimbangan optimal antara kinerja dan konsumsi sumber daya untuk perangkat edge

### 2. Playground Interaktif
- **Lingkungan Pengujian Lokal**: Uji model secara lokal sebelum penerapan edge
- **Eksperimen Multi-modal**: Uji dengan gambar, teks, dan input lain yang umum dalam skenario edge
- **Penyetelan Parameter**: Bereksperimen dengan berbagai parameter model untuk mengoptimalkan keterbatasan edge
- **Pemantauan Kinerja Real-time**: Amati kecepatan inferensi dan penggunaan sumber daya selama pengembangan

### 3. Agent Builder untuk Aplikasi Edge
- **Prompt Engineering**: Buat prompt yang dioptimalkan untuk bekerja secara efisien dengan model edge yang lebih kecil
- **Integrasi Alat MCP**: Integrasikan alat Model Context Protocol untuk kemampuan agen edge yang lebih baik
- **Pembuatan Kode**: Hasilkan kode siap produksi yang dioptimalkan untuk skenario penerapan edge
- **Output Terstruktur**: Rancang agen yang memberikan respons terstruktur yang konsisten untuk aplikasi edge

### 4. Evaluasi dan Pengujian Model
- **Metrik Kinerja**: Evaluasi model menggunakan metrik yang relevan untuk penerapan edge (latensi, penggunaan memori, akurasi)
- **Pengujian Batch**: Uji beberapa konfigurasi model secara bersamaan untuk menemukan pengaturan edge yang optimal
- **Evaluasi Kustom**: Buat kriteria evaluasi khusus untuk kasus penggunaan Edge AI
- **Profil Sumber Daya**: Analisis kebutuhan memori dan komputasi untuk perencanaan penerapan edge

### 5. Konversi dan Optimasi Model
- **Konversi ONNX**: Konversi model dari berbagai format ke ONNX untuk kompatibilitas edge
- **Kuantisasi**: Kurangi ukuran model dan tingkatkan kecepatan inferensi melalui teknik kuantisasi
- **Optimasi Perangkat Keras**: Optimalkan model untuk perangkat keras edge tertentu (CPU, GPU, NPU)
- **Transformasi Format**: Transformasi model dari Hugging Face dan sumber lain untuk penerapan edge

### 6. Fine-tuning untuk Skenario Edge
- **Adaptasi Domain**: Sesuaikan model untuk kasus penggunaan dan lingkungan edge tertentu
- **Pelatihan Lokal**: Latih model secara lokal dengan dukungan GPU untuk kebutuhan spesifik edge
- **Integrasi Azure**: Manfaatkan Azure Container Apps untuk fine-tuning berbasis cloud sebelum penerapan edge
- **Transfer Learning**: Adaptasi model yang sudah dilatih untuk tugas dan keterbatasan spesifik edge

### 7. Pemantauan Kinerja dan Tracing
- **Analisis Kinerja Edge**: Pantau kinerja model dalam kondisi mirip edge
- **Pengumpulan Trace**: Kumpulkan data kinerja yang terperinci untuk optimasi
- **Identifikasi Bottleneck**: Identifikasi masalah kinerja sebelum penerapan ke perangkat edge
- **Pelacakan Penggunaan Sumber Daya**: Pantau memori, CPU, dan waktu inferensi untuk optimasi edge

## Alur Kerja Pengembangan Edge AI

### Fase 1: Penemuan dan Pemilihan Model
1. **Jelajahi Katalog Model**: Gunakan katalog model untuk menemukan model yang cocok untuk penerapan edge
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
2. **Prompt Engineering**: Kembangkan prompt yang bekerja efektif dengan model edge yang lebih kecil
3. **Pengujian Integrasi**: Uji agen dalam kondisi edge yang disimulasikan
4. **Pembuatan Kode**: Hasilkan kode produksi yang dioptimalkan untuk penerapan edge

### Fase 4: Evaluasi dan Pengujian
1. **Evaluasi Batch**: Uji beberapa konfigurasi untuk menemukan pengaturan edge yang optimal
2. **Profil Kinerja**: Analisis kecepatan inferensi, penggunaan memori, dan akurasi
3. **Simulasi Edge**: Uji dalam kondisi yang mirip dengan lingkungan penerapan edge target
4. **Pengujian Stres**: Evaluasi kinerja di bawah berbagai kondisi beban

### Fase 5: Persiapan Penerapan
1. **Optimasi Akhir**: Terapkan optimasi akhir berdasarkan hasil pengujian
2. **Pengemasan Penerapan**: Paketkan model dan kode untuk penerapan edge
3. **Dokumentasi**: Dokumentasikan persyaratan dan konfigurasi penerapan
4. **Persiapan Pemantauan**: Siapkan pemantauan dan pencatatan untuk penerapan produksi

## Target Audiens untuk Pengembangan Edge AI

### Pengembang Edge AI
- Pengembang aplikasi yang membangun perangkat edge dan solusi IoT berbasis AI
- Pengembang sistem tertanam yang mengintegrasikan kemampuan AI ke perangkat dengan keterbatasan sumber daya
- Pengembang seluler yang membuat aplikasi AI di perangkat untuk smartphone dan tablet

### Insinyur Edge AI
- Insinyur AI yang mengoptimalkan model untuk penerapan edge dan mengelola pipeline inferensi
- Insinyur DevOps yang menerapkan dan mengelola model AI di infrastruktur edge yang terdistribusi
- Insinyur kinerja yang mengoptimalkan beban kerja AI untuk keterbatasan perangkat keras edge

### Peneliti dan Pendidik
- Peneliti AI yang mengembangkan model dan algoritma yang efisien untuk komputasi edge
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
- **Augmented Reality**: Terapkan pengenalan objek dan pelacakan real-time untuk aplikasi AR
- **Pemantauan Kesehatan**: Jalankan model analisis kesehatan pada perangkat wearable dan peralatan medis
- **Sistem Otonom**: Implementasikan model pengambilan keputusan untuk drone, robot, dan kendaraan

### Infrastruktur Komputasi Edge
- **Pusat Data Edge**: Terapkan model AI di pusat data edge untuk aplikasi latensi rendah
- **Integrasi CDN**: Integrasikan kemampuan pemrosesan AI ke dalam jaringan pengiriman konten
- **Edge 5G**: Manfaatkan komputasi edge 5G untuk aplikasi berbasis AI
- **Komputasi Fog**: Implementasikan pemrosesan AI dalam lingkungan komputasi fog

## Instalasi dan Pengaturan

### Instalasi Cepat
Instal ekstensi AI Toolkit langsung dari Visual Studio Code Marketplace:

```
Install: AI Toolkit for Visual Studio Code (ms-windows-ai-studio.windows-ai-studio)
```

### Prasyarat untuk Pengembangan Edge AI
- **ONNX Runtime**: Instal ONNX Runtime untuk inferensi model
- **Ollama** (Opsional): Instal Ollama untuk penyajian model lokal
- **Lingkungan Python**: Siapkan Python dengan pustaka AI yang diperlukan
- **Alat Perangkat Keras Edge**: Instal alat pengembangan spesifik perangkat keras (CUDA, OpenVINO, dll.)

### Konfigurasi Awal
1. Buka VS Code dan instal ekstensi AI Toolkit
2. Konfigurasikan sumber model (ONNX, Ollama, penyedia cloud)
3. Siapkan lingkungan pengembangan lokal untuk pengujian edge
4. Konfigurasikan opsi akselerasi perangkat keras untuk mesin pengembangan Anda

## Memulai Pengembangan Edge AI

### Langkah 1: Pemilihan Model
1. Buka tampilan AI Toolkit di Activity Bar
2. Jelajahi Model Catalog untuk model yang kompatibel dengan edge
3. Filter berdasarkan ukuran model, format (ONNX), dan karakteristik kinerja
4. Bandingkan model menggunakan alat perbandingan bawaan

### Langkah 2: Pengujian Lokal
1. Gunakan Playground untuk menguji model yang dipilih secara lokal
2. Bereksperimen dengan berbagai prompt dan parameter
3. Pantau metrik kinerja selama pengujian
4. Evaluasi respons model untuk persyaratan kasus penggunaan edge

### Langkah 3: Optimasi Model
1. Gunakan alat Konversi Model untuk optimasi penerapan edge
2. Terapkan kuantisasi untuk mengurangi ukuran model
3. Uji model yang dioptimalkan untuk memastikan kinerja yang dapat diterima
4. Dokumentasikan pengaturan optimasi dan kompromi kinerja

### Langkah 4: Pengembangan Agen
1. Gunakan Agent Builder untuk membuat agen AI yang dioptimalkan untuk edge
2. Kembangkan prompt yang bekerja efektif dengan model yang lebih kecil
3. Integrasikan alat dan API yang diperlukan untuk skenario edge
4. Uji agen dalam kondisi edge yang disimulasikan

### Langkah 5: Evaluasi dan Penerapan
1. Gunakan evaluasi massal untuk menguji beberapa konfigurasi
2. Profil kinerja di bawah berbagai kondisi
3. Siapkan paket penerapan untuk perangkat edge target
4. Siapkan pemantauan dan pencatatan untuk penerapan produksi

## Praktik Terbaik untuk Pengembangan Edge AI

### Pemilihan Model
- **Keterbatasan Ukuran**: Pilih model yang sesuai dengan batasan memori perangkat target
- **Kecepatan Inferensi**: Prioritaskan model dengan waktu inferensi cepat untuk aplikasi real-time
- **Kompromi Akurasi**: Seimbangkan akurasi model dengan keterbatasan sumber daya
- **Kompatibilitas Format**: Pilih format ONNX atau format yang dioptimalkan perangkat keras untuk penerapan edge

### Teknik Optimasi
- **Kuantisasi**: Gunakan kuantisasi INT8 atau INT4 untuk mengurangi ukuran model dan meningkatkan kecepatan
- **Pruning**: Hapus parameter model yang tidak diperlukan untuk mengurangi kebutuhan komputasi
- **Knowledge Distillation**: Buat model yang lebih kecil yang mempertahankan kinerja model yang lebih besar
- **Akselerasi Perangkat Keras**: Manfaatkan NPU, GPU, atau akselerator khusus jika tersedia

### Alur Kerja Pengembangan
- **Pengujian Iteratif**: Uji secara sering dalam kondisi mirip edge selama pengembangan
- **Pemantauan Kinerja**: Pantau penggunaan sumber daya dan kecepatan inferensi secara terus-menerus
- **Kontrol Versi**: Lacak versi model dan pengaturan optimasi
- **Dokumentasi**: Dokumentasikan semua keputusan optimasi dan kompromi kinerja

### Pertimbangan Penerapan
- **Pemantauan Sumber Daya**: Pantau memori, CPU, dan penggunaan daya dalam produksi
- **Strategi Cadangan**: Terapkan mekanisme cadangan untuk kegagalan model
- **Mekanisme Pembaruan**: Rencanakan pembaruan model dan manajemen versi
- **Keamanan**: Terapkan langkah-langkah keamanan yang sesuai untuk aplikasi AI di edge

## Integrasi dengan Kerangka Kerja Edge AI

### ONNX Runtime
- **Penerapan Lintas Platform**: Terapkan model ONNX di berbagai platform edge
- **Optimasi Perangkat Keras**: Manfaatkan optimasi spesifik perangkat keras dari ONNX Runtime
- **Dukungan Mobile**: Gunakan ONNX Runtime Mobile untuk aplikasi di smartphone dan tablet
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
- **Hybrid Cloud-Edge**: Gabungkan pelatihan di cloud dengan inferensi di edge
- **Penerapan Modul**: Terapkan model AI sebagai modul IoT Edge
- **Manajemen Perangkat**: Kelola perangkat edge dan pembaruan model secara remote
- **Telemetri**: Kumpulkan data kinerja dan metrik model dari penerapan di edge

## Skenario Edge AI Lanjutan

### Penerapan Multi-Model
- **Ensemble Model**: Terapkan beberapa model untuk meningkatkan akurasi atau redundansi
- **Pengujian A/B**: Uji berbagai model secara bersamaan di perangkat edge
- **Pemilihan Dinamis**: Pilih model berdasarkan kondisi perangkat saat ini
- **Berbagi Sumber Daya**: Optimalkan penggunaan sumber daya di antara beberapa model yang diterapkan

### Federated Learning
- **Pelatihan Terdistribusi**: Latih model di berbagai perangkat edge
- **Pelestarian Privasi**: Jaga data pelatihan tetap lokal sambil berbagi peningkatan model
- **Pembelajaran Kolaboratif**: Biarkan perangkat belajar dari pengalaman kolektif
- **Koordinasi Edge-Cloud**: Koordinasikan pembelajaran antara perangkat edge dan infrastruktur cloud

### Pemrosesan Real-time
- **Pemrosesan Stream**: Proses aliran data kontinu di perangkat edge
- **Inferensi Berlatensi Rendah**: Optimalkan untuk latensi inferensi minimal
- **Pemrosesan Batch**: Proses batch data secara efisien di perangkat edge
- **Pemrosesan Adaptif**: Sesuaikan pemrosesan berdasarkan kemampuan perangkat saat ini

## Pemecahan Masalah Pengembangan Edge AI

### Masalah Umum
- **Keterbatasan Memori**: Model terlalu besar untuk memori perangkat target
- **Kecepatan Inferensi**: Inferensi model terlalu lambat untuk kebutuhan real-time
- **Penurunan Akurasi**: Optimasi mengurangi akurasi model secara tidak dapat diterima
- **Kompatibilitas Perangkat Keras**: Model tidak kompatibel dengan perangkat keras target

### Strategi Debugging
- **Profiling Kinerja**: Gunakan fitur tracing AI Toolkit untuk mengidentifikasi hambatan
- **Pemantauan Sumber Daya**: Pantau penggunaan memori dan CPU selama pengembangan
- **Pengujian Bertahap**: Uji optimasi secara bertahap untuk mengisolasi masalah
- **Simulasi Perangkat Keras**: Gunakan alat pengembangan untuk mensimulasikan perangkat keras target

### Solusi Optimasi
- **Quantisasi Lebih Lanjut**: Terapkan teknik quantisasi yang lebih agresif
- **Arsitektur Model**: Pertimbangkan arsitektur model yang dioptimalkan untuk edge
- **Optimasi Pra-pemrosesan**: Optimalkan pra-pemrosesan data untuk keterbatasan edge
- **Optimasi Inferensi**: Gunakan optimasi inferensi spesifik perangkat keras

## Sumber Daya dan Langkah Selanjutnya

### Dokumentasi
- [Panduan Model AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/models)
- [Dokumentasi Model Playground](https://code.visualstudio.com/docs/intelligentapps/playground)
- [Dokumentasi ONNX Runtime](https://onnxruntime.ai/)
- [Dokumentasi Windows ML](https://docs.microsoft.com/en-us/windows/ai/)

### Komunitas dan Dukungan
- [GitHub AI Toolkit VS Code](https://github.com/microsoft/vscode-ai-toolkit)
- [Komunitas ONNX](https://github.com/onnx/onnx)
- [Komunitas Pengembang Edge AI](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [Marketplace Ekstensi VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Sumber Belajar
- [Kursus Dasar Edge AI](./Module01/README.md)
- [Panduan Model Bahasa Kecil](./Module02/README.md)
- [Strategi Penerapan Edge](./Module03/README.md)
- [Pengembangan Edge AI Windows](./windowdeveloper.md)

## Kesimpulan

AI Toolkit untuk Visual Studio Code menyediakan platform yang komprehensif untuk pengembangan Edge AI, mulai dari penemuan dan optimasi model hingga penerapan dan pemantauan. Dengan memanfaatkan alat dan alur kerja yang terintegrasi, pengembang dapat dengan efisien membuat, menguji, dan menerapkan aplikasi AI yang berjalan secara efektif pada perangkat edge dengan sumber daya terbatas.

Dukungan toolkit untuk ONNX, Ollama, dan berbagai penyedia cloud, dikombinasikan dengan kemampuan optimasi dan evaluasinya, menjadikannya pilihan ideal untuk pengembangan Edge AI. Baik Anda membangun aplikasi IoT, fitur AI mobile, atau sistem kecerdasan embedded, AI Toolkit menyediakan alat dan alur kerja yang diperlukan untuk penerapan Edge AI yang sukses.

Seiring dengan perkembangan Edge AI, AI Toolkit untuk VS Code tetap berada di garis depan, menyediakan alat dan kemampuan mutakhir bagi pengembang untuk membangun generasi berikutnya dari aplikasi edge yang cerdas.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.