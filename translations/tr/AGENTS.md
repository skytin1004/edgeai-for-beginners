<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:33:58+00:00",
  "source_file": "AGENTS.md",
  "language_code": "tr"
}
-->
# AGENTS.md

## Proje Genel Bakışı

EdgeAI for Beginners, Küçük Dil Modelleri (SLM'ler) ile Edge AI geliştirmeyi öğreten kapsamlı bir eğitim deposudur. Kurs, EdgeAI temellerini, model dağıtımını, optimizasyon tekniklerini ve Microsoft Foundry Local ve çeşitli AI çerçevelerini kullanarak üretime hazır uygulamaları kapsamaktadır.

**Anahtar Teknolojiler:**
- Python 3.8+ (AI/ML örnekleri için birincil dil)
- .NET C# (AI/ML örnekleri)
- JavaScript/Node.js ve Electron (masaüstü uygulamaları için)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI Çerçeveleri: LangChain, Semantic Kernel, Chainlit
- Model Optimizasyonu: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Depo Türü:** 8 modül ve 10 kapsamlı örnek uygulama içeren eğitim içeriği deposu

**Mimari:** Edge AI dağıtım desenlerini gösteren pratik örneklerle çok modüllü bir öğrenme yolu

## Depo Yapısı

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Kurulum Komutları

### Depo Kurulumu

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python Örnek Kurulumu (Modül08 ve Python örnekleri)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Node.js Örnek Kurulumu (Örnek 08 - Windows Sohbet Uygulaması)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Local Kurulumu

Modül08 örneklerini çalıştırmak için Foundry Local gereklidir:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Geliştirme İş Akışı

### İçerik Geliştirme

Bu depo öncelikli olarak **Markdown eğitim içeriği** içermektedir. Değişiklik yaparken:

1. İlgili modül dizinlerindeki `.md` dosyalarını düzenleyin
2. Mevcut biçimlendirme kalıplarını takip edin
3. Kod örneklerinin doğru ve test edilmiş olduğundan emin olun
4. Gerekirse ilgili çeviri içeriğini güncelleyin (veya otomasyonun bunu yapmasına izin verin)

### Örnek Uygulama Geliştirme

Python örnekleri için (örnekler 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electron örneği için (örnek 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Örnek Uygulamaların Test Edilmesi

Python örneklerinde otomatik testler yoktur, ancak çalıştırılarak doğrulanabilir:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron örneği için test altyapısı mevcuttur:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Test Talimatları

### İçerik Doğrulama

Depo, otomatik çeviri iş akışlarını kullanır. Çeviriler için manuel test gerekmez.

**İçerik değişiklikleri için manuel doğrulama:**
1. `.md` dosyalarını önizleyerek Markdown render'ını gözden geçirin
2. Tüm bağlantıların geçerli hedeflere işaret ettiğini doğrulayın
3. Belgelerde yer alan kod parçacıklarını test edin
4. Görsellerin doğru yüklendiğinden emin olun

### Örnek Uygulama Testi

**Modül08/örnekler/08 (Electron uygulaması) kapsamlı testlere sahiptir:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python örnekleri manuel olarak test edilmelidir:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Kod Stili Kuralları

### Markdown İçeriği

- Tutarlı başlık hiyerarşisi kullanın (# başlık için, ## ana bölümler için, ### alt bölümler için)
- Kod bloklarını dil belirteçleriyle ekleyin: ```python, ```bash, ```javascript
- Tablolar, listeler ve vurgu için mevcut biçimlendirmeyi takip edin
- Satırları okunabilir tutun (~80-100 karakter hedefleyin, ancak katı değil)
- Dahili referanslar için göreceli bağlantılar kullanın

### Python Kod Stili

- PEP 8 kurallarına uyun
- Uygun yerlerde tür ipuçları kullanın
- Fonksiyonlar ve sınıflar için docstring ekleyin
- Anlamlı değişken adları kullanın
- Fonksiyonları odaklanmış ve öz tutun

### JavaScript/Node.js Kod Stili

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Ana kurallar:**
- Örnek 08'de sağlanan ESLint yapılandırması
- Kod biçimlendirme için Prettier
- Modern ES6+ sözdizimini kullanın
- Kod tabanındaki mevcut desenleri takip edin

## Çekme İsteği Kuralları

### Başlık Formatı
```
[ModuleXX] Brief description of change
```
veya
```
[Module08/samples/XX] Description for sample changes
```

### Göndermeden Önce

**İçerik değişiklikleri için:**
- Değiştirilen tüm Markdown dosyalarını önizleyin
- Bağlantıların ve görsellerin çalıştığını doğrulayın
- Yazım hatalarını ve dilbilgisi hatalarını kontrol edin

**Örnek kod değişiklikleri için (Modül08/örnekler/08):**
```bash
npm run lint
npm test
```

**Python örnek değişiklikleri için:**
- Örneğin başarıyla çalıştığını test edin
- Hata işleme mekanizmasının çalıştığını doğrulayın
- Foundry Local ile uyumluluğu kontrol edin

### İnceleme Süreci

- Eğitim içeriği değişiklikleri doğruluk ve açıklık açısından incelenir
- Kod örnekleri işlevsellik açısından test edilir
- Çeviri güncellemeleri GitHub Actions tarafından otomatik olarak ele alınır

## Çeviri Sistemi

**ÖNEMLİ:** Bu depo, GitHub Actions aracılığıyla otomatik çeviri kullanır.

- Çeviriler `/translations/` dizininde bulunur (50+ dil)
- `co-op-translator.yml` iş akışı ile otomatikleştirilmiştir
- **Çeviri dosyalarını manuel olarak düzenlemeyin** - üzerine yazılacaktır
- Yalnızca kök ve modül dizinlerindeki İngilizce kaynak dosyaları düzenleyin
- Çeviriler `main` dalına yapılan push işlemlerinde otomatik olarak oluşturulur

## Foundry Local Entegrasyonu

Çoğu Modül08 örneği için Microsoft Foundry Local'ın çalışıyor olması gerekir:

### Foundry Local'ı Başlatma
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### Foundry Local'ı Doğrulama
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Örnekler için Ortam Değişkenleri

Çoğu örnek şu ortam değişkenlerini kullanır:
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Derleme ve Dağıtım

### İçerik Dağıtımı

Bu depo öncelikli olarak dokümantasyon içerir - içerik için bir derleme süreci gerekmez.

### Örnek Uygulama Derleme

**Electron Uygulaması (Modül08/örnekler/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python Örnekleri:**
Derleme süreci yoktur - örnekler doğrudan Python yorumlayıcısı ile çalıştırılır.

## Yaygın Sorunlar ve Sorun Giderme

### Foundry Local Çalışmıyor
**Sorun:** Örnekler bağlantı hatalarıyla başarısız oluyor

**Çözüm:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Python Sanal Ortam Sorunları
**Sorun:** Modül ithalat hataları

**Çözüm:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Electron Derleme Sorunları
**Sorun:** npm install veya derleme hataları

**Çözüm:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Çeviri İş Akışı Çakışmaları
**Sorun:** Çeviri PR'ı değişikliklerinizle çakışıyor

**Çözüm:**
- Yalnızca İngilizce kaynak dosyaları düzenleyin
- Otomatik çeviri iş akışının çevirileri ele almasına izin verin
- Çakışmalar oluşursa, çeviriler birleştirildikten sonra `main` dalını dalınıza birleştirin

## Ek Kaynaklar

### Öğrenme Yolları
- **Başlangıç Yolu:** Modüller 01-02 (7-9 saat)
- **Orta Seviye Yolu:** Modüller 03-04 (9-11 saat)
- **İleri Seviye Yolu:** Modüller 05-07 (12-15 saat)
- **Uzman Yolu:** Modül 08 (8-10 saat)

### Anahtar Modül İçeriği
- **Modül01:** EdgeAI temelleri ve gerçek dünya vaka çalışmaları
- **Modül02:** Küçük Dil Modeli (SLM) aileleri ve mimarileri
- **Modül03:** Yerel ve bulut dağıtım stratejileri
- **Modül04:** Birden fazla çerçeve ile model optimizasyonu
- **Modül05:** SLMOps - üretim operasyonları
- **Modül06:** AI ajanları ve fonksiyon çağrısı
- **Modül07:** Platforma özgü uygulamalar
- **Modül08:** Foundry Local araç seti ile 10 kapsamlı örnek

### Harici Bağımlılıklar
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Yerel AI model çalışma zamanı
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimizasyon çerçevesi
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Model optimizasyon araç seti
- [OpenVINO](https://docs.openvino.ai/) - Intel'in optimizasyon araç seti

## Projeye Özgü Notlar

### Modül08 Örnek Uygulamaları

Depo, 10 kapsamlı örnek uygulama içerir:

1. **01-REST Chat Quickstart** - Temel OpenAI SDK entegrasyonu
2. **02-OpenAI SDK Integration** - Gelişmiş SDK özellikleri
3. **03-Model Discovery & Benchmarking** - Model karşılaştırma araçları
4. **04-Chainlit RAG Application** - Geri alma ile artırılmış üretim
5. **05-Multi-Agent Orchestration** - Temel ajan koordinasyonu
6. **06-Models-as-Tools Router** - Akıllı model yönlendirme
7. **07-Direct API Client** - Düşük seviyeli API entegrasyonu
8. **08-Windows 11 Chat App** - Yerel Electron masaüstü uygulaması
9. **09-Advanced Multi-Agent System** - Karmaşık ajan orkestrasyonu
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel entegrasyonu

Her bir örnek, Foundry Local ile Edge AI geliştirme konusunun farklı yönlerini göstermektedir.

### Performans Dikkatleri

- SLM'ler kenar dağıtımı için optimize edilmiştir (2-16GB RAM)
- Yerel çıkarım 50-500ms yanıt süreleri sağlar
- Kuantizasyon teknikleri %75 boyut azaltımı ve %85 performans koruması sağlar
- Yerel modellerle gerçek zamanlı konuşma yetenekleri

### Güvenlik ve Gizlilik

- Tüm işlemler yerel olarak gerçekleştirilir - buluta veri gönderilmez
- Gizlilik hassasiyeti olan uygulamalar için uygundur (sağlık, finans)
- Veri egemenliği gereksinimlerini karşılar
- Foundry Local tamamen yerel donanımda çalışır

---

**Bu, Edge AI geliştirmeyi öğretmeye odaklanan bir eğitim deposudur. Ana katkı modeli, eğitim içeriğini geliştirmek ve Edge AI kavramlarını gösteren örnek uygulamalar eklemek/geliştirmektir.**

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.