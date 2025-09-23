<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T18:25:23+00:00",
  "source_file": "Module08/README.md",
  "language_code": "tr"
}
-->
# Modül 08: Microsoft Foundry Local ile Uygulamalı Çalışma - Geliştirici Araç Seti

## Genel Bakış

Microsoft Foundry Local, kenar yapay zeka geliştirmede yeni bir nesli temsil eder ve geliştiricilere AI uygulamalarını yerel olarak oluşturma, dağıtma ve ölçeklendirme için güçlü araçlar sunar. Aynı zamanda Azure AI Foundry ile sorunsuz entegrasyon sağlar. Bu modül, Foundry Local'ın kurulumundan ileri düzey ajan geliştirmeye kadar kapsamlı bir rehber sunar.

**Anahtar Teknolojiler:**
- Microsoft Foundry Local CLI ve SDK
- Azure AI Foundry entegrasyonu
- Cihaz üzerinde model çıkarımı
- Yerel model önbellekleme ve optimizasyon
- Ajan tabanlı mimariler

## Modül Öğrenme Hedefleri

Bu modülü tamamladığınızda:

- **Foundry Local Kurulumunda Ustalaşın**: Foundry Local'ı Windows 11 üzerinde kurun, yapılandırın ve optimize edin
- **Çeşitli Modelleri Dağıtın**: phi, qwen, deepseek ve GPT-OSS-20B modellerini CLI komutlarıyla yerel olarak çalıştırın
- **Üretim Çözümleri Oluşturun**: Gelişmiş istem mühendisliği ve veri entegrasyonu ile AI uygulamaları oluşturun
- **Açık Kaynak Ekosisteminden Yararlanın**: Hugging Face modellerini ve topluluk katkılarını entegre edin
- **AI Mimari Karşılaştırmaları Yapın**: LLM'ler ve SLM'ler arasındaki avantaj ve dezavantajları anlayın, dağıtım stratejilerini öğrenin
- **AI Ajanları Geliştirin**: Foundry Local'ın mimarisi ve temellendirme yeteneklerini kullanarak akıllı ajanlar oluşturun
- **Modelleri Araç Olarak Uygulayın**: Kurumsal uygulamalar için modüler, özelleştirilebilir AI çözümleri oluşturun

## Oturum Yapısı

### [1: Foundry Local ile Başlangıç](./01.FoundryLocalSetup.md)
**Odak Noktası**: Kurulum, CLI yapılandırması, model önbellekleme ve donanım hızlandırma

**Öğrenecekleriniz:**
- Foundry Local'ı Windows 11 üzerinde tamamen kurma
- CLI yapılandırması ve komut yapısı
- Performans için model önbellekleme stratejileri
- Donanım hızlandırma ayarları ve optimizasyon
- phi, qwen, deepseek ve GPT-OSS-20B modellerinin uygulamalı dağıtımı

**Süre**: 2-3 saat  
**Ön Koşullar**: Windows 11, temel komut satırı bilgisi

---

### [2: Azure AI Foundry ile AI Çözümleri Oluşturun](./02.AzureAIFoundryIntegration.md)
**Odak Noktası**: Gelişmiş istem mühendisliği, veri entegrasyonu ve uygulanabilir görevler

**Öğrenecekleriniz:**
- Gelişmiş istem mühendisliği teknikleri
- Veri entegrasyonu desenleri ve en iyi uygulamalar
- Foundry Local ile uygulanabilir AI görevleri oluşturma
- Azure AI Foundry entegrasyon iş akışları
- Performans optimizasyonu ve izleme

**Süre**: 2-3 saat  
**Ön Koşullar**: 1. Oturumun tamamlanması, Azure hesabı (isteğe bağlı)

---

### [3: Açık Kaynak Modeller Foundry Local](./03.OpenSourceModels.md)
**Odak Noktası**: Hugging Face entegrasyonu, model seçimi stratejileri ve topluluk katkıları

**Öğrenecekleriniz:**
- Foundry Local ile Hugging Face model entegrasyonu
- Kendi modelinizi getirme (BYOM) stratejileri ve uygulamaları
- Model Mondays serisi içgörüleri ve topluluk katkıları
- Özel model dağıtımı ve optimizasyon
- Topluluk modeli değerlendirme ve seçim kriterleri

**Süre**: 2-3 saat  
**Ön Koşullar**: 1-2. Oturumun tamamlanması, Hugging Face hesabı

---

### [4: En Son Modelleri Keşfedin - LLM'ler, SLM'ler ve Cihaz Üzerinde Çıkarım](./04.CuttingEdgeModels.md)
**Odak Noktası**: Model karşılaştırması, Phi ve ONNX Runtime ile EdgeAI, ileri düzey demolar

**Öğrenecekleriniz:**
- LLM'ler ve SLM'ler arasında kapsamlı karşılaştırma ve kullanım durumları
- Yerel ve bulut çıkarım arasındaki avantaj-dezavantajlar ve karar çerçeveleri
- Phi ve ONNX Runtime ile EdgeAI uygulaması
- Chainlit RAG Sohbet Uygulaması geliştirme ve dağıtımı
- WebGPU çıkarım optimizasyon teknikleri
- AI PC SDK entegrasyonu ve yetenekleri

**Süre**: 3-4 saat  
**Ön Koşullar**: 1-3. Oturumun tamamlanması, çıkarım kavramlarını anlama

---

### [5: Foundry Local ile Hızlı AI Destekli Ajanlar Oluşturun](./05.AIPoweredAgents.md)
**Odak Noktası**: Hızlı GenAI uygulama geliştirme, sistem istemleri, temellendirme ve ajan mimarileri

**Öğrenecekleriniz:**
- Foundry Local ajan mimarisi ve tasarım desenleri
- Ajan davranışı için sistem istem mühendisliği
- Güvenilir ajan yanıtları için temellendirme teknikleri
- Hızlı GenAI uygulama geliştirme iş akışları
- Ajan orkestrasyonu ve çoklu ajan sistemleri
- AI ajanları için üretim dağıtım stratejileri

**Süre**: 3-4 saat  
**Ön Koşullar**: 1-4. Oturumun tamamlanması, AI ajanları hakkında temel bilgi

---

### [6: Foundry Local - Modelleri Araç Olarak Kullanma](./06.ModelsAsTools.md)
**Odak Noktası**: Modüler AI çözümleri, cihaz üzerinde dağıtım ve kurumsal ölçeklendirme

**Öğrenecekleriniz:**
- AI modellerini modüler, özelleştirilebilir araçlar olarak kullanma
- Bulut bağımlılığı olmadan cihaz üzerinde dağıtım
- Düşük gecikmeli, maliyet verimli ve gizlilik koruyucu çıkarım
- SDK, API ve CLI entegrasyon desenleri
- Belirli kullanım durumları için model özelleştirme
- Yerelden Azure AI Foundry'e ölçeklendirme stratejileri
- Kurumsal düzeyde AI uygulama mimarileri

**Süre**: 3-4 saat  
**Ön Koşullar**: Önceki tüm oturumlar, kurumsal geliştirme deneyimi faydalı olabilir

## Ön Koşullar

### Sistem Gereksinimleri
- **İşletim Sistemi**: Windows 11 (22H2 veya daha yeni)
- **Bellek**: 16GB RAM (daha büyük modeller için 32GB önerilir)
- **Depolama**: Model önbellekleme için 50GB boş alan
- **Donanım**: NPU destekli cihaz önerilir (Copilot+ PC), GPU isteğe bağlı
- **Ağ**: İlk model indirmeleri için yüksek hızlı internet

### Geliştirme Ortamı
- AI Toolkit uzantısı ile Visual Studio Code
- Python 3.10+ ve pip
- Sürüm kontrol için Git
- PowerShell veya Komut İstemi
- Azure CLI (isteğe bağlı bulut entegrasyonu için)

### Bilgi Ön Koşulları
- AI/ML kavramları hakkında temel bilgi
- Komut satırı bilgisi
- Python programlama temelleri
- REST API kavramları
- İstem oluşturma ve model çıkarımı hakkında temel bilgi

## Modül Zaman Çizelgesi

**Toplam Tahmini Süre**: 15-20 saat

| Oturum | Odak Alanı | Süre | Zorluk Seviyesi |
|--------|------------|------|-----------------|
|  1 | Kurulum ve Temeller | 2-3 saat | Başlangıç |
|  2 | AI Çözümleri | 2-3 saat | Orta |
|  3 | Açık Kaynak | 2-3 saat | Orta |
|  4 | İleri Düzey Modeller | 3-4 saat | İleri |
|  5 | AI Ajanları | 3-4 saat | İleri |
|  6 | Kurumsal Araçlar | 3-4 saat | Uzman |

## Anahtar Kaynaklar

### Birincil Dokümantasyon
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local Dokümantasyonu](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays Serisi](https://aka.ms/model-mondays)

### Topluluk Kaynakları
- [Foundry Local Topluluk Tartışmaları](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry Örnekleri](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI Geliştirici Topluluğu](https://techcommunity.microsoft.com/category/artificialintelligence)

## Öğrenme Çıktıları

Bu modülü tamamladığınızda şunları yapabileceksiniz:

### Teknik Ustalık
- **Dağıtım ve Yönetim**: Foundry Local kurulumlarını geliştirme ve üretim ortamlarında yönetme
- **Model Entegrasyonu**: Microsoft, Hugging Face ve topluluk kaynaklarından çeşitli model aileleriyle sorunsuz çalışma
- **Uygulama Geliştirme**: Gelişmiş özellikler ve optimizasyonlarla üretime hazır AI uygulamaları oluşturma
- **Ajan Geliştirme**: Temellendirme, akıl yürütme ve araç entegrasyonu ile sofistike AI ajanları uygulama

### Stratejik Anlayış
- **Mimari Kararlar**: Yerel ve bulut dağıtımı arasında bilinçli seçimler yapma
- **Performans Optimizasyonu**: Farklı donanım yapılandırmalarında çıkarım performansını optimize etme
- **Kurumsal Ölçeklendirme**: Yerel prototiplerden kurumsal dağıtımlara ölçeklenen uygulamalar tasarlama
- **Gizlilik ve Güvenlik**: Yerel çıkarım ile gizlilik koruyucu AI çözümleri uygulama

### Yenilik Kapasiteleri
- **Hızlı Prototipleme**: AI uygulama konseptlerini hızlı bir şekilde oluşturma ve test etme
- **Topluluk Entegrasyonu**: Açık kaynak modellerinden yararlanma ve ekosisteme katkıda bulunma
- **İleri Düzey Desenler**: RAG, ajanlar ve araç entegrasyonu gibi en son AI desenlerini uygulama
- **Geleceğe Hazır Geliştirme**: Gelişen AI teknolojileri ve desenlerine hazır uygulamalar oluşturma

## Başlangıç

1. **Ortamınızı Hazırlayın**: Windows 11 ve önerilen donanım özelliklerini sağlayın
2. **Ön Koşulları Kurun**: Geliştirme araçlarını ve bağımlılıkları kurun
3. **1. Oturum ile Başlayın**: Foundry Local kurulumuna ve temel ayarlara başlayın
4. **Sıralı İlerleyin**: Öğrenme sürecini optimize etmek için oturumları sırayla tamamlayın
5. **Sürekli Pratik Yapın**: Kavramları uygulamalı alıştırmalar ve projelerle pekiştirin

## Başarı Ölçütleri

Modül boyunca ilerlemenizi takip edin:

- [ ] Foundry Local'ı başarıyla kurun ve yapılandırın
- [ ] En az 4 farklı model ailesini dağıtın ve çalıştırın
- [ ] Veri entegrasyonu ile eksiksiz bir AI çözümü oluşturun
- [ ] En az 2 açık kaynak modeli entegre edin
- [ ] İşlevsel bir RAG sohbet uygulaması oluşturun
- [ ] Bir AI ajanı geliştirin ve dağıtın
- [ ] Modelleri araç olarak kullanan bir mimari uygulayın

## Örnekler için Hızlı Başlangıç

### 1) Ortam kurulumu (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Yerel bir modeli başlatma (yeni terminal)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Chainlit demosunu çalıştırma (4. Oturum)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Çoklu ajan koordinatörünü çalıştırma (5. Oturum)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Bağlantı hataları görürseniz, Foundry Local'ı doğrulayın:
```cmd
curl http://localhost:8000/v1/models
```

### Yönlendirici yapılandırması (6. Oturum)
Yönlendirici hızlı bir sağlık kontrolü yapar ve env tabanlı yapılandırmayı destekler:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Bu modül, Microsoft'un kurumsal düzeydeki araçlarını açık kaynak ekosisteminin esnekliği ve yeniliği ile birleştirerek kenar yapay zeka geliştirmede en son teknolojiyi temsil eder. Foundry Local'da ustalaşarak, AI uygulama geliştirme alanında ön saflarda yer alacaksınız.

Azure OpenAI (2. Oturum) için gerekli ortam değişkenleri ve API sürüm ayarları için örnek README dosyasına bakın.

## Örnekler Genel Bakış

- `samples/01`: Foundry Local'a hızlı REST sohbet (`chat_quickstart.py`).
- `samples/02`: OpenAI SDK entegrasyonu (`sdk_quickstart.py`).
- `samples/03`: Model keşfi + hızlı test (`list_and_bench.cmd`).
- `samples/04`: Chainlit RAG demosu (`app.py`).
- `samples/05`: Çoklu ajan orkestrasyonu (`python -m samples.05.agents.coordinator`).
- `samples/06`: Modelleri Araç Olarak Kullanma yönlendiricisi (`python samples\06\router.py`).

---

