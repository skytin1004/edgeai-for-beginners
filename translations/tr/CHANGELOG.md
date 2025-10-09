<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T10:29:20+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "tr"
}
-->
# Değişiklik Günlüğü

EdgeAI for Beginners için yapılan tüm önemli değişiklikler burada belgelenmiştir. Bu proje, tarih bazlı girişler ve Keep a Changelog stilini (Eklendi, Değiştirildi, Düzeltildi, Kaldırıldı, Belgeler, Taşındı) kullanır.

## 2025-10-08

### Eklendi - Atölye Kapsamlı Güncellemesi
- **Atölye README.md tamamen yeniden yazıldı**:
  - Edge AI'nin değer önerisini (gizlilik, performans, maliyet) açıklayan kapsamlı bir giriş eklendi
  - Ayrıntılı yetkinliklerle birlikte 6 temel öğrenme hedefi oluşturuldu
  - Teslimatlar ve yetkinlik matrisi içeren öğrenme çıktıları tablosu eklendi
  - Endüstriyle ilgili kariyer odaklı beceriler bölümü eklendi
  - Ön koşullar ve 3 adımlı kurulum ile hızlı başlangıç kılavuzu eklendi
  - Python örnekleri için kaynak tabloları oluşturuldu (8 dosya ve çalışma süreleriyle)
  - Jupyter defterleri tablosu eklendi (zorluk dereceleriyle birlikte 8 defter)
  - Belge tablosu oluşturuldu (7 ana belge ve "Ne Zaman Kullanılır" rehberiyle)
  - Farklı beceri seviyeleri için öğrenme yolu önerileri eklendi

- **Atölye doğrulama ve test altyapısı**:
  - `scripts/validate_samples.py` oluşturuldu - Söz dizimi, ithalatlar ve en iyi uygulamalar için kapsamlı doğrulama aracı
  - `scripts/test_samples.py` oluşturuldu - Tüm Python örnekleri için duman testi çalıştırıcısı
  - `scripts/README.md` dosyasına doğrulama belgeleri eklendi

- **Kapsamlı belgeler**:
  - `SAMPLES_UPDATE_SUMMARY.md` oluşturuldu - Tüm iyileştirmeleri kapsayan 400+ satırlık ayrıntılı rehber
  - `UPDATE_COMPLETE.md` oluşturuldu - Güncelleme tamamlanmasının yönetici özeti
  - `QUICK_REFERENCE.md` oluşturuldu - Atölye için hızlı başvuru kartı

### Değiştirildi - Atölye Python Örneklerinin Modernizasyonu
- **Tüm 8 Python örneği en iyi uygulamalarla güncellendi**:
  - Tüm I/O işlemleri etrafında try-except bloklarıyla hata yönetimi geliştirildi
  - Tür ipuçları ve kapsamlı docstring'ler eklendi
  - Tutarlı [INFO]/[ERROR]/[RESULT] günlükleme deseni uygulandı
  - Opsiyonel ithalatlar kurulum ipuçlarıyla korundu
  - Tüm örneklerde kullanıcı geri bildirimi iyileştirildi

- **session01/chat_bootstrap.py**:
  - Müşteri başlatma işlemi kapsamlı hata mesajlarıyla geliştirildi
  - Akış hatası yönetimi parça doğrulamasıyla iyileştirildi
  - Hizmet kullanılamazlığı için daha iyi istisna yönetimi eklendi

- **session02/rag_pipeline.py**:
  - Sentence-transformers için ithalat korumaları kurulum ipuçlarıyla eklendi
  - Gömme ve üretim işlemleri için hata yönetimi geliştirildi
  - Yapılandırılmış sonuçlarla çıktı formatlama iyileştirildi

- **session02/rag_eval_ragas.py**:
  - Opsiyonel ithalatlar (ragas, datasets) kullanıcı dostu hata mesajlarıyla korundu
  - Değerlendirme metrikleri için hata yönetimi eklendi
  - Değerlendirme sonuçları için çıktı formatlama geliştirildi

- **session03/benchmark_oss_models.py**:
  - Zarif bozulma uygulandı (model hatalarında devam eder)
  - Ayrıntılı ilerleme raporlama ve model başına hata yönetimi eklendi
  - İstatistik hesaplama kapsamlı hata kurtarma ile geliştirildi

- **session04/model_compare.py**:
  - Tür ipuçları eklendi (Tuple dönüş türleri)
  - Yapılandırılmış JSON sonuçlarıyla çıktı formatlama geliştirildi
  - Model başına hata yönetimi kurtarma ile uygulandı

- **session05/agents_orchestrator.py**:
  - Agent.act() kapsamlı docstring'lerle geliştirildi
  - Aşama bazlı günlükleme ile boru hattı hata yönetimi eklendi
  - Bellek yönetimi ve durum takibi iyileştirildi

- **session06/models_router.py**:
  - Tüm yönlendirme bileşenleri için işlev belgeleri geliştirildi
  - route() işlevinde ayrıntılı günlükleme eklendi
  - Yapılandırılmış sonuçlarla test çıktısı iyileştirildi

- **session06/models_pipeline.py**:
  - chat() yardımcı işlevine hata yönetimi eklendi
  - pipeline() aşama günlükleme ve ilerleme raporlama ile geliştirildi
  - main() kapsamlı hata kurtarma ile iyileştirildi

### Belgeler - Atölye Belgelendirme Geliştirmesi
- Ana README.md, uygulamalı öğrenme yolunu vurgulayan Atölye bölümüyle güncellendi
- STUDY_GUIDE.md, kapsamlı Atölye bölümüyle geliştirildi:
  - Öğrenme hedefleri ve çalışma odak alanları
  - Öz değerlendirme soruları
  - Zaman tahminleriyle uygulamalı alıştırmalar
  - Yoğun ve yarı zamanlı çalışma için zaman tahsisi
  - İlerleme izleme şablonuna Atölye eklendi
- Zaman tahsisi kılavuzu 20 saatten 30 saate güncellendi (Atölye dahil)
- README'ye Atölye örnek açıklamaları ve öğrenme çıktıları eklendi

### Düzeltildi
- Atölye örnekleri arasında tutarsız hata yönetimi desenleri giderildi
- Opsiyonel bağımlılık ithalat hataları uygun korumalarla düzeltildi
- Kritik işlevlerde eksik tür ipuçları düzeltildi
- Hata senaryolarında yetersiz kullanıcı geri bildirimi ele alındı
- Kapsamlı test altyapısıyla doğrulama sorunları düzeltildi

---

## 2025-09-23

### Değiştirildi - Büyük Modül 08 Modernizasyonu
- **Microsoft Foundry-Local depo desenleriyle kapsamlı uyum**:
  - Tüm kod örnekleri modern `FoundryLocalManager` ve OpenAI SDK entegrasyonunu kullanacak şekilde güncellendi
  - Eski manuel `requests` çağrıları uygun SDK kullanımıyla değiştirildi
  - Resmi Microsoft belgeleri ve örnekleriyle uygulama desenleri uyumlu hale getirildi

- **05.AIPoweredAgents.md modernizasyonu**:
  - Çoklu ajan orkestrasyonu modern SDK desenlerini kullanacak şekilde güncellendi
  - Gelişmiş özelliklerle koordinatör uygulaması geliştirildi (geri bildirim döngüleri, performans izleme)
  - Kapsamlı hata yönetimi ve hizmet sağlık kontrolü eklendi
  - Yerel örneklere uygun referanslar entegre edildi (`samples/05/multi_agent_orchestration.ipynb`)
  - Eski `functions` yerine modern `tools` parametresini kullanacak şekilde işlev çağrısı örnekleri güncellendi
  - İzleme ve istatistik takibi ile üretime hazır desenler eklendi

- **06.ModelsAsTools.md tamamen yeniden yazıldı**:
  - Temel araç kaydı, akıllı model yönlendirici uygulamasıyla değiştirildi
  - Farklı görev türleri için anahtar kelime tabanlı model seçimi eklendi (genel, akıl yürütme, kod, yaratıcı)
  - Esnek model atamasıyla çevre tabanlı yapılandırma entegre edildi
  - Kapsamlı hizmet sağlık izleme ve hata yönetimiyle geliştirildi
  - İstek izleme ve performans takibiyle üretim dağıtım desenleri eklendi
  - Yerel uygulama ile uyumlu hale getirildi (`samples/06/router.py` ve `samples/06/model_router.ipynb`)

- **Belgelendirme yapısı iyileştirmeleri**:
  - Modernizasyon ve SDK uyumunu vurgulayan genel bakış bölümleri eklendi
  - Daha iyi okunabilirlik için emojiler ve daha iyi formatlama ile geliştirildi
  - Belgeler boyunca yerel örnek dosyalara uygun referanslar eklendi
  - Üretime hazır uygulama rehberi ve en iyi uygulamalar dahil edildi

### Eklendi
- Modern SDK entegrasyonunu vurgulayan Modül 08 dosyalarında kapsamlı genel bakış bölümleri
- Gelişmiş özellikleri sergileyen mimari öne çıkanlar (çoklu ajan sistemleri, akıllı yönlendirme)
- Uygulamalı deneyim için yerel örnek uygulamalara doğrudan referanslar
- İzleme ve hata yönetimi desenleriyle üretim dağıtım rehberi
- Gelişmiş özellikler ve karşılaştırmalar içeren etkileşimli Jupyter defter örnekleri

### Düzeltildi
- Belgeler ve gerçek örnek uygulamalar arasındaki uyum sorunları
- Modül 08 boyunca eski SDK kullanım desenleri
- Kapsamlı yerel örnek kitaplığına eksik referanslar
- Farklı bölümler arasında tutarsız uygulama yaklaşımları

---

## 2025-09-18

### Eklendi
- Modül 08: Microsoft Foundry Local – Tam Geliştirici Araç Seti
  - Altı oturum: kurulum, Azure AI Foundry entegrasyonu, açık kaynak modeller, ileri düzey demolar, ajanlar ve araç olarak modeller
  - `Module08/samples/01`–`06` altında çalıştırılabilir örnekler ve Windows cmd talimatları
    - `01` REST hızlı sohbet (`chat_quickstart.py`)
    - `02` SDK hızlı başlangıç OpenAI/Foundry Local ve Azure OpenAI desteğiyle (`sdk_quickstart.py`)
    - `03` CLI listeleme ve kıyaslama (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Çoklu ajan orkestrasyonu (`python -m samples.05.agents.coordinator`)
    - `06` Araç olarak Modeller yönlendirici (`router.py`)
- Oturum 2 SDK örneğinde ortam değişkeni yapılandırmasıyla Azure OpenAI desteği
- `.vscode/settings.json`, `Module08/.venv`'e işaret edecek şekilde Python analiz çözümlemesini iyileştirdi
- `.env`, VS Code/Pylance farkındalığı için `PYTHONPATH` ipucu içeriyor

### Değiştirildi
- Varsayılan model Modül 08 belgeleri ve örneklerinde `phi-4-mini` olarak güncellendi; Modül 08'de kalan `phi-3.5` referansları kaldırıldı
- Yönlendirici (`Module08/samples/06/router.py`) iyileştirmeleri:
  - Regex ayrıştırma ile `foundry service status` üzerinden uç nokta keşfi
  - Başlangıçta `/v1/models` sağlık kontrolü
  - Ortam yapılandırılabilir model kaydı (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Gereksinimler güncellendi: `Module08/requirements.txt` artık `openai` içeriyor (`requests`, `chainlit` ile birlikte)
- Chainlit örnek rehberi netleştirildi ve sorun giderme eklendi; çalışma alanı ayarlarıyla ithalat çözümü

### Düzeltildi
- İthalat sorunları çözüldü:
  - Yönlendirici artık var olmayan bir `utils` modülüne bağlı değil; işlevler satır içi hale getirildi
  - Koordinatör, göreceli ithalat kullanıyor (`from .specialists import ...`) ve modül yolu üzerinden çağrılıyor
  - VS Code/Pylance yapılandırması `chainlit` ve paket ithalatlarını çözmek için güncellendi
- `STUDY_GUIDE.md`'deki küçük bir yazım hatası düzeltildi ve Modül 08 kapsamı eklendi

### Kaldırıldı
- Kullanılmayan `Module08/infra/obs.py` silindi ve boş `infra/` dizini kaldırıldı; gözlemlenebilirlik desenleri belgelerde isteğe bağlı olarak korundu

### Taşındı
- Modül 08 demoları `Module08/samples` altında oturum numaralı klasörlerde birleştirildi
  - Chainlit uygulaması `samples/04`'e taşındı
  - Ajanlar `samples/05`'e taşındı ve paket çözümü için `__init__.py` dosyaları eklendi

### Belgeler
- Modül 08 oturum belgeleri ve tüm örnek README'leri Microsoft Learn ve güvenilir satıcı referanslarıyla zenginleştirildi
- `Module08/README.md`, Örnekler Genel Bakışı, yönlendirici yapılandırması ve doğrulama ipuçlarıyla güncellendi
- `Module07/README.md`, Windows Foundry Local bölümü Learn belgelerine karşı doğrulandı
- `STUDY_GUIDE.md` güncellendi:
  - Genel bakış, programlar, ilerleme izleyiciye Modül 08 eklendi
  - Kapsamlı Referanslar bölümü eklendi (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Geçmiş (özet)
- Kurs mimarisi ve modülleri oluşturuldu (Modüller 01–07)
- Yinelemeli içerik modernizasyonu, format standardizasyonu ve ek vaka çalışmaları
- Optimizasyon çerçeveleri kapsamı genişletildi (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Yayınlanmamış / Bekleyen (öneriler)
- Foundry Local kullanılabilirliğini doğrulamak için isteğe bağlı örnek başına duman testleri
- Model referanslarını hizalamak için çevirileri gözden geçirme (ör. `phi-4-mini`)
- Takımlar çalışma alanı genelinde katılık tercih ederse minimal pyright yapılandırması ekleme

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmemektedir.