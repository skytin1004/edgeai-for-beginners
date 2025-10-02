<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77bb931ce93583c081cf7861f43d9662",
  "translation_date": "2025-10-02T12:50:25+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "tr"
}
-->
# Windows Edge AI Geliştirme Rehberi

## Giriş

Windows Edge AI Geliştirme'ye hoş geldiniz - Microsoft'un Windows AI Foundry platformunu kullanarak cihaz üzerinde yapay zeka gücünden yararlanan akıllı uygulamalar oluşturmak için kapsamlı rehberiniz. Bu rehber, Windows geliştiricilerinin en son Edge AI özelliklerini uygulamalarına entegre ederken Windows donanım hızlandırmasının tüm avantajlarından faydalanmalarını sağlamak için özel olarak tasarlanmıştır.

### Windows AI Avantajı

Windows AI Foundry, model seçimi ve ince ayarından optimizasyon ve CPU, GPU, NPU ve hibrit bulut mimarileri arasında dağıtıma kadar yapay zeka geliştirici yaşam döngüsünün tamamını destekleyen birleşik, güvenilir ve güvenli bir platform sunar. Bu platform, yapay zeka geliştirmeyi demokratikleştirerek şu avantajları sağlar:

- **Donanım Soyutlama**: AMD, Intel, NVIDIA ve Qualcomm silikonları arasında sorunsuz dağıtım
- **Cihaz Üzerinde Zeka**: Tamamen yerel donanımda çalışan, gizliliği koruyan yapay zeka
- **Optimize Performans**: Windows donanım yapılandırmaları için önceden optimize edilmiş modeller
- **Kurumsal Hazırlık**: Üretim seviyesinde güvenlik ve uyumluluk özellikleri

### Edge AI için Neden Windows?

**Evrensel Donanım Desteği**  
Windows ML, tüm Windows ekosistemi genelinde otomatik donanım optimizasyonu sağlar, böylece yapay zeka uygulamalarınız altta yatan silikon mimarisi ne olursa olsun en iyi şekilde çalışır.

**Entegre AI Çalışma Zamanı**  
Yerleşik Windows ML çıkarım motoru, karmaşık kurulum gereksinimlerini ortadan kaldırır ve geliştiricilerin altyapı yerine uygulama mantığına odaklanmasını sağlar.

**Copilot+ PC Optimizasyonu**  
Özel Neural Processing Unit'lere (NPU'lar) sahip yeni nesil Windows cihazları için tasarlanmış API'ler, watt başına olağanüstü performans sunar.

**Geliştirici Ekosistemi**  
Visual Studio entegrasyonu, kapsamlı belgeler ve geliştirme döngülerini hızlandıran örnek uygulamalar gibi zengin araçlar.

## Öğrenme Hedefleri

Bu Windows Edge AI geliştirme rehberini tamamlayarak, Windows platformunda üretime hazır yapay zeka uygulamaları oluşturmak için gerekli temel becerileri öğreneceksiniz.

### Temel Teknik Yetkinlikler

**Windows AI Foundry Uzmanlığı**  
- Windows AI Foundry platformunun mimarisini ve bileşenlerini anlayın  
- Windows ekosisteminde yapay zeka geliştirme yaşam döngüsünü yönetin  
- Cihaz üzerinde yapay zeka uygulamaları için güvenlik en iyi uygulamalarını uygulayın  
- Farklı Windows donanım yapılandırmaları için uygulamaları optimize edin  

**API Entegrasyonu Uzmanlığı**  
- Metin, görsel ve çok modlu uygulamalar için Windows AI API'lerini öğrenin  
- Phi Silica dil modeli entegrasyonunu metin üretimi ve akıl yürütme için uygulayın  
- Yerleşik görüntü işleme API'lerini kullanarak bilgisayar görme yeteneklerini dağıtın  
- LoRA (Low-Rank Adaptation) tekniklerini kullanarak önceden eğitilmiş modelleri özelleştirin  

**Foundry Local Uygulaması**  
- Foundry Local CLI kullanarak açık kaynaklı dil modellerini gözden geçirin, değerlendirin ve dağıtın  
- Yerel dağıtım için model optimizasyonunu ve kuantizasyonu anlayın  
- İnternet bağlantısı olmadan çalışan çevrimdışı yapay zeka yeteneklerini uygulayın  
- Üretim ortamlarında model yaşam döngülerini ve güncellemelerini yönetin  

**Windows ML Dağıtımı**  
- Özel ONNX modellerini Windows uygulamalarına getirin  
- CPU, GPU ve NPU mimarileri arasında otomatik donanım hızlandırmasından yararlanın  
- Optimal kaynak kullanımı ile gerçek zamanlı çıkarım uygulayın  
- Çeşitli Windows cihaz kategorileri için ölçeklenebilir yapay zeka uygulamaları tasarlayın  

### Uygulama Geliştirme Becerileri

**Çapraz Platform Windows Geliştirme**  
- Evrensel Windows dağıtımı için .NET MAUI kullanarak yapay zeka destekli uygulamalar oluşturun  
- Yapay zeka yeteneklerini Win32, UWP ve İlerici Web Uygulamalarına entegre edin  
- Yapay zeka işlem durumlarına uyum sağlayan duyarlı UI tasarımları uygulayın  
- Asenkron yapay zeka işlemlerini uygun kullanıcı deneyimi desenleriyle yönetin  

**Performans Optimizasyonu**  
- Farklı donanım yapılandırmaları arasında yapay zeka çıkarım performansını profilleyin ve optimize edin  
- Büyük dil modelleri için verimli bellek yönetimi uygulayın  
- Mevcut donanım yeteneklerine göre zarif bir şekilde degrade olan uygulamalar tasarlayın  
- Sık kullanılan yapay zeka işlemleri için önbellek stratejileri uygulayın  

**Üretim Hazırlığı**  
- Kapsamlı hata işleme ve geri dönüş mekanizmaları uygulayın  
- Yapay zeka uygulama performansı için telemetri ve izleme tasarlayın  
- Yerel yapay zeka model depolama ve yürütme için güvenlik en iyi uygulamalarını uygulayın  
- Kurumsal ve tüketici uygulamaları için dağıtım stratejileri planlayın  

### İş ve Stratejik Anlayış

**Yapay Zeka Uygulama Mimarisi**  
- Yerel ve bulut yapay zeka işlemleri arasında optimize eden hibrit mimariler tasarlayın  
- Model boyutu, doğruluk ve çıkarım hızı arasındaki ödünleşimleri değerlendirin  
- Gizliliği korurken zekayı etkinleştiren veri akışı mimarileri planlayın  
- Kullanıcı talepleriyle ölçeklenen maliyet etkin yapay zeka çözümleri uygulayın  

**Pazar Konumlandırması**  
- Windows'a özgü yapay zeka uygulamalarının rekabet avantajlarını anlayın  
- Cihaz üzerinde yapay zekanın üstün kullanıcı deneyimleri sağladığı kullanım durumlarını belirleyin  
- Yapay zeka destekli Windows uygulamaları için pazara giriş stratejileri geliştirin  
- Uygulamaları Windows ekosisteminin avantajlarından yararlanacak şekilde konumlandırın  

## Windows App SDK Yapay Zeka Örnekleri

Windows App SDK, çeşitli çerçeveler ve dağıtım senaryoları arasında yapay zeka entegrasyonunu gösteren kapsamlı örnekler sunar. Bu örnekler, Windows yapay zeka geliştirme desenlerini anlamak için temel referanslardır.

### Windows AI Foundry Örnekleri

| Örnek | Çerçeve | Odak Alanı | Temel Özellikler |
|-------|---------|------------|------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API'leri Entegrasyonu | Windows AI API'lerini, ARM64 optimizasyonunu ve paketlenmiş dağıtımı gösteren tam WinUI uygulaması |

**Temel Teknolojiler:**  
- Windows AI API'leri  
- WinUI 3 çerçevesi  
- ARM64 platform optimizasyonu  
- Copilot+ PC uyumluluğu  
- Paketlenmiş uygulama dağıtımı  

**Ön Koşullar:**  
- Windows 11, Copilot+ PC önerilir  
- Visual Studio 2022  
- ARM64 yapılandırması  
- Windows App SDK 1.8.1+  

### Windows ML Örnekleri

#### C++ Örnekleri

| Örnek | Tür | Odak Alanı | Temel Özellikler |
|-------|-----|------------|------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsol Uygulaması | Temel Windows ML | EP keşfi, komut satırı seçenekleri, model derleme |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsol Uygulaması | Çerçeve Dağıtımı | Paylaşılan çalışma zamanı, daha küçük dağıtım boyutu |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsol Uygulaması | Bağımsız Dağıtım | Bağımsız dağıtım, çalışma zamanı bağımlılıkları yok |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Kütüphane Kullanımı | Paylaşılan kütüphanede WindowsML, bellek yönetimi |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet Eğitimi | Model dönüştürme, EP derleme, Build 2025 eğitimi |

#### C# Örnekleri

**Konsol Uygulamaları**

| Örnek | Tür | Odak Alanı | Temel Özellikler |
|-------|-----|------------|------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konsol Uygulaması | Temel C# Entegrasyonu | Paylaşılan yardımcı kullanım, komut satırı arayüzü |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet Eğitimi | Model dönüştürme, EP derleme, Build 2025 eğitimi |

**GUI Uygulamaları**

| Örnek | Çerçeve | Odak Alanı | Temel Özellikler |
|-------|---------|------------|------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Masaüstü GUI | WPF arayüzü ile görüntü sınıflandırma |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Geleneksel GUI | Windows Forms ile görüntü sınıflandırma |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Modern GUI | WinUI 3 arayüzü ile görüntü sınıflandırma |

#### Python Örnekleri

| Örnek | Dil | Odak Alanı | Temel Özellikler |
|-------|-----|------------|------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Görüntü Sınıflandırma | WinML Python bağlamaları, toplu görüntü işleme |

### Örnek Ön Koşulları

**Sistem Gereksinimleri:**  
- Windows 11 PC, sürüm 24H2 (yapı 26100) veya daha yüksek  
- C++ ve .NET iş yükleri ile Visual Studio 2022  
- Windows App SDK 1.8.1 veya daha yeni  
- x64 ve ARM64 cihazlarda Python örnekleri için Python 3.10-3.13  

**Windows AI Foundry Özel:**  
- Optimal performans için Copilot+ PC önerilir  
- Windows AI örnekleri için ARM64 yapılandırması  
- Paket kimliği gerekli (paketlenmemiş uygulamalar artık desteklenmiyor)  

### Ortak Örnek İş Akışı

Çoğu Windows ML örneği şu standart deseni takip eder:

1. **Ortamı Başlat** - ONNX Runtime ortamı oluşturun  
2. **Çalıştırma Sağlayıcılarını Kaydedin** - Mevcut donanım hızlandırıcılarını keşfedin ve kaydedin (CPU, GPU, NPU)  
3. **Modeli Yükle** - ONNX modelini yükleyin, isteğe bağlı olarak hedef donanım için derleyin  
4. **Girdi Ön İşleme** - Görüntüleri/verileri model giriş formatına dönüştürün  
5. **Çıkarım Çalıştır** - Modeli çalıştırın ve tahminler alın  
6. **Sonuçları İşleyin** - Softmax uygulayın ve en iyi tahminleri görüntüleyin  

### Kullanılan Model Dosyaları

| Model | Amaç | Dahil | Notlar |
|-------|------|-------|-------|
| SqueezeNet | Hafif görüntü sınıflandırma | ✅ Dahil | Önceden eğitilmiş, kullanıma hazır |
| ResNet-50 | Yüksek doğrulukta görüntü sınıflandırma | ❌ Dönüştürme gerekli | Dönüştürme için [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) kullanın |

### Donanım Desteği

Tüm örnekler mevcut donanımı otomatik olarak algılar ve kullanır:  
- **CPU** - Tüm Windows cihazlarında evrensel destek  
- **GPU** - Mevcut grafik donanımı için otomatik algılama ve optimizasyon  
- **NPU** - Desteklenen cihazlarda Neural Processing Unit'lerden yararlanır (Copilot+ PC'ler)

## Windows AI Foundry Platform Bileşenleri

### 1. Windows AI API'leri

Windows AI API'leri, cihaz üzerinde modeller tarafından desteklenen, Copilot+ PC cihazlarında verimlilik ve performans için optimize edilmiş, kullanıma hazır yapay zeka yetenekleri sağlar.

#### Temel API Kategorileri

**Phi Silica Dil Modeli**  
- Metin üretimi ve akıl yürütme için küçük ama güçlü dil modeli  
- Minimum güç tüketimi ile gerçek zamanlı çıkarım için optimize edilmiş  
- LoRA tekniklerini kullanarak özel ince ayar desteği  
- Windows semantik arama ve bilgi alma ile entegrasyon  

**Bilgisayar Görme API'leri**  
- **Metin Tanıma (OCR)**: Görüntülerden yüksek doğrulukla metin çıkarma  
- **Görüntü Süper Çözünürlük**: Yerel yapay zeka modelleri kullanarak görüntüleri büyütme  
- **Görüntü Segmentasyonu**: Görüntülerdeki belirli nesneleri tanımlama ve ayırma  
- **Görüntü Açıklaması**: Görsel içerik için ayrıntılı metin açıklamaları oluşturma  
- **Nesne Silme**: Görüntülerden istenmeyen nesneleri yapay zeka destekli doldurma ile kaldırma  

**Çok Modlu Yetkinlikler**  
- **Görsel-Metin Entegrasyonu**: Metin ve görüntü anlayışını birleştirme  
- **Semantik Arama**: Multimedya içerik üzerinde doğal dil sorguları etkinleştirme  
- **Bilgi Alma**: Yerel verilerle akıllı arama deneyimleri oluşturma  

### 2. Foundry Local

Foundry Local, geliştiricilere Windows Silicon üzerinde açık kaynaklı dil modellerine hızlı erişim sağlar ve yerel uygulamalarda modelleri gözden geçirme, test etme, etkileşim kurma ve dağıtma yeteneği sunar.

#### Foundry Local Örnek Uygulamaları

[Foundry Local deposu](https://github.com/microsoft/Foundry-Local/tree/main/samples), çeşitli programlama dilleri ve çerçeveler arasında kapsamlı örnekler sunar ve çeşitli entegrasyon desenlerini ve kullanım durumlarını gösterir.

| Örnek | Dil/Çerçeve | Odak Alanı | Temel Özellikler |
|-------|-------------|------------|------------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | RAG Uygulaması | Semantik Kernel entegrasyonu, Qdrant vektör deposu, JINA gömme, belge alma, akışlı sohbet |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Masaüstü Sohbet Uygulaması | Çapraz platform sohbet, yerel/bulut model geçişi, OpenAI SDK entegrasyonu, gerçek zamanlı akış |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Temel Entegrasyon | Basit SDK kullanımı, model başlatma, temel sohbet işlevselliği |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Temel Entegrasyon | Python SDK kullanımı, akışlı yanıtlar, OpenAI uyumlu API |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Sistem Entegrasyonu | Düşük seviyeli SDK kullanımı, asenkron işlemler, reqwest HTTP istemcisi |

#### Kullanım Durumuna Göre Örnek Kategorileri

**RAG (Retrieval-Augmented Generation)**  
- **dotNET/rag**: Semantik Kernel, Qdrant vektör veritabanı ve JINA gömme kullanarak tam RAG uygulaması  
- **Mimari**: Belge alma → Metin parçalama → Vektör gömme → Benzerlik arama → Bağlam farkındalıklı yanıtlar  
- **Teknolojiler**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX gömme, akışlı sohbet tamamlama  


- **Özellikler**: Model seçici, akış yanıtları, hata yönetimi, platformlar arası dağıtım  
- **Mimari**: Electron ana işlem, IPC iletişimi, güvenli preload scriptleri  

**SDK Entegrasyon Örnekleri**  
- **JavaScript (Node.js)**: Temel model etkileşimi ve akış yanıtları  
- **Python**: OpenAI uyumlu API kullanımı ile asenkron akış  
- **Rust**: Asenkron işlemler için reqwest ve tokio ile düşük seviyeli entegrasyon  

#### Foundry Local Örnekleri için Ön Koşullar  

**Sistem Gereksinimleri:**  
- Foundry Local yüklü Windows 11  
- JavaScript/Electron örnekleri için Node.js v16+  
- C# örnekleri için .NET 8.0+  
- Python örnekleri için Python 3.10+  
- Rust örnekleri için Rust 1.70+  

**Kurulum:**  
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```
  

#### Örnek Bazlı Kurulum  

**dotNET RAG Örneği:**  
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```
  
**Electron Chat Örneği:**  
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```
  
**JavaScript/Python/Rust Örnekleri:**  
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```
  

#### Temel Özellikler  

**Model Kataloğu**  
- Önceden optimize edilmiş açık kaynaklı modellerin kapsamlı koleksiyonu  
- CPU, GPU ve NPU'lar üzerinde optimize edilmiş modellerle anında dağıtım  
- Llama, Mistral, Phi ve özel alan modelleri gibi popüler model ailelerini destekler  

**CLI Entegrasyonu**  
- Model yönetimi ve dağıtımı için komut satırı arayüzü  
- Otomatik optimizasyon ve kuantizasyon iş akışları  
- Popüler geliştirme ortamları ve CI/CD süreçleriyle entegrasyon  

**Yerel Dağıtım**  
- Bulut bağımlılığı olmadan tamamen çevrimdışı çalışma  
- Özel model formatları ve yapılandırmalarını destekler  
- Otomatik donanım optimizasyonu ile verimli model sunumu  

### 3. Windows ML  

Windows ML, Windows üzerinde özel modellerin geniş donanım ekosistemi boyunca verimli bir şekilde dağıtılmasını sağlayan temel AI platformu ve entegre çıkarım çalışma zamanı olarak hizmet verir.  

#### Mimari Avantajlar  

**Evrensel Donanım Desteği**  
- AMD, Intel, NVIDIA ve Qualcomm silikon için otomatik optimizasyon  
- CPU, GPU ve NPU yürütme desteği ile şeffaf geçiş  
- Platforma özgü optimizasyon çalışmalarını ortadan kaldıran donanım soyutlama  

**Model Esnekliği**  
- Popüler çerçevelerden otomatik dönüşüm ile ONNX model formatını destekler  
- Üretim seviyesinde performansla özel model dağıtımı  
- Mevcut Windows uygulama mimarileriyle entegrasyon  

**Kurumsal Entegrasyon**  
- Windows güvenlik ve uyumluluk çerçeveleriyle uyumlu  
- Kurumsal dağıtım ve yönetim araçlarını destekler  
- Windows cihaz yönetimi ve izleme sistemleriyle entegrasyon  

## Geliştirme İş Akışı  

### Aşama 1: Ortam Kurulumu ve Araç Yapılandırması  

**Geliştirme Ortamı Hazırlığı**  
1. C++ ve .NET iş yükleriyle Visual Studio 2022'yi yükleyin  
2. Windows App SDK 1.8.1 veya daha yenisini yükleyin  
3. Windows AI Foundry CLI araçlarını yapılandırın  
4. Visual Studio Code için AI Toolkit uzantısını kurun  
5. Performans profil oluşturma ve izleme araçlarını kurun  
6. Copilot+ PC optimizasyonu için ARM64 yapı yapılandırmasını sağlayın  

**Örnek Depo Kurulumu**  
1. [Windows App SDK Samples deposunu](https://github.com/microsoft/WindowsAppSDK-Samples) klonlayın  
2. Windows AI API örnekleri için `Samples/WindowsAIFoundry/cs-winui` dizinine gidin  
3. Kapsamlı Windows ML örnekleri için `Samples/WindowsML` dizinine gidin  
4. Hedef platformlarınız için [yapı gereksinimlerini](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) inceleyin  

**AI Geliştirme Galerisi Keşfi**  
- Örnek uygulamaları ve referans uygulamaları keşfedin  
- Windows AI API'lerini etkileşimli demolarla test edin  
- En iyi uygulamalar ve desenler için kaynak kodu inceleyin  
- Özel kullanım durumunuz için ilgili örnekleri belirleyin  

### Aşama 2: Model Seçimi ve Entegrasyon  

**Gereksinim Analizi**  
- AI yetenekleri için işlevsel gereksinimleri tanımlayın  
- Performans kısıtlamalarını ve optimizasyon hedeflerini belirleyin  
- Gizlilik ve güvenlik gereksinimlerini değerlendirin  
- Dağıtım mimarisi ve ölçeklendirme stratejilerini planlayın  

**Model Değerlendirme**  
- Kullanım durumunuz için açık kaynaklı modelleri test etmek için Foundry Local'ı kullanın  
- Özel model gereksinimlerine karşı Windows AI API'lerini kıyaslayın  
- Model boyutu, doğruluk ve çıkarım hızı arasındaki ödünleşimleri değerlendirin  
- Seçilen modellerle entegrasyon yaklaşımlarını prototipleyin  

### Aşama 3: Uygulama Geliştirme  

**Temel Entegrasyon**  
- Uygun hata yönetimi ile Windows AI API entegrasyonunu uygulayın  
- AI işleme iş akışlarını destekleyen kullanıcı arayüzleri tasarlayın  
- Model çıkarımı için önbellekleme ve optimizasyon stratejileri uygulayın  
- AI operasyon performansı için telemetri ve izleme ekleyin  

**Test ve Doğrulama**  
- Uygulamaları farklı Windows donanım yapılandırmaları üzerinde test edin  
- Çeşitli yük koşulları altında performans metriklerini doğrulayın  
- AI işlevselliği güvenilirliği için otomatik testler uygulayın  
- AI destekli özelliklerle kullanıcı deneyimi testleri gerçekleştirin  

### Aşama 4: Optimizasyon ve Dağıtım  

**Performans Optimizasyonu**  
- Hedef donanım yapılandırmaları arasında uygulama performansını profilleyin  
- Bellek kullanımı ve model yükleme stratejilerini optimize edin  
- Mevcut donanım yeteneklerine dayalı uyarlanabilir davranışlar uygulayın  
- Farklı performans senaryoları için kullanıcı deneyimini ince ayar yapın  

**Üretim Dağıtımı**  
- Uygulamaları uygun AI model bağımlılıkları ile paketleyin  
- Modeller ve uygulama mantığı için güncelleme mekanizmaları uygulayın  
- Üretim ortamları için izleme ve analiz yapılandırın  
- Kurumsal ve tüketici dağıtımları için yayılma stratejileri planlayın  

## Pratik Uygulama Örnekleri  

### Örnek 1: Akıllı Belge İşleme Uygulaması  

Birden fazla AI yeteneği kullanarak belgeleri işleyen bir Windows uygulaması oluşturun:  

**Kullanılan Teknolojiler:**  
- Belge özetleme ve soru yanıtlama için Phi Silica  
- Tarama belgelerinden metin çıkarımı için OCR API'leri  
- Grafik ve diyagram analizi için Görüntü Açıklama API'leri  
- Belge sınıflandırması için özel ONNX modelleri  

**Uygulama Yaklaşımı:**  
- Modüler AI bileşenleriyle eklenti mimarisi tasarlayın  
- Büyük belge grupları için asenkron işleme uygulayın  
- Uzun süreli işlemler için ilerleme göstergeleri ve iptal desteği ekleyin  
- Hassas belge işleme için çevrimdışı yetenekler dahil edin  

### Örnek 2: Perakende Envanter Yönetim Sistemi  

Perakende uygulamaları için AI destekli bir envanter sistemi oluşturun:  

**Kullanılan Teknolojiler:**  
- Ürün tanımlama için Görüntü Segmentasyonu  
- Marka ve kategori sınıflandırması için özel görüntü modelleri  
- Özel perakende dil modellerinin Foundry Local dağıtımı  
- Mevcut POS ve envanter sistemleriyle entegrasyon  

**Uygulama Yaklaşımı:**  
- Gerçek zamanlı ürün taraması için kamera entegrasyonu oluşturun  
- Barkod ve görsel ürün tanıma uygulayın  
- Yerel dil modelleri kullanarak doğal dil envanter sorguları ekleyin  
- Çok mağazalı dağıtım için ölçeklenebilir mimari tasarlayın  

### Örnek 3: Sağlık Belgeleri Asistanı  

Gizliliği koruyan bir sağlık belgeleri aracı geliştirin:  

**Kullanılan Teknolojiler:**  
- Tıbbi not oluşturma ve klinik karar desteği için Phi Silica  
- El yazısı tıbbi kayıtları dijitalleştirmek için OCR  
- Windows ML aracılığıyla dağıtılan özel tıbbi dil modelleri  
- Tıbbi bilgi geri alımı için yerel vektör depolama  

**Uygulama Yaklaşımı:**  
- Hasta gizliliği için tamamen çevrimdışı çalışma sağlayın  
- Tıbbi terminoloji doğrulama ve öneri uygulayın  
- Düzenleyici uyumluluk için denetim kaydı ekleyin  
- Mevcut Elektronik Sağlık Kaydı sistemleriyle entegrasyon tasarlayın  

## Performans Optimizasyon Stratejileri  

### Donanım Farkındalığı ile Geliştirme  

**NPU Optimizasyonu**  
- Copilot+ PC'lerde NPU yeteneklerinden yararlanacak uygulamalar tasarlayın  
- NPU olmayan cihazlarda GPU/CPU'ya zarif bir şekilde geçiş yapın  
- NPU'ya özgü hızlandırma için model formatlarını optimize edin  
- NPU kullanımını ve termal özelliklerini izleyin  

**Bellek Yönetimi**  
- Verimli model yükleme ve önbellekleme stratejileri uygulayın  
- Başlangıç süresini azaltmak için büyük modeller için bellek eşleme kullanın  
- Kaynak kısıtlı cihazlar için bellek dostu uygulamalar tasarlayın  
- Bellek optimizasyonu için model kuantizasyonu uygulayın  

**Pil Verimliliği**  
- Minimum güç tüketimi için AI işlemlerini optimize edin  
- Pil durumuna göre uyarlanabilir işlem uygulayın  
- Sürekli AI işlemleri için verimli arka plan işleme tasarlayın  
- Enerji kullanımını optimize etmek için güç profil oluşturma araçlarını kullanın  

### Ölçeklenebilirlik Düşünceleri  

**Çoklu İş Parçacığı**  
- Eşzamanlı işlem için iş parçacığı güvenli AI işlemleri tasarlayın  
- Mevcut çekirdekler arasında verimli iş dağıtımı uygulayın  
- Engellemeyen AI işlemleri için async/await desenlerini kullanın  
- Farklı donanım yapılandırmaları için iş parçacığı havuzu optimizasyonu planlayın  

**Önbellekleme Stratejileri**  
- Sık kullanılan AI işlemleri için akıllı önbellekleme uygulayın  
- Model güncellemeleri için önbellek geçersiz kılma stratejileri tasarlayın  
- Pahalı ön işleme işlemleri için kalıcı önbellekleme kullanın  
- Çok kullanıcılı senaryolar için dağıtılmış önbellekleme uygulayın  

## Güvenlik ve Gizlilik En İyi Uygulamaları  

### Veri Koruma  

**Yerel İşleme**  
- Hassas verilerin asla yerel cihazdan ayrılmamasını sağlayın  
- AI modelleri ve geçici veriler için güvenli depolama uygulayın  
- Uygulama sandboxing için Windows güvenlik özelliklerini kullanın  
- Depolanan modeller ve ara işleme sonuçları için şifreleme uygulayın  

**Model Güvenliği**  
- Yükleme ve yürütmeden önce model bütünlüğünü doğrulayın  
- Güvenli model güncelleme mekanizmaları uygulayın  
- Manipülasyonu önlemek için imzalı modeller kullanın  
- Model dosyaları ve yapılandırma için erişim kontrolleri uygulayın  

### Uyumluluk Düşünceleri  

**Düzenleyici Uyum**  
- Uygulamaları GDPR, HIPAA ve diğer düzenleyici gereksinimlere uygun şekilde tasarlayın  
- AI karar verme süreçleri için denetim kaydı uygulayın  
- AI tarafından oluşturulan sonuçlar için şeffaflık özellikleri sağlayın  
- Kullanıcıların AI veri işleme üzerinde kontrol sahibi olmasını sağlayın  

**Kurumsal Güvenlik**  
- Windows kurumsal güvenlik politikalarıyla entegrasyon sağlayın  
- Kurumsal yönetim araçları aracılığıyla yönetilen dağıtımı destekleyin  
- AI özellikleri için rol tabanlı erişim kontrolleri uygulayın  
- AI işlevselliği için yönetim kontrolleri sağlayın  

## Sorun Giderme ve Hata Ayıklama  

### Yaygın Geliştirme Zorlukları  

**Yapılandırma Sorunları**  
- Windows AI API örnekleri için ARM64 platform yapılandırmasını sağlayın  
- Windows App SDK sürüm uyumluluğunu doğrulayın (1.8.1+ gerekli)  
- Paket kimliğinin doğru yapılandırıldığından emin olun (Windows AI API'leri için gereklidir)  
- Hedef çerçeve sürümünü destekleyen yapı araçlarını doğrulayın  

**Model Yükleme Sorunları**  
- ONNX model uyumluluğunu Windows ML ile doğrulayın  
- Model dosyası bütünlüğünü ve format gereksinimlerini kontrol edin  
- Belirli modeller için donanım yetenek gereksinimlerini doğrulayın  
- Model yükleme sırasında bellek tahsisi sorunlarını hata ayıklayın  
- Donanım hızlandırma için yürütme sağlayıcı kaydını sağlayın  

**Dağıtım Modu Düşünceleri**  
- **Kendi Kendine İçerik Modu**: Daha büyük dağıtım boyutuyla tamamen desteklenir  
- **Çerçeveye Bağımlı Mod**: Daha küçük ayak izi ancak paylaşılan çalışma zamanı gerektirir  
- **Paketlenmemiş Uygulamalar**: Windows AI API'leri için artık desteklenmiyor  
- Kendi kendine içerik ARM64 dağıtımı için `dotnet run -p:Platform=ARM64 -p:SelfContained=true` kullanın  

**Performans Sorunları**  
- Farklı donanım yapılandırmaları arasında uygulama performansını profilleyin  
- AI işleme hatlarında darboğazları belirleyin  
- Veri ön işleme ve son işleme işlemlerini optimize edin  
- Performans izleme ve uyarı sistemleri uygulayın  

**Entegrasyon Zorlukları**  
- Uygun hata yönetimi ile API entegrasyon sorunlarını hata ayıklayın  
- Giriş veri formatlarını ve ön işleme gereksinimlerini doğrulayın  
- Kenar durumları ve hata koşullarını kapsamlı bir şekilde test edin  
- Üretim sorunlarını hata ayıklamak için kapsamlı günlük kaydı uygulayın  

### Hata Ayıklama Araçları ve Teknikleri  

**Visual Studio Entegrasyonu**  
- Model yürütme analizi için AI Toolkit hata ayıklayıcıyı kullanın  
- AI işlemleri için performans profil oluşturma uygulayın  
- Uygun istisna yönetimi ile asenkron AI işlemlerini hata ayıklayın  
- Optimizasyon için bellek profil oluşturma araçlarını kullanın  

**Windows AI Foundry Araçları**  
- Model testi ve doğrulama için Foundry Local CLI'den yararlanın  
- Entegrasyon doğrulaması için Windows AI API test araçlarını kullanın  
- AI operasyon izleme için özel günlük kaydı uygulayın  
- AI işlevselliği güvenilirliği için otomatik testler oluşturun  

## Uygulamalarınızı Geleceğe Hazırlama  

### Gelişen Teknolojiler  

**Yeni Nesil Donanım**  
- Gelecekteki NPU yeteneklerinden yararlanacak uygulamalar tasarlayın  
- Artan model boyutları ve karmaşıklığı için plan yapın  
- Gelişen donanım için uyarlanabilir mimariler uygulayın  
- Gelecekteki uyumluluk için kuantum hazır algoritmaları düşünün  

**Gelişmiş AI Yetenekleri**  
- Daha fazla veri türü arasında çok modlu AI entegrasyonu için hazırlanın  
- Birden fazla cihaz arasında gerçek zamanlı işbirlikçi AI planlayın  
- Federated learning yetenekleri için tasarım yapın  
- Edge-bulut hibrit zeka mimarilerini düşünün  

### Sürekli Öğrenme ve Uyarlama  

**Model Güncellemeleri**  
- Sorunsuz model güncelleme mekanizmaları uygulayın  
- Geliştirilmiş model yeteneklerine uyum sağlayacak uygulamalar tasarlayın  
- Mevcut modellerle geriye dönük uyumluluk planlayın  
- Model performans değerlendirmesi için A/B testi uygulayın  

**Özellik Evrimi**  
- Yeni AI yeteneklerini barındıracak modüler mimariler tasarlayın  
- Gelişen Windows AI API'lerinin entegrasyonu için plan yapın  
- Kademeli yetenek yayılımı için özellik bayrakları uygulayın  
- Gelişmiş AI özelliklerine uyum sağlayan kullanıcı arayüzleri tasarlayın  

## Sonuç  

Windows Edge AI geliştirme, güçlü AI yeteneklerinin sağlam, güvenli ve ölçeklenebilir Windows platformuyla birleşimini temsil eder. Windows AI Foundry ekosistemine hakim olarak, geliştiriciler olağanüstü kullanıcı deneyimleri sunan ve gizlilik, güvenlik ve performansın en yüksek standartlarını koruyan akıllı uygulamalar oluşturabilirler.  

Windows AI API'leri, Foundry Local ve Windows ML kombinasyonu
- [Windows App SDK Örnekleri Deposu](https://github.com/microsoft/WindowsAppSDK-Samples)

### Geliştirme Araçları
- [Visual Studio Code için AI Toolkit](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Geliştirici Galerisi](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Örnekleri](https://learn.microsoft.com/windows/ai/samples/)
- [Model Dönüştürme Araçları](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Teknik Destek
- [Windows ML Belgeleri](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime Belgeleri](https://onnxruntime.ai/docs/)
- [Windows App SDK Belgeleri](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Sorun Bildir - Windows App SDK Örnekleri](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Topluluk ve Destek
- [Windows Geliştirici Topluluğu](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blogu](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Eğitimi](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Bu rehber, hızla gelişen Windows AI ekosistemiyle birlikte evrilmek üzere tasarlanmıştır. Düzenli güncellemeler, en son platform yetenekleri ve geliştirme en iyi uygulamalarıyla uyumu sağlar.*

[08. Microsoft Foundry Local ile Uygulamalı Çalışma - Tam Geliştirici Araç Seti](../Module08/README.md)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.