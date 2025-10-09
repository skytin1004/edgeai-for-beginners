<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T10:36:23+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "tr"
}
-->
# Foundry Local SDK Güncellemeleri

## Genel Bakış

**Resmi Foundry Local Python SDK**'yi doğru şekilde kullanmak için Workshop not defterleri ve yardımcı araçlar güncellendi. Aşağıdaki desenler takip edildi:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Değiştirilen Dosyalar

### 1. `Workshop/samples/workshop_utils.py`

**Değişiklikler:**
- ✅ `foundry-local-sdk` paketi için import hatası işleme eklendi
- ✅ Resmi SDK desenleriyle belgeler geliştirildi
- ✅ Unicode sembolleri (✓, ✗, ⚠) ile daha iyi günlükleme sağlandı
- ✅ Örneklerle kapsamlı docstring'ler eklendi
- ✅ CLI komutlarına referans veren daha iyi hata mesajları eklendi
- ✅ Resmi SDK belgelerine uygun hale getirmek için yorumlar güncellendi

**Ana İyileştirmeler:**

#### Import Hatası İşleme
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Geliştirilmiş `get_client()` Fonksiyonu
- SDK başlatma deseni hakkında ayrıntılı belgeler eklendi
- `FoundryLocalManager`'ın hizmeti otomatik olarak başlattığı açıklandı
- Donanım optimizasyonlu varyantlara model takma adı çözümlemesi açıklandı
- Endpoint bilgisiyle günlükleme geliştirildi
- Sorun giderme adımlarını öneren daha iyi hata mesajları eklendi

#### Geliştirilmiş `chat_once()` Fonksiyonu
- Kullanım örnekleriyle kapsamlı docstring eklendi
- OpenAI SDK uyumluluğu açıklandı
- Akış desteği (kwargs aracılığıyla) belgelenmiştir
- CLI komut önerileriyle daha iyi hata mesajları sağlandı
- Model kullanılabilirliği kontrolü hakkında notlar eklendi

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Değişiklikler:**
- ✅ Tüm markdown hücreleri SDK referanslarıyla güncellendi
- ✅ Kod yorumları SDK desen açıklamalarıyla geliştirildi
- ✅ Hücre belgeleri ve açıklamaları iyileştirildi
- ✅ Sorun giderme rehberi eklendi
- ✅ Model kataloğu güncellendi ('gpt-oss-20b' yerine 'phi-3.5-mini' kullanıldı)
- ✅ Görsel göstergelerle daha iyi çıktı formatlama sağlandı
- ✅ SDK bağlantıları ve referansları eklendi

**Hücre Bazında Güncellemeler:**

#### Hücre 1 (Başlık)
- SDK belgelerine bağlantılar eklendi
- Resmi GitHub depolarına referans verildi

#### Hücre 2 (Senaryo)
- Numaralandırılmış adımlarla yeniden formatlandı
- Amaç tabanlı yönlendirme deseni açıklandı
- Yerel çalıştırma avantajları vurgulandı

#### Hücre 3 (Bağımlılık Kurulumu)
- Her paketin ne sağladığı açıklandı
- SDK yetenekleri (takma ad çözümleme, donanım optimizasyonu) belgelenmiştir

#### Hücre 4 (Ortam Kurulumu)
- Fonksiyon docstring'leri geliştirildi
- SDK desenlerini açıklayan satır içi yorumlar eklendi
- Model kataloğu yapısı belgelenmiştir
- Öncelik/yetenek eşlemesi açıklandı

#### Hücre 5 (Katalog Kontrolü)
- Görsel onay işaretleri (✓) eklendi
- Daha iyi formatlanmış çıktı

#### Hücre 6 (Amaç Algılama Testi)
- Çıktı tablo tarzında yeniden formatlandı
- Hem amaç hem de seçilen model gösteriliyor

#### Hücre 7 (Yönlendirme Fonksiyonu)
- Kapsamlı SDK desen açıklaması
- Başlatma akışı belgelenmiştir
- Tüm özellikler listelenmiştir (yeniden deneme, izleme, hatalar)
- SDK referans bağlantısı eklendi

#### Hücre 8 (Toplu Demo)
- Beklenen sonuçların açıklaması geliştirildi
- Sorun giderme bölümü eklendi
- Hata ayıklama için CLI komutları dahil edildi
- Daha iyi formatlanmış çıktı görüntüsü

### 3. `Workshop/notebooks/session06_README.md` (Yeni Dosya)

**Kapsamlı belgeler oluşturuldu:**

1. **Genel Bakış**: Mimari diyagram ve bileşen açıklaması
2. **SDK Entegrasyonu**: Resmi desenleri takip eden kod örnekleri
3. **Ön Koşullar**: Adım adım kurulum talimatları
4. **Kullanım**: Not defterini nasıl çalıştıracağınız ve özelleştireceğiniz
5. **Model Takma Adları**: Donanım optimizasyonlu varyantların açıklaması
6. **Sorun Giderme**: Yaygın sorunlar ve çözümleri
7. **Genişletme**: Amaçlar, modeller ve özel mantık ekleme
8. **Performans İpuçları**: Üretim kullanımı için en iyi uygulamalar
9. **Kaynaklar**: Resmi belgeler ve topluluk bağlantıları

## SDK Desen Uygulaması

### Resmi Desen (Foundry Local belgelerinden)

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

### Workshop_utils'deki Uygulamamız

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

**Yaklaşımımızın Faydaları:**
- ✅ Resmi SDK desenini tam olarak takip eder
- ✅ Tekrar eden başlatmayı önlemek için önbellekleme ekler
- ✅ Üretim dayanıklılığı için yeniden deneme mantığı içerir
- ✅ Token kullanım takibini destekler
- ✅ Daha iyi hata mesajları sağlar
- ✅ Resmi örneklerle uyumlu kalır

## Model Kataloğu Değişiklikleri

### Önce
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Sonra
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Sebep:** 'gpt-oss-20b' (standart olmayan takma ad) yerine 'phi-3.5-mini' (resmi Foundry Local takma adı) kullanıldı.

## Bağımlılıklar

### Güncellenmiş requirements.txt

Workshop requirements.txt zaten şunları içeriyor:
```
foundry-local-sdk
openai>=1.30.0
```

Foundry Local entegrasyonu için yalnızca bu paketler gereklidir.

## Güncellemeleri Test Etme

### 1. Foundry Local'ın Çalıştığını Doğrulayın

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Mevcut Modelleri Kontrol Edin

```bash
foundry model ls
```

Bu modellerin mevcut olduğundan veya otomatik olarak indirileceğinden emin olun:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Not Defterini Çalıştırın

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Veya VS Code'da açıp tüm hücreleri çalıştırın.

### 4. Beklenen Davranış

**Hücre 1 (Kurulum):** Paketler başarıyla kurulur  
**Hücre 2 (Kurulum):** Hata yok, importlar çalışır  
**Hücre 3 (Doğrulama):** ✓ ile model listesi gösterir  
**Hücre 4 (Amaç Testi):** Amaç algılama sonuçlarını gösterir  
**Hücre 5 (Yönlendirme):** ✓ Yönlendirme fonksiyonu hazır  
**Hücre 6 (Çalıştırma):** İstekleri modellere yönlendirir, sonuçları gösterir  

### 5. Bağlantı Hatalarını Giderme

Eğer `APIConnectionError: Connection error` görürseniz:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Ortam Değişkenleri

Aşağıdaki ortam değişkenleri desteklenmektedir:

| Değişken | Varsayılan | Açıklama |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | Token kullanımını yazdırmak için `1` olarak ayarlayın |
| `RETRY_ON_FAIL` | `1` | Yeniden deneme mantığını etkinleştirir |
| `RETRY_BACKOFF` | `1.0` | İlk yeniden deneme gecikmesi (saniye) |
| `FOUNDRY_LOCAL_ENDPOINT` | Otomatik | Hizmet endpointini geçersiz kılar |

### Kullanım Örnekleri

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Eski Desenden Geçiş

Mevcut kodunuzda doğrudan API çağrıları kullanıyorsanız, işte nasıl geçiş yapacağınız:

### Önce (Doğrudan API)
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

### Sonra (SDK)
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

### Geçişin Faydaları
- ✅ Otomatik hizmet yönetimi
- ✅ Model takma adı çözümlemesi
- ✅ Donanım optimizasyonu seçimi
- ✅ Daha iyi hata işleme
- ✅ OpenAI SDK uyumluluğu
- ✅ Akış desteği

## Referanslar

### Resmi Belgeler
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK Kaynağı**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI Referansı**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Sorun Giderme**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Workshop Kaynakları
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Örnek Not Defteri**: `Workshop/notebooks/session06_models_router.ipynb`

### Topluluk
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Sorunları**: https://github.com/microsoft/Foundry-Local/issues

## Sonraki Adımlar

1. **Değişiklikleri İnceleyin**: Güncellenmiş dosyaları okuyun  
2. **Not Defterini Test Edin**: session06_models_router.ipynb dosyasını çalıştırın  
3. **SDK'yı Doğrulayın**: foundry-local-sdk'nin kurulu olduğundan emin olun  
4. **Hizmeti Kontrol Edin**: Foundry Local'ın çalıştığını doğrulayın  
5. **Belgeleri Keşfedin**: Yeni session06_README.md dosyasını okuyun  

## Özet

Bu güncellemeler, Workshop materyallerinin **resmi Foundry Local SDK desenlerini** GitHub deposunda belgelenen şekilde tam olarak takip etmesini sağlar. Tüm kod örnekleri, belgeler ve yardımcı araçlar artık Microsoft'un yerel AI modeli dağıtımı için önerdiği en iyi uygulamalarla uyumlu.

Değişiklikler şu alanları iyileştirir:
- ✅ **Doğruluk**: Resmi SDK desenlerini kullanır  
- ✅ **Belgeler**: Kapsamlı açıklamalar ve örnekler  
- ✅ **Hata İşleme**: Daha iyi mesajlar ve sorun giderme rehberi  
- ✅ **Bakım Kolaylığı**: Resmi standartlara uygun  
- ✅ **Kullanıcı Deneyimi**: Daha net talimatlar ve hata ayıklama yardımı  

---

**Güncellendi:** 8 Ekim 2025  
**SDK Sürümü:** foundry-local-sdk (en son)  
**Workshop Dalı:** Reactor

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.