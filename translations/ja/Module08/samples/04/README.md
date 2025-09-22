<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T12:28:25+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "ja"
}
-->
# セッション4 サンプル: Chainlit RAG デモ

Foundry Local を使用して最小限の Chainlit アプリを実行します。

## 前提条件
- Windows 11、Python 3.10以上
- Foundry Local がインストールされ、モデルが利用可能（例: `phi-4-mini`）
- `pip install -r Module08\requirements.txt`

## 実行方法 (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## 検証
```cmd
curl http://localhost:8000/v1/models
```

## トラブルシューティング
- VS Code に「chainlit could not be resolved」と表示される場合:
	- インタープリターを選択: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- 依存関係がインストールされていることを確認: `pip install -r Module08\requirements.txt`

## 参考資料
- Open WebUI の使い方 (Open WebUI を使用したチャットアプリ): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (学習用): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

