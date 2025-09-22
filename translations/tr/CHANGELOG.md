<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T18:22:46+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "tr"
}
-->
# Değişiklik Günlüğü

EdgeAI for Beginners için yapılan tüm önemli değişiklikler burada belgelenmiştir. Bu proje, tarih bazlı girişler ve Keep a Changelog stilini (Eklendi, Değiştirildi, Düzeltildi, Kaldırıldı, Belgeler, Taşındı) kullanır.

## 2025-09-18

### Eklendi
- Modül 08: Microsoft Foundry Local – Tam Geliştirici Araç Seti
  - Altı oturum: kurulum, Azure AI Foundry entegrasyonu, açık kaynak modeller, en son demolar, ajanlar ve araç olarak modeller
  - `Module08/samples/01`–`06` altında çalıştırılabilir örnekler, Windows cmd talimatlarıyla
    - `01` REST hızlı sohbet (`chat_quickstart.py`)
    - `02` SDK hızlı başlangıç OpenAI/Foundry Local ve Azure OpenAI desteği ile (`sdk_quickstart.py`)
    - `03` CLI listeleme ve kıyaslama (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Çoklu ajan orkestrasyonu (`python -m samples.05.agents.coordinator`)
    - `06` Araç olarak modeller yönlendirici (`router.py`)
- Oturum 2 SDK örneğinde Azure OpenAI desteği, ortam değişkeni yapılandırması ile
- `.vscode/settings.json`, `Module08/.venv`'e işaret ederek Python analiz çözümlemesini iyileştirmek için
- `.env` dosyası, VS Code/Pylance farkındalığı için `PYTHONPATH` ipucu içeriyor

### Değiştirildi
- Varsayılan model, Modül 08 belgeleri ve örneklerinde `phi-4-mini` olarak güncellendi; Modül 08 içindeki kalan `phi-3.5` referansları kaldırıldı
- Yönlendirici (`Module08/samples/06/router.py`) iyileştirmeleri:
  - Regex analizi ile `foundry service status` üzerinden uç nokta keşfi
  - Başlangıçta `/v1/models` sağlık kontrolü
  - Ortam yapılandırılabilir model kaydı (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Gereksinimler güncellendi: `Module08/requirements.txt` artık `openai` içeriyor (`requests`, `chainlit` ile birlikte)
- Chainlit örnek rehberi netleştirildi ve sorun giderme eklendi; çalışma alanı ayarları üzerinden import çözümü

### Düzeltildi
- Import sorunları çözüldü:
  - Yönlendirici artık var olmayan bir `utils` modülüne bağlı değil; fonksiyonlar iç içe yerleştirildi
  - Koordinatör, göreceli import kullanıyor (`from .specialists import ...`) ve modül yolu üzerinden çağrılıyor
  - VS Code/Pylance yapılandırması, `chainlit` ve paket importlarını çözmek için
- `STUDY_GUIDE.md` dosyasındaki küçük bir yazım hatası düzeltildi ve Modül 08 kapsamı eklendi

### Kaldırıldı
- Kullanılmayan `Module08/infra/obs.py` silindi ve boş `infra/` dizini kaldırıldı; gözlemlenebilirlik desenleri belgelerde isteğe bağlı olarak korundu

### Taşındı
- Modül 08 demoları, oturum numaralı klasörlerle `Module08/samples` altında birleştirildi
  - Chainlit uygulaması `samples/04`'e taşındı
  - Ajanlar `samples/05`'e taşındı ve paket çözümü için `__init__.py` dosyaları eklendi

### Belgeler
- Modül 08 oturum belgeleri ve tüm örnek README'leri Microsoft Learn ve güvenilir satıcı referansları ile zenginleştirildi
- `Module08/README.md` örnekler genel bakışı, yönlendirici yapılandırması ve doğrulama ipuçları ile güncellendi
- `Module07/README.md` Windows Foundry Local bölümü Learn belgelerine karşı doğrulandı
- `STUDY_GUIDE.md` güncellendi:
  - Modül 08 genel bakış, programlar, ilerleme takipçisi eklendi
  - Kapsamlı Referanslar bölümü eklendi (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Tarihsel (özet)
- Kurs mimarisi ve modüller oluşturuldu (Modüller 01–07)
- İçerik modernizasyonu, formatlama standardizasyonu ve ek vaka çalışmaları ile iteratif güncellemeler
- Optimizasyon çerçeveleri kapsamı genişletildi (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Yayınlanmamış / Bekleyen (öneriler)
- Foundry Local kullanılabilirliğini doğrulamak için isteğe bağlı örnek başına duman testleri
- Model referanslarını hizalamak için çevirileri gözden geçirme (ör. `phi-4-mini`)
- Takımlar çalışma alanı genelinde sıkılık tercih ederse minimal pyright yapılandırması ekleme

---

