<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d1b3c0fecfd713c2df903a0633249dc9",
  "translation_date": "2025-10-08T19:09:06+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "ja"
}
-->
# セッション4: 最新モデルの探求 – LLM、SLM、オンデバイス推論

## 概要

ローカル推論とクラウド推論のシナリオにおける大規模言語モデル（LLM）と小規模言語モデル（SLM）を比較します。ONNX Runtimeの加速、WebGPU実行、ハイブリッドRAG体験を活用したデプロイメントパターンを学びます。ローカルモデルを使用したChainlit RAGデモと、オプションでOpenWebUIの探索を含みます。WebGPU推論スターターを適応させ、PhiとGPT-OSS-20Bの能力およびコスト/性能のトレードオフを評価します。

## 学習目標

- **比較**: SLMとLLMのレイテンシー、メモリ、品質の軸での違い
- **デプロイ**: ONNXRuntimeと（対応している場合）WebGPUを使用したモデル
- **実行**: ブラウザベースの推論（プライバシーを保護するインタラクティブデモ）
- **統合**: Chainlit RAGパイプラインをローカルSLMバックエンドと統合
- **評価**: 軽量な品質とコストのヒューリスティックを使用

## 前提条件

- セッション1～3を完了していること
- `chainlit`がインストールされていること（Module08の`requirements.txt`に既に含まれています）
- WebGPU対応ブラウザ（Windows 11上の最新のEdge / Chrome）
- Foundry Localが稼働していること（`foundry status`）

### クロスプラットフォームの注意点

Windowsが主なターゲット環境です。macOS開発者でネイティブバイナリを待っている場合：
1. Windows 11のVM（Parallels / UTM）またはリモートWindowsワークステーションでFoundry Localを実行してください。
2. サービスを公開（デフォルトポート5273）し、macOSで設定してください：
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. 前のセッションと同じPython仮想環境の手順を使用してください。

Chainlitのインストール（両プラットフォーム）：
```bash
pip install chainlit
```

## デモフロー（30分）

### 1. Phi（SLM）とGPT-OSS-20B（LLM）の比較（6分）

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

追跡項目：応答の深さ、事実の正確性、スタイルの豊かさ、レイテンシー。

### 2. ONNX Runtimeの加速（5分）

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   set BENCH_MODELS=phi-4-mini
#   python Workshop\samples\session03\benchmark_oss_models.py
```

GPUを有効にした後のスループットの変化を観察します。

### 3. ブラウザでのWebGPU推論（6分）

スターター`04-webgpu-inference`を適応（`samples/04-cutting-edge/webgpu_demo.html`を作成）：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

ファイルをブラウザで開き、低レイテンシーのローカルラウンドトリップを観察します。

### 4. Chainlit RAGチャットアプリ（7分）

最小限の`samples/04-cutting-edge/chainlit_app.py`：

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

実行：

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. スタータープロジェクト: `04-webgpu-inference`の適応（6分）

成果物：
- プレースホルダーのフェッチロジックをストリーミングトークンに置き換える（`stream=True`エンドポイントバリアントが有効になったら使用）
- レイテンシーチャート（クライアント側）を追加し、phiとgpt-oss-20bの切り替えを表示
- RAGコンテキストをインラインで埋め込む（参考文書用のテキストエリア）

## 評価ヒューリスティック

| カテゴリ | Phi-4-mini | GPT-OSS-20B | 観察 |
|----------|------------|-------------|-------------|
| レイテンシー（コールド） | 速い | 遅い | SLMは迅速にウォームアップ |
| メモリ | 低い | 高い | デバイスの実現可能性 |
| コンテキストの遵守 | 良好 | 強力 | 大規模モデルはより冗長になる可能性 |
| コスト（ローカル） | 最小限 | 高い（リソース） | エネルギー/時間のトレードオフ |
| 最適な使用ケース | エッジアプリ | 深い推論 | ハイブリッドパイプラインが可能 |

## 環境の検証

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python Workshop\samples\session03\benchmark_oss_models.py
```

## トラブルシューティング

| 症状 | 原因 | 対策 |
|---------|-------|--------|
| Webページのフェッチ失敗 | CORSまたはサービス停止 | エンドポイントを確認するために`curl`を使用；必要に応じてCORSプロキシを有効化 |
| Chainlitが空白 | 環境がアクティブでない | venvをアクティブ化し、依存関係を再インストール |
| 高レイテンシー | モデルがロードされたばかり | 小さなプロンプトシーケンスでウォームアップ |

## 参考文献

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Docs: https://docs.chainlit.io
- RAG評価（Ragas）: https://docs.ragas.io

---

**セッションの所要時間**: 30分  
**難易度**: 上級

## サンプルシナリオとワークショップのマッピング

| ワークショップ成果物 | シナリオ | 目的 | データ / プロンプトソース |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | SLMとLLMを評価するアーキテクチャチームによるエグゼクティブサマリー生成 | レイテンシーとトークン使用量の差を定量化 | 単一の`COMPARE_PROMPT`環境変数 |
| `chainlit_app.py`（RAGデモ） | 内部知識アシスタントプロトタイプ | 短い回答を最小限の語彙検索で基盤化 | ファイル内のインライン`DOCS`リスト |
| `webgpu_demo.html` | 未来的なオンデバイスブラウザ推論プレビュー | 低レイテンシーのローカルラウンドトリップとUXナラティブを表示 | ライブユーザープロンプトのみ |

### シナリオナラティブ
製品組織はエグゼクティブブリーフィング生成を求めています。軽量SLM（phi-4-mini）がサマリーを作成し、大型LLM（gpt-oss-20b）が高優先度のレポートのみを精査します。セッションスクリプトはハイブリッド設計を正当化するために経験的なレイテンシーとトークンメトリクスをキャプチャし、Chainlitデモは小型モデルの回答を事実に基づかせる方法を示します。WebGPUコンセプトページはブラウザ加速が成熟した際の完全クライアントサイド処理のビジョンパスを提供します。

### 最小限のRAGコンテキスト（Chainlit）
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### ハイブリッドドラフト→精査フロー（擬似コード）
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

両方のレイテンシーコンポーネントを追跡し、平均コストを報告します。

### オプションの強化

| フォーカス | 強化 | 理由 | 実装のヒント |
|-------|------------|-----|---------------------|
| 比較メトリクス | トークン使用量と最初のトークンレイテンシーを追跡 | 全体的な性能ビュー | 強化されたベンチマークスクリプト（セッション3）を使用し、`BENCH_STREAM=1`を設定 |
| ハイブリッドパイプライン | SLMドラフト → LLM精査 | レイテンシーとコストを削減 | phi-4-miniで生成し、gpt-oss-20bでサマリーを精査 |
| ストリーミングUI | Chainlitでのより良いUX | インクリメンタルフィードバック | ローカルストリーミングが公開されたら`stream=True`を使用；チャンクを蓄積 |
| WebGPUキャッシュ | JS初期化を高速化 | 再コンパイルオーバーヘッドを削減 | コンパイル済みシェーダーアーティファクトをキャッシュ（将来のランタイム機能） |
| 決定論的QAセット | 公平なモデル比較 | 変動を排除 | 固定プロンプトリスト + 評価実行時の`temperature=0` |
| 出力スコアリング | 構造化された品質レンズ | 単なる逸話を超える | 簡単なルーブリック：一貫性 / 事実性 / 簡潔さ（1–5） |
| エネルギー / リソースノート | 教室での議論 | トレードオフを示す | OSモニター（`foundry system info`、タスクマネージャー、`nvidia-smi`） + ベンチマークスクリプトの出力を使用 |
| コストエミュレーション | クラウドの正当化前 | スケーリング計画 | トークンを仮想クラウド価格にマッピングしてTCOナラティブを作成 |
| レイテンシー分解 | ボトルネックを特定 | 最適化を目指す | プロンプト準備、リクエスト送信、最初のトークン、完全な完了を測定 |
| RAG + LLMフォールバック | 品質の安全ネット | 難しいクエリを改善 | SLMの回答長が閾値未満または信頼性が低い場合 → エスカレーション |

#### ハイブリッドドラフト/精査パターンの例

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### レイテンシー分解スケッチ

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

モデル間で公平な比較を行うため、一貫した測定スキャフォルディングを使用してください。

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な表現が含まれる可能性があります。原文（元の言語で記載された文書）が公式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いかねます。