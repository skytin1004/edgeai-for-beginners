<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-22T12:28:59+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "ja"
}
-->
# Foundry Local の Windows インストールガイド (検証済み)

このガイドでは、Microsoft Foundry Local を Windows にインストール、実行、統合する方法を説明します。すべての手順とコマンドは Microsoft Learn ドキュメントに基づいて検証されています。

- はじめに: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- アーキテクチャ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI リファレンス: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDK の統合: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF モデルのコンパイル (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: ローカル vs クラウド: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Windows へのインストール / アップグレード

- インストール:
```cmd
winget install Microsoft.FoundryLocal
```
- アップグレード:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- バージョン確認:
```cmd
foundry --version
```

## 2) CLI の基本操作 (3つのカテゴリ)

- モデル:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- サービス:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- キャッシュ:
```cmd
foundry cache --help
foundry cache list
```

注意事項:
- サービスは OpenAI 互換の REST API を公開します。エンドポイントのポートは動的に割り当てられるため、`foundry service status` を使用して確認してください。
- SDK を使用すると便利です。対応している場合、SDK はエンドポイントの自動検出を行います。

## 3) ローカルエンドポイントの確認 (動的ポート)

Foundry Local はサービス起動時に動的ポートを割り当てます:
```cmd
foundry service status
```
報告された `http://localhost:<PORT>` を OpenAI 互換のパス (例: `/v1/chat/completions`) として `base_url` に使用してください。

## 4) OpenAI Python SDK を使った簡易テスト

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
参考:
- SDK 統合: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) 独自モデルの利用 (Olive を使ったコンパイル)

カタログにないモデルが必要な場合、Olive を使用して ONNX にコンパイルし、Foundry Local で利用できます。

概要 (詳細な手順はドキュメントを参照してください):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
ドキュメント:
- BYOM コンパイル: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) トラブルシューティング

- サービスの状態とログを確認:
```cmd
foundry service status
foundry service diag
```
- キャッシュのクリアまたは移動:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- 最新のプレビュー版に更新:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) 関連する Windows 開発者向け情報

- Foundry Local や Windows ML を含む、Windows ローカル vs クラウド AI の選択肢:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit と Foundry Local (チャットエンドポイント URL を取得するには `foundry service status` を使用):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

