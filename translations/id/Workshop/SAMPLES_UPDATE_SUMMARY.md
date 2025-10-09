<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-09T19:30:03+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "id"
}
-->
# Ringkasan Pembaruan SDK Lokal Foundry - Contoh Workshop

## Gambaran Umum

Semua contoh Python di direktori `Workshop/samples` telah diperbarui untuk mengikuti praktik terbaik SDK Lokal Foundry dan memastikan konsistensi di seluruh workshop.

**Tanggal**: 8 Oktober 2025  
**Lingkup**: 9 file Python di 6 sesi workshop  
**Fokus Utama**: Penanganan kesalahan, dokumentasi, pola SDK, pengalaman pengguna

---

## File yang Diperbarui

### Sesi 01: Memulai
- ✅ `chat_bootstrap.py` - Contoh dasar chat dan streaming

### Sesi 02: Solusi RAG
- ✅ `rag_pipeline.py` - Implementasi RAG dengan embeddings
- ✅ `rag_eval_ragas.py` - Evaluasi RAG dengan metrik RAGAS

### Sesi 03: Model Sumber Terbuka
- ✅ `benchmark_oss_models.py` - Benchmarking multi-model

### Sesi 04: Model Terkini
- ✅ `model_compare.py` - Perbandingan SLM vs LLM

### Sesi 05: Agen Berbasis AI
- ✅ `agents_orchestrator.py` - Koordinasi multi-agen

### Sesi 06: Model sebagai Alat
- ✅ `models_router.py` - Routing model berbasis intent
- ✅ `models_pipeline.py` - Pipeline multi-langkah yang diarahkan

### Infrastruktur Pendukung
- ✅ `workshop_utils.py` - Sudah mengikuti praktik terbaik (tidak ada perubahan yang diperlukan)

---

## Perbaikan Utama

### 1. Penanganan Kesalahan yang Ditingkatkan

**Sebelum:**
```python
manager, client, model_id = get_client(alias)
```

**Sesudah:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Manfaat:**
- Penanganan kesalahan yang lebih baik dengan pesan kesalahan yang jelas
- Petunjuk pemecahan masalah yang dapat ditindaklanjuti
- Kode keluar yang sesuai untuk scripting

### 2. Manajemen Impor yang Lebih Baik

**Sebelum:**
```python
from sentence_transformers import SentenceTransformer
```

**Sesudah:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Manfaat:**
- Panduan yang jelas saat dependensi hilang
- Mencegah kesalahan impor yang membingungkan
- Instruksi instalasi yang ramah pengguna

### 3. Dokumentasi Komprehensif

**Ditambahkan ke semua contoh:**
- Dokumentasi variabel lingkungan dalam docstring
- Tautan referensi SDK
- Contoh penggunaan
- Dokumentasi fungsi/parameter yang mendetail
- Petunjuk tipe untuk dukungan IDE yang lebih baik

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

### 4. Umpan Balik Pengguna yang Ditingkatkan

**Ditambahkan logging informatif:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Indikator progres:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Output terstruktur:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Benchmarking yang Kuat

**Perbaikan Sesi 03:**
- Penanganan kesalahan per-model (melanjutkan saat gagal)
- Pelaporan progres yang mendetail
- Eksekusi putaran pemanasan dengan benar
- Dukungan pengukuran latensi token pertama
- Pemisahan tahap yang jelas

### 6. Petunjuk Tipe yang Konsisten

**Ditambahkan di seluruh:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Manfaat:**
- Autocomplete IDE yang lebih baik
- Deteksi kesalahan lebih awal
- Kode yang lebih mudah dipahami

### 7. Router Model yang Ditingkatkan

**Perbaikan Sesi 06:**
- Dokumentasi deteksi intent yang komprehensif
- Penjelasan algoritma pemilihan model
- Log routing yang mendetail
- Format output pengujian
- Pemulihan kesalahan dalam pengujian batch

### 8. Orkestrasi Multi-Agen

**Perbaikan Sesi 05:**
- Pelaporan progres tahap demi tahap
- Penanganan kesalahan per-agen
- Struktur pipeline yang jelas
- Dokumentasi manajemen memori yang lebih baik

---

## Daftar Periksa Pengujian

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

## Referensi Variabel Lingkungan

### Global (Semua Contoh)
| Variabel | Deskripsi | Default |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias model yang digunakan | Bervariasi berdasarkan contoh |
| `FOUNDRY_LOCAL_ENDPOINT` | Menimpa endpoint layanan | Terdeteksi otomatis |
| `SHOW_USAGE` | Menampilkan penggunaan token | `0` |
| `RETRY_ON_FAIL` | Mengaktifkan logika retry | `1` |
| `RETRY_BACKOFF` | Penundaan retry awal | `1.0` |

### Spesifik Contoh
| Variabel | Digunakan Oleh | Deskripsi |
|----------|---------|-------------|
| `EMBED_MODEL` | Sesi 02 | Nama model embedding |
| `RAG_QUESTION` | Sesi 02 | Pertanyaan uji untuk RAG |
| `BENCH_MODELS` | Sesi 03 | Model yang di-benchmark (dipisahkan koma) |
| `BENCH_ROUNDS` | Sesi 03 | Jumlah putaran benchmark |
| `BENCH_PROMPT` | Sesi 03 | Prompt uji untuk benchmark |
| `BENCH_STREAM` | Sesi 03 | Mengukur latensi token pertama |
| `SLM_ALIAS` | Sesi 04 | Model bahasa kecil |
| `LLM_ALIAS` | Sesi 04 | Model bahasa besar |
| `COMPARE_PROMPT` | Sesi 04 | Prompt uji perbandingan |
| `AGENT_MODEL_PRIMARY` | Sesi 05 | Model agen utama |
| `AGENT_MODEL_EDITOR` | Sesi 05 | Model agen editor |
| `AGENT_QUESTION` | Sesi 05 | Pertanyaan uji untuk agen |
| `PIPELINE_TASK` | Sesi 06 | Tugas untuk pipeline |

---

## Perubahan yang Merusak

**Tidak Ada** - Semua perubahan kompatibel dengan versi sebelumnya.

Script yang ada akan tetap berfungsi. Fitur baru meliputi:
- Variabel lingkungan opsional
- Pesan kesalahan yang ditingkatkan (tidak merusak fungsionalitas)
- Logging tambahan (dapat disembunyikan)
- Petunjuk tipe yang lebih baik (tidak berdampak pada runtime)

---

## Praktik Terbaik yang Diterapkan

### 1. Selalu Gunakan Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Pola Penanganan Kesalahan yang Tepat
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Logging Informatif
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Petunjuk Tipe
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

### 6. Dukungan Variabel Lingkungan
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Degradasi yang Anggun
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

## Masalah Umum & Solusi

### Masalah: Kesalahan Impor
**Solusi:** Instal dependensi yang hilang
```bash
pip install sentence-transformers ragas datasets numpy
```

### Masalah: Kesalahan Koneksi
**Solusi:** Pastikan Foundry Lokal berjalan
```bash
foundry service status
foundry model run phi-4-mini
```

### Masalah: Model Tidak Ditemukan
**Solusi:** Periksa model yang tersedia
```bash
foundry model ls
foundry model download <alias>
```

### Masalah: Performa Lambat
**Solusi:** Gunakan model yang lebih kecil atau sesuaikan parameter
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Langkah Selanjutnya

### 1. Uji Semua Contoh
Ikuti daftar periksa pengujian di atas untuk memastikan semua contoh berfungsi dengan benar.

### 2. Perbarui Dokumentasi
- Perbarui file markdown sesi dengan contoh baru
- Tambahkan bagian pemecahan masalah ke README utama
- Buat panduan referensi cepat

### 3. Buat Pengujian Integrasi
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Tambahkan Benchmark Performa
Lacak peningkatan performa dari perbaikan penanganan kesalahan.

### 5. Umpan Balik Pengguna
Kumpulkan umpan balik dari peserta workshop tentang:
- Kejelasan pesan kesalahan
- Kelengkapan dokumentasi
- Kemudahan penggunaan

---

## Sumber Daya

- **SDK Lokal Foundry**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Referensi Cepat**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Catatan Migrasi**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Repositori Utama**: https://github.com/microsoft/Foundry-Local

---

## Pemeliharaan

### Menambahkan Contoh Baru
Ikuti pola ini saat membuat contoh baru:

1. Gunakan `workshop_utils` untuk manajemen klien
2. Tambahkan penanganan kesalahan yang komprehensif
3. Sertakan dukungan variabel lingkungan
4. Tambahkan petunjuk tipe dan docstring
5. Berikan logging informatif
6. Sertakan contoh penggunaan dalam docstring
7. Tautkan ke dokumentasi SDK

### Meninjau Pembaruan
Saat meninjau pembaruan contoh, periksa:
- [ ] Penanganan kesalahan pada semua operasi I/O
- [ ] Petunjuk tipe pada fungsi publik
- [ ] Docstring yang komprehensif
- [ ] Dokumentasi variabel lingkungan
- [ ] Umpan balik pengguna yang informatif
- [ ] Tautan referensi SDK
- [ ] Gaya kode yang konsisten

---

**Ringkasan**: Semua contoh Python Workshop kini mengikuti praktik terbaik SDK Lokal Foundry dengan penanganan kesalahan yang ditingkatkan, dokumentasi komprehensif, dan pengalaman pengguna yang lebih baik. Tidak ada perubahan yang merusak - semua fungsionalitas yang ada tetap terjaga dan ditingkatkan.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.