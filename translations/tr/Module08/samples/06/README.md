<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T18:34:50+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "tr"
}
-->
# Oturum 6 Örneği: Araç Olarak Modeller

Bu örnek, kullanıcı istemine göre bir model seçen ve Foundry Local’ın OpenAI uyumlu uç noktasını çağıran minimal bir yönlendirici + araç kaydı uygular.

## Dosyalar
- `router.py`: basit kayıt ve sezgisel yönlendirme; uç nokta keşfi + sağlık kontrolü.

## Çalıştırma (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Notlar
- Yönlendirici, `general`, `reasoning` ve `code` araçları arasında seçim yapmak için basit anahtar kelime sezgilerini kullanır ve başlangıçta `/v1/models` yazdırır.
- Ortam değişkenleri ile yapılandırın:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-distill-qwen-7b"},"code":{"model":"qwen2.5-7b-instruct"}}
```

## Referanslar
- Foundry Local (Öğren): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Çıkarım SDK'ları ile entegrasyon: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

