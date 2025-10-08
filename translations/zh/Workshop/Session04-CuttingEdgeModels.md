<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d1b3c0fecfd713c2df903a0633249dc9",
  "translation_date": "2025-10-08T16:15:38+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "zh"
}
-->
# 第四节：探索前沿模型——LLM、SLM与设备端推理

## 摘要

比较大型语言模型（LLM）与小型语言模型（SLM）在本地与云端推理场景中的表现。学习利用 ONNX Runtime 加速、WebGPU 执行以及混合 RAG 体验的部署模式。包括一个使用本地模型的 Chainlit RAG 演示，以及可选的 OpenWebUI 探索。您将调整一个 WebGPU 推理入门项目，并评估 Phi 与 GPT-OSS-20B 的能力及成本/性能权衡。

## 学习目标

- **对比** SLM 与 LLM 在延迟、内存和质量方面的差异
- **部署** 使用 ONNXRuntime 和（支持的情况下）WebGPU 的模型
- **运行** 基于浏览器的推理（隐私保护的交互式演示）
- **集成** 一个使用本地 SLM 后端的 Chainlit RAG 管道
- **评估** 使用轻量化的质量与成本启发式方法

## 前置条件

- 完成第 1–3 节
- 已安装 `chainlit`（已包含在 Module08 的 `requirements.txt` 中）
- 支持 WebGPU 的浏览器（Windows 11 上的最新 Edge / Chrome）
- Foundry Local 正在运行（`foundry status`）

### 跨平台注意事项

Windows 仍是主要目标环境。对于等待原生二进制文件的 macOS 开发者：
1. 在 Windows 11 虚拟机（Parallels / UTM）或远程 Windows 工作站中运行 Foundry Local。
2. 暴露服务（默认端口 5273），并在 macOS 上设置：
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

3. 使用与之前课程相同的 Python 虚拟环境步骤。

Chainlit 安装（两种平台均适用）：
```bash
pip install chainlit
```


## 演示流程（30 分钟）

### 1. 对比 Phi（SLM）与 GPT-OSS-20B（LLM）（6 分钟）

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

跟踪：响应深度、事实准确性、风格丰富性、延迟。

### 2. ONNX Runtime 加速（5 分钟）

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   set BENCH_MODELS=phi-4-mini
#   python Workshop\samples\session03\benchmark_oss_models.py
```

观察启用 GPU 与仅使用 CPU 后的吞吐量变化。

### 3. 浏览器中的 WebGPU 推理（6 分钟）

调整入门项目 `04-webgpu-inference`（创建 `samples/04-cutting-edge/webgpu_demo.html`）：

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

在浏览器中打开文件；观察低延迟的本地往返。

### 4. Chainlit RAG 聊天应用（7 分钟）

最小化的 `samples/04-cutting-edge/chainlit_app.py`：

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

运行：

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```


### 5. 入门项目：调整 `04-webgpu-inference`（6 分钟）

交付内容：
- 替换占位符的 fetch 逻辑为流式令牌（启用 `stream=True` 端点变体后使用）
- 添加延迟图表（客户端）用于 Phi 与 GPT-OSS-20B 切换
- 内嵌 RAG 上下文（参考文档的文本区域）

## 评估启发式方法

| 类别 | Phi-4-mini | GPT-OSS-20B | 观察 |
|------|------------|-------------|------|
| 延迟（冷启动） | 快速 | 较慢 | SLM 启动速度快 |
| 内存 | 低 | 高 | 设备可行性 |
| 上下文遵从性 | 良好 | 强 | 较大的模型可能更详细 |
| 成本（本地） | 极低 | 较高（资源） | 能耗/时间权衡 |
| 最佳使用场景 | 边缘应用 | 深度推理 | 可实现混合管道 |

## 验证环境

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python Workshop\samples\session03\benchmark_oss_models.py
```


## 故障排除

| 症状 | 原因 | 解决方法 |
|------|------|----------|
| 网页获取失败 | CORS 或服务不可用 | 使用 `curl` 验证端点；如有需要启用 CORS 代理 |
| Chainlit 空白 | 环境未激活 | 激活虚拟环境并重新安装依赖 |
| 高延迟 | 模型刚加载 | 使用小型提示序列预热 |

## 参考资料

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit 文档: https://docs.chainlit.io
- RAG 评估（Ragas）: https://docs.ragas.io

---

**课程时长**: 30 分钟  
**难度**: 高级

## 示例场景与工作坊映射

| 工作坊成果 | 场景 | 目标 | 数据 / 提示来源 |
|------------|------|------|----------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | 架构团队评估 SLM 与 LLM 用于执行摘要生成 | 量化延迟与令牌使用差异 | 单一 `COMPARE_PROMPT` 环境变量 |
| `chainlit_app.py`（RAG 演示） | 内部知识助手原型 | 用最少的词汇检索支持简短回答 | 文件中的内嵌 `DOCS` 列表 |
| `webgpu_demo.html` | 未来设备端浏览器推理预览 | 展示低延迟本地往返与用户体验叙述 | 仅实时用户提示 |

### 场景叙述

产品团队需要一个执行摘要生成器。轻量级 SLM（phi-4-mini）起草摘要；较大的 LLM（gpt-oss-20b）仅用于优化高优先级报告。课程脚本捕获经验性延迟与令牌指标以证明混合设计的合理性，同时 Chainlit 演示展示了如何通过检索支持使小型模型的回答更具事实性。WebGPU 概念页面为浏览器加速成熟时的完全客户端处理提供了愿景路径。

### 最小 RAG 上下文（Chainlit）

```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```


### 混合起草→优化流程（伪代码）

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

跟踪两个延迟组件以报告混合平均成本。

### 可选增强

| 重点 | 增强 | 原因 | 实现提示 |
|------|------|------|---------|
| 比较指标 | 跟踪令牌使用与首令牌延迟 | 全面性能视图 | 使用增强的基准脚本（第三节）并启用 `BENCH_STREAM=1` |
| 混合管道 | SLM 起草 → LLM 优化 | 降低延迟与成本 | 使用 phi-4-mini 生成，使用 gpt-oss-20b 优化摘要 |
| 流式 UI | Chainlit 中更好的用户体验 | 增量反馈 | 一旦本地流式功能暴露，使用 `stream=True`；累积块 |
| WebGPU 缓存 | 更快的 JS 初始化 | 减少重新编译开销 | 缓存已编译的着色器工件（未来运行时功能） |
| 确定性 QA 集 | 公平的模型比较 | 消除变量 | 固定提示列表并在评估运行中使用 `temperature=0` |
| 输出评分 | 结构化质量视角 | 超越轶事 | 简单评分标准：连贯性 / 事实性 / 简洁性（1–5） |
| 能耗 / 资源说明 | 课堂讨论 | 展示权衡 | 使用操作系统监视器（`foundry system info`、任务管理器、`nvidia-smi`）和基准脚本输出 |
| 成本模拟 | 云端前的论证 | 规划扩展 | 将令牌映射到假设的云定价以构建 TCO 叙述 |
| 延迟分解 | 识别瓶颈 | 定位优化 | 测量提示准备、请求发送、首令牌、完整完成 |
| RAG + LLM 回退 | 质量安全网 | 改善复杂查询 | 如果 SLM 回答长度低于阈值或信心较低 → 升级处理 |

#### 示例混合起草/优化模式

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```


#### 延迟分解示意图

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

在模型间使用一致的测量框架以确保公平比较。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文档的原始语言版本为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用本翻译而引起的任何误解或误读不承担责任。