<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "142e0d1a5b794b8333cfd4895804ced5",
  "translation_date": "2025-09-18T00:10:03+00:00",
  "source_file": "Module07/README.md",
  "language_code": "tr"
}
-->
# Bölüm 07: EdgeAI Örnekleri

Edge AI, yapay zekanın edge computing ile birleşimini temsil eder ve cihazlarda bulut bağlantısına ihtiyaç duymadan akıllı işlem yapmayı mümkün kılar. Bu bölüm, farklı platformlar ve çerçeveler üzerinde beş farklı EdgeAI uygulamasını inceleyerek, yapay zeka modellerini edge'de çalıştırmanın esnekliğini ve gücünü gözler önüne seriyor.

## 1. NVIDIA Jetson Orin Nano ile EdgeAI

NVIDIA Jetson Orin Nano, erişilebilir edge AI hesaplama alanında bir dönüm noktasıdır. Kredi kartı boyutunda kompakt bir form faktöründe 67 TOPS'a kadar yapay zeka performansı sunar. Bu güçlü edge AI platformu, hobi meraklıları, öğrenciler ve profesyonel geliştiriciler için üretken yapay zeka geliştirmeyi demokratikleştirir.

### Temel Özellikler
- 67 TOPS'a kadar yapay zeka performansı sunar—önceki modeline göre 1.7 kat iyileştirme
- Yapay zeka işlemleri için 1024 CUDA çekirdeği ve 32 Tensor Çekirdeği
- Maksimum 1.5 GHz frekansa sahip 6 çekirdekli Arm Cortex-A78AE v8.2 64-bit CPU
- Sadece $249 fiyatıyla geliştiricilere, öğrencilere ve üreticilere en uygun ve erişilebilir platformu sunar

### Uygulamalar
Jetson Orin Nano, modern üretken yapay zeka modellerini çalıştırmada mükemmeldir; bunlar arasında görsel dönüştürücüler, büyük dil modelleri ve görsel-dil modelleri bulunur. Özellikle GenAI kullanım senaryoları için tasarlanmıştır ve artık avuç içi boyutundaki bir cihazda birkaç LLM çalıştırabilirsiniz. Popüler kullanım alanları arasında yapay zeka destekli robotlar, akıllı dronlar, akıllı kameralar ve otonom edge cihazları yer alır.

**Daha Fazla Bilgi Edinin**: [NVIDIA'nın Jetson Orin Nano Süper Bilgisayarı: EdgeAI'deki Bir Sonraki Büyük Adım](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. .NET MAUI ve ONNX Runtime GenAI ile Mobil Uygulamalarda EdgeAI

Bu çözüm, .NET MAUI (Multi-platform App UI) ve ONNX Runtime GenAI kullanarak üretken yapay zekayı ve büyük dil modellerini (LLM'ler) çapraz platform mobil uygulamalara entegre etmenin nasıl mümkün olduğunu gösterir. Bu yaklaşım, .NET geliştiricilerinin Android ve iOS cihazlarında yerel olarak çalışan gelişmiş yapay zeka destekli mobil uygulamalar oluşturmasını sağlar.

### Temel Özellikler
- Hem Android hem de iOS uygulamaları için tek bir kod tabanı sağlayan .NET MAUI çerçevesi üzerine inşa edilmiştir
- ONNX Runtime GenAI entegrasyonu, üretken yapay zeka modellerini doğrudan mobil cihazlarda çalıştırmayı mümkün kılar
- CPU, GPU ve özel mobil yapay zeka işlemcileri dahil olmak üzere mobil cihazlara özel donanım hızlandırıcılarını destekler
- ONNX Runtime aracılığıyla iOS için CoreML ve Android için NNAPI gibi platforma özgü optimizasyonlar
- Ön ve son işleme, çıkarım, logits işleme, arama ve örnekleme, KV önbellek yönetimi dahil olmak üzere tam üretken yapay zeka döngüsünü uygular

### Geliştirme Avantajları
.NET MAUI yaklaşımı, geliştiricilerin mevcut C# ve .NET becerilerini kullanarak çapraz platform yapay zeka uygulamaları oluşturmasına olanak tanır. ONNX Runtime GenAI çerçevesi, Llama, Mistral, Phi, Gemma ve diğer birçok model mimarisini destekler. Optimize edilmiş ARM64 çekirdekleri, INT4 kuantize matris çarpımını hızlandırarak mobil donanımda verimli performans sağlar ve tanıdık .NET geliştirme deneyimini korur.

### Kullanım Alanları
Bu çözüm, .NET teknolojilerini kullanarak yapay zeka destekli mobil uygulamalar oluşturmak isteyen geliştiriciler için idealdir. Akıllı sohbet botları, görüntü tanıma uygulamaları, dil çeviri araçları ve tamamen cihaz üzerinde çalışan, gizliliği artırılmış ve çevrimdışı çalışabilen kişiselleştirilmiş öneri sistemleri gibi uygulamalar bu kapsamda yer alır.

**Daha Fazla Bilgi Edinin**: [.NET MAUI ONNX Runtime GenAI Örneği](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. Azure'da Küçük Dil Modelleri Motoru ile EdgeAI

Microsoft'un Azure tabanlı EdgeAI çözümü, Küçük Dil Modellerini (SLM'ler) bulut-edge hibrit ortamlarında verimli bir şekilde dağıtmaya odaklanır. Bu yaklaşım, bulut ölçeğinde yapay zeka hizmetleri ile edge dağıtım gereksinimleri arasındaki boşluğu doldurur.

### Mimari Avantajlar
- Azure AI hizmetleri ile sorunsuz entegrasyon
- ONNX Runtime ile SLM'leri/LLM'leri ve çok modelli modelleri cihazda ve bulutta çalıştırma
- Kurumsal ölçekli dağıtım için optimize edilmiştir
- Sürekli model güncellemeleri ve yönetimi desteği

### Kullanım Alanları
Azure EdgeAI uygulaması, bulut yönetim yetenekleriyle kurumsal düzeyde yapay zeka dağıtımı gerektiren senaryolarda mükemmeldir. Bu senaryolar arasında akıllı belge işleme, gerçek zamanlı analiz ve hem bulut hem de edge computing kaynaklarını kullanan hibrit yapay zeka iş akışları bulunur.

**Daha Fazla Bilgi Edinin**: [Azure EdgeAI SLM Motoru](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. Windows ML ile EdgeAI

Windows ML, Microsoft'un cihazda model çıkarımı için optimize edilmiş ve basitleştirilmiş dağıtım sağlayan en son çalışma zamanı olup, Windows AI Foundry'nin temelini oluşturur. Bu platform, geliştiricilerin PC donanımının tüm spektrumundan yararlanan yapay zeka destekli Windows uygulamaları oluşturmasını sağlar.

### Platform Yetenekleri
- Windows 11'in 24H2 (26100 yapı numarası) veya daha yüksek sürümünü çalıştıran tüm PC'lerde çalışır
- NPUs veya GPU'lara sahip olmayan PC'ler dahil tüm x64 ve ARM64 PC donanımında çalışır
- Geliştiricilerin kendi modellerini getirip AMD, Intel, NVIDIA ve Qualcomm gibi silikon ortak ekosistemi genelinde verimli bir şekilde dağıtmasını sağlar
- Altyapı API'lerini kullanarak, geliştiricilerin farklı silikonları hedeflemek için birden fazla uygulama derlemesi oluşturmasına gerek kalmaz

### Geliştirici Avantajları
Windows ML, donanım ve yürütme sağlayıcılarını soyutlayarak kod yazmaya odaklanmanızı sağlar. Ayrıca, Windows ML, piyasaya sürülen en son NPUs, GPUs ve CPUs'u desteklemek için otomatik olarak güncellenir. Platform, çeşitli Windows donanım ekosistemi genelinde yapay zeka geliştirme için birleşik bir çerçeve sunar.

**Daha Fazla Bilgi Edinin**: 
- [Windows ML Genel Bakış](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Geliştirme Kılavuzu](../windowdeveloper.md) - Windows Edge AI geliştirme için kapsamlı kılavuz

## 5. Foundry Local Uygulamaları ile EdgeAI

Foundry Local, yerel dil modellerini semantik arama yetenekleriyle birleştirerek .NET kullanarak Retrieval Augmented Generation (RAG) uygulamaları oluşturmayı mümkün kılar. Bu yaklaşım, tamamen yerel altyapıda çalışan gizlilik odaklı yapay zeka çözümleri sunar.

### Teknik Mimari
- Phi-3 dil modeli, Yerel Gömüler ve Semantik Kernel'i birleştirerek bir RAG senaryosu oluşturur
- İçeriği ve semantik anlamını temsil eden kayan noktalı değerlerden oluşan diziler (vektörler) olarak gömüler kullanır
- Semantik Kernel, Phi-3 ve Akıllı Bileşenleri entegre ederek sorunsuz bir RAG hattı oluşturur
- SQLite ve Qdrant gibi yerel vektör veritabanlarını destekler

### Uygulama Avantajları
RAG, yani Retrieval Augmented Generation, "bir şeyler arayıp isteme eklemek" anlamına gelir. Bu yerel uygulama, özel bilgi tabanlarına dayalı akıllı yanıtlar sağlarken veri gizliliğini garanti eder. Bu yaklaşım, veri egemenliği ve çevrimdışı çalışma yetenekleri gerektiren kurumsal senaryolar için özellikle değerlidir.

**Daha Fazla Bilgi Edinin**: [Foundry Local RAG Örnekleri](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## Windows EdgeAI Geliştirme Kaynakları

Özellikle Windows platformunu hedefleyen geliştiriciler için, Windows EdgeAI ekosistemini kapsayan kapsamlı bir kılavuz oluşturduk. Bu kaynak, Windows AI Foundry hakkında API'ler, araçlar ve Windows üzerinde EdgeAI geliştirme için en iyi uygulamalar hakkında ayrıntılı bilgi sağlar.

### Windows AI Foundry Platformu
Windows AI Foundry platformu, Windows cihazlarında Edge AI geliştirme için özel olarak tasarlanmış araçlar ve API'lerden oluşan kapsamlı bir paket sunar. Buna NPU hızlandırmalı donanım, Windows ML entegrasyonu ve platforma özgü optimizasyon teknikleri dahildir.

**Kapsamlı Kılavuz**: [Windows EdgeAI Geliştirme Kılavuzu](../windowdeveloper.md)

Bu kılavuz şunları kapsar:
- Windows AI Foundry platformu genel bakışı ve bileşenleri
- NPU donanımında verimli çıkarım için Phi Silica API
- Görüntü işleme ve OCR için Bilgisayar Görüşü API'leri
- Windows ML çalışma zamanı entegrasyonu ve optimizasyonu
- Yerel geliştirme ve test için Foundry Local CLI
- Windows cihazları için donanım optimizasyon stratejileri
- Pratik uygulama örnekleri ve en iyi uygulamalar

### Edge AI Geliştirme için AI Araç Seti
Visual Studio Code kullanan geliştiriciler için AI Toolkit uzantısı, Edge AI uygulamaları oluşturma, test etme ve dağıtma için özel olarak tasarlanmış kapsamlı bir geliştirme ortamı sağlar. Bu araç seti, Edge AI geliştirme iş akışını VS Code içinde kolaylaştırır.

**Geliştirme Kılavuzu**: [Edge AI Geliştirme için AI Araç Seti](../aitoolkit.md)

AI Toolkit kılavuzu şunları kapsar:
- Edge dağıtımı için model keşfi ve seçimi
- Yerel test ve optimizasyon iş akışları
- Edge modelleri için ONNX ve Ollama entegrasyonu
- Model dönüştürme ve kuantizasyon teknikleri
- Edge senaryoları için ajan geliştirme
- Performans değerlendirme ve izleme
- Dağıtım hazırlığı ve en iyi uygulamalar

## Sonuç

Bu beş EdgeAI uygulaması, günümüzde mevcut olan edge yapay zeka çözümlerinin olgunluğunu ve çeşitliliğini göstermektedir. Jetson Orin Nano gibi donanım hızlandırmalı edge cihazlardan ONNX Runtime GenAI ve Windows ML gibi yazılım çerçevelerine kadar, geliştiriciler edge'de akıllı uygulamalar dağıtmak için benzeri görülmemiş seçeneklere sahiptir.

Tüm bu platformlar arasında ortak bir tema, yapay zeka yeteneklerinin demokratikleşmesidir; bu, farklı beceri seviyelerine ve kullanım senaryolarına sahip geliştiriciler için sofistike makine öğrenimini erişilebilir hale getirir. Mobil uygulamalar, masaüstü yazılımlar veya gömülü sistemler oluştururken, bu EdgeAI çözümleri edge'de verimli ve gizlilik odaklı çalışan bir sonraki nesil akıllı uygulamalar için temel sağlar.

Her platform benzersiz avantajlar sunar: Jetson Orin Nano donanım hızlandırmalı edge hesaplama için, ONNX Runtime GenAI çapraz platform mobil geliştirme için, Azure EdgeAI kurumsal bulut-edge entegrasyonu için, Windows ML Windows'a özgü uygulamalar için ve Foundry Local gizlilik odaklı RAG uygulamaları için. Birlikte, EdgeAI geliştirme için kapsamlı bir ekosistem oluştururlar.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.