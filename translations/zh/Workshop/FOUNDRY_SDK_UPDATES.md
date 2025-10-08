<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T16:13:20+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "zh"
}
-->
# Foundry Local SDK 更新

## 概述

更新了 Workshop 笔记本和工具，以正确使用 **官方 Foundry Local Python SDK**，遵循以下模式：
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## 修改的文件

### 1. `Workshop/samples/workshop_utils.py`

**更改内容：**
- ✅ 添加了对 `foundry-local-sdk` 包的导入错误处理
- ✅ 使用官方 SDK 模式增强了文档
- ✅ 使用 Unicode 符号（✓, ✗, ⚠）改进了日志记录
- ✅ 添加了全面的文档字符串和示例
- ✅ 提供了更详细的错误信息，参考 CLI 命令
- ✅ 更新了注释以匹配官方 SDK 文档

**主要改进：**

#### 导入错误处理
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### 增强的 `get_client()` 函数
- 添加了关于 SDK 初始化模式的详细文档
- 说明了 `FoundryLocalManager` 会自动启动服务
- 解释了模型别名解析为硬件优化版本的过程
- 改进了日志记录，显示端点信息
- 提供了更好的错误信息，建议排查步骤

#### 增强的 `chat_once()` 函数
- 添加了全面的文档字符串和使用示例
- 说明了与 OpenAI SDK 的兼容性
- 记录了流式支持（通过 kwargs）
- 改进了错误信息，提供 CLI 命令建议
- 添加了关于模型可用性检查的说明

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**更改内容：**
- ✅ 更新了所有 Markdown 单元格，添加 SDK 参考
- ✅ 使用 SDK 模式解释增强了代码注释
- ✅ 改进了单元格文档和说明
- ✅ 添加了故障排除指导
- ✅ 更新了模型目录（将 'gpt-oss-20b' 替换为 'phi-3.5-mini'）
- ✅ 使用视觉指示器改进了输出格式
- ✅ 在整个笔记本中添加了 SDK 链接和参考

**单元格逐步更新：**

#### 单元格 1（标题）
- 添加了 SDK 文档链接
- 参考了官方 GitHub 仓库

#### 单元格 2（场景）
- 使用编号步骤重新格式化
- 明确了基于意图的路由模式
- 强调了本地执行的优势

#### 单元格 3（依赖安装）
- 添加了每个包提供功能的解释
- 记录了 SDK 的能力（别名解析、硬件优化）

#### 单元格 4（环境设置）
- 增强了函数文档字符串
- 添加了内联注释，解释 SDK 模式
- 记录了模型目录结构
- 明确了优先级/能力匹配

#### 单元格 5（目录检查）
- 添加了视觉检查标记（✓）
- 更好地格式化了输出

#### 单元格 6（意图检测测试）
- 将输出重新格式化为表格样式
- 显示了意图和选定模型

#### 单元格 7（路由函数）
- 全面的 SDK 模式解释
- 记录了初始化流程
- 列出了所有功能（重试、跟踪、错误处理）
- 添加了 SDK 参考链接

#### 单元格 8（批量演示）
- 增强了预期结果的说明
- 添加了故障排除部分
- 包括了调试的 CLI 命令
- 更好地格式化了输出显示

### 3. `Workshop/notebooks/session06_README.md`（新文件）

**创建了全面的文档，涵盖以下内容：**

1. **概述**：架构图和组件说明
2. **SDK 集成**：遵循官方模式的代码示例
3. **前提条件**：逐步设置说明
4. **使用方法**：如何运行和自定义笔记本
5. **模型别名**：硬件优化版本的解释
6. **故障排除**：常见问题及解决方案
7. **扩展**：如何添加意图、模型和自定义逻辑
8. **性能提示**：生产环境的最佳实践
9. **资源**：官方文档和社区链接

## SDK 模式实现

### 官方模式（来自 Foundry Local 文档）

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

### 我们的实现（在 workshop_utils 中）

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

**我们方法的优势：**
- ✅ 完全遵循官方 SDK 模式
- ✅ 添加了缓存以避免重复初始化
- ✅ 包括了生产环境的重试逻辑
- ✅ 支持令牌使用跟踪
- ✅ 提供了更好的错误信息
- ✅ 与官方示例保持兼容

## 模型目录更改

### 之前
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### 之后
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**原因：** 将 'gpt-oss-20b'（非标准别名）替换为 'phi-3.5-mini'（官方 Foundry Local 别名）。

## 依赖项

### 更新的 requirements.txt

Workshop 的 requirements.txt 已包含：
```
foundry-local-sdk
openai>=1.30.0
```

这些是 Foundry Local 集成所需的唯一包。

## 测试更新

### 1. 验证 Foundry Local 是否正在运行

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. 检查可用模型

```bash
foundry model ls
```

确保以下模型可用或将自动下载：
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. 运行笔记本

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

或者在 VS Code 中打开并运行所有单元格。

### 4. 预期行为

**单元格 1（安装）：** 成功安装包  
**单元格 2（设置）：** 无错误，导入正常  
**单元格 3（验证）：** 显示 ✓ 和模型列表  
**单元格 4（测试意图）：** 显示意图检测结果  
**单元格 5（路由器）：** 显示 ✓ 路由函数已准备好  
**单元格 6（执行）：** 将提示路由到模型并显示结果  

### 5. 故障排除连接错误

如果出现 `APIConnectionError: Connection error`：

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## 环境变量

支持以下环境变量：

| 变量名              | 默认值   | 描述                     |
|---------------------|---------|--------------------------|
| `SHOW_USAGE`        | `0`     | 设置为 `1` 以打印令牌使用情况 |
| `RETRY_ON_FAIL`     | `1`     | 启用重试逻辑             |
| `RETRY_BACKOFF`     | `1.0`   | 初始重试延迟（秒）       |
| `FOUNDRY_LOCAL_ENDPOINT` | 自动   | 覆盖服务端点            |

### 使用示例

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## 从旧模式迁移

如果您有使用直接 API 调用的现有代码，以下是迁移方法：

### 之前（直接 API）
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

### 之后（SDK）
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

### 迁移的优势
- ✅ 自动服务管理
- ✅ 模型别名解析
- ✅ 硬件优化选择
- ✅ 更好的错误处理
- ✅ 与 OpenAI SDK 兼容
- ✅ 支持流式处理

## 参考资料

### 官方文档
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK 源代码**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI 参考**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **故障排除**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Workshop 资源
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **示例笔记本**: `Workshop/notebooks/session06_models_router.ipynb`

### 社区
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## 下一步

1. **审查更改**：阅读更新的文件  
2. **测试笔记本**：运行 session06_models_router.ipynb  
3. **验证 SDK**：确保已安装 foundry-local-sdk  
4. **检查服务**：确认 Foundry Local 正在运行  
5. **探索文档**：阅读新的 session06_README.md  

## 总结

这些更新确保 Workshop 材料完全遵循 **官方 Foundry Local SDK 模式**，与 GitHub 仓库中的文档一致。所有代码示例、文档和工具现在都符合微软推荐的本地 AI 模型部署最佳实践。

这些更改改进了：
- ✅ **正确性**：使用官方 SDK 模式  
- ✅ **文档**：全面的说明和示例  
- ✅ **错误处理**：更好的消息和故障排除指导  
- ✅ **可维护性**：遵循官方约定  
- ✅ **用户体验**：更清晰的说明和调试帮助  

---

**更新日期：** 2025年10月8日  
**SDK 版本：** foundry-local-sdk（最新）  
**Workshop 分支：** Reactor  

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。