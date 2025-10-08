<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-08T16:34:10+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "zh"
}
-->
# 研讨会示例 - Foundry Local SDK 更新摘要

## 概述

`Workshop/samples` 目录中的所有 Python 示例已更新，以遵循 Foundry Local SDK 的最佳实践，并确保整个研讨会的一致性。

**日期**：2025年10月8日  
**范围**：涉及6个研讨会课程中的9个Python文件  
**主要关注点**：错误处理、文档编写、SDK模式、用户体验

---

## 更新文件

### 第01课：入门
- ✅ `chat_bootstrap.py` - 基础聊天和流式处理示例

### 第02课：RAG 解决方案
- ✅ `rag_pipeline.py` - 使用嵌入的 RAG 实现
- ✅ `rag_eval_ragas.py` - 使用 RAGAS 指标进行 RAG 评估

### 第03课：开源模型
- ✅ `benchmark_oss_models.py` - 多模型基准测试

### 第04课：前沿模型
- ✅ `model_compare.py` - SLM 与 LLM 的比较

### 第05课：AI 驱动的代理
- ✅ `agents_orchestrator.py` - 多代理协调

### 第06课：模型作为工具
- ✅ `models_router.py` - 基于意图的模型路由
- ✅ `models_pipeline.py` - 多步骤路由管道

### 支持性基础设施
- ✅ `workshop_utils.py` - 已遵循最佳实践（无需更改）

---

## 主要改进

### 1. 增强的错误处理

**之前：**
```python
manager, client, model_id = get_client(alias)
```
  
**之后：**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```
  
**优势：**
- 提供清晰的错误信息，实现优雅的错误处理
- 提供可操作的故障排除提示
- 为脚本提供正确的退出代码

### 2. 更好的导入管理

**之前：**
```python
from sentence_transformers import SentenceTransformer
```
  
**之后：**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```
  
**优势：**
- 缺少依赖时提供清晰的指导
- 避免晦涩的导入错误
- 提供用户友好的安装说明

### 3. 全面的文档

**为所有示例新增内容：**
- 在文档字符串中记录环境变量
- 添加 SDK 参考链接
- 提供使用示例
- 详细的函数/参数文档
- 添加类型提示以增强 IDE 支持

**示例：**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```
  

### 4. 改进的用户反馈

**新增信息性日志：**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```
  
**进度指示器：**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```
  
**结构化输出：**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```
  

### 5. 强大的基准测试

**第03课改进：**
- 针对每个模型的错误处理（失败时继续）
- 详细的进度报告
- 正确执行预热轮次
- 支持首个令牌延迟测量
- 阶段清晰分离

### 6. 一致的类型提示

**全面添加：**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```
  
**优势：**
- 更好的 IDE 自动补全
- 提前发现错误
- 自文档化代码

### 7. 增强的模型路由器

**第06课改进：**
- 全面的意图检测文档
- 模型选择算法说明
- 详细的路由日志
- 测试输出格式化
- 批量测试中的错误恢复

### 8. 多代理协调

**第05课改进：**
- 阶段性进度报告
- 针对每个代理的错误处理
- 清晰的管道结构
- 更好的内存管理文档

---

## 测试清单

### 前置条件
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```
  

### 测试每个示例

#### 第01课
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```
  
#### 第02课
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```
  
#### 第03课
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```
  
#### 第04课
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```
  
#### 第05课
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```
  
#### 第06课
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```
  

---

## 环境变量参考

### 全局（适用于所有示例）
| 变量名 | 描述 | 默认值 |
|--------|------|--------|
| `FOUNDRY_LOCAL_ALIAS` | 使用的模型别名 | 根据示例而定 |
| `FOUNDRY_LOCAL_ENDPOINT` | 覆盖服务端点 | 自动检测 |
| `SHOW_USAGE` | 显示令牌使用情况 | `0` |
| `RETRY_ON_FAIL` | 启用重试逻辑 | `1` |
| `RETRY_BACKOFF` | 初始重试延迟 | `1.0` |

### 示例特定
| 变量名 | 使用示例 | 描述 |
|--------|----------|------|
| `EMBED_MODEL` | 第02课 | 嵌入模型名称 |
| `RAG_QUESTION` | 第02课 | RAG 测试问题 |
| `BENCH_MODELS` | 第03课 | 要基准测试的模型（逗号分隔） |
| `BENCH_ROUNDS` | 第03课 | 基准测试轮次 |
| `BENCH_PROMPT` | 第03课 | 基准测试提示 |
| `BENCH_STREAM` | 第03课 | 测量首个令牌延迟 |
| `SLM_ALIAS` | 第04课 | 小型语言模型 |
| `LLM_ALIAS` | 第04课 | 大型语言模型 |
| `COMPARE_PROMPT` | 第04课 | 比较测试提示 |
| `AGENT_MODEL_PRIMARY` | 第05课 | 主代理模型 |
| `AGENT_MODEL_EDITOR` | 第05课 | 编辑代理模型 |
| `AGENT_QUESTION` | 第05课 | 代理测试问题 |
| `PIPELINE_TASK` | 第06课 | 管道任务 |

---

## 重大变更

**无** - 所有更改均向后兼容。

现有脚本将继续运行。新增功能包括：
- 可选的环境变量
- 增强的错误信息（不影响功能）
- 额外的日志记录（可禁用）
- 更好的类型提示（无运行时影响）

---

## 实施的最佳实践

### 1. 始终使用 Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```
  
### 2. 正确的错误处理模式
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```
  
### 3. 信息性日志记录
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```
  
### 4. 类型提示
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```
  
### 5. 全面的文档字符串
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```
  
### 6. 环境变量支持
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```
  
### 7. 优雅降级
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```
  

---

## 常见问题及解决方案

### 问题：导入错误
**解决方案**：安装缺失的依赖项  
```bash
pip install sentence-transformers ragas datasets numpy
```
  

### 问题：连接错误
**解决方案**：确保 Foundry Local 正在运行  
```bash
foundry service status
foundry model run phi-4-mini
```
  

### 问题：找不到模型
**解决方案**：检查可用模型  
```bash
foundry model ls
foundry model download <alias>
```
  

### 问题：性能较慢
**解决方案**：使用较小的模型或调整参数  
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```
  

---

## 下一步

### 1. 测试所有示例
按照上述测试清单验证所有示例是否正常运行。

### 2. 更新文档
- 更新课程的 Markdown 文件，添加新示例
- 在主 README 中添加故障排除部分
- 创建快速参考指南

### 3. 创建集成测试
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```
  

### 4. 添加性能基准
跟踪错误处理改进带来的性能提升。

### 5. 用户反馈
收集研讨会参与者的反馈，关注以下方面：
- 错误信息的清晰度
- 文档的完整性
- 易用性

---

## 资源

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **快速参考**: `Workshop/FOUNDRY_SDK_QUICKREF.md`  
- **迁移说明**: `Workshop/SDK_MIGRATION_NOTES.md`  
- **主仓库**: https://github.com/microsoft/Foundry-Local  

---

## 维护

### 添加新示例
创建新示例时，请遵循以下模式：

1. 使用 `workshop_utils` 管理客户端
2. 添加全面的错误处理
3. 支持环境变量
4. 添加类型提示和文档字符串
5. 提供信息性日志
6. 在文档字符串中包含使用示例
7. 链接到 SDK 文档

### 审核更新
审核示例更新时，请检查：
- [ ] 所有 I/O 操作的错误处理
- [ ] 公共函数的类型提示
- [ ] 全面的文档字符串
- [ ] 环境变量文档
- [ ] 信息性用户反馈
- [ ] SDK 参考链接
- [ ] 一致的代码风格

---

**总结**：所有研讨会 Python 示例现已遵循 Foundry Local SDK 的最佳实践，具备增强的错误处理、全面的文档和改进的用户体验。无重大变更 - 所有现有功能均得以保留并优化。

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。