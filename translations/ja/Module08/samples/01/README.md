<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T12:27:51+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "ja"
}
-->
# セッション1 サンプル: RESTを使った簡易チャット

Pythonの`requests`を使用してFoundry Localに最小限のチャットリクエストを送信します。

## 前提条件
- Foundry Localサービスがモデル（例: `phi-4-mini`）を実行中であること
- `pip install -r ../../requirements.txt` を実行済みであること

## 実行方法 (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## 参考資料
- Foundry Local (学習): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI互換API概要: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

