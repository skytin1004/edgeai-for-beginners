<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T12:28:13+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "ja"
}
-->
# セッション6 サンプル: ツールとしてのモデル

このサンプルでは、ユーザープロンプトに基づいてモデルを選択し、Foundry LocalのOpenAI互換エンドポイントを呼び出す、最小限のルーター＋ツールレジストリを実装しています。

## ファイル
- `router.py`: シンプルなレジストリとヒューリスティックルーティング、エンドポイントの検出＋ヘルスチェック。

## 実行方法 (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## 注意事項
- このルーターは、`general`、`reasoning`、`code`ツールの中から選択するために、簡単なキーワードヒューリスティックを使用し、起動時に`/v1/models`を出力します。
- 環境変数を使用して設定します:
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

## 参考資料
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- 推論SDKとの統合: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

