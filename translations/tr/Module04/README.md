<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c0cb9f7bcff2bc170532d8870a891f38",
  "translation_date": "2025-09-17T23:29:58+00:00",
  "source_file": "Module04/README.md",
  "language_code": "tr"
}
-->
# Bölüm 04: Model Format Dönüşümü ve Kuantizasyon - Bölüm Genel Bakış

EdgeAI'nin ortaya çıkışı, kaynakları sınırlı cihazlarda gelişmiş makine öğrenimi yeteneklerini kullanabilmek için model format dönüşümü ve kuantizasyonu önemli teknolojiler haline getirdi. Bu kapsamlı bölüm, edge senaryolarında modelleri anlamak, uygulamak ve optimize etmek için eksiksiz bir rehber sunar.

## 📚 Bölüm Yapısı ve Öğrenme Yolu

Bu bölüm, edge bilişim için model optimizasyonunu anlamak ve uygulamak adına birbirini tamamlayan altı ilerleyici bölümden oluşmaktadır:

---

## [Bölüm 1: Model Format Dönüşümü ve Kuantizasyon Temelleri](./01.Introduce.md)

### 🎯 Genel Bakış
Bu temel bölüm, edge bilişim ortamlarında model optimizasyonu için teorik çerçeveyi oluşturur. 1-bit ile 8-bit hassasiyet seviyeleri arasındaki kuantizasyon sınırlarını ve önemli format dönüşüm stratejilerini kapsar.

**Ana Konular:**
- Hassasiyet sınıflandırma çerçevesi (ultra düşük, düşük, orta hassasiyet)
- GGUF ve ONNX formatlarının avantajları ve kullanım alanları
- Operasyonel verimlilik ve dağıtım esnekliği için kuantizasyonun faydaları
- Performans karşılaştırmaları ve bellek kullanım analizleri

**Öğrenme Çıktıları:**
- Kuantizasyon sınırlarını ve sınıflandırmalarını anlamak
- Uygun format dönüşüm tekniklerini belirlemek
- Edge dağıtımı için ileri düzey optimizasyon stratejilerini öğrenmek

---

## [Bölüm 2: Llama.cpp Uygulama Rehberi](./02.Llamacpp.md)

### 🎯 Genel Bakış
Llama.cpp'nin uygulanması için kapsamlı bir rehber. Bu güçlü C++ çerçevesi, çeşitli donanım yapılandırmalarında minimum kurulumla verimli Büyük Dil Modeli çıkarımı sağlar.

**Ana Konular:**
- Windows, macOS ve Linux platformlarında kurulum
- GGUF format dönüşümü ve çeşitli kuantizasyon seviyeleri (Q2_K'den Q8_0'a)
- CUDA, Metal, OpenCL ve Vulkan ile donanım hızlandırma
- Python entegrasyonu ve üretim dağıtım stratejileri

**Öğrenme Çıktıları:**
- Platformlar arası kurulum ve kaynak koddan derlemeyi öğrenmek
- Model kuantizasyonu ve optimizasyon tekniklerini uygulamak
- REST API entegrasyonu ile sunucu modunda modelleri dağıtmak

---

## [Bölüm 3: Microsoft Olive Optimizasyon Paketi](./03.MicrosoftOlive.md)

### 🎯 Genel Bakış
Microsoft Olive'nin keşfi, çeşitli donanım platformlarında kurumsal düzeyde model dağıtımı için tasarlanmış, 40'tan fazla yerleşik optimizasyon bileşenine sahip donanım odaklı bir model optimizasyon araç seti.

**Ana Konular:**
- Dinamik ve statik kuantizasyon ile otomatik optimizasyon özellikleri
- CPU, GPU ve NPU dağıtımı için donanım odaklı zeka
- Popüler model desteği (Llama, Phi, Qwen, Gemma) kutudan çıktığı gibi
- Azure ML ile entegrasyon ve üretim iş akışları

**Öğrenme Çıktıları:**
- Çeşitli model mimarileri için otomatik optimizasyonu kullanmak
- Platformlar arası dağıtım stratejilerini uygulamak
- Kurumsal düzeyde optimizasyon iş akışları oluşturmak

---

## [Bölüm 4: OpenVINO Araç Seti Optimizasyon Paketi](./04.openvino.md)

### 🎯 Genel Bakış
Intel'in OpenVINO araç setinin kapsamlı bir incelemesi. Bu açık kaynaklı platform, bulut, şirket içi ve edge ortamlarında gelişmiş Sinir Ağı Sıkıştırma Çerçevesi (NNCF) yetenekleriyle performanslı AI çözümleri sunar.

**Ana Konular:**
- Donanım hızlandırma ile platformlar arası dağıtım (CPU, GPU, VPU, AI hızlandırıcılar)
- Gelişmiş kuantizasyon ve budama için Sinir Ağı Sıkıştırma Çerçevesi (NNCF)
- Büyük dil modeli optimizasyonu ve dağıtımı için OpenVINO GenAI
- Kurumsal düzeyde model sunucu yetenekleri ve ölçeklenebilir dağıtım stratejileri

**Öğrenme Çıktıları:**
- OpenVINO model dönüşüm ve optimizasyon iş akışlarını öğrenmek
- NNCF ile gelişmiş kuantizasyon tekniklerini uygulamak
- Çeşitli donanım platformlarında optimize edilmiş modelleri Model Sunucu ile dağıtmak

---

## [Bölüm 5: Apple MLX Çerçevesi Derinlemesine İnceleme](./05.AppleMLX.md)

### 🎯 Genel Bakış
Apple MLX'in kapsamlı bir incelemesi. Bu devrim niteliğindeki çerçeve, Apple Silicon üzerinde verimli makine öğrenimi için özel olarak tasarlanmıştır ve Büyük Dil Modeli yetenekleri ile yerel dağıtıma odaklanır.

**Ana Konular:**
- Birleşik bellek mimarisi avantajları ve Metal Performans Shader'ları
- LLaMA, Mistral, Phi-3, Qwen ve Code Llama modelleri için destek
- Verimli model özelleştirme için LoRA ince ayarı
- Hugging Face entegrasyonu ve kuantizasyon desteği (4-bit ve 8-bit)

**Öğrenme Çıktıları:**
- Apple Silicon optimizasyonunu LLM dağıtımı için öğrenmek
- İnce ayar ve model özelleştirme tekniklerini uygulamak
- Gelişmiş gizlilik özellikleriyle kurumsal AI uygulamaları oluşturmak

---

## [Bölüm 6: Edge AI Geliştirme İş Akışı Sentezi](./06.workflow-synthesis.md)

### 🎯 Genel Bakış
Tüm optimizasyon çerçevelerinin birleşik iş akışlarına, karar matrislerine ve çeşitli platformlar ve kullanım senaryoları için üretime hazır en iyi uygulamalara dönüştürülmesinin kapsamlı bir sentezi.

**Ana Konular:**
- Birden fazla optimizasyon çerçevesini entegre eden birleşik iş akışı mimarisi
- Çerçeve seçimi karar ağaçları ve performans ödünleşim analizi
- Üretim hazır olma doğrulaması ve kapsamlı dağıtım stratejileri
- Gelişen donanım ve model mimarileri için geleceğe yönelik stratejiler

**Öğrenme Çıktıları:**
- Gereksinimlere ve kısıtlamalara dayalı sistematik çerçeve seçimini öğrenmek
- Kapsamlı izleme ile üretim düzeyinde Edge AI iş akışları uygulamak
- Gelişen teknolojiler ve gereksinimlerle uyumlu iş akışları tasarlamak

---

## 🎯 Bölüm Öğrenme Çıktıları

Bu kapsamlı bölümü tamamladıktan sonra okuyucular şunları başaracaktır:

### **Teknik Uzmanlık**
- Kuantizasyon sınırlarını ve pratik uygulamalarını derinlemesine anlamak
- Birden fazla optimizasyon çerçevesiyle uygulamalı deneyim
- Edge bilişim ortamları için üretim dağıtım becerileri

### **Stratejik Anlayış**
- Donanım odaklı optimizasyon seçimi yetenekleri
- Performans ödünleşimleri hakkında bilinçli karar verme
- Kurumsal düzeyde dağıtım ve izleme stratejileri

### **Performans Karşılaştırmaları**

| Çerçeve     | Kuantizasyon | Bellek Kullanımı | Hız Artışı       | Kullanım Alanı               |
|-------------|--------------|------------------|------------------|------------------------------|
| Llama.cpp   | Q4_K_M       | ~4GB            | 2-3x            | Platformlar arası dağıtım    |
| Olive       | INT4         | %60-75 azalma   | 2-6x            | Kurumsal iş akışları         |
| OpenVINO    | INT8/INT4    | %50-75 azalma   | 2-5x            | Intel donanım optimizasyonu  |
| MLX         | 4-bit        | ~4GB            | 2-4x            | Apple Silicon optimizasyonu  |

## 🚀 Sonraki Adımlar ve İleri Uygulamalar

Bu bölüm şunlar için eksiksiz bir temel sağlar:
- Belirli alanlar için özel model geliştirme
- Edge AI optimizasyonunda araştırma
- Ticari AI uygulama geliştirme
- Büyük ölçekli kurumsal Edge AI dağıtımları

Bu altı bölümden elde edilen bilgiler, hızla gelişen edge AI model optimizasyonu ve dağıtımı alanında gezinmek için kapsamlı bir araç seti sunar.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.