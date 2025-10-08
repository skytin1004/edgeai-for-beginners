<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T19:07:05+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "ja"
}
-->
# Foundry Local SDKの更新

## 概要

**公式Foundry Local Python SDK**の使用に合わせて、Workshopのノートブックとユーティリティを更新しました。以下のパターンに従っています：
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## 修正されたファイル

### 1. `Workshop/samples/workshop_utils.py`

**変更点:**
- ✅ `foundry-local-sdk`パッケージのインポートエラー処理を追加
- ✅ 公式SDKパターンに基づいたドキュメントを強化
- ✅ Unicode記号（✓, ✗, ⚠）を使用したログを改善
- ✅ 例を含む包括的なdocstringを追加
- ✅ CLIコマンドを参照するエラーメッセージを改善
- ✅ 公式SDKドキュメントに合わせたコメントを更新

**主な改善点:**

#### インポートエラー処理
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### `get_client()`関数の強化
- SDK初期化パターンに関する詳細なドキュメントを追加
- `FoundryLocalManager`がサービスを自動的に開始することを明確化
- ハードウェア最適化されたモデルエイリアス解決について説明
- エンドポイント情報を含むログを改善
- トラブルシューティング手順を提案するエラーメッセージを改善

#### `chat_once()`関数の強化
- 使用例を含む包括的なdocstringを追加
- OpenAI SDKとの互換性を明確化
- ストリーミングサポート（kwargs経由）を文書化
- CLIコマンドの提案を含むエラーメッセージを改善
- モデルの利用可能性チェックに関する注意事項を追加

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**変更点:**
- ✅ SDK参照を含むすべてのMarkdownセルを更新
- ✅ SDKパターンの説明を含むコードコメントを強化
- ✅ セルのドキュメントと説明を改善
- ✅ トラブルシューティングガイダンスを追加
- ✅ モデルカタログを更新（'gpt-oss-20b'を'phi-3.5-mini'に置き換え）
- ✅ 視覚的なインジケーターを使用した出力フォーマットを改善
- ✅ SDKリンクと参照を随所に追加

**セルごとの更新内容:**

#### セル1（タイトル）
- SDKドキュメントリンクを追加
- 公式GitHubリポジトリを参照

#### セル2（シナリオ）
- 番号付きステップで再フォーマット
- 意図ベースのルーティングパターンを明確化
- ローカル実行の利点を強調

#### セル3（依存関係のインストール）
- 各パッケージが提供する内容を説明
- SDKの機能（エイリアス解決、ハードウェア最適化）を文書化

#### セル4（環境設定）
- 関数のdocstringを強化
- SDKパターンを説明するインラインコメントを追加
- モデルカタログ構造を文書化
- 優先順位/能力のマッチングを明確化

#### セル5（カタログチェック）
- 視覚的なチェックマーク（✓）を追加
- 出力をより良いフォーマットに変更

#### セル6（意図検出テスト）
- 出力を表形式に再フォーマット
- 意図と選択されたモデルの両方を表示

#### セル7（ルーティング関数）
- 包括的なSDKパターンの説明を追加
- 初期化フローを文書化
- すべての機能（リトライ、トラッキング、エラー）をリスト化
- SDK参照リンクを追加

#### セル8（バッチデモ）
- 期待される結果の説明を強化
- トラブルシューティングセクションを追加
- デバッグ用CLIコマンドを含む
- 出力表示をより良いフォーマットに変更

### 3. `Workshop/notebooks/session06_README.md`（新規ファイル）

**包括的なドキュメントを作成しました：**

1. **概要**: アーキテクチャ図とコンポーネントの説明
2. **SDK統合**: 公式パターンに従ったコード例
3. **前提条件**: ステップバイステップのセットアップ手順
4. **使用方法**: ノートブックの実行とカスタマイズ方法
5. **モデルエイリアス**: ハードウェア最適化されたバリアントの説明
6. **トラブルシューティング**: よくある問題と解決策
7. **拡張**: 意図、モデル、カスタムロジックの追加方法
8. **パフォーマンスのヒント**: 本番環境でのベストプラクティス
9. **リソース**: 公式ドキュメントとコミュニティへのリンク

## SDKパターンの実装

### 公式パターン（Foundry Localドキュメントより）

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### ワークショップユーティリティでの実装

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**私たちのアプローチの利点:**
- ✅ 公式SDKパターンを正確に遵守
- ✅ 繰り返し初期化を避けるためのキャッシュを追加
- ✅ 本番環境の堅牢性を高めるリトライロジックを追加
- ✅ トークン使用状況のトラッキングをサポート
- ✅ より良いエラーメッセージを提供
- ✅ 公式の例との互換性を維持

## モデルカタログの変更

### 変更前
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### 変更後
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**理由:** 'gpt-oss-20b'（非標準エイリアス）を'phi-3.5-mini'（公式Foundry Localエイリアス）に置き換え。

## 依存関係

### 更新されたrequirements.txt

Workshopのrequirements.txtにはすでに以下が含まれています：
```
foundry-local-sdk
openai>=1.30.0
```

Foundry Local統合に必要なパッケージはこれだけです。

## 更新内容のテスト

### 1. Foundry Localが実行中であることを確認

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. 利用可能なモデルを確認

```bash
foundry model ls
```

以下のモデルが利用可能であるか、または自動ダウンロードされることを確認してください：
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. ノートブックを実行

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

またはVS Codeで開き、すべてのセルを実行してください。

### 4. 期待される動作

**セル1（インストール）:** パッケージが正常にインストールされる  
**セル2（セットアップ）:** エラーなし、インポートが成功  
**セル3（確認）:** モデルリストが✓で表示される  
**セル4（意図テスト）:** 意図検出結果が表示される  
**セル5（ルーター）:** ✓ ルート関数が準備完了と表示される  
**セル6（実行）:** プロンプトがモデルにルーティングされ、結果が表示される  

### 5. 接続エラーのトラブルシューティング

`APIConnectionError: Connection error`が表示された場合：

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## 環境変数

以下の環境変数がサポートされています：

| 変数 | デフォルト | 説明 |
|------|-----------|------|
| `SHOW_USAGE` | `0` | トークン使用状況を表示するには`1`に設定 |
| `RETRY_ON_FAIL` | `1` | リトライロジックを有効化 |
| `RETRY_BACKOFF` | `1.0` | 初期リトライ遅延（秒） |
| `FOUNDRY_LOCAL_ENDPOINT` | 自動 | サービスエンドポイントを上書き |

### 使用例

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## 古いパターンからの移行

既存のコードで直接API呼び出しを使用している場合、以下のように移行できます：

### 変更前（直接API）
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### 変更後（SDK）
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### 移行の利点
- ✅ 自動サービス管理
- ✅ モデルエイリアス解決
- ✅ ハードウェア最適化選択
- ✅ より良いエラー処理
- ✅ OpenAI SDK互換性
- ✅ ストリーミングサポート

## 参考資料

### 公式ドキュメント
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDKソース**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLIリファレンス**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **トラブルシューティング**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### ワークショップリソース
- **セッション06 README**: `Workshop/notebooks/session06_README.md`
- **ワークショップユーティリティ**: `Workshop/samples/workshop_utils.py`
- **サンプルノートブック**: `Workshop/notebooks/session06_models_router.ipynb`

### コミュニティ
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## 次のステップ

1. **変更内容を確認**: 更新されたファイルを読み込む  
2. **ノートブックをテスト**: session06_models_router.ipynbを実行  
3. **SDKを確認**: foundry-local-sdkがインストールされていることを確認  
4. **サービスを確認**: Foundry Localが実行中であることを確認  
5. **ドキュメントを探索**: 新しいsession06_README.mdを読む  

## まとめ

これらの更新により、ワークショップの資料が**公式Foundry Local SDKパターン**に完全に準拠するようになりました。すべてのコード例、ドキュメント、ユーティリティが、Microsoftが推奨するローカルAIモデル展開のベストプラクティスに沿っています。

変更内容は以下を改善します：
- ✅ **正確性**: 公式SDKパターンを使用  
- ✅ **ドキュメント**: 包括的な説明と例  
- ✅ **エラー処理**: より良いメッセージとトラブルシューティングガイダンス  
- ✅ **保守性**: 公式の規約に従う  
- ✅ **ユーザー体験**: より明確な指示とデバッグ支援  

---

**更新日:** 2025年10月8日  
**SDKバージョン:** foundry-local-sdk（最新）  
**ワークショップブランチ:** Reactor

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源とみなしてください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤った解釈について、当方は一切の責任を負いません。