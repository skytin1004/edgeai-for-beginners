<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9c2dacb560380677a2c923171d3e423d",
  "translation_date": "2025-09-22T22:28:26+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "ms"
}
-->
# Panduan Pembangunan Windows Edge AI

## Pengenalan

Selamat datang ke Pembangunan Windows Edge AI - panduan lengkap anda untuk membina aplikasi pintar yang memanfaatkan kuasa AI pada peranti menggunakan platform Windows AI Foundry dari Microsoft. Panduan ini direka khusus untuk pembangun Windows yang ingin mengintegrasikan keupayaan Edge AI terkini ke dalam aplikasi mereka sambil memanfaatkan sepenuhnya pecutan perkakasan Windows.

### Kelebihan Windows AI

Windows AI Foundry mewakili platform yang bersatu, boleh dipercayai, dan selamat yang menyokong keseluruhan kitaran hayat pembangunan AI - daripada pemilihan model dan penalaan kepada pengoptimuman dan penyebaran merentasi seni bina CPU, GPU, NPU, dan awan hibrid. Platform ini mendemokrasikan pembangunan AI dengan menyediakan:

- **Abstraksi Perkakasan**: Penyebaran lancar merentasi silikon AMD, Intel, NVIDIA, dan Qualcomm
- **Kecerdasan Pada Peranti**: AI yang memelihara privasi dan beroperasi sepenuhnya pada perkakasan tempatan
- **Prestasi Dioptimumkan**: Model yang telah dioptimumkan untuk konfigurasi perkakasan Windows
- **Sedia untuk Perusahaan**: Ciri keselamatan dan pematuhan gred pengeluaran

### Mengapa Windows untuk Edge AI?

**Sokongan Perkakasan Universal**  
Windows ML menyediakan pengoptimuman perkakasan automatik merentasi keseluruhan ekosistem Windows, memastikan aplikasi AI anda berprestasi optimum tanpa mengira seni bina silikon yang mendasari.

**Runtime AI Terintegrasi**  
Enjin inferensi Windows ML terbina dalam menghapuskan keperluan persediaan yang kompleks, membolehkan pembangun memberi tumpuan kepada logik aplikasi dan bukannya kebimbangan infrastruktur.

**Pengoptimuman PC Copilot+**  
API yang dibina khusus untuk peranti Windows generasi akan datang dengan Unit Pemprosesan Neural (NPU) yang memberikan prestasi luar biasa per watt.

**Ekosistem Pembangun**  
Alat yang kaya termasuk integrasi Visual Studio, dokumentasi komprehensif, dan aplikasi contoh yang mempercepatkan kitaran pembangunan.

## Objektif Pembelajaran

Dengan melengkapkan panduan pembangunan Windows Edge AI ini, anda akan menguasai kemahiran penting untuk membina aplikasi AI yang sedia untuk pengeluaran pada platform Windows.

### Kompetensi Teknikal Teras

**Penguasaan Windows AI Foundry**  
- Memahami seni bina dan komponen platform Windows AI Foundry  
- Menavigasi kitaran hayat pembangunan AI sepenuhnya dalam ekosistem Windows  
- Melaksanakan amalan terbaik keselamatan untuk aplikasi AI pada peranti  
- Mengoptimumkan aplikasi untuk konfigurasi perkakasan Windows yang berbeza  

**Kepakaran Integrasi API**  
- Menguasai API Windows AI untuk aplikasi teks, penglihatan, dan multimodal  
- Melaksanakan integrasi model bahasa Phi Silica untuk penjanaan teks dan penaakulan  
- Menyebarkan keupayaan penglihatan komputer menggunakan API pemprosesan imej terbina dalam  
- Menyesuaikan model yang telah dilatih menggunakan teknik LoRA (Low-Rank Adaptation)  

**Pelaksanaan Tempatan Foundry**  
- Melayari, menilai, dan menyebarkan model bahasa sumber terbuka menggunakan Foundry Local CLI  
- Memahami pengoptimuman model dan kuantisasi untuk penyebaran tempatan  
- Melaksanakan keupayaan AI luar talian yang berfungsi tanpa sambungan internet  
- Mengurus kitaran hayat model dan kemas kini dalam persekitaran pengeluaran  

**Penyebaran Windows ML**  
- Membawa model ONNX tersuai ke aplikasi Windows menggunakan Windows ML  
- Memanfaatkan pecutan perkakasan automatik merentasi seni bina CPU, GPU, dan NPU  
- Melaksanakan inferensi masa nyata dengan penggunaan sumber yang optimum  
- Merancang aplikasi AI yang boleh diskalakan untuk kategori peranti Windows yang pelbagai  

### Kemahiran Pembangunan Aplikasi

**Pembangunan Windows Merentas Platform**  
- Membina aplikasi berkuasa AI menggunakan .NET MAUI untuk penyebaran universal Windows  
- Mengintegrasikan keupayaan AI ke dalam aplikasi Win32, UWP, dan Web Progresif  
- Melaksanakan reka bentuk UI responsif yang menyesuaikan diri dengan keadaan pemprosesan AI  
- Mengendalikan operasi AI asinkron dengan corak pengalaman pengguna yang sesuai  

**Pengoptimuman Prestasi**  
- Memprofil dan mengoptimumkan prestasi inferensi AI merentasi konfigurasi perkakasan yang berbeza  
- Melaksanakan pengurusan memori yang cekap untuk model bahasa besar  
- Merancang aplikasi yang merosot dengan anggun berdasarkan keupayaan perkakasan yang tersedia  
- Mengaplikasikan strategi caching untuk operasi AI yang sering digunakan  

**Kesediaan Pengeluaran**  
- Melaksanakan pengendalian ralat yang komprehensif dan mekanisme sandaran  
- Merancang telemetri dan pemantauan untuk prestasi aplikasi AI  
- Mengaplikasikan amalan terbaik keselamatan untuk penyimpanan dan pelaksanaan model AI tempatan  
- Merancang strategi penyebaran untuk aplikasi perusahaan dan pengguna  

### Pemahaman Perniagaan dan Strategik

**Seni Bina Aplikasi AI**  
- Merancang seni bina hibrid yang mengoptimumkan antara pemprosesan AI tempatan dan awan  
- Menilai pertukaran antara saiz model, ketepatan, dan kelajuan inferensi  
- Merancang seni bina aliran data yang mengekalkan privasi sambil membolehkan kecerdasan  
- Melaksanakan penyelesaian AI yang kos efektif yang boleh diskalakan dengan permintaan pengguna  

**Kedudukan Pasaran**  
- Memahami kelebihan kompetitif aplikasi AI asli Windows  
- Mengenal pasti kes penggunaan di mana AI pada peranti memberikan pengalaman pengguna yang unggul  
- Membangunkan strategi go-to-market untuk aplikasi Windows yang dipertingkatkan AI  
- Memposisikan aplikasi untuk memanfaatkan faedah ekosistem Windows  

## Komponen Platform Windows AI Foundry

### 1. API Windows AI

API Windows AI menyediakan keupayaan AI yang sedia digunakan yang dikuasakan oleh model pada peranti, dioptimumkan untuk kecekapan dan prestasi pada peranti Copilot+ PC dengan persediaan minimum yang diperlukan.

#### Kategori API Teras

**Model Bahasa Phi Silica**  
- Model bahasa kecil tetapi berkuasa untuk penjanaan teks dan penaakulan  
- Dioptimumkan untuk inferensi masa nyata dengan penggunaan kuasa minimum  
- Sokongan untuk penalaan tersuai menggunakan teknik LoRA  
- Integrasi dengan carian semantik Windows dan pengambilan pengetahuan  

**API Penglihatan Komputer**  
- **Pengecaman Teks (OCR)**: Ekstrak teks daripada imej dengan ketepatan tinggi  
- **Super Resolusi Imej**: Meningkatkan skala imej menggunakan model AI tempatan  
- **Segmentasi Imej**: Mengenal pasti dan mengasingkan objek tertentu dalam imej  
- **Penerangan Imej**: Menjana penerangan teks terperinci untuk kandungan visual  
- **Padam Objek**: Menghapuskan objek yang tidak diingini daripada imej dengan inpainting berkuasa AI  

**Keupayaan Multimodal**  
- **Integrasi Penglihatan-Bahasa**: Menggabungkan pemahaman teks dan imej  
- **Carian Semantik**: Membolehkan pertanyaan bahasa semula jadi merentasi kandungan multimedia  
- **Pengambilan Pengetahuan**: Membina pengalaman carian pintar dengan data tempatan  

### 2. Foundry Local

Foundry Local menyediakan pembangun akses cepat kepada model bahasa sumber terbuka yang sedia digunakan pada Windows Silicon, menawarkan keupayaan untuk melayari, menguji, berinteraksi, dan menyebarkan model dalam aplikasi tempatan.

#### Ciri Utama

**Katalog Model**  
- Koleksi komprehensif model sumber terbuka yang telah dioptimumkan  
- Model dioptimumkan merentasi CPU, GPU, dan NPU untuk penyebaran segera  
- Sokongan untuk keluarga model popular termasuk Llama, Mistral, Phi, dan model domain khusus  

**Integrasi CLI**  
- Antara muka baris arahan untuk pengurusan dan penyebaran model  
- Aliran kerja pengoptimuman dan kuantisasi automatik  
- Integrasi dengan persekitaran pembangunan popular dan saluran CI/CD  

**Penyebaran Tempatan**  
- Operasi luar talian sepenuhnya tanpa pergantungan awan  
- Sokongan untuk format dan konfigurasi model tersuai  
- Penyajian model yang cekap dengan pengoptimuman perkakasan automatik  

### 3. Windows ML

Windows ML berfungsi sebagai platform AI teras dan runtime inferensi terintegrasi pada Windows, membolehkan pembangun menyebarkan model tersuai dengan cekap merentasi ekosistem perkakasan Windows yang luas.

#### Faedah Seni Bina

**Sokongan Perkakasan Universal**  
- Pengoptimuman automatik untuk silikon AMD, Intel, NVIDIA, dan Qualcomm  
- Sokongan untuk pelaksanaan CPU, GPU, dan NPU dengan pertukaran yang telus  
- Abstraksi perkakasan yang menghapuskan kerja pengoptimuman khusus platform  

**Fleksibiliti Model**  
- Sokongan untuk format model ONNX dengan penukaran automatik daripada rangka kerja popular  
- Penyebaran model tersuai dengan prestasi gred pengeluaran  
- Integrasi dengan seni bina aplikasi Windows yang sedia ada  

**Integrasi Perusahaan**  
- Serasi dengan rangka kerja keselamatan dan pematuhan Windows  
- Sokongan untuk alat penyebaran dan pengurusan perusahaan  
- Integrasi dengan sistem pengurusan dan pemantauan peranti Windows  

## Aliran Kerja Pembangunan

### Fasa 1: Persediaan Persekitaran dan Konfigurasi Alat

**Persediaan Persekitaran Pembangunan**  
1. Pasang Visual Studio dengan sambungan AI Toolkit  
2. Konfigurasikan alat CLI Windows AI Foundry  
3. Sediakan persekitaran ujian model tempatan  
4. Tetapkan alat pemprofilan prestasi dan pemantauan  

**Penerokaan Galeri Dev AI**  
- Terokai aplikasi contoh dan pelaksanaan rujukan  
- Uji API Windows AI dengan demonstrasi interaktif  
- Semak kod sumber untuk amalan dan corak terbaik  
- Kenal pasti sampel yang relevan untuk kes penggunaan khusus anda  

### Fasa 2: Pemilihan dan Integrasi Model

**Analisis Keperluan**  
- Tentukan keperluan fungsional untuk keupayaan AI  
- Tetapkan kekangan prestasi dan sasaran pengoptimuman  
- Menilai keperluan privasi dan keselamatan  
- Merancang seni bina penyebaran dan strategi penskalaan  

**Penilaian Model**  
- Gunakan Foundry Local untuk menguji model sumber terbuka untuk kes penggunaan anda  
- Penanda aras API Windows AI terhadap keperluan model tersuai  
- Menilai pertukaran antara saiz model, ketepatan, dan kelajuan inferensi  
- Prototip pendekatan integrasi dengan model terpilih  

### Fasa 3: Pembangunan Aplikasi

**Integrasi Teras**  
- Melaksanakan integrasi API Windows AI dengan pengendalian ralat yang sesuai  
- Merancang antara muka pengguna yang menampung aliran kerja pemprosesan AI  
- Melaksanakan strategi caching dan pengoptimuman untuk inferensi model  
- Menambah telemetri dan pemantauan untuk prestasi operasi AI  

**Ujian dan Pengesahan**  
- Uji aplikasi merentasi konfigurasi perkakasan Windows yang berbeza  
- Sahkan metrik prestasi di bawah pelbagai keadaan beban  
- Melaksanakan ujian automatik untuk kebolehpercayaan fungsi AI  
- Lakukan ujian pengalaman pengguna dengan ciri yang dipertingkatkan AI  

### Fasa 4: Pengoptimuman dan Penyebaran

**Pengoptimuman Prestasi**  
- Profil prestasi aplikasi merentasi konfigurasi perkakasan sasaran  
- Mengoptimumkan penggunaan memori dan strategi pemuatan model  
- Melaksanakan tingkah laku adaptif berdasarkan keupayaan perkakasan yang tersedia  
- Menyempurnakan pengalaman pengguna untuk senario prestasi yang berbeza  

**Penyebaran Pengeluaran**  
- Pek aplikasi dengan kebergantungan model AI yang sesuai  
- Melaksanakan mekanisme kemas kini untuk model dan logik aplikasi  
- Konfigurasikan pemantauan dan analitik untuk persekitaran pengeluaran  
- Merancang strategi pelancaran untuk penyebaran perusahaan dan pengguna  

## Contoh Pelaksanaan Praktikal

### Contoh 1: Aplikasi Pemprosesan Dokumen Pintar

Bina aplikasi Windows yang memproses dokumen menggunakan pelbagai keupayaan AI:

**Teknologi Digunakan:**  
- Phi Silica untuk penjumlahan dokumen dan menjawab soalan  
- API OCR untuk ekstraksi teks daripada dokumen yang diimbas  
- API Penerangan Imej untuk analisis carta dan rajah  
- Model ONNX tersuai untuk pengelasan dokumen  

**Pendekatan Pelaksanaan:**  
- Merancang seni bina modular dengan komponen AI yang boleh dipasang  
- Melaksanakan pemprosesan asinkron untuk kumpulan dokumen besar  
- Menambah penunjuk kemajuan dan sokongan pembatalan untuk operasi jangka panjang  
- Termasuk keupayaan luar talian untuk pemprosesan dokumen sensitif  

### Contoh 2: Sistem Pengurusan Inventori Runcit

Cipta sistem inventori berkuasa AI untuk aplikasi runcit:

**Teknologi Digunakan:**  
- Segmentasi Imej untuk pengenalan produk  
- Model penglihatan tersuai untuk pengelasan jenama dan kategori  
- Penyebaran tempatan Foundry Local model bahasa runcit khusus  
- Integrasi dengan sistem POS dan inventori sedia ada  

**Pendekatan Pelaksanaan:**  
- Membina integrasi kamera untuk pengimbasan produk masa nyata  
- Melaksanakan pengecaman produk visual dan kod bar  
- Menambah pertanyaan inventori bahasa semula jadi menggunakan model bahasa tempatan  
- Merancang seni bina yang boleh diskalakan untuk penyebaran berbilang kedai  

### Contoh 3: Pembantu Dokumentasi Penjagaan Kesihatan

Membangunkan alat dokumentasi penjagaan kesihatan yang memelihara privasi:

**Teknologi Digunakan:**  
- Phi Silica untuk penjanaan nota perubatan dan sokongan keputusan klinikal  
- OCR untuk mendigitalkan rekod perubatan tulisan tangan  
- Model bahasa perubatan tersuai yang disebarkan melalui Windows ML  
- Penyimpanan vektor tempatan untuk pengambilan pengetahuan perubatan  

**Pendekatan Pelaksanaan:**  
- Memastikan operasi luar talian sepenuhnya untuk privasi pesakit  
- Melaksanakan pengesahan dan cadangan terminologi perubatan  
- Menambah log audit untuk pematuhan peraturan  
- Merancang integrasi dengan sistem Rekod Kesihatan Elektronik sedia ada  

## Strategi Pengoptimuman Prestasi

### Pembangunan Sedar Perkakasan

**Pengoptimuman NPU**  
- Merancang aplikasi untuk memanfaatkan keupayaan NPU pada PC Copilot+  
- Melaksanakan sandaran anggun kepada GPU/CPU pada peranti tanpa NPU  
- Mengoptimumkan format model untuk pecutan khusus NPU  
- Memantau penggunaan NPU dan ciri termal  

**Pengurusan Memori**  
- Melaksanakan strategi pemuatan dan caching model yang cekap  
- Menggunakan pemetaan memori untuk model besar bagi mengurangkan masa permulaan  
- Merancang aplikasi yang sedar memori untuk peranti dengan sumber terhad  
- Melaksanakan kuantisasi model untuk pengoptimuman memori  

**Kecekapan Bateri**  
- Mengoptimumkan operasi AI untuk penggunaan kuasa minimum  
- Melaksanakan pemprosesan adaptif berdasarkan status bateri  
- Merancang pemprosesan latar belakang yang cekap untuk operasi AI berterusan  
- Menggunakan alat pemprofilan kuasa untuk mengoptimumkan penggunaan tenaga  

### Pertimbangan Skalabiliti

**Multi-Threading**  
- Merancang operasi AI yang selamat benang untuk pemprosesan serentak  
- Melaksanakan pengagihan kerja yang cekap merentasi teras yang tersedia  
- Menggunakan corak async/await untuk operasi AI yang tidak menyekat  
- Merancang pengoptimuman kolam benang untuk konfigurasi perkakasan yang berbeza  

**Strategi Caching**  
- Melaksanakan caching pintar untuk operasi AI yang sering digunakan  
- Merancang strategi pembatalan cache untuk kemas kini model  
- Menggunakan caching berterusan untuk operasi prapemprosesan yang mahal  
- Melaksanakan caching teragih untuk senario berbilang pengguna  

## Amalan Terbaik Keselamatan dan Privasi

### Perlindungan Data

**Pemprosesan Tempatan**  
- Memastikan data sensitif tidak pernah meninggalkan peranti tempatan  
- Melaksanakan penyimpanan selamat untuk model AI dan data sementara  
- Menggunakan ciri keselamatan Windows untuk sandboxing aplikasi  
- Mengaplikasikan penyulitan untuk model yang disimpan dan hasil pemprosesan sementara  

**Keselamatan Model**  
- Mengesahkan integriti model sebelum pemuatan dan pelaksanaan  
- Melaksanakan mekanisme kemas kini model yang selamat  
- Menggunakan model yang ditandatangani untuk mencegah pengubahan  
- Mengaplikasikan kawalan akses untuk fail model dan konfigurasi  

### Pertimbangan Pematuhan

**Penyelarasan Peraturan**  
- Merancang aplikasi untuk memenuhi GDPR, HIPAA, dan keperluan peraturan lain  
- Melaksanakan log audit untuk proses membuat keputusan AI  
- Menyediakan ciri ketelusan untuk hasil yang dijana AI  
- Membolehkan kawalan pengguna ke atas pemprosesan data AI  

**Keselamatan Perusahaan**  
- Mengintegrasikan dengan dasar keselamatan perusahaan Windows  
- Menyokong penyebaran terurus melalui alat pengurusan perusahaan  
- Melaksanakan kawalan akses berdasarkan peranan untuk ciri AI  
- Menyediakan kawalan pentadbiran untuk fungsi AI  

## Penyelesaian Masalah dan Debugging

### Cabaran Pembangunan Biasa

**Isu Pemuatan Model**  
- Mengesahkan keserasian model ONNX dengan Windows ML  
- Memeriksa integriti fail model dan keperlu
- Gunakan Foundry Local CLI untuk pengujian dan pengesahan model
- Gunakan alat ujian Windows AI API untuk pengesahan integrasi
- Laksanakan log tersuai untuk pemantauan operasi AI
- Cipta ujian automatik untuk kebolehpercayaan fungsi AI

## Menjamin Masa Depan Aplikasi Anda

### Teknologi Muncul

**Perkakasan Generasi Seterusnya**
- Reka aplikasi untuk memanfaatkan keupayaan NPU masa depan
- Rancang untuk saiz model yang lebih besar dan kerumitan yang meningkat
- Laksanakan seni bina adaptif untuk perkakasan yang berkembang
- Pertimbangkan algoritma yang bersedia untuk kuantum bagi keserasian masa depan

**Keupayaan AI Lanjutan**
- Bersedia untuk integrasi AI multimodal merentasi lebih banyak jenis data
- Rancang untuk AI kolaboratif masa nyata antara pelbagai peranti
- Reka untuk keupayaan pembelajaran teragih
- Pertimbangkan seni bina kecerdasan hibrid tepi-awan

### Pembelajaran dan Penyesuaian Berterusan

**Kemas Kini Model**
- Laksanakan mekanisme kemas kini model yang lancar
- Reka aplikasi untuk menyesuaikan diri dengan keupayaan model yang dipertingkatkan
- Rancang untuk keserasian ke belakang dengan model sedia ada
- Laksanakan ujian A/B untuk penilaian prestasi model

**Evolusi Ciri**
- Reka seni bina modular yang boleh menampung keupayaan AI baharu
- Rancang untuk integrasi API Windows AI yang muncul
- Laksanakan bendera ciri untuk pelancaran keupayaan secara beransur-ansur
- Reka antara muka pengguna yang menyesuaikan diri dengan ciri AI yang dipertingkatkan

## Kesimpulan

Pembangunan Windows Edge AI mewakili gabungan keupayaan AI yang hebat dengan platform Windows yang kukuh, selamat, dan boleh diskalakan. Dengan menguasai ekosistem Windows AI Foundry, pembangun boleh mencipta aplikasi pintar yang memberikan pengalaman pengguna yang luar biasa sambil mengekalkan piawaian tertinggi dalam privasi, keselamatan, dan prestasi.

Gabungan Windows AI APIs, Foundry Local, dan Windows ML menyediakan asas yang tiada tandingan untuk membina generasi seterusnya aplikasi Windows pintar. Ketika AI terus berkembang, platform Windows memastikan aplikasi anda akan berkembang dengan teknologi yang muncul sambil mengekalkan keserasian dan prestasi merentasi ekosistem perkakasan Windows yang pelbagai.

Sama ada anda membina aplikasi pengguna, penyelesaian perusahaan, atau alat industri khusus, pembangunan Windows Edge AI memberi kuasa kepada anda untuk mencipta pengalaman yang pintar, responsif, dan sangat terintegrasi yang memanfaatkan sepenuhnya potensi peranti Windows moden.

## Sumber Tambahan

Untuk panduan langkah demi langkah Windows mengenai Foundry Local (pemasangan, CLI, endpoint dinamik, penggunaan SDK), lihat panduan repo: [foundrylocal.md](./foundrylocal.md).

### Dokumentasi dan Pembelajaran
- [Dokumentasi Windows AI Foundry](https://learn.microsoft.com/windows/ai/)
- [Rujukan Windows AI APIs](https://learn.microsoft.com/windows/ai/apis/)
- [Foundry Local Getting Started](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Gambaran Keseluruhan Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)

### Alat Pembangunan
- [AI Toolkit untuk Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Contoh Windows AI](https://learn.microsoft.com/windows/ai/samples/)

### Komuniti dan Sokongan
- [Komuniti Pembangun Windows](https://developer.microsoft.com/en-us/windows/)
- [Blog Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Latihan Microsoft Learn AI](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Panduan ini direka untuk berkembang seiring dengan ekosistem Windows AI yang maju dengan pesat. Kemas kini berkala memastikan penjajaran dengan keupayaan platform terkini dan amalan terbaik pembangunan.*

---

