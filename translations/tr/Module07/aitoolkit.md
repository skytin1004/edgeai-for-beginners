<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-18T00:21:26+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "tr"
}
-->
# Visual Studio Code için AI Toolkit - Edge AI Geliştirme Rehberi

## Giriş

Edge AI geliştirme için Visual Studio Code AI Toolkit kullanımı hakkında kapsamlı rehbere hoş geldiniz. Yapay zeka, merkezi bulut bilişimden dağıtılmış edge cihazlara doğru ilerlerken, geliştiricilerin edge dağıtımının benzersiz zorluklarını - kaynak kısıtlamalarından çevrimdışı çalışma gereksinimlerine kadar - ele alabilecek güçlü ve entegre araçlara ihtiyacı vardır.

Visual Studio Code için AI Toolkit, edge cihazlarda verimli bir şekilde çalışan yapay zeka uygulamaları oluşturmak, test etmek ve optimize etmek için özel olarak tasarlanmış eksiksiz bir geliştirme ortamı sunarak bu boşluğu doldurur. IoT sensörleri, mobil cihazlar, gömülü sistemler veya edge sunucular için geliştirme yapıyor olun, bu araç seti, tanıdık VS Code ortamında tüm geliştirme iş akışınızı kolaylaştırır.

Bu rehber, AI Toolkit'i Edge AI projelerinizde kullanmak için gerekli temel kavramlar, araçlar ve en iyi uygulamalar konusunda size rehberlik edecek; başlangıçtaki model seçiminden üretim dağıtımına kadar.

## Genel Bakış

AI Toolkit, VS Code içinde eksiksiz bir Edge AI uygulama yaşam döngüsü için entegre bir geliştirme ortamı sağlar. OpenAI, Anthropic, Google ve GitHub gibi sağlayıcılardan popüler yapay zeka modelleriyle sorunsuz entegrasyon sunarken, ONNX ve Ollama aracılığıyla yerel model dağıtımını destekler - cihaz üzerinde çıkarım gerektiren Edge AI uygulamaları için kritik özellikler.

AI Toolkit'i Edge AI geliştirme için ayıran şey, tüm edge dağıtım hattına odaklanmasıdır. Geleneksel yapay zeka geliştirme araçları genellikle bulut dağıtımını hedeflerken, AI Toolkit model optimizasyonu, kaynak kısıtlı testler ve edge'e özgü performans değerlendirmesi için özel özellikler içerir. Araç seti, edge AI geliştirmenin farklı gereksinimler gerektirdiğini anlar - daha küçük model boyutları, daha hızlı çıkarım süreleri, çevrimdışı yetenekler ve donanıma özgü optimizasyonlar.

Platform, basit cihaz üzeri çıkarımdan karmaşık çoklu model edge mimarilerine kadar çeşitli dağıtım senaryolarını destekler. Başarılı edge dağıtımı için gerekli olan model dönüştürme, kuantizasyon ve optimizasyon araçlarını sağlarken, VS Code'un bilinen geliştirici verimliliğini korur.

## Öğrenme Hedefleri

Bu rehberin sonunda şunları yapabileceksiniz:

### Temel Yetkinlikler
- Edge AI geliştirme iş akışları için Visual Studio Code AI Toolkit'i **kurun ve yapılandırın**
- Model Kataloğu, Playground ve Agent Builder dahil olmak üzere AI Toolkit arayüzünde **gezinin ve kullanın**
- Performans ve kaynak kısıtlamalarına dayalı olarak edge dağıtımına uygun yapay zeka modellerini **seçin ve değerlendirin**
- Edge cihazlar için ONNX formatı ve kuantizasyon tekniklerini kullanarak modelleri **dönüştürün ve optimize edin**

### Edge AI Geliştirme Becerileri
- Entegre geliştirme ortamını kullanarak Edge AI uygulamaları **tasarlayın ve uygulayın**
- Yerel çıkarım ve kaynak izleme kullanarak edge benzeri koşullarda model testleri **yapın**
- Edge dağıtım senaryoları için optimize edilmiş yapay zeka ajanları **oluşturun ve özelleştirin**
- Edge bilişimle ilgili metrikleri (gecikme, bellek kullanımı, doğruluk) kullanarak model performansını **değerlendirin**

### Optimizasyon ve Dağıtım
- Model boyutunu azaltmak için **kuantizasyon ve budama tekniklerini uygulayın** ve kabul edilebilir performansı koruyun
- CPU, GPU ve NPU hızlandırma dahil olmak üzere belirli edge donanım platformları için modelleri **optimize edin**
- Kaynak yönetimi ve geri dönüş stratejileri dahil olmak üzere edge AI geliştirme için en iyi uygulamaları **uygulayın**
- Edge cihazlarda üretim dağıtımı için modelleri ve uygulamaları **hazırlayın**

### İleri Düzey Edge AI Kavramları
- ONNX Runtime, Windows ML ve TensorFlow Lite dahil olmak üzere edge AI çerçeveleriyle **entegrasyon sağlayın**
- Edge ortamları için çoklu model mimarileri ve federatif öğrenme senaryolarını **uygulayın**
- Bellek kısıtlamaları, çıkarım hızı ve donanım uyumluluğu gibi yaygın edge AI sorunlarını **çözün**
- Üretimdeki edge AI uygulamaları için izleme ve günlükleme stratejileri **tasarlayın**

### Pratik Uygulama
- Model seçiminden dağıtıma kadar uçtan uca Edge AI çözümleri **oluşturun**
- Edge'e özgü geliştirme iş akışları ve optimizasyon tekniklerinde **uzmanlık gösterin**
- IoT, mobil ve gömülü uygulamalar dahil olmak üzere gerçek dünya edge AI kullanım durumlarına **öğrenilen kavramları uygulayın**
- Farklı edge AI dağıtım stratejilerini ve bunların avantajlarını **değerlendirin ve karşılaştırın**

## Edge AI Geliştirme için Temel Özellikler

### 1. Model Kataloğu ve Keşfi
- **Yerel Model Desteği**: Edge dağıtımı için özel olarak optimize edilmiş yapay zeka modellerini keşfedin ve erişin
- **ONNX Entegrasyonu**: Edge çıkarımı için verimli ONNX formatındaki modellere erişin
- **Ollama Desteği**: Gizlilik ve çevrimdışı çalışma için Ollama aracılığıyla yerel olarak çalışan modellerden yararlanın
- **Model Karşılaştırması**: Edge cihazlar için performans ve kaynak tüketimi arasında optimal dengeyi bulmak için modelleri yan yana karşılaştırın

### 2. Etkileşimli Playground
- **Yerel Test Ortamı**: Edge dağıtımından önce modelleri yerel olarak test edin
- **Çoklu Mod Deneyimi**: Edge senaryolarında tipik olan görüntüler, metinler ve diğer girdilerle test yapın
- **Parametre Ayarı**: Edge kısıtlamalarına göre optimize etmek için farklı model parametreleriyle deney yapın
- **Gerçek Zamanlı Performans İzleme**: Geliştirme sırasında çıkarım hızı ve kaynak kullanımını gözlemleyin

### 3. Edge Uygulamaları için Agent Builder
- **Prompt Mühendisliği**: Daha küçük edge modelleriyle verimli çalışan optimize edilmiş istemler oluşturun
- **MCP Araç Entegrasyonu**: Edge ajan yeteneklerini artırmak için Model Context Protocol araçlarını entegre edin
- **Kod Üretimi**: Edge dağıtım senaryoları için optimize edilmiş üretim kodu oluşturun
- **Yapılandırılmış Çıktılar**: Edge uygulamaları için tutarlı, yapılandırılmış yanıtlar sağlayan ajanlar tasarlayın

### 4. Model Değerlendirme ve Test
- **Performans Metrikleri**: Edge dağıtımıyla ilgili metrikler kullanarak modelleri değerlendirin (gecikme, bellek kullanımı, doğruluk)
- **Toplu Test**: Edge ayarlarını optimize etmek için birden fazla model yapılandırmasını aynı anda test edin
- **Özel Değerlendirme**: Edge AI kullanım durumlarına özel değerlendirme kriterleri oluşturun
- **Kaynak Profili**: Edge dağıtım planlaması için bellek ve hesaplama gereksinimlerini analiz edin

### 5. Model Dönüştürme ve Optimizasyon
- **ONNX Dönüşümü**: Çeşitli formatlardan ONNX'e modelleri dönüştürerek edge uyumluluğu sağlayın
- **Kuantizasyon**: Model boyutunu azaltın ve kuantizasyon teknikleriyle çıkarım hızını artırın
- **Donanım Optimizasyonu**: Belirli edge donanımı (CPU, GPU, NPU) için modelleri optimize edin
- **Format Dönüşümü**: Hugging Face ve diğer kaynaklardan gelen modelleri edge dağıtımı için dönüştürün

### 6. Edge Senaryoları için İnce Ayar
- **Alan Adaptasyonu**: Belirli edge kullanım durumları ve ortamları için modelleri özelleştirin
- **Yerel Eğitim**: Edge'e özgü gereksinimler için GPU desteğiyle modelleri yerel olarak eğitin
- **Azure Entegrasyonu**: Edge dağıtımından önce bulut tabanlı ince ayar için Azure Container Apps'ten yararlanın
- **Transfer Öğrenimi**: Önceden eğitilmiş modelleri edge'e özgü görevler ve kısıtlamalar için uyarlayın

### 7. Performans İzleme ve İzleme
- **Edge Performans Analizi**: Edge benzeri koşullarda model performansını izleyin
- **İz Toplama**: Optimizasyon için ayrıntılı performans verileri toplayın
- **Darboğaz Tanımlama**: Edge cihazlara dağıtımdan önce performans sorunlarını belirleyin
- **Kaynak Kullanımı Takibi**: Edge optimizasyonu için bellek, CPU ve çıkarım süresini izleyin

## Edge AI Geliştirme İş Akışı

### Aşama 1: Model Keşfi ve Seçimi
1. **Model Kataloğunu Keşfedin**: Edge dağıtımı için uygun modelleri bulmak için model kataloğunu kullanın
2. **Performansı Karşılaştırın**: Modelleri boyut, doğruluk ve çıkarım hızı temelinde değerlendirin
3. **Yerel Test Yapın**: Edge dağıtımından önce Ollama veya ONNX modellerini kullanarak yerel test yapın
4. **Kaynak Gereksinimlerini Değerlendirin**: Hedef edge cihazlar için bellek ve hesaplama ihtiyaçlarını belirleyin

### Aşama 2: Model Optimizasyonu
1. **ONNX'e Dönüştürün**: Seçilen modelleri edge uyumluluğu için ONNX formatına dönüştürün
2. **Kuantizasyon Uygulayın**: INT8 veya INT4 kuantizasyon ile model boyutunu azaltın
3. **Donanım Optimizasyonu**: Hedef edge donanımı (ARM, x86, özel hızlandırıcılar) için optimize edin
4. **Performans Doğrulaması**: Optimize edilmiş modellerin kabul edilebilir doğruluğu koruduğunu doğrulayın

### Aşama 3: Uygulama Geliştirme
1. **Ajan Tasarımı**: Agent Builder'ı kullanarak edge'e optimize edilmiş yapay zeka ajanları oluşturun
2. **Prompt Mühendisliği**: Daha küçük edge modelleriyle etkili çalışan istemler geliştirin
3. **Entegrasyon Testi**: Ajanları simüle edilmiş edge koşullarında test edin
4. **Kod Üretimi**: Edge dağıtımı için optimize edilmiş üretim kodu oluşturun

### Aşama 4: Değerlendirme ve Test
1. **Toplu Değerlendirme**: Birden fazla yapılandırmayı test ederek optimal edge ayarlarını bulun
2. **Performans Profili**: Çıkarım hızı, bellek kullanımı ve doğruluğu analiz edin
3. **Edge Simülasyonu**: Hedef edge dağıtım ortamına benzer koşullarda test yapın
4. **Stres Testi**: Çeşitli yük koşulları altında performansı değerlendirin

### Aşama 5: Dağıtım Hazırlığı
1. **Son Optimizasyon**: Test sonuçlarına dayalı son optimizasyonları uygulayın
2. **Dağıtım Paketleme**: Edge dağıtımı için modelleri ve kodu paketleyin
3. **Dokümantasyon**: Dağıtım gereksinimlerini ve yapılandırmayı belgeleyin
4. **İzleme Ayarı**: Üretim dağıtımı için izleme ve günlükleme hazırlayın

## Edge AI Geliştirme için Hedef Kitle

### Edge AI Geliştiricileri
- Yapay zeka destekli edge cihazlar ve IoT çözümleri geliştiren uygulama geliştiricileri
- Kaynak kısıtlı cihazlara yapay zeka yeteneklerini entegre eden gömülü sistem geliştiricileri
- Akıllı telefonlar ve tabletler için cihaz üzeri yapay zeka uygulamaları oluşturan mobil geliştiriciler

### Edge AI Mühendisleri
- Edge dağıtımı için modelleri optimize eden ve çıkarım hatlarını yöneten yapay zeka mühendisleri
- Dağıtılmış edge altyapısında yapay zeka modellerini dağıtan ve yöneten DevOps mühendisleri
- Edge donanım kısıtlamaları için yapay zeka iş yüklerini optimize eden performans mühendisleri

### Araştırmacılar ve Eğitimciler
- Edge bilişim için verimli modeller ve algoritmalar geliştiren yapay zeka araştırmacıları
- Edge AI kavramlarını öğreten ve optimizasyon tekniklerini gösteren eğitimciler
- Edge AI dağıtımındaki zorluklar ve çözümler hakkında bilgi edinen öğrenciler

## Edge AI Kullanım Durumları

### Akıllı IoT Cihazları
- **Gerçek Zamanlı Görüntü Tanıma**: IoT kameraları ve sensörlerinde bilgisayarlı görme modellerini dağıtın
- **Ses İşleme**: Akıllı hoparlörlerde konuşma tanıma ve doğal dil işleme uygulayın
- **Tahmine Dayalı Bakım**: Endüstriyel edge cihazlarında anomali algılama modelleri çalıştırın
- **Çevresel İzleme**: Çevresel uygulamalar için sensör veri analizi modellerini dağıtın

### Mobil ve Gömülü Uygulamalar
- **Cihaz Üzerinde Çeviri**: Çevrimdışı çalışan dil çeviri modellerini uygulayın
- **Artırılmış Gerçeklik**: AR uygulamaları için gerçek zamanlı nesne tanıma ve izleme dağıtın
- **Sağlık İzleme**: Giyilebilir cihazlar ve tıbbi ekipmanlarda sağlık analizi modelleri çalıştırın
- **Otonom Sistemler**: Dronlar, robotlar ve araçlar için karar verme modelleri uygulayın

### Edge Bilişim Altyapısı
- **Edge Veri Merkezleri**: Düşük gecikmeli uygulamalar için edge veri merkezlerinde yapay zeka modellerini dağıtın
- **CDN Entegrasyonu**: İçerik dağıtım ağlarına yapay zeka işleme yeteneklerini entegre edin
- **5G Edge**: 5G edge bilişimden yararlanarak yapay zeka destekli uygulamalar oluşturun
- **Fog Bilişim**: Fog bilişim ortamlarında yapay zeka işleme uygulayın

## Kurulum ve Ayar

### Hızlı Kurulum
AI Toolkit uzantısını doğrudan Visual Studio Code Marketplace'ten yükleyin:

```
Install: AI Toolkit for Visual Studio Code (ms-windows-ai-studio.windows-ai-studio)
```

### Edge AI Geliştirme için Ön Koşullar
- **ONNX Runtime**: Model çıkarımı için ONNX Runtime'ı yükleyin
- **Ollama** (Opsiyonel): Yerel model sunumu için Ollama'yı yükleyin
- **Python Ortamı**: Gerekli yapay zeka kütüphaneleriyle Python'u kurun
- **Edge Donanım Araçları**: CUDA, OpenVINO gibi donanıma özel geliştirme araçlarını yükleyin

### İlk Yapılandırma
1. VS Code'u açın ve AI Toolkit uzantısını yükleyin
2. Model kaynaklarını yapılandırın (ONNX, Ollama, bulut sağlayıcılar)
3. Edge testi için yerel geliştirme ortamını ayarlayın
4. Geliştirme makineniz için donanım hızlandırma seçeneklerini yapılandırın

## Edge AI Geliştirmeye Başlama

### Adım 1: Model Seçimi
1. Etkinlik Çubuğunda AI Toolkit görünümünü açın
2. Edge uyumlu modeller için Model Kataloğunu gözden geçirin
3. Model boyutu, format (ONNX) ve performans özelliklerine göre filtreleme yapın
4. Dahili karşılaştırma araçlarını kullanarak modelleri karşılaştırın

### Adım 2: Yerel Test
1. Playground'u kullanarak seçilen modelleri yerel olarak test edin
2. Farklı istemler ve parametrelerle deney yapın
3. Test sırasında performans metriklerini izleyin
4. Edge kullanım durumu gereksinimleri için model yanıtlarını değerlendirin

### Adım 3: Model Optimizasyonu
1. Model Dönüştürme araçlarını kullanarak edge dağıtımı için optimize edin
2. Model boyutunu azaltmak için kuantizasyon uygulayın
3. Optimize edilmiş modelleri kabul edilebilir performansı sağlamak için test edin
4. Optimizasyon ayarlarını ve performans ödünlerini belgeleyin

### Adım 4: Ajan Geliştirme
1. Agent Builder'ı kullanarak edge'e optimize edilmiş yapay zeka ajanları oluşturun
2. Daha küçük modellerle etkili çalışan istemler geliştirin
3. Edge senaryoları için gerekli araçları ve API'leri entegre edin
4. Ajanları simüle edilmiş edge koşullarında test edin

### Adım 5: Değerlendirme ve Dağıtım
1. Toplu değerlendirme kullanarak birden fazla yapılandırmayı test edin
2. Çeşitli koşullar altında performans profili oluşturun
3. Hedef edge cihazlar için dağıtım paketlerini hazırlayın
4. Üretim dağıtımı için izleme ve günlükleme ayarlarını yapın

## Edge AI Geliştirme için En İyi Uygulamalar

### Model Seçimi
- **Boyut Kısıtlamaları**: H
- **Güvenlik**: Edge AI uygulamaları için uygun güvenlik önlemlerini uygulayın

## Edge AI Çerçeveleri ile Entegrasyon

### ONNX Runtime
- **Platformlar Arası Dağıtım**: ONNX modellerini farklı edge platformlarında dağıtın
- **Donanım Optimizasyonu**: ONNX Runtime'ın donanıma özel optimizasyonlarından yararlanın
- **Mobil Destek**: Akıllı telefon ve tablet uygulamaları için ONNX Runtime Mobile kullanın
- **IoT Entegrasyonu**: ONNX Runtime'ın hafif dağıtımlarıyla IoT cihazlarında dağıtım yapın

### Windows ML
- **Windows Cihazları**: Windows tabanlı edge cihazlar ve PC'ler için optimize edin
- **NPU Hızlandırma**: Windows cihazlarındaki Neural Processing Unit'lerden yararlanın
- **DirectML**: Windows platformlarında GPU hızlandırması için DirectML kullanın
- **UWP Entegrasyonu**: Universal Windows Platform uygulamalarıyla entegre edin

### TensorFlow Lite
- **Mobil Optimizasyon**: TensorFlow Lite modellerini mobil ve gömülü cihazlarda dağıtın
- **Donanım Delegeleri**: Hızlandırma için özel donanım delegeleri kullanın
- **Mikro Kontrolcüler**: TensorFlow Lite Micro ile mikro kontrolcülerde dağıtım yapın
- **Platformlar Arası Destek**: Android, iOS ve gömülü Linux sistemlerinde dağıtım yapın

### Azure IoT Edge
- **Bulut-Edge Hibrit**: Bulut eğitimini edge çıkarımı ile birleştirin
- **Modül Dağıtımı**: AI modellerini IoT Edge modülleri olarak dağıtın
- **Cihaz Yönetimi**: Edge cihazlarını ve model güncellemelerini uzaktan yönetin
- **Telemetri**: Edge dağıtımlarından performans verileri ve model metrikleri toplayın

## İleri Düzey Edge AI Senaryoları

### Çoklu Model Dağıtımı
- **Model Toplulukları**: Daha iyi doğruluk veya yedeklilik için birden fazla model dağıtın
- **A/B Testi**: Edge cihazlarında farklı modelleri aynı anda test edin
- **Dinamik Seçim**: Mevcut cihaz koşullarına göre modeller seçin
- **Kaynak Paylaşımı**: Birden fazla dağıtılmış model arasında kaynak kullanımını optimize edin

### Federated Learning
- **Dağıtılmış Eğitim**: Modelleri birden fazla edge cihazında eğitin
- **Gizlilik Koruma**: Eğitim verilerini yerel tutarken model iyileştirmelerini paylaşın
- **İşbirlikçi Öğrenme**: Cihazların kolektif deneyimlerden öğrenmesini sağlayın
- **Edge-Bulut Koordinasyonu**: Edge cihazları ve bulut altyapısı arasında öğrenmeyi koordine edin

### Gerçek Zamanlı İşleme
- **Akış İşleme**: Edge cihazlarında sürekli veri akışlarını işleyin
- **Düşük Gecikmeli Çıkarım**: Minimum çıkarım gecikmesi için optimize edin
- **Toplu İşleme**: Edge cihazlarında veri gruplarını verimli bir şekilde işleyin
- **Uyarlanabilir İşleme**: Mevcut cihaz yeteneklerine göre işlemi ayarlayın

## Edge AI Geliştirme Sorunlarını Giderme

### Yaygın Sorunlar
- **Bellek Kısıtlamaları**: Model, hedef cihazın belleği için çok büyük
- **Çıkarım Hızı**: Model çıkarımı gerçek zamanlı gereksinimler için çok yavaş
- **Doğruluk Kaybı**: Optimizasyon, model doğruluğunu kabul edilemez şekilde düşürüyor
- **Donanım Uyumluluğu**: Model, hedef donanımla uyumlu değil

### Hata Ayıklama Stratejileri
- **Performans Profili**: AI Toolkit'in izleme özelliklerini kullanarak darboğazları belirleyin
- **Kaynak İzleme**: Geliştirme sırasında bellek ve CPU kullanımını izleyin
- **Kademeli Test**: Sorunları izole etmek için optimizasyonları kademeli olarak test edin
- **Donanım Simülasyonu**: Hedef donanımı simüle etmek için geliştirme araçlarını kullanın

### Optimizasyon Çözümleri
- **Daha Fazla Kuantizasyon**: Daha agresif kuantizasyon teknikleri uygulayın
- **Model Mimarisi**: Edge için optimize edilmiş farklı model mimarilerini düşünün
- **Ön İşleme Optimizasyonu**: Edge kısıtlamaları için veri ön işlemesini optimize edin
- **Çıkarım Optimizasyonu**: Donanıma özel çıkarım optimizasyonlarını kullanın

## Kaynaklar ve Sonraki Adımlar

### Dokümantasyon
- [AI Toolkit Modeller Kılavuzu](https://code.visualstudio.com/docs/intelligentapps/models)
- [Model Playground Dokümantasyonu](https://code.visualstudio.com/docs/intelligentapps/playground)
- [ONNX Runtime Dokümantasyonu](https://onnxruntime.ai/)
- [Windows ML Dokümantasyonu](https://docs.microsoft.com/en-us/windows/ai/)

### Topluluk ve Destek
- [VS Code AI Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit)
- [ONNX Topluluğu](https://github.com/onnx/onnx)
- [Edge AI Geliştirici Topluluğu](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [VS Code Uzantı Pazarı](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Öğrenme Kaynakları
- [Edge AI Temelleri Kursu](./Module01/README.md)
- [Küçük Dil Modelleri Kılavuzu](./Module02/README.md)
- [Edge Dağıtım Stratejileri](./Module03/README.md)
- [Windows Edge AI Geliştirme](./windowdeveloper.md)

## Sonuç

Visual Studio Code için AI Toolkit, model keşfi ve optimizasyonundan dağıtım ve izlemeye kadar Edge AI geliştirme için kapsamlı bir platform sunar. Entegre araçları ve iş akışlarını kullanarak, geliştiriciler kaynak kısıtlı edge cihazlarında etkili bir şekilde çalışan AI uygulamaları oluşturabilir, test edebilir ve dağıtabilir.

ONNX, Ollama ve çeşitli bulut sağlayıcıları için sunduğu destek, optimizasyon ve değerlendirme yetenekleriyle AI Toolkit, Edge AI geliştirme için ideal bir seçimdir. IoT uygulamaları, mobil AI özellikleri veya gömülü zeka sistemleri oluşturuyor olun, AI Toolkit başarılı Edge AI dağıtımı için gereken araçları ve iş akışlarını sağlar.

Edge AI gelişmeye devam ederken, VS Code için AI Toolkit, geliştiricilere bir sonraki nesil zeki edge uygulamalarını oluşturmak için en son araçları ve yetenekleri sunarak ön planda kalmaya devam ediyor.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.