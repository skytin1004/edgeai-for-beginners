<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T18:35:05+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "tr"
}
-->
# Oturum 4 Örneği: Chainlit RAG Demo

Minimal Chainlit uygulamasını Foundry Local üzerinde çalıştırın.

## Ön Koşullar
- Windows 11, Python 3.10+
- Foundry Local kurulu ve bir model mevcut (örneğin, `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Çalıştırma (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Doğrulama
```cmd
curl http://localhost:8000/v1/models
```

## Sorun Giderme
- Eğer VS Code "chainlit çözümlenemedi" hatası veriyorsa:
	- Yorumlayıcıyı seçin: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Bağımlılıkların yüklü olduğundan emin olun: `pip install -r Module08\requirements.txt`

## Referanslar
- Open WebUI nasıl yapılır (Open WebUI ile sohbet uygulaması): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Öğren): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

