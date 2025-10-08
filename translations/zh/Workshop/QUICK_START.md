<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20ef6223850f0ab7b6e546a6df0d7d68",
  "translation_date": "2025-10-08T16:14:35+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "zh"
}
-->
# 工作坊快速入门指南

## 前置条件

### 1. 安装 Foundry Local

请按照官方安装指南操作：  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. 安装 Python 依赖

在工作坊目录下运行：

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## 运行工作坊示例

### 会话 01：基础聊天

```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What are the benefits of local AI?"
```

**环境变量：**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### 会话 02：RAG 流程

```bash
cd Workshop/samples/session02
python rag_pipeline.py
```

**环境变量：**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### 会话 02：RAG 评估 (Ragas)

```bash
python rag_eval_ragas.py
```

**注意**：需要通过 `requirements.txt` 安装额外依赖

### 会话 03：性能基准测试

```bash
cd Workshop/samples/session03
python benchmark_oss_models.py
```

**环境变量：**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**输出**：包含延迟、吞吐量和首字节时间的 JSON 数据

### 会话 04：模型对比

```bash
cd Workshop/samples/session04
python model_compare.py
```

**环境变量：**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### 会话 05：多代理编排

```bash
cd Workshop/samples/session05
python agents_orchestrator.py
```

**环境变量：**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### 会话 06：模型路由器

```bash
cd Workshop/samples/session06
python models_router.py
```

**测试路由逻辑**，支持多种意图（代码、摘要、分类）

### 会话 06：流程

```bash
python models_pipeline.py
```

**复杂的多步骤流程**，包括规划、执行和优化

## 脚本

### 导出基准测试报告

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**输出**：Markdown 表格 + JSON 指标

### 检查 Markdown CLI 模式

```bash
python lint_markdown_cli.py --verbose
```

**目的**：检测文档中已弃用的 CLI 模式

## 测试

### 烟雾测试

```bash
cd Workshop
python -m tests.smoke
```

**测试**：关键示例的基本功能

## 故障排除

### 服务未运行

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### 模块导入错误

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### 连接错误

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### 模型未找到

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## 环境变量参考

### 核心配置
| 变量 | 默认值 | 描述 |
|------|--------|------|
| `FOUNDRY_LOCAL_ALIAS` | 视情况而定 | 使用的模型别名 |
| `FOUNDRY_LOCAL_ENDPOINT` | 自动 | 覆盖服务端点 |
| `SHOW_USAGE` | `0` | 显示令牌使用统计 |
| `RETRY_ON_FAIL` | `1` | 启用重试逻辑 |
| `RETRY_BACKOFF` | `1.0` | 初始重试延迟（秒） |

### 会话专用
| 变量 | 默认值 | 描述 |
|------|--------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | 嵌入模型 |
| `RAG_QUESTION` | 见示例 | RAG 测试问题 |
| `BENCH_MODELS` | 视情况而定 | 逗号分隔的模型列表 |
| `BENCH_ROUNDS` | `3` | 基准测试迭代次数 |
| `BENCH_PROMPT` | 见示例 | 基准测试提示 |
| `BENCH_STREAM` | `0` | 测量首字节延迟 |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | 主代理模型 |
| `AGENT_MODEL_EDITOR` | 主代理 | 编辑代理模型 |
| `SLM_ALIAS` | `phi-4-mini` | 小型语言模型 |
| `LLM_ALIAS` | `qwen2.5-7b` | 大型语言模型 |
| `COMPARE_PROMPT` | 见示例 | 对比提示 |

## 推荐模型

### 开发与测试
- **phi-4-mini** - 平衡质量与速度
- **qwen2.5-0.5b** - 分类任务非常快
- **gemma-2-2b** - 质量较好，速度适中

### 生产场景
- **phi-4-mini** - 通用用途
- **deepseek-coder-1.3b** - 代码生成
- **qwen2.5-7b** - 高质量响应

## SDK 文档

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  

## 获取帮助

1. 检查服务状态：`foundry service status`  
2. 查看日志：检查 Foundry Local 服务日志  
3. 查看 SDK 文档：https://github.com/microsoft/Foundry-Local  
4. 查看示例代码：所有示例均附有详细的文档注释  

## 下一步

1. 按顺序完成所有工作坊会话  
2. 尝试使用不同的模型  
3. 根据您的用例修改示例  
4. 查看 `SDK_MIGRATION_NOTES.md` 以了解高级模式  

---

**最后更新**：2025-01-08  
**工作坊版本**：最新  
**SDK**：Foundry Local Python SDK

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。