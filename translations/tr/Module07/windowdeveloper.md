<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9c2dacb560380677a2c923171d3e423d",
  "translation_date": "2025-09-22T18:21:11+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "tr"
}
-->
# Windows Edge AI Geliştirme Rehberi

## Giriş

Windows Edge AI Geliştirme'ye hoş geldiniz - Microsoft'un Windows AI Foundry platformunu kullanarak cihaz üzerinde yapay zeka gücünden yararlanan akıllı uygulamalar oluşturmanız için kapsamlı rehberiniz. Bu rehber, Windows geliştiricilerinin en son Edge AI özelliklerini uygulamalarına entegre ederken Windows donanım hızlandırmasının tüm avantajlarından faydalanmalarını sağlamak için özel olarak tasarlanmıştır.

### Windows AI Avantajı

Windows AI Foundry, model seçimi ve ince ayarından optimizasyon ve CPU, GPU, NPU ve hibrit bulut mimarileri üzerinde dağıtıma kadar tüm yapay zeka geliştirici yaşam döngüsünü destekleyen birleşik, güvenilir ve güvenli bir platform sunar. Bu platform, yapay zeka geliştirmeyi demokratikleştirerek şu avantajları sağlar:

- **Donanım Soyutlama**: AMD, Intel, NVIDIA ve Qualcomm silikonları arasında sorunsuz dağıtım
- **Cihaz Üzerinde Zeka**: Tamamen yerel donanımda çalışan, gizliliği koruyan yapay zeka
- **Optimize Performans**: Windows donanım yapılandırmaları için önceden optimize edilmiş modeller
- **Kurumsal Hazırlık**: Üretim seviyesinde güvenlik ve uyumluluk özellikleri

### Neden Windows Edge AI için?

**Evrensel Donanım Desteği**  
Windows ML, tüm Windows ekosistemi genelinde otomatik donanım optimizasyonu sağlar, böylece yapay zeka uygulamalarınız altta yatan silikon mimarisinden bağımsız olarak en iyi performansı gösterir.

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
- Gerçek zamanlı çıkarımı optimal kaynak kullanımı ile uygulayın  
- Çeşitli Windows cihaz kategorileri için ölçeklenebilir yapay zeka uygulamaları tasarlayın  

### Uygulama Geliştirme Becerileri

**Çapraz Platform Windows Geliştirme**  
- Evrensel Windows dağıtımı için .NET MAUI kullanarak yapay zeka destekli uygulamalar oluşturun  
- Yapay zeka yeteneklerini Win32, UWP ve İlerleyici Web Uygulamalarına entegre edin  
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
- Gizliliği korurken zekayı mümkün kılan veri akışı mimarilerini planlayın  
- Kullanıcı talepleriyle ölçeklenen maliyet etkin yapay zeka çözümleri uygulayın  

**Pazar Konumlandırması**  
- Windows'a özgü yapay zeka uygulamalarının rekabet avantajlarını anlayın  
- Cihaz üzerinde yapay zekanın üstün kullanıcı deneyimleri sağladığı kullanım senaryolarını belirleyin  
- Yapay zeka destekli Windows uygulamaları için pazara giriş stratejileri geliştirin  
- Uygulamaları Windows ekosisteminin avantajlarından yararlanacak şekilde konumlandırın  

## Windows AI Foundry Platform Bileşenleri

### 1. Windows AI API'leri

Windows AI API'leri, Copilot+ PC cihazlarında minimum kurulum gereksinimiyle verimlilik ve performans için optimize edilmiş cihaz üzerindeki modeller tarafından desteklenen kullanıma hazır yapay zeka yetenekleri sağlar.

#### Temel API Kategorileri

**Phi Silica Dil Modeli**  
- Metin üretimi ve akıl yürütme için küçük ama güçlü dil modeli  
- Minimum güç tüketimiyle gerçek zamanlı çıkarım için optimize edilmiş  
- LoRA tekniklerini kullanarak özel ince ayar desteği  
- Windows semantik arama ve bilgi alma ile entegrasyon  

**Bilgisayar Görme API'leri**  
- **Metin Tanıma (OCR)**: Görüntülerden yüksek doğrulukla metin çıkarma  
- **Görüntü Süper Çözünürlük**: Yerel yapay zeka modelleri kullanarak görüntüleri yükseltme  
- **Görüntü Segmentasyonu**: Görüntülerdeki belirli nesneleri tanımlama ve ayırma  
- **Görüntü Açıklaması**: Görsel içerik için ayrıntılı metin açıklamaları oluşturma  
- **Nesne Silme**: Görüntülerden istenmeyen nesneleri yapay zeka destekli boyama ile kaldırma  

**Çok Modlu Yetkinlikler**  
- **Görsel-Metin Entegrasyonu**: Metin ve görüntü anlayışını birleştirme  
- **Semantik Arama**: Multimedya içerik üzerinde doğal dil sorguları etkinleştirme  
- **Bilgi Alma**: Yerel veriyle akıllı arama deneyimleri oluşturma  

### 2. Foundry Local

Foundry Local, geliştiricilere Windows Silicon üzerinde yerel uygulamalarda modelleri gözden geçirme, test etme, etkileşimde bulunma ve dağıtma yeteneği sunan kullanıma hazır açık kaynaklı dil modellerine hızlı erişim sağlar.

#### Temel Özellikler

**Model Kataloğu**  
- Önceden optimize edilmiş açık kaynaklı modellerin kapsamlı koleksiyonu  
- Anında dağıtım için CPU, GPU ve NPU'lar arasında optimize edilmiş modeller  
- Llama, Mistral, Phi ve özel alan modelleri gibi popüler model aileleri için destek  

**CLI Entegrasyonu**  
- Model yönetimi ve dağıtımı için komut satırı arayüzü  
- Otomatik optimizasyon ve kuantizasyon iş akışları  
- Popüler geliştirme ortamları ve CI/CD boru hatları ile entegrasyon  

**Yerel Dağıtım**  
- Bulut bağımlılıkları olmadan tamamen çevrimdışı çalışma  
- Özel model formatları ve yapılandırmaları için destek  
- Otomatik donanım optimizasyonu ile verimli model sunumu  

### 3. Windows ML

Windows ML, geliştiricilerin geniş Windows donanım ekosistemi genelinde özel modelleri verimli bir şekilde dağıtmasına olanak tanıyan temel yapay zeka platformu ve entegre çıkarım çalışma zamanıdır.

#### Mimari Avantajlar

**Evrensel Donanım Desteği**  
- AMD, Intel, NVIDIA ve Qualcomm silikonları için otomatik optimizasyon  
- CPU, GPU ve NPU yürütme desteği ile şeffaf geçiş  
- Platforma özgü optimizasyon çalışmalarını ortadan kaldıran donanım soyutlama  

**Model Esnekliği**  
- Popüler çerçevelerden otomatik dönüşüm ile ONNX model formatı desteği  
- Üretim seviyesinde performansla özel model dağıtımı  
- Mevcut Windows uygulama mimarileri ile entegrasyon  

**Kurumsal Entegrasyon**  
- Windows güvenlik ve uyumluluk çerçeveleri ile uyumlu  
- Kurumsal dağıtım ve yönetim araçları için destek  
- Windows cihaz yönetimi ve izleme sistemleri ile entegrasyon  

## Geliştirme İş Akışı

### Aşama 1: Ortam Kurulumu ve Araç Yapılandırması

**Geliştirme Ortamı Hazırlığı**  
1. Visual Studio'yu AI Toolkit uzantısı ile yükleyin  
2. Windows AI Foundry CLI araçlarını yapılandırın  
3. Yerel model test ortamını kurun  
4. Performans profilleme ve izleme araçlarını oluşturun  

**AI Dev Galerisi Keşfi**  
- Örnek uygulamaları ve referans uygulamaları keşfedin  
- Windows AI API'lerini etkileşimli demolarla test edin  
- En iyi uygulamalar ve desenler için kaynak kodu inceleyin  
- Özel kullanım senaryonuz için ilgili örnekleri belirleyin  

### Aşama 2: Model Seçimi ve Entegrasyonu

**Gereksinim Analizi**  
- Yapay zeka yetenekleri için işlevsel gereksinimleri tanımlayın  
- Performans kısıtlamalarını ve optimizasyon hedeflerini belirleyin  
- Gizlilik ve güvenlik gereksinimlerini değerlendirin  
- Dağıtım mimarisi ve ölçekleme stratejilerini planlayın  

**Model Değerlendirme**  
- Kullanım senaryonuz için açık kaynaklı modelleri test etmek için Foundry Local'i kullanın  
- Özel model gereksinimlerine karşı Windows AI API'lerini karşılaştırın  
- Model boyutu, doğruluk ve çıkarım hızı arasındaki ödünleşimleri değerlendirin  
- Seçilen modellerle entegrasyon yaklaşımlarını prototipleyin  

### Aşama 3: Uygulama Geliştirme

**Temel Entegrasyon**  
- Windows AI API entegrasyonunu uygun hata işleme ile uygulayın  
- Yapay zeka işlem iş akışlarını barındıran kullanıcı arayüzleri tasarlayın  
- Model çıkarımı için önbellek ve optimizasyon stratejileri uygulayın  
- Yapay zeka işlem performansı için telemetri ve izleme ekleyin  

**Test ve Doğrulama**  
- Farklı Windows donanım yapılandırmaları arasında uygulamaları test edin  
- Çeşitli yük koşulları altında performans metriklerini doğrulayın  
- Yapay zeka işlevselliği güvenilirliği için otomatik testler uygulayın  
- Yapay zeka destekli özelliklerle kullanıcı deneyimi testleri gerçekleştirin  

### Aşama 4: Optimizasyon ve Dağıtım

**Performans Optimizasyonu**  
- Hedef donanım yapılandırmaları arasında uygulama performansını profilleyin  
- Bellek kullanımı ve model yükleme stratejilerini optimize edin  
- Mevcut donanım yeteneklerine dayalı uyarlanabilir davranış uygulayın  
- Farklı performans senaryoları için kullanıcı deneyimini ince ayar yapın  

**Üretim Dağıtımı**  
- Uygulamaları uygun yapay zeka model bağımlılıkları ile paketleyin  
- Modeller ve uygulama mantığı için güncelleme mekanizmaları uygulayın  
- Üretim ortamları için izleme ve analiz yapılandırın  
- Kurumsal ve tüketici dağıtımları için yayılma stratejileri planlayın  

## Pratik Uygulama Örnekleri

### Örnek 1: Akıllı Belge İşleme Uygulaması

Birden fazla yapay zeka yeteneği kullanarak belgeleri işleyen bir Windows uygulaması oluşturun:

**Kullanılan Teknolojiler:**  
- Belge özetleme ve soru yanıtlama için Phi Silica  
- Tarama belgelerinden metin çıkarma için OCR API'leri  
- Grafik ve diyagram analizi için Görüntü Açıklama API'leri  
- Belge sınıflandırması için özel ONNX modelleri  

**Uygulama Yaklaşımı:**  
- Modüler yapay zeka bileşenleriyle tasarım mimarisi oluşturun  
- Büyük belge grupları için asenkron işlem uygulayın  
- Uzun süreli işlemler için ilerleme göstergeleri ve iptal desteği ekleyin  
- Hassas belge işleme için çevrimdışı yetenekler dahil edin  

### Örnek 2: Perakende Envanter Yönetim Sistemi

Perakende uygulamalar için yapay zeka destekli bir envanter sistemi oluşturun:

**Kullanılan Teknolojiler:**  
- Ürün tanımlama için Görüntü Segmentasyonu  
- Marka ve kategori sınıflandırması için özel görsel modeller  
- Özel perakende dil modellerinin Foundry Local dağıtımı  
- Mevcut POS ve envanter sistemleri ile entegrasyon  

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
- Tıbbi bilgi alma için yerel vektör depolama  

**Uygulama Yaklaşımı:**  
- Hasta gizliliği için tamamen çevrimdışı çalışma sağlayın  
- Tıbbi terminoloji doğrulama ve öneri uygulayın  
- Düzenleyici uyumluluk için denetim kaydı ekleyin  
- Mevcut Elektronik Sağlık Kaydı sistemleri ile entegrasyon tasarlayın  

## Performans Optimizasyon Stratejileri

### Donanım Bilinçli Geliştirme

**NPU Optimizasyonu**  
- Copilot+ PC'lerde NPU yeteneklerinden yararlanacak uygulamalar tasarlayın  
- NPU olmayan cihazlarda GPU/CPU'ya zarif bir şekilde geçiş yapın  
- NPU'ya özgü hızlandırma için model formatlarını optimize edin  
- NPU kullanımını ve termal özelliklerini izleyin  

**Bellek Yönetimi**  
- Büyük modeller için verimli model yükleme ve önbellek stratejileri uygulayın  
- Başlangıç süresini azaltmak için bellek eşleme kullanın  
- Kaynak kısıtlı cihazlar için bellek bilinci uygulamalar tasarlayın  
- Bellek optimizasyonu için model kuantizasyonu uygulayın  

**Pil Verimliliği**  
- Minimum güç tüketimi için yapay zeka işlemlerini optimize edin  
- Pil durumuna dayalı uyarlanabilir işlem uygulayın  
- Sürekli yapay zeka işlemleri için verimli arka plan işlem tasarlayın  
- Enerji kullanımını optimize etmek için güç profilleme araçlarını kullanın  

### Ölçeklenebilirlik Düşünceleri

**Çoklu İş Parçacığı**  
- Eşzamanlı işlem için iş parçacığı güvenli yapay zeka işlemleri tasarlayın  
- Mevcut çekirdekler arasında verimli iş dağıtımı uygulayın  
- Engellemeyen yapay zeka işlemleri için async/await desenlerini kullanın  
- Farklı donanım yapılandırmaları için iş parçacığı havuzu optimizasyonunu planlayın  

**Önbellek Stratejileri**  
- Sık kullanılan yapay zeka işlemleri için akıllı önbellek uygulayın  
- Model güncellemeleri için önbellek geçersiz kılma stratejileri tasarlayın  
-
- Model test etme ve doğrulama için Foundry Local CLI'yi kullanın  
- Entegrasyon doğrulaması için Windows AI API test araçlarını kullanın  
- AI operasyon takibi için özel loglama uygulayın  
- AI işlevselliğinin güvenilirliği için otomatik testler oluşturun  

## Uygulamalarınızı Geleceğe Hazırlama  

### Gelişen Teknolojiler  

**Yeni Nesil Donanım**  
- Uygulamaları gelecekteki NPU yeteneklerinden faydalanacak şekilde tasarlayın  
- Artan model boyutları ve karmaşıklığı için plan yapın  
- Gelişen donanımlara uyum sağlayacak adaptif mimariler uygulayın  
- Gelecekte uyumluluk için kuantum hazır algoritmaları göz önünde bulundurun  

**Gelişmiş AI Yetenekleri**  
- Daha fazla veri türü arasında çok modlu AI entegrasyonuna hazırlanın  
- Birden fazla cihaz arasında gerçek zamanlı işbirlikçi AI için plan yapın  
- Federated learning yetenekleri için tasarım yapın  
- Edge-cloud hibrit zeka mimarilerini göz önünde bulundurun  

### Sürekli Öğrenme ve Uyarlama  

**Model Güncellemeleri**  
- Sorunsuz model güncelleme mekanizmaları uygulayın  
- Uygulamaları geliştirilmiş model yeteneklerine uyum sağlayacak şekilde tasarlayın  
- Mevcut modellerle geriye dönük uyumluluk için plan yapın  
- Model performans değerlendirmesi için A/B testleri uygulayın  

**Özellik Gelişimi**  
- Yeni AI yeteneklerini destekleyecek modüler mimariler tasarlayın  
- Gelişen Windows AI API'lerinin entegrasyonu için plan yapın  
- Kademeli yetenek sunumu için özellik bayrakları uygulayın  
- Gelişmiş AI özelliklerine uyum sağlayan kullanıcı arayüzleri tasarlayın  

## Sonuç  

Windows Edge AI geliştirme, güçlü AI yeteneklerini sağlam, güvenli ve ölçeklenebilir Windows platformuyla birleştirir. Windows AI Foundry ekosistemine hakim olarak, geliştiriciler hem üstün kullanıcı deneyimleri sunan hem de gizlilik, güvenlik ve performans standartlarını en üst düzeyde tutan akıllı uygulamalar oluşturabilirler.  

Windows AI API'leri, Foundry Local ve Windows ML'nin birleşimi, bir sonraki nesil akıllı Windows uygulamalarını oluşturmak için eşsiz bir temel sağlar. AI sürekli gelişirken, Windows platformu uygulamalarınızın gelişen teknolojilerle ölçeklenmesini ve çeşitli Windows donanım ekosisteminde uyumluluk ve performansını korumasını garanti eder.  

İster tüketici uygulamaları, ister kurumsal çözümler, isterse özel endüstri araçları geliştiriyor olun, Windows Edge AI geliştirme, modern Windows cihazlarının tam potansiyelinden faydalanan akıllı, duyarlı ve derinlemesine entegre deneyimler oluşturmanızı sağlar.  

## Ek Kaynaklar  

Foundry Local'ın adım adım Windows rehberi (kurulum, CLI, dinamik endpoint, SDK kullanımı) için repo kılavuzuna bakın: [foundrylocal.md](./foundrylocal.md).  

### Dokümantasyon ve Öğrenme  
- [Windows AI Foundry Dokümantasyonu](https://learn.microsoft.com/windows/ai/)  
- [Windows AI API'leri Referansı](https://learn.microsoft.com/windows/ai/apis/)  
- [Foundry Local Başlangıç Kılavuzu](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)  
- [Windows ML Genel Bakış](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)  

### Geliştirme Araçları  
- [Visual Studio Code için AI Araç Seti](https://learn.microsoft.com/windows/ai/toolkit/)  
- [AI Geliştirici Galerisi](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)  
- [Windows AI Örnekleri](https://learn.microsoft.com/windows/ai/samples/)  

### Topluluk ve Destek  
- [Windows Geliştirici Topluluğu](https://developer.microsoft.com/en-us/windows/)  
- [Windows AI Foundry Blogu](https://blogs.windows.com/windowsdeveloper/)  
- [Microsoft Learn AI Eğitimi](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)  

---  

*Bu rehber, hızla ilerleyen Windows AI ekosistemine uyum sağlamak için tasarlanmıştır. Düzenli güncellemeler, en son platform yetenekleri ve geliştirme en iyi uygulamalarıyla uyumu garanti eder.*  

---

