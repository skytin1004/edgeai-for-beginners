<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50d80c321803b5170d9a9cd9bbfb37a3",
  "translation_date": "2025-09-24T21:30:47+00:00",
  "source_file": "Module08/README.md",
  "language_code": "tr"
}
-->
# Modül 08: Microsoft Foundry Local ile Uygulamalı Çalışma - Geliştirici Araç Seti

## Genel Bakış

Microsoft Foundry Local, kenar yapay zeka geliştirmede yeni bir nesli temsil eder ve geliştiricilere, Azure AI Foundry ile sorunsuz entegrasyonu korurken, yapay zeka uygulamalarını yerel olarak oluşturmak, dağıtmak ve ölçeklendirmek için güçlü araçlar sunar. Bu modül, Foundry Local'ın kurulumundan ileri düzey ajan geliştirmeye kadar kapsamlı bir rehber sunar.

**Anahtar Teknolojiler:**
- Microsoft Foundry Local CLI ve SDK
- Azure AI Foundry entegrasyonu
- Cihaz üzerinde model çıkarımı
- Yerel model önbellekleme ve optimizasyon
- Ajan tabanlı mimariler

## Öğrenme Hedefleri

Bu modülü tamamladığınızda:

- **Foundry Local'ı Uzmanlıkla Kullanmayı Öğrenin**: Windows 11 geliştirme için kurulum, yapılandırma ve optimizasyon yapın
- **Çeşitli Modelleri Dağıtın**: phi, qwen, deepseek ve GPT modellerini CLI komutlarıyla yerel olarak çalıştırın
- **Üretim Çözümleri Oluşturun**: Gelişmiş istem mühendisliği ve veri entegrasyonu ile yapay zeka uygulamaları oluşturun
- **Açık Kaynak Ekosisteminden Yararlanın**: Hugging Face modellerini ve topluluk katkılarını entegre edin
- **Yapay Zeka Ajanları Geliştirin**: Temellendirme ve orkestrasyon yeteneklerine sahip akıllı ajanlar oluşturun
- **Kurumsal Kalıpları Uygulayın**: Üretim dağıtımı için modüler, ölçeklenebilir yapay zeka çözümleri oluşturun

## Oturum Yapısı

### [1: Foundry Local ile Başlangıç](./01.FoundryLocalSetup.md)
**Odak Noktası**: Kurulum, CLI ayarları, model dağıtımı ve donanım optimizasyonu

**Anahtar Konular**: Tam kurulum • CLI komutları • Model önbellekleme • Donanım hızlandırma • Çoklu model dağıtımı

**Örnekler**: [REST Sohbet Hızlı Başlangıç](./samples/01/README.md) • [OpenAI SDK Entegrasyonu](./samples/02/README.md) • [Model Keşfi ve Karşılaştırma](./samples/03/README.md)

**Süre**: 2-3 saat | **Seviye**: Başlangıç

---

### [2: Azure AI Foundry ile Yapay Zeka Çözümleri Oluşturun](./02.AzureAIFoundryIntegration.md)
**Odak Noktası**: Gelişmiş istem mühendisliği, veri entegrasyonu ve bulut bağlantısı

**Anahtar Konular**: İstem mühendisliği • Veri entegrasyonu • Azure iş akışları • Performans optimizasyonu • İzleme

**Örnekler**: [Chainlit RAG Uygulaması](./samples/04/README.md)

**Süre**: 2-3 saat | **Seviye**: Orta

---

### [3: Açık Kaynak Modeller Foundry Local](./03.OpenSourceModels.md)
**Odak Noktası**: Hugging Face entegrasyonu, BYOM stratejileri ve topluluk modelleri

**Anahtar Konular**: HuggingFace entegrasyonu • Kendi modelinizi getirin • Model Pazartesi içgörüleri • Topluluk katkıları • Model seçimi

**Örnekler**: [Çoklu Ajan Orkestrasyonu](./samples/05/README.md)

**Süre**: 2-3 saat | **Seviye**: Orta

---

### [4: En Son Modelleri Keşfedin](./04.CuttingEdgeModels.md)
**Odak Noktası**: LLM'ler ve SLM'ler, EdgeAI uygulaması ve ileri düzey demolar

**Anahtar Konular**: Model karşılaştırması • Kenar ve bulut çıkarımı • Phi + ONNX Runtime • Chainlit RAG uygulaması • WebGPU optimizasyonu

**Örnekler**: [Araç Olarak Modeller Yönlendirici](./samples/06/README.md)

**Süre**: 3-4 saat | **Seviye**: İleri

---

### [5: Hızlı Yapay Zeka Destekli Ajanlar Oluşturun](./05.AIPoweredAgents.md)
**Odak Noktası**: Ajan mimarileri, sistem istemleri, temellendirme ve orkestrasyon

**Anahtar Konular**: Ajan tasarım kalıpları • Sistem istem mühendisliği • Temellendirme teknikleri • Çoklu ajan sistemleri • Üretim dağıtımı

**Örnekler**: [Çoklu Ajan Orkestrasyonu](./samples/05/README.md) • [Gelişmiş Çoklu Ajan Sistemi](./samples/09/README.md)

**Süre**: 3-4 saat | **Seviye**: İleri

---

### [6: Foundry Local - Araç Olarak Modeller](./06.ModelsAsTools.md)
**Odak Noktası**: Modüler yapay zeka çözümleri, kurumsal ölçeklendirme ve üretim kalıpları

**Anahtar Konular**: Araç olarak modeller • Cihaz üzerinde dağıtım • SDK/API entegrasyonu • Kurumsal mimariler • Ölçeklendirme stratejileri

**Örnekler**: [Araç Olarak Modeller Yönlendirici](./samples/06/README.md) • [Foundry Araçlar Çerçevesi](./samples/10/README.md)

**Süre**: 3-4 saat | **Seviye**: Uzman

---

### [7: Doğrudan API Entegrasyon Kalıpları](./samples/07/README.md)
**Odak Noktası**: SDK bağımlılıkları olmadan maksimum kontrol için saf REST API entegrasyonu

**Anahtar Konular**: HTTP istemci uygulaması • Özel kimlik doğrulama • Model sağlık izleme • Akış yanıtları • Üretim hata yönetimi

**Örnekler**: [Doğrudan API İstemcisi](./samples/07/README.md)

**Süre**: 2-3 saat | **Seviye**: Orta

---

### [8: Windows 11 Yerel Sohbet Uygulaması](./samples/08/README.md)
**Odak Noktası**: Foundry Local entegrasyonu ile modern yerel sohbet uygulamaları oluşturma

**Anahtar Konular**: Electron geliştirme • Fluent Tasarım Sistemi • Yerel Windows entegrasyonu • Gerçek zamanlı akış • Sohbet arayüzü tasarımı

**Örnekler**: [Windows 11 Sohbet Uygulaması](./samples/08/README.md)

**Süre**: 3-4 saat | **Seviye**: İleri

---

### [9: Gelişmiş Çoklu Ajan Orkestrasyonu](./samples/09/README.md)
**Odak Noktası**: Karmaşık ajan koordinasyonu, özel görev delegasyonu ve işbirlikçi yapay zeka iş akışları

**Anahtar Konular**: Akıllı ajan koordinasyonu • Fonksiyon çağrı kalıpları • Ajanlar arası iletişim • İş akışı orkestrasyonu • Kalite güvence mekanizmaları

**Örnekler**: [Gelişmiş Çoklu Ajan Sistemi](./samples/09/README.md)

**Süre**: 4-5 saat | **Seviye**: Uzman

---

### [10: Foundry Local Araçlar Çerçevesi](./samples/10/README.md)
**Odak Noktası**: Foundry Local'ı mevcut uygulamalara ve çerçevelere entegre etmek için araç odaklı mimari

**Anahtar Konular**: LangChain entegrasyonu • Semantik Çekirdek fonksiyonları • REST API çerçeveleri • CLI araçları • Jupyter entegrasyonu • Üretim dağıtım kalıpları

**Örnekler**: [Foundry Araçlar Çerçevesi](./samples/10/README.md)

**Süre**: 4-5 saat | **Seviye**: Uzman

## Ön Koşullar

### Sistem Gereksinimleri
- **İşletim Sistemi**: Windows 11 (22H2 veya daha yeni)
- **Bellek**: 16GB RAM (Daha büyük modeller için 32GB önerilir)
- **Depolama**: Model önbellekleme için 50GB boş alan
- **Donanım**: NPU destekli cihaz önerilir (Copilot+ PC), GPU isteğe bağlı
- **Ağ**: İlk model indirmeleri için yüksek hızlı internet

### Geliştirme Ortamı
- AI Toolkit uzantısı ile Visual Studio Code
- Python 3.10+ ve pip
- Sürüm kontrolü için Git
- PowerShell veya Komut İstemi
- Azure CLI (isteğe bağlı, bulut entegrasyonu için)

### Bilgi Ön Koşulları
- Yapay zeka/makine öğrenimi kavramlarına temel düzeyde hakimiyet
- Komut satırı kullanımı bilgisi
- Python programlama temelleri
- REST API kavramları
- İstem oluşturma ve model çıkarımı hakkında temel bilgi

## Modül Zaman Çizelgesi

**Tahmini Toplam Süre**: 30-38 saat

| Oturum | Odak Alanı | Örnekler | Süre | Zorluk |
|--------|------------|----------|------|--------|
|  1 | Kurulum ve Temeller | 01, 02, 03 | 2-3 saat | Başlangıç |
|  2 | Yapay Zeka Çözümleri | 04 | 2-3 saat | Orta |
|  3 | Açık Kaynak | 05 | 2-3 saat | Orta |
|  4 | İleri Modeller | 06 | 3-4 saat | İleri |
|  5 | Yapay Zeka Ajanları | 05, 09 | 3-4 saat | İleri |
|  6 | Kurumsal Araçlar | 06, 10 | 3-4 saat | Uzman |
|  7 | Doğrudan API Entegrasyonu | 07 | 2-3 saat | Orta |
|  8 | Windows 11 Sohbet Uygulaması | 08 | 3-4 saat | İleri |
|  9 | Gelişmiş Çoklu Ajan | 09 | 4-5 saat | Uzman |
| 10 | Araçlar Çerçevesi | 10 | 4-5 saat | Uzman |

## Anahtar Kaynaklar

**Resmi Belgeler:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Kaynak kodu ve resmi örnekler
- [Azure AI Foundry Belgeleri](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Tam kurulum ve kullanım rehberi
- [Model Pazartesi Serisi](https://aka.ms/model-mondays) - Haftalık model öne çıkanlar ve eğitimler

**Topluluk ve Destek:**
- [Foundry Local Tartışmaları](https://github.com/microsoft/Foundry-Local/discussions) - Topluluk Soru-Cevap ve özellik talepleri
- [Microsoft Yapay Zeka Geliştirici Topluluğu](https://techcommunity.microsoft.com/category/artificialintelligence) - En son haberler ve en iyi uygulamalar

## Öğrenme Çıktıları

Bu modülü tamamladığınızda, aşağıdaki becerilere sahip olacaksınız:

### Teknik Uzmanlık
- **Dağıtım ve Yönetim**: Foundry Local kurulumlarını geliştirme ve üretim ortamlarında yönetme
- **Model Entegrasyonu**: Microsoft, Hugging Face ve topluluk kaynaklarından çeşitli model aileleriyle sorunsuz çalışma
- **Uygulama Geliştirme**: Gelişmiş özellikler ve optimizasyonlarla üretime hazır yapay zeka uygulamaları oluşturma
- **Ajan Geliştirme**: Temellendirme, akıl yürütme ve araç entegrasyonu ile karmaşık yapay zeka ajanları uygulama

### Stratejik Anlayış
- **Mimari Kararlar**: Yerel ve bulut dağıtımı arasında bilinçli seçimler yapma
- **Performans Optimizasyonu**: Farklı donanım yapılandırmaları arasında çıkarım performansını optimize etme
- **Kurumsal Ölçeklendirme**: Yerel prototiplerden kurumsal dağıtımlara ölçeklenen uygulamalar tasarlama
- **Gizlilik ve Güvenlik**: Yerel çıkarım ile gizliliği koruyan yapay zeka çözümleri uygulama

### Yenilikçi Yetkinlikler
- **Hızlı Prototipleme**: Tüm 10 örnek kalıbı boyunca yapay zeka uygulama konseptlerini hızlıca oluşturma ve test etme
- **Topluluk Entegrasyonu**: Açık kaynak modellerinden yararlanma ve ekosisteme katkıda bulunma
- **İleri Kalıplar**: RAG, ajanlar ve araç entegrasyonu dahil olmak üzere en son yapay zeka kalıplarını uygulama
- **Çerçeve Uzmanlığı**: LangChain, Semantik Çekirdek, Chainlit ve Electron ile uzman düzeyde entegrasyon
- **Üretim Dağıtımı**: Yerel prototiplerden kurumsal sistemlere ölçeklenebilir yapay zeka çözümleri dağıtma
- **Geleceğe Hazır Geliştirme**: Gelişen yapay zeka teknolojileri ve kalıplarına hazır uygulamalar oluşturma

## Başlangıç

1. **Ortam Kurulumu**: Windows 11 ve önerilen donanımı (bkz. Ön Koşullar) sağlayın
2. **Foundry Local'ı Kurun**: Tam kurulum ve yapılandırma için Oturum 1'i takip edin
3. **Örnek 01'i Çalıştırın**: Kurulumu doğrulamak için temel REST API entegrasyonu ile başlayın
4. **Örnekler Üzerinde İlerleyin**: 01-10 örneklerini tamamlayarak kapsamlı bir uzmanlık kazanın

## Başarı Ölçütleri

Tüm 10 kapsamlı örnek üzerinden ilerlemenizi takip edin:

### Temel Seviye (Örnekler 01-03)
- [ ] Foundry Local'ı başarıyla kurun ve yapılandırın
- [ ] REST API entegrasyonunu tamamlayın (Örnek 01)
- [ ] OpenAI SDK uyumluluğunu uygulayın (Örnek 02)
- [ ] Model keşfi ve karşılaştırma gerçekleştirin (Örnek 03)

### Uygulama Seviyesi (Örnekler 04-06)
- [ ] En az 4 farklı model ailesini dağıtın ve çalıştırın
- [ ] İşlevsel bir RAG sohbet uygulaması oluşturun (Örnek 04)
- [ ] Çoklu ajan orkestrasyon sistemi oluşturun (Örnek 05)
- [ ] Akıllı model yönlendirme uygulayın (Örnek 06)

### İleri Entegrasyon Seviyesi (Örnekler 07-10)
- [ ] Üretime hazır bir API istemcisi oluşturun (Örnek 07)
- [ ] Windows 11 yerel sohbet uygulaması geliştirin (Örnek 08)
- [ ] Gelişmiş çoklu ajan sistemi uygulayın (Örnek 09)
- [ ] Kapsamlı bir araçlar çerçevesi oluşturun (Örnek 10)

### Uzmanlık Göstergeleri
- [ ] Tüm 10 örneği hatasız çalıştırın
- [ ] Belirli kullanım durumları için en az 3 örneği özelleştirin
- [ ] Üretim benzeri ortamlarda 2+ örnek dağıtın
- [ ] Örnek kodda iyileştirmeler veya genişletmeler yapın
- [ ] Foundry Local kalıplarını kişisel/profesyonel projelere entegre edin

## Hızlı Başlangıç Rehberi - Tüm 10 Örnek

### Ortam Kurulumu (Tüm Örnekler İçin Gereklidir)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Temel Örnekler (01-06)

**Örnek 01: REST Sohbet Hızlı Başlangıç**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Örnek 02: OpenAI SDK Entegrasyonu**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Örnek 03: Model Keşfi ve Karşılaştırma**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Örnek 04: Chainlit RAG Uygulaması**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Örnek 05: Çoklu Ajan Orkestrasyonu**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Örnek 06: Araç Olarak Modeller Yönlendirici**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b-instruct

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### İleri Entegrasyon Örnekleri (07-10)

**Örnek 07: Doğrudan API İstemcisi**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**Örnek 08: Windows 11 Sohbet Uygulaması**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**Örnek 09: Gelişmiş Çoklu Ajan Sistemi**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**Örnek 10: Foundry Araçlar Çerçevesi**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### Yaygın Sorunları Giderme

**Foundry Local Bağlantı Hataları**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Model Yükleme Sor
Bu modül, Microsoft'un kurumsal düzeydeki araçlarını açık kaynak ekosisteminin esneklik ve yenilikleriyle birleştirerek, uç yapay zeka geliştirmede en son teknolojiyi temsil ediyor. Foundry Local'ı 10 kapsamlı örnek üzerinden öğrenerek, yapay zeka uygulama geliştirme alanında öncü bir konuma ulaşacaksınız.

**Tam Öğrenme Yolu:**
- **Temel** (Örnekler 01-03): API entegrasyonu ve model yönetimi
- **Uygulamalar** (Örnekler 04-06): RAG, ajanlar ve akıllı yönlendirme
- **İleri Düzey** (Örnekler 07-10): Üretim çerçeveleri ve kurumsal entegrasyon

Azure OpenAI entegrasyonu (Oturum 2) için, gerekli ortam değişkenleri ve API sürüm ayarları hakkında bilgi almak üzere her bir örneğin README dosyasına bakın.

---

