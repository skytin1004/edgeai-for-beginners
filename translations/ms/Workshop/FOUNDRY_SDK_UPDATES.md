<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T19:11:56+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "ms"
}
-->
# Kemas Kini SDK Tempatan Foundry

## Gambaran Keseluruhan

Notebook dan utiliti Workshop telah dikemas kini untuk menggunakan **SDK Python Tempatan Foundry rasmi** dengan mengikuti corak daripada:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Fail yang Dikemas Kini

### 1. `Workshop/samples/workshop_utils.py`

**Perubahan:**
- ✅ Menambah pengendalian ralat import untuk pakej `foundry-local-sdk`
- ✅ Meningkatkan dokumentasi dengan corak SDK rasmi
- ✅ Memperbaiki log dengan simbol Unicode (✓, ✗, ⚠)
- ✅ Menambah docstring yang komprehensif dengan contoh
- ✅ Meningkatkan mesej ralat dengan rujukan kepada arahan CLI
- ✅ Mengemas kini komen untuk sepadan dengan dokumentasi SDK rasmi

**Penambahbaikan Utama:**

#### Pengendalian Ralat Import
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Fungsi `get_client()` yang Dipertingkatkan
- Menambah dokumentasi terperinci tentang corak inisialisasi SDK
- Menjelaskan bahawa `FoundryLocalManager` memulakan perkhidmatan secara automatik
- Menerangkan resolusi alias model kepada varian yang dioptimumkan untuk perkakasan
- Memperbaiki log dengan maklumat titik akhir
- Meningkatkan mesej ralat dengan cadangan langkah penyelesaian masalah

#### Fungsi `chat_once()` yang Dipertingkatkan
- Menambah docstring yang komprehensif dengan contoh penggunaan
- Menjelaskan keserasian SDK OpenAI
- Mendokumentasikan sokongan penstriman (melalui kwargs)
- Memperbaiki mesej ralat dengan cadangan arahan CLI
- Menambah nota tentang pemeriksaan ketersediaan model

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Perubahan:**
- ✅ Mengemas kini semua sel markdown dengan rujukan SDK
- ✅ Memperbaiki komen kod dengan penjelasan corak SDK
- ✅ Meningkatkan dokumentasi dan penjelasan sel
- ✅ Menambah panduan penyelesaian masalah
- ✅ Mengemas kini katalog model (menggantikan 'gpt-oss-20b' dengan 'phi-3.5-mini')
- ✅ Memperbaiki format output dengan indikator visual
- ✅ Menambah pautan dan rujukan SDK di seluruh dokumen

**Kemas Kini Sel demi Sel:**

#### Sel 1 (Tajuk)
- Menambah pautan dokumentasi SDK
- Merujuk repositori GitHub rasmi

#### Sel 2 (Senario)
- Memformat semula dengan langkah bernombor
- Menjelaskan corak penghalaan berdasarkan niat
- Menekankan manfaat pelaksanaan tempatan

#### Sel 3 (Pemasangan Kebergantungan)
- Menambah penjelasan tentang apa yang disediakan oleh setiap pakej
- Mendokumentasikan keupayaan SDK (resolusi alias, pengoptimuman perkakasan)

#### Sel 4 (Persediaan Persekitaran)
- Meningkatkan docstring fungsi
- Menambah komen dalam talian yang menerangkan corak SDK
- Mendokumentasikan struktur katalog model
- Menjelaskan pemadanan keutamaan/keupayaan

#### Sel 5 (Pemeriksaan Katalog)
- Menambah tanda semak visual (✓)
- Memformat output dengan lebih baik

#### Sel 6 (Ujian Pengesanan Niat)
- Memformat semula output sebagai gaya jadual
- Menunjukkan kedua-dua niat dan model yang dipilih

#### Sel 7 (Fungsi Penghalaan)
- Penjelasan corak SDK yang komprehensif
- Mendokumentasikan aliran inisialisasi
- Menyenaraikan semua ciri (cuba semula, penjejakan, ralat)
- Menambah pautan rujukan SDK

#### Sel 8 (Demo Batch)
- Meningkatkan penjelasan tentang apa yang dijangka
- Menambah bahagian penyelesaian masalah
- Menyertakan arahan CLI untuk debugging
- Memformat paparan output dengan lebih baik

### 3. `Workshop/notebooks/session06_README.md` (Fail Baru)

**Mencipta dokumentasi komprehensif yang merangkumi:**

1. **Gambaran Keseluruhan**: Diagram seni bina dan penjelasan komponen
2. **Integrasi SDK**: Contoh kod yang mengikuti corak rasmi
3. **Prasyarat**: Arahan persediaan langkah demi langkah
4. **Penggunaan**: Cara menjalankan dan menyesuaikan notebook
5. **Alias Model**: Penjelasan tentang varian yang dioptimumkan untuk perkakasan
6. **Penyelesaian Masalah**: Isu biasa dan penyelesaian
7. **Pengembangan**: Cara menambah niat, model, dan logik tersuai
8. **Petua Prestasi**: Amalan terbaik untuk penggunaan produksi
9. **Sumber**: Pautan kepada dokumen rasmi dan komuniti

## Pelaksanaan Corak SDK

### Corak Rasmi (daripada dokumen Foundry Local)

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

### Pelaksanaan Kami (dalam workshop_utils)

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
- ✅ Mengikuti corak SDK rasmi dengan tepat
- ✅ Menambah caching untuk mengelakkan inisialisasi berulang
- ✅ Menyertakan logik cuba semula untuk ketahanan produksi
- ✅ Menyokong penjejakan penggunaan token
- ✅ Memberikan mesej ralat yang lebih baik
- ✅ Kekal serasi dengan contoh rasmi

## Perubahan Katalog Model

### Sebelum
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Selepas
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Sebab:** Menggantikan 'gpt-oss-20b' (alias tidak standard) dengan 'phi-3.5-mini' (alias rasmi Foundry Local).

## Kebergantungan

### Kemas Kini requirements.txt

Fail requirements.txt Workshop sudah termasuk:
```
foundry-local-sdk
openai>=1.30.0
```

Ini adalah satu-satunya pakej yang diperlukan untuk integrasi Foundry Local.

## Ujian Kemas Kini

### 1. Sahkan Foundry Local Berjalan

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

Pastikan model berikut tersedia atau akan dimuat turun secara automatik:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Jalankan Notebook

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Atau buka dalam VS Code dan jalankan semua sel.

### 4. Tingkah Laku yang Dijangka

**Sel 1 (Pemasangan):** Berjaya memasang pakej
**Sel 2 (Persediaan):** Tiada ralat, import berfungsi
**Sel 3 (Pengesahan):** Menunjukkan ✓ dengan senarai model
**Sel 4 (Ujian Niat):** Menunjukkan hasil pengesanan niat
**Sel 5 (Penghala):** Menunjukkan ✓ Fungsi penghalaan sedia
**Sel 6 (Pelaksanaan):** Mengarahkan arahan kepada model, menunjukkan hasil

### 5. Penyelesaian Masalah Ralat Sambungan

Jika anda melihat `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Pembolehubah Persekitaran

Pembolehubah persekitaran berikut disokong:

| Pembolehubah | Lalai | Penerangan |
|--------------|-------|------------|
| `SHOW_USAGE` | `0` | Tetapkan kepada `1` untuk mencetak penggunaan token |
| `RETRY_ON_FAIL` | `1` | Aktifkan logik cuba semula |
| `RETRY_BACKOFF` | `1.0` | Kelewatan cuba semula awal (saat) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Ganti titik akhir perkhidmatan |

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

## Migrasi daripada Corak Lama

Jika anda mempunyai kod sedia ada yang menggunakan panggilan API langsung, berikut cara untuk bermigrasi:

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

### Selepas (SDK)
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
- ✅ Pengurusan perkhidmatan automatik
- ✅ Resolusi alias model
- ✅ Pemilihan pengoptimuman perkakasan
- ✅ Pengendalian ralat yang lebih baik
- ✅ Keserasian SDK OpenAI
- ✅ Sokongan penstriman

## Rujukan

### Dokumentasi Rasmi
- **GitHub Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Sumber SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Rujukan CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **API REST**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Penyelesaian Masalah**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Sumber Workshop
- **README Sesi 06**: `Workshop/notebooks/session06_README.md`
- **Utiliti Workshop**: `Workshop/samples/workshop_utils.py`
- **Notebook Contoh**: `Workshop/notebooks/session06_models_router.ipynb`

### Komuniti
- **Discord**: https://aka.ms/foundry-local-discord
- **Isu GitHub**: https://github.com/microsoft/Foundry-Local/issues

## Langkah Seterusnya

1. **Semak Perubahan**: Baca fail yang dikemas kini
2. **Uji Notebook**: Jalankan session06_models_router.ipynb
3. **Sahkan SDK**: Pastikan foundry-local-sdk dipasang
4. **Periksa Perkhidmatan**: Sahkan Foundry Local berjalan
5. **Terokai Dokumen**: Baca session06_README.md yang baru

## Ringkasan

Kemas kini ini memastikan bahan Workshop mengikuti **corak SDK Tempatan Foundry rasmi** seperti yang didokumentasikan dalam repositori GitHub. Semua contoh kod, dokumentasi, dan utiliti kini sejajar dengan amalan terbaik yang disyorkan oleh Microsoft untuk pelaksanaan model AI tempatan.

Perubahan ini meningkatkan:
- ✅ **Ketepatan**: Menggunakan corak SDK rasmi
- ✅ **Dokumentasi**: Penjelasan dan contoh yang komprehensif
- ✅ **Pengendalian Ralat**: Mesej dan panduan penyelesaian masalah yang lebih baik
- ✅ **Kebolehselenggaraan**: Mengikuti konvensyen rasmi
- ✅ **Pengalaman Pengguna**: Arahan yang lebih jelas dan bantuan debugging

---

**Dikemas Kini:** 8 Oktober 2025  
**Versi SDK:** foundry-local-sdk (terkini)  
**Cawangan Workshop:** Reactor

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.