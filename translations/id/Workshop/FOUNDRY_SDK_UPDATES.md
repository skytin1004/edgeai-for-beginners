<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T19:11:24+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "id"
}
-->
# Pembaruan Foundry Local SDK

## Ikhtisar

Notebook dan utilitas Workshop telah diperbarui untuk menggunakan **Foundry Local Python SDK resmi** dengan mengikuti pola dari:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## File yang Dimodifikasi

### 1. `Workshop/samples/workshop_utils.py`

**Perubahan:**
- ✅ Menambahkan penanganan kesalahan impor untuk paket `foundry-local-sdk`
- ✅ Meningkatkan dokumentasi dengan pola SDK resmi
- ✅ Memperbaiki logging dengan simbol Unicode (✓, ✗, ⚠)
- ✅ Menambahkan docstring yang komprehensif dengan contoh
- ✅ Pesan kesalahan yang lebih baik dengan referensi perintah CLI
- ✅ Memperbarui komentar agar sesuai dengan dokumentasi SDK resmi

**Peningkatan Utama:**

#### Penanganan Kesalahan Impor
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Fungsi `get_client()` yang Ditingkatkan
- Menambahkan dokumentasi rinci tentang pola inisialisasi SDK
- Menjelaskan bahwa `FoundryLocalManager` secara otomatis memulai layanan
- Menjelaskan resolusi alias model ke varian yang dioptimalkan untuk perangkat keras
- Memperbaiki logging dengan informasi endpoint
- Pesan kesalahan yang lebih baik dengan saran langkah pemecahan masalah

#### Fungsi `chat_once()` yang Ditingkatkan
- Menambahkan docstring komprehensif dengan contoh penggunaan
- Menjelaskan kompatibilitas dengan OpenAI SDK
- Mendokumentasikan dukungan streaming (melalui kwargs)
- Pesan kesalahan yang lebih baik dengan saran perintah CLI
- Menambahkan catatan tentang pemeriksaan ketersediaan model

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Perubahan:**
- ✅ Memperbarui semua sel markdown dengan referensi SDK
- ✅ Memperbaiki komentar kode dengan penjelasan pola SDK
- ✅ Dokumentasi dan penjelasan sel yang ditingkatkan
- ✅ Menambahkan panduan pemecahan masalah
- ✅ Memperbarui katalog model (mengganti 'gpt-oss-20b' dengan 'phi-3.5-mini')
- ✅ Format output yang lebih baik dengan indikator visual
- ✅ Menambahkan tautan dan referensi SDK di seluruh bagian

**Pembaruan Sel-per-Sel:**

#### Sel 1 (Judul)
- Menambahkan tautan dokumentasi SDK
- Merujuk ke repositori GitHub resmi

#### Sel 2 (Skenario)
- Diformat ulang dengan langkah-langkah bernomor
- Menjelaskan pola routing berbasis intent
- Menekankan manfaat eksekusi lokal

#### Sel 3 (Instalasi Dependensi)
- Menambahkan penjelasan tentang apa yang disediakan setiap paket
- Mendokumentasikan kemampuan SDK (resolusi alias, optimasi perangkat keras)

#### Sel 4 (Pengaturan Lingkungan)
- Docstring fungsi yang ditingkatkan
- Menambahkan komentar inline yang menjelaskan pola SDK
- Mendokumentasikan struktur katalog model
- Menjelaskan pencocokan prioritas/kemampuan

#### Sel 5 (Pemeriksaan Katalog)
- Menambahkan tanda centang visual (✓)
- Format output yang lebih baik

#### Sel 6 (Uji Deteksi Intent)
- Format output ulang menjadi gaya tabel
- Menampilkan intent dan model yang dipilih

#### Sel 7 (Fungsi Routing)
- Penjelasan pola SDK yang komprehensif
- Mendokumentasikan alur inisialisasi
- Mencantumkan semua fitur (retry, tracking, errors)
- Menambahkan tautan referensi SDK

#### Sel 8 (Demo Batch)
- Penjelasan yang lebih baik tentang apa yang diharapkan
- Menambahkan bagian pemecahan masalah
- Menyertakan perintah CLI untuk debugging
- Format tampilan output yang lebih baik

### 3. `Workshop/notebooks/session06_README.md` (File Baru)

**Membuat dokumentasi komprehensif yang mencakup:**

1. **Ikhtisar**: Diagram arsitektur dan penjelasan komponen
2. **Integrasi SDK**: Contoh kode mengikuti pola resmi
3. **Prasyarat**: Instruksi pengaturan langkah demi langkah
4. **Penggunaan**: Cara menjalankan dan menyesuaikan notebook
5. **Alias Model**: Penjelasan tentang varian yang dioptimalkan untuk perangkat keras
6. **Pemecahan Masalah**: Masalah umum dan solusinya
7. **Ekstensi**: Cara menambahkan intent, model, dan logika kustom
8. **Tips Performa**: Praktik terbaik untuk penggunaan produksi
9. **Sumber Daya**: Tautan ke dokumen resmi dan komunitas

## Implementasi Pola SDK

### Pola Resmi (dari dokumen Foundry Local)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### Implementasi Kami (di workshop_utils)

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**Manfaat Pendekatan Kami:**
- ✅ Mengikuti pola SDK resmi secara tepat
- ✅ Menambahkan caching untuk menghindari inisialisasi berulang
- ✅ Menyertakan logika retry untuk ketahanan produksi
- ✅ Mendukung pelacakan penggunaan token
- ✅ Memberikan pesan kesalahan yang lebih baik
- ✅ Tetap kompatibel dengan contoh resmi

## Perubahan Katalog Model

### Sebelumnya
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Setelah
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alasan:** Mengganti 'gpt-oss-20b' (alias non-standar) dengan 'phi-3.5-mini' (alias resmi Foundry Local).

## Dependensi

### Diperbarui requirements.txt

File requirements.txt Workshop sudah mencakup:
```
foundry-local-sdk
openai>=1.30.0
```

Ini adalah satu-satunya paket yang diperlukan untuk integrasi Foundry Local.

## Pengujian Pembaruan

### 1. Verifikasi Foundry Local Berjalan

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Periksa Model yang Tersedia

```bash
foundry model ls
```

Pastikan model berikut tersedia atau akan diunduh otomatis:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Jalankan Notebook

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Atau buka di VS Code dan jalankan semua sel.

### 4. Perilaku yang Diharapkan

**Sel 1 (Instalasi):** Berhasil menginstal paket  
**Sel 2 (Pengaturan):** Tidak ada kesalahan, impor berhasil  
**Sel 3 (Verifikasi):** Menampilkan ✓ dengan daftar model  
**Sel 4 (Uji Intent):** Menampilkan hasil deteksi intent  
**Sel 5 (Router):** Menampilkan ✓ Fungsi routing siap  
**Sel 6 (Eksekusi):** Merutekan prompt ke model, menampilkan hasil  

### 5. Pemecahan Masalah Kesalahan Koneksi

Jika Anda melihat `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Variabel Lingkungan

Variabel lingkungan berikut didukung:

| Variabel | Default | Deskripsi |
|----------|---------|-----------|
| `SHOW_USAGE` | `0` | Atur ke `1` untuk mencetak penggunaan token |
| `RETRY_ON_FAIL` | `1` | Aktifkan logika retry |
| `RETRY_BACKOFF` | `1.0` | Penundaan retry awal (detik) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Ganti endpoint layanan |

### Contoh Penggunaan

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migrasi dari Pola Lama

Jika Anda memiliki kode yang menggunakan panggilan API langsung, berikut cara migrasinya:

### Sebelum (API Langsung)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### Setelah (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### Manfaat Migrasi
- ✅ Manajemen layanan otomatis
- ✅ Resolusi alias model
- ✅ Pemilihan optimasi perangkat keras
- ✅ Penanganan kesalahan yang lebih baik
- ✅ Kompatibilitas dengan OpenAI SDK
- ✅ Dukungan streaming

## Referensi

### Dokumentasi Resmi
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Sumber SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Referensi CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Pemecahan Masalah**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Sumber Daya Workshop
- **README Sesi 06**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Notebook Contoh**: `Workshop/notebooks/session06_models_router.ipynb`

### Komunitas
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Langkah Selanjutnya

1. **Tinjau Perubahan**: Baca file yang diperbarui  
2. **Uji Notebook**: Jalankan session06_models_router.ipynb  
3. **Verifikasi SDK**: Pastikan foundry-local-sdk terinstal  
4. **Periksa Layanan**: Konfirmasi Foundry Local berjalan  
5. **Jelajahi Dokumen**: Baca session06_README.md yang baru  

## Ringkasan

Pembaruan ini memastikan materi Workshop mengikuti **pola SDK Foundry Local resmi** persis seperti yang didokumentasikan di repositori GitHub. Semua contoh kode, dokumentasi, dan utilitas sekarang selaras dengan praktik terbaik yang direkomendasikan Microsoft untuk penerapan model AI lokal.

Perubahan ini meningkatkan:
- ✅ **Kebenaran**: Menggunakan pola SDK resmi  
- ✅ **Dokumentasi**: Penjelasan dan contoh yang komprehensif  
- ✅ **Penanganan Kesalahan**: Pesan dan panduan pemecahan masalah yang lebih baik  
- ✅ **Pemeliharaan**: Mengikuti konvensi resmi  
- ✅ **Pengalaman Pengguna**: Instruksi yang lebih jelas dan bantuan debugging  

---

**Diperbarui:** 8 Oktober 2025  
**Versi SDK:** foundry-local-sdk (terbaru)  
**Cabang Workshop:** Reactor

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.