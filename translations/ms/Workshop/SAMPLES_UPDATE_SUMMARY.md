<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-09T19:30:28+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "ms"
}
-->
# Contoh Bengkel - Ringkasan Kemas Kini Foundry Local SDK

## Gambaran Keseluruhan

Semua contoh Python dalam direktori `Workshop/samples` telah dikemas kini untuk mengikuti amalan terbaik Foundry Local SDK dan memastikan konsistensi di seluruh bengkel.

**Tarikh**: 8 Oktober 2025  
**Skop**: 9 fail Python merangkumi 6 sesi bengkel  
**Fokus Utama**: Pengendalian ralat, dokumentasi, corak SDK, pengalaman pengguna

---

## Fail yang Dikemas Kini

### Sesi 01: Memulakan
- ✅ `chat_bootstrap.py` - Contoh asas sembang dan penstriman

### Sesi 02: Penyelesaian RAG
- ✅ `rag_pipeline.py` - Pelaksanaan RAG dengan embeddings
- ✅ `rag_eval_ragas.py` - Penilaian RAG dengan metrik RAGAS

### Sesi 03: Model Sumber Terbuka
- ✅ `benchmark_oss_models.py` - Penanda aras pelbagai model

### Sesi 04: Model Terkini
- ✅ `model_compare.py` - Perbandingan SLM vs LLM

### Sesi 05: Agen Berkuasa AI
- ✅ `agents_orchestrator.py` - Penyelarasan pelbagai agen

### Sesi 06: Model Sebagai Alat
- ✅ `models_router.py` - Penghalaan model berdasarkan niat
- ✅ `models_pipeline.py` - Saluran berperingkat pelbagai langkah

### Infrastruktur Sokongan
- ✅ `workshop_utils.py` - Sudah mengikuti amalan terbaik (tiada perubahan diperlukan)

---

## Penambahbaikan Utama

### 1. Pengendalian Ralat yang Dipertingkatkan

**Sebelum:**
```python
manager, client, model_id = get_client(alias)
```

**Selepas:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Manfaat:**
- Pengendalian ralat yang lebih baik dengan mesej ralat yang jelas
- Petunjuk penyelesaian masalah yang boleh diambil tindakan
- Kod keluar yang sesuai untuk skrip

### 2. Pengurusan Import yang Lebih Baik

**Sebelum:**
```python
from sentence_transformers import SentenceTransformer
```

**Selepas:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Manfaat:**
- Panduan jelas apabila kebergantungan tiada
- Mengelakkan ralat import yang tidak jelas
- Arahan pemasangan yang mesra pengguna

### 3. Dokumentasi Komprehensif

**Ditambah pada semua contoh:**
- Dokumentasi pembolehubah persekitaran dalam docstring
- Pautan rujukan SDK
- Contoh penggunaan
- Dokumentasi fungsi/parameter yang terperinci
- Petunjuk jenis untuk sokongan IDE yang lebih baik

**Contoh:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. Maklum Balas Pengguna yang Dipertingkatkan

**Ditambah log maklumat:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Penunjuk kemajuan:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Output berstruktur:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Penanda Aras yang Kukuh

**Penambahbaikan Sesi 03:**
- Pengendalian ralat per model (teruskan jika berlaku kegagalan)
- Pelaporan kemajuan yang terperinci
- Pusingan pemanasan dilaksanakan dengan betul
- Sokongan pengukuran latensi token pertama
- Pemisahan peringkat yang jelas

### 6. Petunjuk Jenis yang Konsisten

**Ditambah di seluruh:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Manfaat:**
- Autolengkap IDE yang lebih baik
- Pengesanan ralat awal
- Kod yang lebih mudah difahami

### 7. Penghala Model yang Dipertingkatkan

**Penambahbaikan Sesi 06:**
- Dokumentasi pengesanan niat yang komprehensif
- Penjelasan algoritma pemilihan model
- Log penghalaan yang terperinci
- Pemformatan output ujian
- Pemulihan ralat dalam ujian batch

### 8. Penyelarasan Pelbagai Agen

**Penambahbaikan Sesi 05:**
- Pelaporan kemajuan peringkat demi peringkat
- Pengendalian ralat per agen
- Struktur saluran yang jelas
- Dokumentasi pengurusan memori yang lebih baik

---

## Senarai Semak Ujian

### Prasyarat
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Uji Setiap Contoh

#### Sesi 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

#### Sesi 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```

#### Sesi 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```

#### Sesi 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```

#### Sesi 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```

#### Sesi 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```

---

## Rujukan Pembolehubah Persekitaran

### Global (Semua Contoh)
| Pembolehubah | Penerangan | Lalai |
|--------------|------------|-------|
| `FOUNDRY_LOCAL_ALIAS` | Alias model yang digunakan | Berbeza mengikut contoh |
| `FOUNDRY_LOCAL_ENDPOINT` | Gantikan titik akhir perkhidmatan | Dikesan secara automatik |
| `SHOW_USAGE` | Paparkan penggunaan token | `0` |
| `RETRY_ON_FAIL` | Aktifkan logik cubaan semula | `1` |
| `RETRY_BACKOFF` | Kelewatan cubaan semula awal | `1.0` |

### Khusus Contoh
| Pembolehubah | Digunakan Oleh | Penerangan |
|--------------|---------------|------------|
| `EMBED_MODEL` | Sesi 02 | Nama model embedding |
| `RAG_QUESTION` | Sesi 02 | Soalan ujian untuk RAG |
| `BENCH_MODELS` | Sesi 03 | Model yang dipisahkan dengan koma untuk penanda aras |
| `BENCH_ROUNDS` | Sesi 03 | Bilangan pusingan penanda aras |
| `BENCH_PROMPT` | Sesi 03 | Prompt ujian untuk penanda aras |
| `BENCH_STREAM` | Sesi 03 | Ukur latensi token pertama |
| `SLM_ALIAS` | Sesi 04 | Model bahasa kecil |
| `LLM_ALIAS` | Sesi 04 | Model bahasa besar |
| `COMPARE_PROMPT` | Sesi 04 | Prompt ujian perbandingan |
| `AGENT_MODEL_PRIMARY` | Sesi 05 | Model agen utama |
| `AGENT_MODEL_EDITOR` | Sesi 05 | Model agen editor |
| `AGENT_QUESTION` | Sesi 05 | Soalan ujian untuk agen |
| `PIPELINE_TASK` | Sesi 06 | Tugas untuk saluran |

---

## Perubahan Besar

**Tiada** - Semua perubahan adalah serasi ke belakang.

Skrip sedia ada akan terus berfungsi. Ciri baharu adalah:
- Pembolehubah persekitaran pilihan
- Mesej ralat yang dipertingkatkan (tidak merosakkan fungsi)
- Log tambahan (boleh disenyapkan)
- Petunjuk jenis yang lebih baik (tiada kesan masa jalan)

---

## Amalan Terbaik yang Dilaksanakan

### 1. Sentiasa Gunakan Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Corak Pengendalian Ralat yang Betul
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Log Maklumat
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Petunjuk Jenis
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Docstring Komprehensif
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. Sokongan Pembolehubah Persekitaran
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Penurunan Prestasi yang Lancar
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## Isu & Penyelesaian Biasa

### Isu: Ralat Import
**Penyelesaian:** Pasang kebergantungan yang hilang
```bash
pip install sentence-transformers ragas datasets numpy
```

### Isu: Ralat Sambungan
**Penyelesaian:** Pastikan Foundry Local sedang berjalan
```bash
foundry service status
foundry model run phi-4-mini
```

### Isu: Model Tidak Ditemui
**Penyelesaian:** Semak model yang tersedia
```bash
foundry model ls
foundry model download <alias>
```

### Isu: Prestasi Perlahan
**Penyelesaian:** Gunakan model yang lebih kecil atau laraskan parameter
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Langkah Seterusnya

### 1. Uji Semua Contoh
Laksanakan senarai semak ujian di atas untuk memastikan semua contoh berfungsi dengan betul.

### 2. Kemas Kini Dokumentasi
- Kemas kini fail markdown sesi dengan contoh baharu
- Tambah bahagian penyelesaian masalah ke README utama
- Cipta panduan rujukan pantas

### 3. Cipta Ujian Integrasi
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Tambah Penanda Aras Prestasi
Jejak penambahbaikan prestasi daripada peningkatan pengendalian ralat.

### 5. Maklum Balas Pengguna
Kumpulkan maklum balas daripada peserta bengkel mengenai:
- Kejelasan mesej ralat
- Kelengkapan dokumentasi
- Kemudahan penggunaan

---

## Sumber

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Rujukan Pantas**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Nota Migrasi**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Repositori Utama**: https://github.com/microsoft/Foundry-Local

---

## Penyelenggaraan

### Menambah Contoh Baharu
Ikuti corak ini semasa mencipta contoh baharu:

1. Gunakan `workshop_utils` untuk pengurusan klien
2. Tambah pengendalian ralat yang komprehensif
3. Sertakan sokongan pembolehubah persekitaran
4. Tambah petunjuk jenis dan docstring
5. Sediakan log maklumat
6. Sertakan contoh penggunaan dalam docstring
7. Pautkan ke dokumentasi SDK

### Menyemak Kemas Kini
Semasa menyemak kemas kini contoh, periksa:
- [ ] Pengendalian ralat pada semua operasi I/O
- [ ] Petunjuk jenis pada fungsi awam
- [ ] Docstring yang komprehensif
- [ ] Dokumentasi pembolehubah persekitaran
- [ ] Maklum balas pengguna yang bermaklumat
- [ ] Pautan rujukan SDK
- [ ] Gaya kod yang konsisten

---

**Ringkasan**: Semua contoh Python Bengkel kini mengikuti amalan terbaik Foundry Local SDK dengan pengendalian ralat yang dipertingkatkan, dokumentasi komprehensif, dan pengalaman pengguna yang lebih baik. Tiada perubahan besar - semua fungsi sedia ada dikekalkan dan dipertingkatkan.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.