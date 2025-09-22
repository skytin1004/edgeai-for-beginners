<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb6eadc312d5658a0cd71c0085b43742",
  "translation_date": "2025-09-22T18:19:48+00:00",
  "source_file": "Module07/README.md",
  "language_code": "tr"
}
-->
# Bölüm 07: EdgeAI Örnekleri

Edge AI, yapay zekanın edge computing ile birleşimini temsil eder ve cihazlarda bulut bağlantısına ihtiyaç duymadan akıllı işlem yapmayı mümkün kılar. Bu bölüm, farklı platformlar ve çerçeveler üzerinde beş farklı EdgeAI uygulamasını inceleyerek, yapay zeka modellerini uçta çalıştırmanın esnekliğini ve gücünü gözler önüne seriyor.

## 1. NVIDIA Jetson Orin Nano ile EdgeAI

NVIDIA Jetson Orin Nano, erişilebilir edge AI hesaplama alanında bir dönüm noktasıdır ve kredi kartı boyutunda kompakt bir form faktöründe 67 TOPS'a kadar yapay zeka performansı sunar. Bu güçlü edge AI platformu, hobi sahipleri, öğrenciler ve profesyonel geliştiriciler için üretken yapay zeka geliştirmeyi demokratikleştirir.

### Temel Özellikler
- 67 TOPS'a kadar yapay zeka performansı sunar—önceki modeline göre 1.7 kat iyileştirme
- Yapay zeka işlemleri için 1024 CUDA çekirdeği ve 32 Tensor Çekirdeği
- Maksimum 1.5 GHz frekansa sahip 6 çekirdekli Arm Cortex-A78AE v8.2 64-bit CPU
- Sadece $249 fiyatıyla geliştiricilere, öğrencilere ve üreticilere en uygun ve erişilebilir platformu sunar

### Uygulamalar
Jetson Orin Nano, modern üretken yapay zeka modellerini çalıştırmada mükemmeldir; bunlar arasında görsel dönüştürücüler, büyük dil modelleri ve görsel-dil modelleri bulunur. GenAI kullanım senaryoları için özel olarak tasarlanmıştır ve artık avuç içi boyutundaki bir cihazda birkaç LLM çalıştırabilirsiniz. Popüler kullanım alanları arasında yapay zeka destekli robotlar, akıllı dronlar, akıllı kameralar ve otonom edge cihazlar yer alır.

**Daha Fazla Bilgi Edinin**: [NVIDIA'nın Jetson Orin Nano Süper Bilgisayarı: EdgeAI'deki Bir Sonraki Büyük Adım](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. .NET MAUI ve ONNX Runtime GenAI ile Mobil Uygulamalarda EdgeAI

Bu çözüm, .NET MAUI (Multi-platform App UI) ve ONNX Runtime GenAI kullanarak üretken yapay zeka ve büyük dil modellerini (LLM'ler) çapraz platform mobil uygulamalara entegre etmenin nasıl mümkün olduğunu gösterir. Bu yaklaşım, .NET geliştiricilerinin Android ve iOS cihazlarında yerel olarak çalışan gelişmiş yapay zeka destekli mobil uygulamalar oluşturmasını sağlar.

### Temel Özellikler
- Hem Android hem de iOS uygulamaları için tek bir kod tabanı sağlayan .NET MAUI çerçevesi üzerine inşa edilmiştir
- ONNX Runtime GenAI entegrasyonu, üretken yapay zeka modellerini doğrudan mobil cihazlarda çalıştırmayı mümkün kılar
- CPU, GPU ve mobil yapay zeka işlemcileri gibi mobil cihazlara özel donanım hızlandırıcılarını destekler
- ONNX Runtime aracılığıyla iOS için CoreML ve Android için NNAPI gibi platforma özgü optimizasyonlar
- Ön ve son işleme, çıkarım, logits işleme, arama ve örnekleme, KV önbellek yönetimi gibi üretken yapay zeka döngüsünün tamamını uygular

### Geliştirme Avantajları
.NET MAUI yaklaşımı, geliştiricilerin mevcut C# ve .NET becerilerini kullanarak çapraz platform yapay zeka uygulamaları oluşturmasına olanak tanır. ONNX Runtime GenAI çerçevesi, Llama, Mistral, Phi, Gemma ve daha birçok model mimarisini destekler. Optimize edilmiş ARM64 çekirdekleri, INT4 kuantize matris çarpımını hızlandırarak mobil donanımda verimli performans sağlar ve tanıdık .NET geliştirme deneyimini korur.

### Kullanım Alanları
Bu çözüm, .NET teknolojilerini kullanarak yapay zeka destekli mobil uygulamalar oluşturmak isteyen geliştiriciler için idealdir. Akıllı sohbet botları, görüntü tanıma uygulamaları, dil çeviri araçları ve tamamen cihaz üzerinde çalışan, gizliliği artırılmış ve çevrimdışı çalışabilen kişiselleştirilmiş öneri sistemleri gibi uygulamalar için uygundur.

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

Windows ML, Microsoft'un cihazda model çıkarımı için optimize edilmiş ve basitleştirilmiş dağıtım sağlayan en son teknolojisidir ve Windows AI Foundry'nin temelini oluşturur. Bu platform, geliştiricilerin PC donanımının tüm spektrumundan yararlanan yapay zeka destekli Windows uygulamaları oluşturmasını sağlar.

### Platform Yetkinlikleri
- Windows 11 çalıştıran tüm PC'lerde (sürüm 24H2, yapı 26100 veya üzeri) çalışır
- NPUs veya GPU'lara sahip olmayan PC'ler dahil tüm x64 ve ARM64 PC donanımlarında çalışır
- Geliştiricilerin kendi modellerini getirip AMD, Intel, NVIDIA ve Qualcomm gibi CPU, GPU, NPU'yu kapsayan silikon ortak ekosistemi genelinde verimli bir şekilde dağıtmasını sağlar
- Altyapı API'lerini kullanarak, geliştiricilerin farklı silikonları hedeflemek için birden fazla uygulama derlemesi oluşturmasına gerek kalmaz

### Geliştirici Avantajları
Windows ML, donanım ve yürütme sağlayıcılarını soyutlar, böylece kodunuzu yazmaya odaklanabilirsiniz. Ayrıca, Windows ML, piyasaya sürüldükçe en son NPUs, GPU'lar ve CPU'ları desteklemek için otomatik olarak güncellenir. Platform, çeşitli Windows donanım ekosistemi genelinde yapay zeka geliştirme için birleşik bir çerçeve sağlar.

**Daha Fazla Bilgi Edinin**: 
- [Windows ML Genel Bakış](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Geliştirme Kılavuzu](../windowdeveloper.md) - Windows Edge AI geliştirme için kapsamlı kılavuz

## 5. Foundry Local Uygulamaları ile EdgeAI

Foundry Local, yerel kaynakları kullanarak .NET'te Retrieval Augmented Generation (RAG) uygulamaları oluşturmayı sağlar ve yerel dil modellerini semantik arama yetenekleriyle birleştirir. Bu yaklaşım, tamamen yerel altyapıda çalışan gizlilik odaklı yapay zeka çözümleri sunar.

### Teknik Mimari
- Phi dil modeli, Yerel Gömüler ve Semantik Kernel'i birleştirerek bir RAG senaryosu oluşturur
- İçeriği ve semantik anlamını temsil eden kayan nokta değerlerinden oluşan diziler (vektörler) olarak gömüler kullanır
- Semantik Kernel, Phi ve Akıllı Bileşenleri entegre ederek sorunsuz bir RAG hattı oluşturur
- SQLite ve Qdrant gibi yerel vektör veritabanlarını destekler

### Uygulama Avantajları
RAG, yani Retrieval Augmented Generation, "bir şeyler arayıp isteme eklemek" anlamına gelir. Bu yerel uygulama, özel bilgi tabanlarına dayalı akıllı yanıtlar sağlarken veri gizliliğini garanti eder. Bu yaklaşım, veri egemenliği ve çevrimdışı çalışma yetenekleri gerektiren kurumsal senaryolar için özellikle değerlidir.

**Daha Fazla Bilgi Edinin**: [Foundry Local RAG Örnekleri](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local, Windows'da modelleri yerel olarak çalıştırmak için ONNX Runtime tarafından desteklenen OpenAI uyumlu bir REST sunucusu sağlar. Aşağıda hızlı bir özet verilmiştir; tam detaylar için resmi belgeleri inceleyin.

- Başlangıç: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Mimari: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI referansı: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Bu depoda tam Windows kılavuzu: [foundrylocal.md](./foundrylocal.md)

Windows'da yükleme veya yükseltme (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

CLI kategorilerini keşfedin:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Bir modeli çalıştırın ve dinamik uç noktayı keşfedin:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Modelleri listelemek için hızlı REST kontrolü (durumdan PORT'u değiştirin):
```cmd
curl -s http://localhost:PORT/v1/models
```

İpuçları:
- SDK entegrasyonu: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Kendi modelinizi getirin (derleme): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI Geliştirme Kaynakları

Özellikle Windows platformunu hedefleyen geliştiriciler için, Windows EdgeAI ekosistemini kapsayan kapsamlı bir kılavuz oluşturduk. Bu kaynak, Windows AI Foundry hakkında detaylı bilgiler, API'ler, araçlar ve Windows'da EdgeAI geliştirme için en iyi uygulamaları sunar.

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

Bu beş EdgeAI uygulaması, günümüzde mevcut olan edge yapay zeka çözümlerinin olgunluğunu ve çeşitliliğini göstermektedir. Jetson Orin Nano gibi donanım hızlandırmalı edge cihazlardan ONNX Runtime GenAI ve Windows ML gibi yazılım çerçevelerine kadar, geliştiriciler yapay zeka destekli uygulamaları uçta dağıtmak için benzeri görülmemiş seçeneklere sahiptir.

Tüm bu platformlar arasında ortak bir nokta, yapay zeka yeteneklerinin demokratikleşmesidir; bu, farklı beceri seviyelerine ve kullanım senaryolarına sahip geliştiriciler için gelişmiş makine öğrenimini erişilebilir hale getirir. Mobil uygulamalar, masaüstü yazılımlar veya gömülü sistemler oluştururken, bu EdgeAI çözümleri, uçta verimli ve gizlilik odaklı çalışan bir sonraki nesil akıllı uygulamalar için temel sağlar.

Her platform benzersiz avantajlar sunar: Jetson Orin Nano donanım hızlandırmalı edge computing için, ONNX Runtime GenAI çapraz platform mobil geliştirme için, Azure EdgeAI kurumsal bulut-edge entegrasyonu için, Windows ML Windows'a özgü uygulamalar için ve Foundry Local gizlilik odaklı RAG uygulamaları için. Birlikte, EdgeAI geliştirme için kapsamlı bir ekosistemi temsil ederler.

---

