<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ec2b092ed161fd4d3907e010f8cf544",
  "translation_date": "2025-09-18T15:04:24+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "ms"
}
-->
# Panduan Pembangunan Windows Edge AI

## Pengenalan

Selamat datang ke Pembangunan Windows Edge AI - panduan komprehensif anda untuk membina aplikasi pintar yang memanfaatkan kuasa AI pada peranti menggunakan platform Windows AI Foundry Microsoft. Panduan ini direka khas untuk pembangun Windows yang ingin mengintegrasikan keupayaan Edge AI terkini ke dalam aplikasi mereka sambil memanfaatkan spektrum penuh pecutan perkakasan Windows.

### Kelebihan Windows AI

Windows AI Foundry mewakili platform yang bersatu, boleh dipercayai, dan selamat yang menyokong keseluruhan kitaran hayat pembangun AI - daripada pemilihan model dan penyesuaian kepada pengoptimuman dan penyebaran merentasi seni bina CPU, GPU, NPU, dan awan hibrid. Platform ini mendemokrasikan pembangunan AI dengan menyediakan:

- **Abstraksi Perkakasan**: Penyebaran lancar merentasi silikon AMD, Intel, NVIDIA, dan Qualcomm
- **Kecerdasan Pada Peranti**: AI yang menjaga privasi dan beroperasi sepenuhnya pada perkakasan tempatan
- **Prestasi Optimum**: Model yang telah dioptimumkan untuk konfigurasi perkakasan Windows
- **Sedia untuk Perusahaan**: Ciri keselamatan dan pematuhan gred pengeluaran

### Mengapa Windows untuk Edge AI?

**Sokongan Perkakasan Universal**  
Windows ML menyediakan pengoptimuman perkakasan automatik merentasi keseluruhan ekosistem Windows, memastikan aplikasi AI anda berprestasi secara optimum tanpa mengira seni bina silikon yang mendasari.

**Runtime AI Terintegrasi**  
Enjin inferensi Windows ML terbina dalam menghapuskan keperluan persediaan yang kompleks, membolehkan pembangun memberi tumpuan kepada logik aplikasi dan bukannya kebimbangan infrastruktur.

**Pengoptimuman PC Copilot+**  
API yang dibina khas untuk peranti Windows generasi akan datang dengan Unit Pemprosesan Neural (NPU) khusus yang memberikan prestasi luar biasa per watt.

**Ekosistem Pembangun**  
Alat yang kaya termasuk integrasi Visual Studio, dokumentasi komprehensif, dan aplikasi contoh yang mempercepatkan kitaran pembangunan.

## Objektif Pembelajaran

Dengan melengkapkan panduan pembangunan Windows Edge AI ini, anda akan menguasai kemahiran penting untuk membina aplikasi AI yang sedia untuk pengeluaran pada platform Windows.

### Kompetensi Teknikal Teras

**Penguasaan Windows AI Foundry**  
- Memahami seni bina dan komponen platform Windows AI Foundry  
- Menavigasi kitaran hayat pembangunan AI sepenuhnya dalam ekosistem Windows  
- Melaksanakan amalan terbaik keselamatan untuk aplikasi AI pada peranti  
- Mengoptimumkan aplikasi untuk pelbagai konfigurasi perkakasan Windows  

**Kepakaran Integrasi API**  
- Menguasai API Windows AI untuk aplikasi teks, visi, dan multimodal  
- Melaksanakan integrasi model bahasa Phi Silica untuk penjanaan teks dan penaakulan  
- Menyebarkan keupayaan visi komputer menggunakan API pemprosesan imej terbina dalam  
- Menyesuaikan model yang telah dilatih menggunakan teknik LoRA (Low-Rank Adaptation)  

**Pelaksanaan Tempatan Foundry**  
- Melayari, menilai, dan menyebarkan model bahasa sumber terbuka menggunakan CLI Foundry Local  
- Memahami pengoptimuman model dan kuantisasi untuk penyebaran tempatan  
- Melaksanakan keupayaan AI luar talian yang berfungsi tanpa sambungan internet  
- Mengurus kitaran hayat model dan kemas kini dalam persekitaran pengeluaran  

**Penyebaran Windows ML**  
- Membawa model ONNX tersuai ke aplikasi Windows menggunakan Windows ML  
- Memanfaatkan pecutan perkakasan automatik merentasi seni bina CPU, GPU, dan NPU  
- Melaksanakan inferensi masa nyata dengan penggunaan sumber yang optimum  
- Merancang aplikasi AI yang boleh diskalakan untuk pelbagai kategori peranti Windows  

### Kemahiran Pembangunan Aplikasi

**Pembangunan Windows Merentas Platform**  
- Membina aplikasi berkuasa AI menggunakan .NET MAUI untuk penyebaran universal Windows  
- Mengintegrasikan keupayaan AI ke dalam Win32, UWP, dan Aplikasi Web Progresif  
- Melaksanakan reka bentuk UI responsif yang menyesuaikan diri dengan keadaan pemprosesan AI  
- Mengendalikan operasi AI asinkron dengan corak pengalaman pengguna yang sesuai  

**Pengoptimuman Prestasi**  
- Profil dan mengoptimumkan prestasi inferensi AI merentasi pelbagai konfigurasi perkakasan  
- Melaksanakan pengurusan memori yang cekap untuk model bahasa besar  
- Merancang aplikasi yang merosot dengan anggun berdasarkan keupayaan perkakasan yang tersedia  
- Menggunakan strategi caching untuk operasi AI yang sering digunakan  

**Kesediaan Pengeluaran**  
- Melaksanakan pengendalian ralat yang komprehensif dan mekanisme fallback  
- Merancang telemetri dan pemantauan untuk prestasi aplikasi AI  
- Menggunakan amalan terbaik keselamatan untuk penyimpanan dan pelaksanaan model AI tempatan  
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

API Windows AI menyediakan keupayaan AI sedia guna yang dikuasakan oleh model pada peranti, dioptimumkan untuk kecekapan dan prestasi pada peranti Copilot+ PC dengan persediaan minimum yang diperlukan.

#### Kategori API Teras

**Model Bahasa Phi Silica**  
- Model bahasa kecil tetapi berkuasa untuk penjanaan teks dan penaakulan  
- Dioptimumkan untuk inferensi masa nyata dengan penggunaan kuasa minimum  
- Sokongan untuk penyesuaian tersuai menggunakan teknik LoRA  
- Integrasi dengan carian semantik Windows dan pengambilan pengetahuan  

**API Visi Komputer**  
- **Pengecaman Teks (OCR)**: Ekstrak teks daripada imej dengan ketepatan tinggi  
- **Super Resolusi Imej**: Meningkatkan skala imej menggunakan model AI tempatan  
- **Segmentasi Imej**: Mengenal pasti dan mengasingkan objek tertentu dalam imej  
- **Penerangan Imej**: Menjana penerangan teks terperinci untuk kandungan visual  
- **Padam Objek**: Menghapuskan objek yang tidak diingini daripada imej dengan inpainting berkuasa AI  

**Keupayaan Multimodal**  
- **Integrasi Visi-Bahasa**: Menggabungkan pemahaman teks dan imej  
- **Carian Semantik**: Membolehkan pertanyaan bahasa semula jadi merentasi kandungan multimedia  
- **Pengambilan Pengetahuan**: Membina pengalaman carian pintar dengan data tempatan  

### 2. Foundry Local

Foundry Local menyediakan pembangun akses cepat kepada model bahasa sumber terbuka sedia guna pada Windows Silicon, menawarkan keupayaan untuk melayari, menguji, berinteraksi, dan menyebarkan model dalam aplikasi tempatan.

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
- Gunakan Foundry Local CLI untuk pengujian dan pengesahan model
- Gunakan alat ujian Windows AI API untuk pengesahan integrasi
- Laksanakan log tersuai untuk pemantauan operasi AI
- Cipta ujian automatik untuk kebolehpercayaan fungsi AI

## Menjamin Masa Depan Aplikasi Anda

### Teknologi Baru

**Perkakasan Generasi Seterusnya**
- Reka aplikasi untuk memanfaatkan keupayaan NPU masa depan
- Rancang untuk saiz model yang lebih besar dan kerumitan yang meningkat
- Laksanakan seni bina adaptif untuk perkakasan yang berkembang
- Pertimbangkan algoritma bersedia kuantum untuk keserasian masa depan

**Keupayaan AI Lanjutan**
- Bersedia untuk integrasi AI multimodal merentasi lebih banyak jenis data
- Rancang untuk AI kolaboratif masa nyata antara pelbagai peranti
- Reka untuk keupayaan pembelajaran teragih
- Pertimbangkan seni bina kecerdasan hibrid tepi-awan

### Pembelajaran dan Penyesuaian Berterusan

**Kemas Kini Model**
- Laksanakan mekanisme kemas kini model yang lancar
- Reka aplikasi untuk menyesuaikan diri dengan keupayaan model yang ditingkatkan
- Rancang untuk keserasian ke belakang dengan model sedia ada
- Laksanakan ujian A/B untuk penilaian prestasi model

**Evolusi Ciri**
- Reka seni bina modular yang boleh menampung keupayaan AI baharu
- Rancang untuk integrasi API Windows AI yang muncul
- Laksanakan bendera ciri untuk pelancaran keupayaan secara beransur-ansur
- Reka antara muka pengguna yang menyesuaikan diri dengan ciri AI yang dipertingkatkan

## Kesimpulan

Pembangunan Windows Edge AI mewakili gabungan keupayaan AI yang kuat dengan platform Windows yang kukuh, selamat, dan boleh diskalakan. Dengan menguasai ekosistem Windows AI Foundry, pembangun boleh mencipta aplikasi pintar yang memberikan pengalaman pengguna yang luar biasa sambil mengekalkan piawaian tertinggi dalam privasi, keselamatan, dan prestasi.

Gabungan Windows AI APIs, Foundry Local, dan Windows ML menyediakan asas yang tiada tandingan untuk membina generasi seterusnya aplikasi Windows pintar. Ketika AI terus berkembang, platform Windows memastikan aplikasi anda akan berkembang dengan teknologi baru sambil mengekalkan keserasian dan prestasi merentasi ekosistem perkakasan Windows yang pelbagai.

Sama ada anda membina aplikasi pengguna, penyelesaian perusahaan, atau alat industri khusus, pembangunan Windows Edge AI memberi kuasa kepada anda untuk mencipta pengalaman yang pintar, responsif, dan sangat terintegrasi yang memanfaatkan sepenuhnya potensi peranti Windows moden.

## Sumber Tambahan

### Dokumentasi dan Pembelajaran
- [Dokumentasi Windows AI Foundry](https://learn.microsoft.com/windows/ai/)
- [Rujukan Windows AI APIs](https://learn.microsoft.com/windows/ai/apis/)
- [Memulakan Foundry Local](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Gambaran Keseluruhan Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)

### Alat Pembangunan
- [Toolkit AI untuk Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [Galeri Pembangunan AI](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Contoh Windows AI](https://learn.microsoft.com/windows/ai/samples/)

### Komuniti dan Sokongan
- [Komuniti Pembangun Windows](https://developer.microsoft.com/en-us/windows/)
- [Blog Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Latihan AI Microsoft Learn](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Panduan ini direka untuk berkembang seiring dengan ekosistem Windows AI yang maju dengan pesat. Kemas kini berkala memastikan penjajaran dengan keupayaan platform terkini dan amalan terbaik pembangunan.*

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.