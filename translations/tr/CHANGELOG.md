<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T21:30:27+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "tr"
}
-->
# Değişiklik Günlüğü

EdgeAI for Beginners için yapılan tüm önemli değişiklikler burada belgelenmiştir. Bu proje, tarih bazlı girişler ve Keep a Changelog stilini (Eklendi, Değiştirildi, Düzeltildi, Kaldırıldı, Belgeler, Taşındı) kullanır.

## 2025-09-23

### Değiştirildi - Modül 08 Büyük Modernizasyon
- **Microsoft Foundry-Local depo desenleriyle kapsamlı uyum**
  - Tüm kod örnekleri modern `FoundryLocalManager` ve OpenAI SDK entegrasyonunu kullanacak şekilde güncellendi
  - Eski manuel `requests` çağrıları uygun SDK kullanımıyla değiştirildi
  - Uygulama desenleri resmi Microsoft belgeleri ve örnekleriyle uyumlu hale getirildi

- **05.AIPoweredAgents.md modernizasyonu**:
  - Çoklu ajan orkestrasyonu modern SDK desenlerini kullanacak şekilde güncellendi
  - Koordinatör uygulaması gelişmiş özelliklerle (geri bildirim döngüleri, performans izleme) geliştirildi
  - Kapsamlı hata yönetimi ve hizmet sağlık kontrolü eklendi
  - Yerel örneklere uygun referanslar entegre edildi (`samples/05/multi_agent_orchestration.ipynb`)
  - Fonksiyon çağrı örnekleri, eski `functions` yerine modern `tools` parametresini kullanacak şekilde güncellendi
  - İzleme ve istatistik takibi ile üretime hazır desenler eklendi

- **06.ModelsAsTools.md tamamen yeniden yazıldı**:
  - Temel araç kaydı, akıllı model yönlendirici uygulamasıyla değiştirildi
  - Farklı görev türleri için (genel, akıl yürütme, kod, yaratıcı) anahtar kelime tabanlı model seçimi eklendi
  - Esnek model ataması ile çevre tabanlı yapılandırma entegre edildi
  - Kapsamlı hizmet sağlık izleme ve hata yönetimi ile geliştirildi
  - İstek izleme ve performans takibi ile üretim dağıtım desenleri eklendi
  - Yerel uygulama ile uyumlu hale getirildi (`samples/06/router.py` ve `samples/06/model_router.ipynb`)

- **Belge yapısı iyileştirmeleri**:
  - Modernizasyon ve SDK uyumunu vurgulayan genel bakış bölümleri eklendi
  - Daha iyi okunabilirlik için emojiler ve daha iyi formatlama ile geliştirildi
  - Belgeler boyunca yerel örnek dosyalara uygun referanslar eklendi
  - Üretime hazır uygulama rehberliği ve en iyi uygulamalar dahil edildi

### Eklendi
- Modül 08 dosyalarına modern SDK entegrasyonunu vurgulayan kapsamlı genel bakış bölümleri
- Gelişmiş özellikleri (çoklu ajan sistemleri, akıllı yönlendirme) gösteren mimari öne çıkanlar
- Uygulamalı deneyim için yerel örnek uygulamalara doğrudan referanslar
- İzleme ve hata yönetimi desenleri ile üretim dağıtım rehberliği
- Gelişmiş özellikler ve karşılaştırmalar içeren etkileşimli Jupyter notebook örnekleri

### Düzeltildi
- Belgeler ile gerçek örnek uygulamalar arasındaki uyum sorunları
- Modül 08 boyunca eski SDK kullanım desenleri
- Kapsamlı yerel örnek kütüphanesine eksik referanslar
- Farklı bölümler arasında tutarsız uygulama yaklaşımları

---

## 2025-09-18

### Eklendi
- Modül 08: Microsoft Foundry Local – Tam Geliştirici Araç Seti
  - Altı oturum: kurulum, Azure AI Foundry entegrasyonu, açık kaynak modeller, son teknoloji demolar, ajanlar ve araç olarak modeller
  - `Module08/samples/01`–`06` altında çalıştırılabilir örnekler ve Windows cmd talimatları
    - `01` REST hızlı sohbet (`chat_quickstart.py`)
    - `02` SDK hızlı başlangıç OpenAI/Foundry Local ve Azure OpenAI desteği ile (`sdk_quickstart.py`)
    - `03` CLI listeleme ve karşılaştırma (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Çoklu ajan orkestrasyonu (`python -m samples.05.agents.coordinator`)
    - `06` Araç olarak modeller yönlendirici (`router.py`)
- Oturum 2 SDK örneğinde ortam değişkeni yapılandırması ile Azure OpenAI desteği
- `.vscode/settings.json` dosyası `Module08/.venv`'e işaret ederek Python analiz çözümlemesini iyileştirir
- `.env` dosyası VS Code/Pylance farkındalığı için `PYTHONPATH` ipucu içerir

### Değiştirildi
- Varsayılan model Modül 08 belgeleri ve örneklerinde `phi-4-mini` olarak güncellendi; Modül 08 içindeki kalan `phi-3.5` referansları kaldırıldı
- Yönlendirici (`Module08/samples/06/router.py`) iyileştirmeleri:
  - Regex analizi ile `foundry service status` üzerinden uç nokta keşfi
  - Başlangıçta `/v1/models` sağlık kontrolü
  - Ortam yapılandırılabilir model kaydı (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Gereksinimler güncellendi: `Module08/requirements.txt` artık `openai` içeriyor (`requests`, `chainlit` ile birlikte)
- Chainlit örnek rehberliği netleştirildi ve sorun giderme eklendi; çalışma alanı ayarları üzerinden ithalat çözümü

### Düzeltildi
- İthalat sorunları çözüldü:
  - Yönlendirici artık var olmayan `utils` modülüne bağlı değil; fonksiyonlar iç içe yerleştirildi
  - Koordinatör, göreceli ithalat kullanıyor (`from .specialists import ...`) ve modül yolu üzerinden çağrılıyor
  - VS Code/Pylance yapılandırması `chainlit` ve paket ithalatlarını çözmek için güncellendi
- `STUDY_GUIDE.md` dosyasındaki küçük bir yazım hatası düzeltildi ve Modül 08 kapsamı eklendi

### Kaldırıldı
- Kullanılmayan `Module08/infra/obs.py` silindi ve boş `infra/` dizini kaldırıldı; gözlemlenebilirlik desenleri belgelerde isteğe bağlı olarak korundu

### Taşındı
- Modül 08 demoları `Module08/samples` altında oturum numaralı klasörlerde birleştirildi
  - Chainlit uygulaması `samples/04`'e taşındı
  - Ajanlar `samples/05`'e taşındı ve paket çözümü için `__init__.py` dosyaları eklendi

### Belgeler
- Modül 08 oturum belgeleri ve tüm örnek README'leri Microsoft Learn ve güvenilir satıcı referansları ile zenginleştirildi
- `Module08/README.md` örnekler genel bakışı, yönlendirici yapılandırması ve doğrulama ipuçları ile güncellendi
- `Module07/README.md` Windows Foundry Local bölümü Learn belgelerine karşı doğrulandı
- `STUDY_GUIDE.md` güncellendi:
  - Genel bakış, programlar, ilerleme takipçisi için Modül 08 eklendi
  - Kapsamlı Referanslar bölümü eklendi (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Tarihsel (özet)
- Kurs mimarisi ve modüller oluşturuldu (Modüller 01–07)
- İçerik modernizasyonu, formatlama standardizasyonu ve ek vaka çalışmaları ile yinelemeli geliştirme
- Optimizasyon çerçeveleri kapsamı genişletildi (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Yayınlanmamış / Bekleyen (öneriler)
- Foundry Local kullanılabilirliğini doğrulamak için isteğe bağlı örnek başlatma testleri
- Model referanslarını (ör. `phi-4-mini`) hizalamak için çevirileri gözden geçirme
- Takımlar çalışma alanı genelinde katılık tercih ederse minimal pyright yapılandırması ekleme

---

