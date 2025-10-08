<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "94b65d49961cabc07f76062d09a5d09c",
  "translation_date": "2025-10-08T19:24:41+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "ja"
}
-->
# セッション6: Foundry Local – モデルをツールとして活用

## 概要

モデルをローカルAIオペレーティングレイヤー内で組み合わせ可能なツールとして扱います。このセッションでは、複数の専門的なSLM/LLM呼び出しを連鎖させ、タスクを選択的にルーティングし、アプリケーションに統一されたSDKインターフェースを提供する方法を紹介します。軽量なモデルルーターとタスクプランナーを構築し、それをアプリスクリプトに統合し、Azure AI Foundryへのスケーリングパスを生産ワークロード向けに概説します。

## 学習目標

- **モデルを概念化**: 宣言された能力を持つ原子的なツールとしてモデルを捉える
- **リクエストをルーティング**: 意図やヒューリスティックスコアに基づいてルーティング
- **マルチステップタスクの出力を連鎖**: 分解 → 解決 → 精査
- **統一されたクライアントAPIを統合**: 下流アプリケーション向け
- **クラウドへのスケール**: OpenAI互換の契約を維持

## 前提条件

- セッション1～5を完了していること
- 複数のローカルモデルがキャッシュされていること (例: `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### クロスプラットフォーム環境スニペット

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOSからのリモート/VMサービスアクセス:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## デモフロー (30分)

### 1. ツール能力の宣言 (5分)

`samples/06-tools/models_catalog.py`を作成:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. 意図検出とルーティング (8分)

`samples/06-tools/router.py`を作成:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. マルチステップタスクの連鎖 (7分)

`samples/06-tools/pipeline.py`を作成:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. スタータープロジェクト: `06-models-as-tools`を適応 (5分)

強化点:
- ストリーミングトークン対応を追加 (進行状況のUI更新)
- 信頼度スコアリングを追加: 語彙の重複やプロンプトルーブリック
- トレースJSONをエクスポート (意図 → モデル → レイテンシ → トークン使用量)
- 繰り返しサブステップのキャッシュ再利用を実装

### 5. Azureへのスケーリングパス (5分)

| レイヤー | ローカル (Foundry) | クラウド (Azure AI Foundry) | 移行戦略 |
|---------|--------------------|----------------------------|----------|
| ルーティング | ヒューリスティックPython | 耐久性のあるマイクロサービス | APIをコンテナ化してデプロイ |
| モデル | SLMキャッシュ | 管理されたデプロイメント | ローカル名をデプロイメントIDにマッピング |
| 可観測性 | CLI統計/手動 | 中央ログとメトリクス | 構造化されたトレースイベントを追加 |
| セキュリティ | ローカルホストのみ | Azure認証/ネットワーキング | シークレット用のキー保管庫を導入 |
| コスト | デバイスリソース | 消費課金 | 予算ガードレールを追加 |

## 検証チェックリスト

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

意図に基づくモデル選択と最終的な精査された出力を期待。

## トラブルシューティング

| 問題 | 原因 | 修正 |
|------|------|------|
| すべてのタスクが同じモデルにルーティングされる | 弱いルール | INTENT_RULESの正規表現セットを強化 |
| パイプラインが途中で失敗する | モデルがロードされていない | `foundry model run <model>`を実行 |
| 出力の一貫性が低い | 精査フェーズがない | 要約/検証パスを追加 |

## 参考資料

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- プロンプト品質パターン: セッション2を参照

---

**セッション時間**: 30分  
**難易度**: エキスパート

## サンプルシナリオとワークショップマッピング

| ワークショップスクリプト / ノートブック | シナリオ | 目的 | データセット / カタログソース |
|------------------------------------------|----------|------|-----------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | 混合意図プロンプトを処理する開発者アシスタント (リファクタリング、要約、分類) | ヒューリスティック意図 → モデルエイリアスルーティングとトークン使用 | インライン`CATALOG` + 正規表現`RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | 複雑なコーディング支援タスクのマルチステップ計画と精査 | 分解 → 専門的な実行 → 要約精査ステップ | 同じ`CATALOG`; ステップは計画出力から派生 |

### シナリオの概要
エンジニアリング生産性ツールが異種タスクを受け取ります: コードのリファクタリング、アーキテクチャノートの要約、フィードバックの分類。レイテンシとリソース使用を最小化するため、小型の一般モデルが計画と要約を担当し、コード専門モデルがリファクタリングを処理し、軽量な分類対応モデルがフィードバックをラベル付けします。パイプラインスクリプトは連鎖と精査を示し、ルータースクリプトは適応的な単一プロンプトルーティングを分離します。

### カタログスナップショット
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### テストプロンプト例
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### トレース拡張 (オプション)
`models_pipeline.py`にステップごとのトレースJSON行を追加:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### エスカレーションヒューリスティック (アイデア)
計画に「最適化」や「セキュリティ」といったキーワードが含まれる場合、またはステップの長さが280文字を超える場合 → そのステップのみ大規模モデル (例: `gpt-oss-20b`) にエスカレーション。

### オプションの強化

| 領域 | 強化内容 | 価値 | ヒント |
|------|----------|------|--------|
| キャッシュ | マネージャーとクライアントオブジェクトの再利用 | レイテンシの低減、オーバーヘッド削減 | `workshop_utils.get_client`を使用 |
| 使用メトリクス | トークンとステップごとのレイテンシをキャプチャ | プロファイリングと最適化 | 各ルーティング呼び出しを計測し、トレースリストに保存 |
| 適応的ルーティング | 信頼度/コストを考慮 | 品質とコストのトレードオフ向上 | スコアリングを追加: プロンプトがN文字以上または正規表現がドメインに一致する場合 → 大規模モデルにエスカレーション |
| 動的能力レジストリ | カタログのホットリロード | 再起動不要の再デプロイ | 実行時に`catalog.json`をロード; ファイルタイムスタンプを監視 |
| フォールバック戦略 | 障害時の堅牢性 | 可用性向上 | プライマリを試行 → 例外時にフォールバックエイリアス |
| ストリーミングパイプライン | 早期フィードバック | UX改善 | 各ステップをストリームし、最終精査入力をバッファリング |
| ベクター意図埋め込み | より微妙なルーティング | 意図精度向上 | プロンプトを埋め込み、クラスタリングし、セントロイドを能力にマッピング |
| トレースエクスポート | 連鎖の監査可能性 | コンプライアンス/報告 | JSON行を出力: ステップ、意図、モデル、レイテンシ_ms、トークン |
| コストシミュレーション | クラウド前の推定 | 予算計画 | モデルごとにトークンあたりの仮想コストを割り当て、タスクごとに集計 |
| 決定論的モード | 再現性の向上 | 安定したベンチマーク | 環境: `temperature=0`, 固定ステップ数 |

#### トレース構造例

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### 適応的エスカレーションスケッチ

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### モデルカタログホットリロード

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```


初期プロトタイプでは過剰なエンジニアリングを避け、段階的に進めましょう。

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は責任を負いません。