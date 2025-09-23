<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-18T15:07:10+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "ms"
}
-->
# Panduan Pembangunan AI Edge dengan AI Toolkit untuk Visual Studio Code

## Pengenalan

Selamat datang ke panduan komprehensif untuk menggunakan AI Toolkit dalam Visual Studio Code bagi pembangunan AI Edge. Ketika kecerdasan buatan (AI) beralih daripada pengkomputeran awan terpusat kepada peranti edge yang teragih, pembangun memerlukan alat yang berkuasa dan terintegrasi untuk menangani cabaran unik dalam pelaksanaan edge - daripada kekangan sumber kepada keperluan operasi luar talian.

AI Toolkit untuk Visual Studio Code menjembatani jurang ini dengan menyediakan persekitaran pembangunan lengkap yang direka khusus untuk membina, menguji, dan mengoptimumkan aplikasi AI yang berjalan dengan cekap pada peranti edge. Sama ada anda membangunkan untuk sensor IoT, peranti mudah alih, sistem terbenam, atau pelayan edge, toolkit ini mempermudah keseluruhan aliran kerja pembangunan anda dalam persekitaran VS Code yang sudah biasa.

Panduan ini akan membawa anda melalui konsep asas, alat, dan amalan terbaik untuk memanfaatkan AI Toolkit dalam projek AI Edge anda, daripada pemilihan model awal hingga pelaksanaan pengeluaran.

## Gambaran Keseluruhan

AI Toolkit menyediakan persekitaran pembangunan terintegrasi untuk keseluruhan kitaran hayat aplikasi AI Edge dalam VS Code. Ia menawarkan integrasi lancar dengan model AI popular daripada penyedia seperti OpenAI, Anthropic, Google, dan GitHub, sambil menyokong pelaksanaan model tempatan melalui ONNX dan Ollama - keupayaan penting untuk aplikasi AI Edge yang memerlukan inferens pada peranti.

Apa yang membezakan AI Toolkit untuk pembangunan AI Edge adalah fokusnya pada keseluruhan saluran pelaksanaan edge. Tidak seperti alat pembangunan AI tradisional yang kebanyakannya menyasarkan pelaksanaan awan, AI Toolkit merangkumi ciri khusus untuk pengoptimuman model, ujian dalam keadaan sumber terhad, dan penilaian prestasi khusus edge. Toolkit ini memahami bahawa pembangunan AI Edge memerlukan pertimbangan yang berbeza - saiz model yang lebih kecil, masa inferens yang lebih pantas, keupayaan luar talian, dan pengoptimuman khusus perkakasan.

Platform ini menyokong pelbagai senario pelaksanaan, daripada inferens pada peranti yang mudah kepada seni bina edge multi-model yang kompleks. Ia menyediakan alat untuk penukaran model, kuantisasi, dan pengoptimuman yang penting untuk pelaksanaan edge yang berjaya, sambil mengekalkan produktiviti pembangun yang terkenal dengan VS Code.

## Objektif Pembelajaran

Menjelang akhir panduan ini, anda akan dapat:

### Kecekapan Teras
- **Memasang dan mengkonfigurasi** AI Toolkit untuk aliran kerja pembangunan AI Edge
- **Menavigasi dan menggunakan** antara muka AI Toolkit, termasuk Model Catalog, Playground, dan Agent Builder
- **Memilih dan menilai** model AI yang sesuai untuk pelaksanaan edge berdasarkan prestasi dan kekangan sumber
- **Menukar dan mengoptimumkan** model menggunakan format ONNX dan teknik kuantisasi untuk peranti edge

### Kemahiran Pembangunan AI Edge
- **Mereka bentuk dan melaksanakan** aplikasi AI Edge menggunakan persekitaran pembangunan terintegrasi
- **Melakukan ujian model** dalam keadaan seperti edge menggunakan inferens tempatan dan pemantauan sumber
- **Mencipta dan menyesuaikan** agen AI yang dioptimumkan untuk senario pelaksanaan edge
- **Menilai prestasi model** menggunakan metrik yang relevan untuk pengkomputeran edge (latensi, penggunaan memori, ketepatan)

### Pengoptimuman dan Pelaksanaan
- **Mengaplikasikan teknik kuantisasi dan pemangkasan** untuk mengurangkan saiz model sambil mengekalkan prestasi yang boleh diterima
- **Mengoptimumkan model** untuk platform perkakasan edge tertentu termasuk pecutan CPU, GPU, dan NPU
- **Melaksanakan amalan terbaik** untuk pembangunan AI Edge termasuk pengurusan sumber dan strategi sandaran
- **Menyediakan model dan aplikasi** untuk pelaksanaan pengeluaran pada peranti edge

### Konsep Lanjutan AI Edge
- **Mengintegrasikan dengan rangka kerja AI Edge** termasuk ONNX Runtime, Windows ML, dan TensorFlow Lite
- **Melaksanakan seni bina multi-model** dan senario pembelajaran teragih untuk persekitaran edge
- **Menyelesaikan masalah biasa AI Edge** termasuk kekangan memori, kelajuan inferens, dan keserasian perkakasan
- **Mereka bentuk strategi pemantauan dan log** untuk aplikasi AI Edge dalam pengeluaran

### Aplikasi Praktikal
- **Membina penyelesaian AI Edge hujung ke hujung** daripada pemilihan model hingga pelaksanaan
- **Menunjukkan kecekapan** dalam aliran kerja pembangunan khusus edge dan teknik pengoptimuman
- **Mengaplikasikan konsep yang dipelajari** kepada kes penggunaan AI Edge dunia sebenar termasuk IoT, mudah alih, dan aplikasi terbenam
- **Menilai dan membandingkan** pelbagai strategi pelaksanaan AI Edge dan kompromi mereka

## Ciri Utama untuk Pembangunan AI Edge

### 1. Katalog Model dan Penemuan
- **Sokongan Model Tempatan**: Temui dan akses model AI yang dioptimumkan khusus untuk pelaksanaan edge
- **Integrasi ONNX**: Akses model dalam format ONNX untuk inferens edge yang cekap
- **Sokongan Ollama**: Manfaatkan model yang berjalan secara tempatan melalui Ollama untuk privasi dan operasi luar talian
- **Perbandingan Model**: Bandingkan model secara bersebelahan untuk mencari keseimbangan optimum antara prestasi dan penggunaan sumber untuk peranti edge

### 2. Playground Interaktif
- **Persekitaran Ujian Tempatan**: Uji model secara tempatan sebelum pelaksanaan edge
- **Eksperimen Multi-modal**: Uji dengan imej, teks, dan input lain yang tipikal dalam senario edge
- **Penalaan Parameter**: Bereksperimen dengan parameter model yang berbeza untuk dioptimumkan bagi kekangan edge
- **Pemantauan Prestasi Masa Nyata**: Perhatikan kelajuan inferens dan penggunaan sumber semasa pembangunan

### 3. Agent Builder untuk Aplikasi Edge
- **Kejuruteraan Prompt**: Cipta prompt yang dioptimumkan untuk berfungsi dengan cekap dengan model edge yang lebih kecil
- **Integrasi Alat MCP**: Integrasikan alat Model Context Protocol untuk keupayaan agen edge yang dipertingkatkan
- **Penjanaan Kod**: Hasilkan kod siap pengeluaran yang dioptimumkan untuk senario pelaksanaan edge
- **Output Berstruktur**: Reka agen yang memberikan respons yang konsisten dan berstruktur sesuai untuk aplikasi edge

### 4. Penilaian dan Ujian Model
- **Metrik Prestasi**: Menilai model menggunakan metrik yang relevan untuk pelaksanaan edge (latensi, penggunaan memori, ketepatan)
- **Ujian Batch**: Uji pelbagai konfigurasi model secara serentak untuk mencari tetapan edge yang optimum
- **Penilaian Tersuai**: Cipta kriteria penilaian tersuai khusus untuk kes penggunaan AI Edge
- **Profil Sumber**: Analisis keperluan memori dan pengiraan untuk perancangan pelaksanaan edge

### 5. Penukaran dan Pengoptimuman Model
- **Penukaran ONNX**: Tukar model daripada pelbagai format kepada ONNX untuk keserasian edge
- **Kuantisasi**: Kurangkan saiz model dan tingkatkan kelajuan inferens melalui teknik kuantisasi
- **Pengoptimuman Perkakasan**: Optimumkan model untuk perkakasan edge tertentu (CPU, GPU, NPU)
- **Transformasi Format**: Transformasi model daripada Hugging Face dan sumber lain untuk pelaksanaan edge

### 6. Penyesuaian untuk Senario Edge
- **Penyesuaian Domain**: Sesuaikan model untuk kes penggunaan dan persekitaran edge tertentu
- **Latihan Tempatan**: Latih model secara tempatan dengan sokongan GPU untuk keperluan khusus edge
- **Integrasi Azure**: Manfaatkan Azure Container Apps untuk penyesuaian berasaskan awan sebelum pelaksanaan edge
- **Pembelajaran Pemindahan**: Sesuaikan model pra-latihan untuk tugas dan kekangan khusus edge

### 7. Pemantauan Prestasi dan Penjejakan
- **Analisis Prestasi Edge**: Pantau prestasi model dalam keadaan seperti edge
- **Pengumpulan Jejak**: Kumpulkan data prestasi terperinci untuk pengoptimuman
- **Pengenalpastian Halangan**: Kenal pasti isu prestasi sebelum pelaksanaan ke peranti edge
- **Penjejakan Penggunaan Sumber**: Pantau memori, CPU, dan masa inferens untuk pengoptimuman edge

## Aliran Kerja Pembangunan AI Edge

### Fasa 1: Penemuan dan Pemilihan Model
1. **Terokai Katalog Model**: Gunakan katalog model untuk mencari model yang sesuai untuk pelaksanaan edge
2. **Bandingkan Prestasi**: Nilai model berdasarkan saiz, ketepatan, dan kelajuan inferens
3. **Uji Secara Tempatan**: Gunakan model Ollama atau ONNX untuk ujian tempatan sebelum pelaksanaan edge
4. **Tentukan Keperluan Sumber**: Tentukan keperluan memori dan pengiraan untuk peranti edge sasaran

### Fasa 2: Pengoptimuman Model
1. **Tukar ke ONNX**: Tukar model terpilih ke format ONNX untuk keserasian edge
2. **Terapkan Kuantisasi**: Kurangkan saiz model melalui kuantisasi INT8 atau INT4
3. **Pengoptimuman Perkakasan**: Optimumkan untuk perkakasan edge sasaran (ARM, x86, pemecut khusus)
4. **Pengesahan Prestasi**: Sahkan model yang dioptimumkan mengekalkan ketepatan yang boleh diterima

### Fasa 3: Pembangunan Aplikasi
1. **Reka Bentuk Agen**: Gunakan Agent Builder untuk mencipta agen AI yang dioptimumkan untuk edge
2. **Kejuruteraan Prompt**: Bangunkan prompt yang berfungsi dengan berkesan dengan model yang lebih kecil
3. **Ujian Integrasi**: Uji agen dalam keadaan simulasi edge
4. **Penjanaan Kod**: Hasilkan kod pengeluaran yang dioptimumkan untuk pelaksanaan edge

### Fasa 4: Penilaian dan Ujian
1. **Penilaian Batch**: Uji pelbagai konfigurasi untuk mencari tetapan edge yang optimum
2. **Profil Prestasi**: Analisis kelajuan inferens, penggunaan memori, dan ketepatan
3. **Simulasi Edge**: Uji dalam keadaan yang serupa dengan persekitaran pelaksanaan edge sasaran
4. **Ujian Tekanan**: Nilai prestasi di bawah pelbagai keadaan beban

### Fasa 5: Persediaan Pelaksanaan
1. **Pengoptimuman Akhir**: Terapkan pengoptimuman akhir berdasarkan hasil ujian
2. **Pembungkusan Pelaksanaan**: Bungkus model dan kod untuk pelaksanaan edge
3. **Dokumentasi**: Dokumentasikan keperluan pelaksanaan dan konfigurasi
4. **Persediaan Pemantauan**: Sediakan pemantauan dan log untuk pelaksanaan edge

## Sasaran Pengguna untuk Pembangunan AI Edge

### Pembangun AI Edge
- Pembangun aplikasi yang membina peranti edge berkuasa AI dan penyelesaian IoT
- Pembangun sistem terbenam yang mengintegrasikan keupayaan AI ke dalam peranti dengan sumber terhad
- Pembangun mudah alih yang mencipta aplikasi AI pada peranti untuk telefon pintar dan tablet

### Jurutera AI Edge
- Jurutera AI yang mengoptimumkan model untuk pelaksanaan edge dan mengurus saluran inferens
- Jurutera DevOps yang melaksanakan dan mengurus model AI di infrastruktur edge yang teragih
- Jurutera prestasi yang mengoptimumkan beban kerja AI untuk kekangan perkakasan edge

### Penyelidik dan Pendidik
- Penyelidik AI yang membangunkan model dan algoritma cekap untuk pengkomputeran edge
- Pendidik yang mengajar konsep AI Edge dan menunjukkan teknik pengoptimuman
- Pelajar yang mempelajari cabaran dan penyelesaian dalam pelaksanaan AI Edge

## Kes Penggunaan AI Edge

### Peranti IoT Pintar
- **Pengecaman Imej Masa Nyata**: Melaksanakan model penglihatan komputer pada kamera dan sensor IoT
- **Pemprosesan Suara**: Melaksanakan pengecaman suara dan pemprosesan bahasa semula jadi pada pembesar suara pintar
- **Penyelenggaraan Ramalan**: Menjalankan model pengesanan anomali pada peranti edge industri
- **Pemantauan Alam Sekitar**: Melaksanakan model analisis data sensor untuk aplikasi alam sekitar

### Aplikasi Mudah Alih dan Terbenam
- **Terjemahan Pada Peranti**: Melaksanakan model terjemahan bahasa yang berfungsi luar talian
- **Realiti Terimbuh**: Melaksanakan pengecaman objek masa nyata dan penjejakan untuk aplikasi AR
- **Pemantauan Kesihatan**: Menjalankan model analisis kesihatan pada peranti boleh pakai dan peralatan perubatan
- **Sistem Autonomi**: Melaksanakan model membuat keputusan untuk dron, robot, dan kenderaan

### Infrastruktur Pengkomputeran Edge
- **Pusat Data Edge**: Melaksanakan model AI di pusat data edge untuk aplikasi latensi rendah
- **Integrasi CDN**: Mengintegrasikan keupayaan pemprosesan AI ke dalam rangkaian penghantaran kandungan
- **5G Edge**: Memanfaatkan pengkomputeran edge 5G untuk aplikasi berkuasa AI
- **Pengkomputeran Kabus**: Melaksanakan pemprosesan AI dalam persekitaran pengkomputeran kabus

## Pemasangan dan Persediaan

### Pemasangan Pantas
Pasang sambungan AI Toolkit terus dari Visual Studio Code Marketplace:

```
Install: AI Toolkit for Visual Studio Code (ms-windows-ai-studio.windows-ai-studio)
```

### Prasyarat untuk Pembangunan AI Edge
- **ONNX Runtime**: Pasang ONNX Runtime untuk inferens model
- **Ollama** (Pilihan): Pasang Ollama untuk pelayan model tempatan
- **Persekitaran Python**: Sediakan Python dengan pustaka AI yang diperlukan
- **Alat Perkakasan Edge**: Pasang alat pembangunan khusus perkakasan (CUDA, OpenVINO, dll.)

### Konfigurasi Awal
1. Buka VS Code dan pasang sambungan AI Toolkit
2. Konfigurasikan sumber model (ONNX, Ollama, penyedia awan)
3. Sediakan persekitaran pembangunan tempatan untuk ujian edge
4. Konfigurasikan pilihan pecutan perkakasan untuk mesin pembangunan anda

## Memulakan Pembangunan AI Edge

### Langkah 1: Pemilihan Model
1. Buka paparan AI Toolkit di Activity Bar
2. Semak imbas Katalog Model untuk model yang serasi dengan edge
3. Tapis mengikut saiz model, format (ONNX), dan ciri prestasi
4. Bandingkan model menggunakan alat perbandingan terbina

### Langkah 2: Ujian Tempatan
1. Gunakan Playground untuk menguji model yang dipilih secara tempatan
2. Bereksperimen dengan prompt dan parameter yang berbeza
3. Pantau metrik prestasi semasa ujian
4. Nilai respons model untuk keperluan kes penggunaan edge

### Langkah 3: Pengoptimuman Model
1. Gunakan alat Penukaran Model untuk dioptimumkan bagi pelaksanaan edge
2. Terapkan kuantisasi untuk mengurangkan saiz model
3. Uji model yang dioptimumkan untuk memastikan prestasi yang boleh diterima
4. Dokumentasikan tetapan pengoptimuman dan kompromi prestasi

### Langkah 4: Pembangunan Agen
1. Gunakan Agent Builder untuk mencipta agen AI yang dioptimumkan untuk edge
2. Bangunkan prompt yang berfungsi dengan berkesan dengan model yang lebih kecil
3. Integrasikan alat dan API yang diperlukan untuk senario edge
4. Uji agen dalam keadaan simulasi edge

### Langkah 5: Penilaian dan Pelaksanaan
1. Gunakan penilaian pukal untuk menguji pelbagai konfigurasi
2. Profilkan prestasi di bawah pelbagai keadaan
3. Sediakan pakej pelaksanaan untuk peranti edge sasaran
4. Sediakan pemantauan dan log untuk pelaksanaan pengeluaran

## Amalan Terbaik untuk Pembangunan AI Edge

### Pemilihan Model
- **Kekangan Saiz**: Pilih model yang sesuai dengan had memori peranti sasaran
- **Kelajuan Inferens**: Utamakan model dengan masa inferens yang pantas untuk aplikasi masa nyata
- **Kompromi Ketepatan**: Seimbangkan ketepatan model dengan kekangan sumber
- **Keserasian Format**: Utamakan format ONNX atau format yang dioptimumkan perkakasan untuk pelaksanaan edge

### Teknik Pengoptimuman
- **Kuantisasi**: Gunakan kuantisasi INT8 atau INT4 untuk mengurangkan saiz model dan meningkatkan kelajuan
- **Pemangkasan**: Buang parameter model yang tidak diperlukan untuk mengurangkan keperluan pengiraan
- **Distilasi Pengetahuan**: Cipta model yang lebih kecil yang mengekalkan prestasi model yang lebih besar
- **Pecutan Perkakasan**: Manfaatkan NPU, GPU, atau pemecut khusus apabila tersedia

### Aliran Kerja Pembangunan
- **Ujian Iteratif**: Uji dengan kerap dalam keadaan seperti edge semasa pembangunan
- **Pemantauan Prestasi**: Pantau penggunaan sumber dan kelajuan inferens secara berterusan
- **Kawalan Versi**: Jejak versi model dan tetapan pengoptimuman
- **Dokumentasi**: Dokumentasikan semua keputusan pengoptimuman dan kompromi prestasi

### Pertimbangan Pelaksanaan
- **Pemantauan Sumber**: Pantau memori, CPU, dan penggunaan kuasa dalam pengeluaran
- **Strategi Sandaran**: Laksanakan mekanisme sandaran untuk kegagalan model
- **Mekanisme Kemas Kini**: Rancang untuk kemas kini model dan pengurusan versi
- **Keselamatan**: Laksanakan langkah keselamatan yang sesuai untuk aplikasi AI di hujung rangkaian

## Integrasi dengan Rangka Kerja AI di Hujung Rangkaian

### ONNX Runtime
- **Penggunaan Merentas Platform**: Gunakan model ONNX di pelbagai platform hujung rangkaian
- **Pengoptimuman Perkakasan**: Manfaatkan pengoptimuman perkakasan khusus ONNX Runtime
- **Sokongan Mudah Alih**: Gunakan ONNX Runtime Mobile untuk aplikasi telefon pintar dan tablet
- **Integrasi IoT**: Gunakan pada peranti IoT dengan edaran ringan ONNX Runtime

### Windows ML
- **Peranti Windows**: Optimumkan untuk peranti hujung rangkaian dan PC berasaskan Windows
- **Pecutan NPU**: Manfaatkan Unit Pemprosesan Neural pada peranti Windows
- **DirectML**: Gunakan DirectML untuk pecutan GPU pada platform Windows
- **Integrasi UWP**: Integrasi dengan aplikasi Universal Windows Platform

### TensorFlow Lite
- **Pengoptimuman Mudah Alih**: Gunakan model TensorFlow Lite pada peranti mudah alih dan tertanam
- **Delegasi Perkakasan**: Gunakan delegasi perkakasan khusus untuk pecutan
- **Mikro Pengawal**: Gunakan pada mikro pengawal dengan TensorFlow Lite Micro
- **Sokongan Merentas Platform**: Gunakan pada Android, iOS, dan sistem Linux tertanam

### Azure IoT Edge
- **Hibrid Awan-Hujung**: Gabungkan latihan awan dengan inferens di hujung rangkaian
- **Penggunaan Modul**: Gunakan model AI sebagai modul IoT Edge
- **Pengurusan Peranti**: Urus peranti hujung rangkaian dan kemas kini model dari jauh
- **Telemetri**: Kumpul data prestasi dan metrik model dari penggunaan di hujung rangkaian

## Senario AI di Hujung Rangkaian yang Lanjutan

### Penggunaan Pelbagai Model
- **Ensemble Model**: Gunakan pelbagai model untuk meningkatkan ketepatan atau redundansi
- **Ujian A/B**: Uji model yang berbeza secara serentak pada peranti hujung rangkaian
- **Pemilihan Dinamik**: Pilih model berdasarkan keadaan semasa peranti
- **Perkongsian Sumber**: Optimumkan penggunaan sumber di antara pelbagai model yang digunakan

### Pembelajaran Teragih
- **Latihan Teragih**: Latih model di pelbagai peranti hujung rangkaian
- **Pemeliharaan Privasi**: Kekalkan data latihan secara tempatan sambil berkongsi peningkatan model
- **Pembelajaran Kolaboratif**: Benarkan peranti belajar daripada pengalaman kolektif
- **Penyelarasan Hujung-Awan**: Selaraskan pembelajaran antara peranti hujung rangkaian dan infrastruktur awan

### Pemprosesan Masa Nyata
- **Pemprosesan Aliran**: Proses aliran data berterusan pada peranti hujung rangkaian
- **Inferens Rendah-Laten**: Optimumkan untuk latensi inferens yang minimum
- **Pemprosesan Kumpulan**: Proses kumpulan data dengan cekap pada peranti hujung rangkaian
- **Pemprosesan Adaptif**: Sesuaikan pemprosesan berdasarkan keupayaan semasa peranti

## Penyelesaian Masalah Pembangunan AI di Hujung Rangkaian

### Isu Biasa
- **Kekangan Memori**: Model terlalu besar untuk memori peranti sasaran
- **Kelajuan Inferens**: Inferens model terlalu perlahan untuk keperluan masa nyata
- **Kemerosotan Ketepatan**: Pengoptimuman mengurangkan ketepatan model secara tidak boleh diterima
- **Keserasian Perkakasan**: Model tidak serasi dengan perkakasan sasaran

### Strategi Penyahpepijat
- **Profil Prestasi**: Gunakan ciri penjejakan AI Toolkit untuk mengenal pasti halangan
- **Pemantauan Sumber**: Pantau penggunaan memori dan CPU semasa pembangunan
- **Ujian Berperingkat**: Uji pengoptimuman secara berperingkat untuk mengasingkan isu
- **Simulasi Perkakasan**: Gunakan alat pembangunan untuk mensimulasikan perkakasan sasaran

### Penyelesaian Pengoptimuman
- **Kuantisasi Lanjutan**: Terapkan teknik kuantisasi yang lebih agresif
- **Seni Bina Model**: Pertimbangkan seni bina model yang dioptimumkan untuk hujung rangkaian
- **Pengoptimuman Prapemprosesan**: Optimumkan prapemprosesan data untuk kekangan hujung rangkaian
- **Pengoptimuman Inferens**: Gunakan pengoptimuman inferens khusus perkakasan

## Sumber dan Langkah Seterusnya

### Dokumentasi
- [Panduan Model AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/models)
- [Dokumentasi Model Playground](https://code.visualstudio.com/docs/intelligentapps/playground)
- [Dokumentasi ONNX Runtime](https://onnxruntime.ai/)
- [Dokumentasi Windows ML](https://docs.microsoft.com/en-us/windows/ai/)

### Komuniti dan Sokongan
- [GitHub AI Toolkit VS Code](https://github.com/microsoft/vscode-ai-toolkit)
- [Komuniti ONNX](https://github.com/onnx/onnx)
- [Komuniti Pembangun AI di Hujung Rangkaian](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [Pasaran Sambungan VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Sumber Pembelajaran
- [Kursus Asas AI di Hujung Rangkaian](./Module01/README.md)
- [Panduan Model Bahasa Kecil](./Module02/README.md)
- [Strategi Penggunaan di Hujung Rangkaian](./Module03/README.md)
- [Pembangunan AI di Hujung Rangkaian Windows](./windowdeveloper.md)

## Kesimpulan

AI Toolkit untuk Visual Studio Code menyediakan platform yang komprehensif untuk pembangunan AI di hujung rangkaian, daripada penemuan dan pengoptimuman model hingga penggunaan dan pemantauan. Dengan memanfaatkan alat dan aliran kerja yang terintegrasi, pembangun dapat mencipta, menguji, dan menggunakan aplikasi AI dengan cekap yang berfungsi dengan baik pada peranti hujung rangkaian yang mempunyai sumber terhad.

Sokongan toolkit untuk ONNX, Ollama, dan pelbagai penyedia awan, digabungkan dengan keupayaan pengoptimuman dan penilaian, menjadikannya pilihan yang ideal untuk pembangunan AI di hujung rangkaian. Sama ada anda membina aplikasi IoT, ciri AI mudah alih, atau sistem kecerdasan tertanam, AI Toolkit menyediakan alat dan aliran kerja yang diperlukan untuk penggunaan AI di hujung rangkaian yang berjaya.

Apabila AI di hujung rangkaian terus berkembang, AI Toolkit untuk VS Code kekal di barisan hadapan, menyediakan pembangun dengan alat dan keupayaan terkini untuk membina generasi seterusnya aplikasi pintar di hujung rangkaian.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.