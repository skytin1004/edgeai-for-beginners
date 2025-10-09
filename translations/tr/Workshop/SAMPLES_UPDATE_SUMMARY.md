<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-09T11:06:38+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "tr"
}
-->
# Atölye Örnekleri - Foundry Local SDK Güncelleme Özeti

## Genel Bakış

`Workshop/samples` dizinindeki tüm Python örnekleri, Foundry Local SDK en iyi uygulamalarına uygun hale getirilmiş ve atölye genelinde tutarlılık sağlanmıştır.

**Tarih**: 8 Ekim 2025  
**Kapsam**: 6 atölye oturumunda 9 Python dosyası  
**Ana Odak**: Hata yönetimi, dokümantasyon, SDK desenleri, kullanıcı deneyimi

---

## Güncellenen Dosyalar

### Oturum 01: Başlarken
- ✅ `chat_bootstrap.py` - Temel sohbet ve akış örnekleri

### Oturum 02: RAG Çözümleri
- ✅ `rag_pipeline.py` - Gömülü RAG uygulaması
- ✅ `rag_eval_ragas.py` - RAGAS metrikleriyle RAG değerlendirmesi

### Oturum 03: Açık Kaynak Modeller
- ✅ `benchmark_oss_models.py` - Çoklu model karşılaştırması

### Oturum 04: En Yeni Modeller
- ✅ `model_compare.py` - SLM ve LLM karşılaştırması

### Oturum 05: Yapay Zeka Destekli Ajanlar
- ✅ `agents_orchestrator.py` - Çoklu ajan koordinasyonu

### Oturum 06: Araç Olarak Modeller
- ✅ `models_router.py` - Niyet tabanlı model yönlendirme
- ✅ `models_pipeline.py` - Çok adımlı yönlendirilmiş işlem hattı

### Destekleyici Altyapı
- ✅ `workshop_utils.py` - Zaten en iyi uygulamalara uygun (değişiklik gerekmedi)

---

## Ana İyileştirmeler

### 1. Geliştirilmiş Hata Yönetimi

**Önce:**
```python
manager, client, model_id = get_client(alias)
```

**Sonra:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Faydalar:**
- Açık hata mesajlarıyla zarif hata yönetimi
- Eyleme geçirilebilir sorun giderme ipuçları
- Betikler için uygun çıkış kodları

### 2. Daha İyi İçe Aktarma Yönetimi

**Önce:**
```python
from sentence_transformers import SentenceTransformer
```

**Sonra:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Faydalar:**
- Eksik bağımlılıklar için net rehberlik
- Anlaşılmaz içe aktarma hatalarını önler
- Kullanıcı dostu kurulum talimatları

### 3. Kapsamlı Dokümantasyon

**Tüm örneklere eklenenler:**
- Docstring'lerde ortam değişkeni dokümantasyonu
- SDK referans bağlantıları
- Kullanım örnekleri
- Ayrıntılı fonksiyon/parametre dokümantasyonu
- Daha iyi IDE desteği için tür ipuçları

**Örnek:**
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

### 4. Geliştirilmiş Kullanıcı Geri Bildirimi

**Bilgilendirici günlükler eklendi:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**İlerleme göstergeleri:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Yapılandırılmış çıktı:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Sağlam Karşılaştırma

**Oturum 03 iyileştirmeleri:**
- Model başına hata yönetimi (hata durumunda devam eder)
- Ayrıntılı ilerleme raporlama
- Isınma turları düzgün bir şekilde yürütüldü
- İlk token gecikme ölçümü desteği
- Aşamaların net ayrımı

### 6. Tutarlı Tür İpuçları

**Her yerde eklendi:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Faydalar:**
- Daha iyi IDE otomatik tamamlama
- Erken hata tespiti
- Kendini belgeleyen kod

### 7. Geliştirilmiş Model Yönlendirici

**Oturum 06 iyileştirmeleri:**
- Kapsamlı niyet algılama dokümantasyonu
- Model seçme algoritması açıklaması
- Ayrıntılı yönlendirme günlükleri
- Test çıktısı formatlama
- Toplu testlerde hata kurtarma

### 8. Çoklu Ajan Orkestrasyonu

**Oturum 05 iyileştirmeleri:**
- Aşama bazlı ilerleme raporlama
- Ajan başına hata yönetimi
- Net işlem hattı yapısı
- Daha iyi bellek yönetimi dokümantasyonu

---

## Test Kontrol Listesi

### Ön Koşullar
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Her Örneği Test Et

#### Oturum 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

#### Oturum 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```

#### Oturum 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```

#### Oturum 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```

#### Oturum 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```

#### Oturum 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```

---

## Ortam Değişkenleri Referansı

### Genel (Tüm Örnekler)
| Değişken | Açıklama | Varsayılan |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Kullanılacak model takma adı | Örneğe göre değişir |
| `FOUNDRY_LOCAL_ENDPOINT` | Hizmet uç noktasını geçersiz kıl | Otomatik algılanır |
| `SHOW_USAGE` | Token kullanımını göster | `0` |
| `RETRY_ON_FAIL` | Yeniden deneme mantığını etkinleştir | `1` |
| `RETRY_BACKOFF` | İlk yeniden deneme gecikmesi | `1.0` |

### Örnek Bazlı
| Değişken | Kullanıldığı Yer | Açıklama |
|----------|------------------|-------------|
| `EMBED_MODEL` | Oturum 02 | Gömülü model adı |
| `RAG_QUESTION` | Oturum 02 | RAG için test sorusu |
| `BENCH_MODELS` | Oturum 03 | Karşılaştırılacak modeller (virgülle ayrılmış) |
| `BENCH_ROUNDS` | Oturum 03 | Karşılaştırma turları sayısı |
| `BENCH_PROMPT` | Oturum 03 | Karşılaştırmalar için test istemi |
| `BENCH_STREAM` | Oturum 03 | İlk token gecikmesini ölç |
| `SLM_ALIAS` | Oturum 04 | Küçük dil modeli |
| `LLM_ALIAS` | Oturum 04 | Büyük dil modeli |
| `COMPARE_PROMPT` | Oturum 04 | Karşılaştırma test istemi |
| `AGENT_MODEL_PRIMARY` | Oturum 05 | Birincil ajan modeli |
| `AGENT_MODEL_EDITOR` | Oturum 05 | Editör ajan modeli |
| `AGENT_QUESTION` | Oturum 05 | Ajanlar için test sorusu |
| `PIPELINE_TASK` | Oturum 06 | İşlem hattı görevi |

---

## Geriye Dönük Uyumsuzluklar

**Yok** - Tüm değişiklikler geriye dönük uyumludur.

Mevcut betikler çalışmaya devam edecektir. Yeni özellikler:
- İsteğe bağlı ortam değişkenleri
- Geliştirilmiş hata mesajları (işlevselliği bozmaz)
- Ek günlükleme (bastırılabilir)
- Daha iyi tür ipuçları (çalışma zamanında etkisi yok)

---

## Uygulanan En İyi Uygulamalar

### 1. Her Zaman Workshop Utils Kullanın
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Doğru Hata Yönetimi Deseni
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Bilgilendirici Günlükleme
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Tür İpuçları
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Kapsamlı Docstring'ler
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

### 6. Ortam Değişkeni Desteği
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Zarif Bozulma
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

## Yaygın Sorunlar ve Çözümleri

### Sorun: İçe Aktarma Hataları
**Çözüm:** Eksik bağımlılıkları yükleyin
```bash
pip install sentence-transformers ragas datasets numpy
```

### Sorun: Bağlantı Hataları
**Çözüm:** Foundry Local'ın çalıştığından emin olun
```bash
foundry service status
foundry model run phi-4-mini
```

### Sorun: Model Bulunamadı
**Çözüm:** Mevcut modelleri kontrol edin
```bash
foundry model ls
foundry model download <alias>
```

### Sorun: Yavaş Performans
**Çözüm:** Daha küçük modeller kullanın veya parametreleri ayarlayın
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Sonraki Adımlar

### 1. Tüm Örnekleri Test Edin
Yukarıdaki test kontrol listesini kullanarak tüm örneklerin doğru çalıştığını doğrulayın.

### 2. Dokümantasyonu Güncelleyin
- Yeni örneklerle oturum markdown dosyalarını güncelleyin
- Ana README'ye sorun giderme bölümü ekleyin
- Hızlı referans kılavuzu oluşturun

### 3. Entegrasyon Testleri Oluşturun
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Performans Karşılaştırmaları Ekleyin
Hata yönetimi iyileştirmelerinden kaynaklanan performans iyileştirmelerini takip edin.

### 5. Kullanıcı Geri Bildirimi
Atölye katılımcılarından şu konularda geri bildirim toplayın:
- Hata mesajlarının açıklığı
- Dokümantasyonun tamlığı
- Kullanım kolaylığı

---

## Kaynaklar

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **Hızlı Referans**: `Workshop/FOUNDRY_SDK_QUICKREF.md`  
- **Geçiş Notları**: `Workshop/SDK_MIGRATION_NOTES.md`  
- **Ana Depo**: https://github.com/microsoft/Foundry-Local  

---

## Bakım

### Yeni Örnekler Eklemek
Yeni örnekler oluştururken şu desenleri izleyin:

1. İstemci yönetimi için `workshop_utils` kullanın
2. Kapsamlı hata yönetimi ekleyin
3. Ortam değişkeni desteği ekleyin
4. Tür ipuçları ve docstring'ler ekleyin
5. Bilgilendirici günlükleme sağlayın
6. Docstring'de kullanım örnekleri ekleyin
7. SDK dokümantasyonuna bağlantı ekleyin

### Güncellemeleri İnceleme
Örnek güncellemelerini incelerken şunları kontrol edin:
- [ ] Tüm G/Ç işlemlerinde hata yönetimi
- [ ] Genel fonksiyonlarda tür ipuçları
- [ ] Kapsamlı docstring'ler
- [ ] Ortam değişkeni dokümantasyonu
- [ ] Bilgilendirici kullanıcı geri bildirimi
- [ ] SDK referans bağlantıları
- [ ] Tutarlı kod stili

---

**Özet**: Tüm Atölye Python örnekleri artık Foundry Local SDK en iyi uygulamalarını takip ediyor ve geliştirilmiş hata yönetimi, kapsamlı dokümantasyon ve iyileştirilmiş kullanıcı deneyimi sunuyor. Geriye dönük uyumsuzluk yok - mevcut işlevsellik korunmuş ve geliştirilmiştir.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.