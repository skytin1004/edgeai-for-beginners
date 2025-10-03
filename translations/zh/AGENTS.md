<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:24:31+00:00",
  "source_file": "AGENTS.md",
  "language_code": "zh"
}
-->
# AGENTS.md

## 项目概述

EdgeAI for Beginners 是一个全面的教育资源库，旨在教授使用小型语言模型（SLMs）进行边缘 AI 开发。课程内容涵盖 EdgeAI 基础知识、模型部署、优化技术以及使用 Microsoft Foundry Local 和各种 AI 框架的生产级实现。

**关键技术：**
- Python 3.8+（AI/ML 示例的主要语言）
- .NET C#（AI/ML 示例）
- JavaScript/Node.js 与 Electron（用于桌面应用程序）
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI 工具包
- OpenAI SDK
- AI 框架：LangChain、Semantic Kernel、Chainlit
- 模型优化：Llama.cpp、Microsoft Olive、OpenVINO、Apple MLX

**资源库类型：** 包含 8 个模块和 10 个综合示例应用的教育内容资源库

**架构：** 多模块学习路径，结合实际示例展示边缘 AI 部署模式

## 资源库结构

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## 设置命令

### 资源库设置

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python 示例设置（模块08和Python示例）

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Node.js 示例设置（示例08 - Windows聊天应用）

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Local 设置

运行模块08示例需要安装 Foundry Local：

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## 开发工作流程

### 内容开发

此资源库主要包含 **Markdown 教育内容**。进行更改时：

1. 编辑适当模块目录中的 `.md` 文件
2. 遵循现有的格式模式
3. 确保代码示例准确且经过测试
4. 如果需要，更新相应的翻译内容（或让自动化处理）

### 示例应用开发

对于 Python 示例（示例01-07, 09-10）：
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

对于 Electron 示例（示例08）：
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### 测试示例应用

Python 示例没有自动化测试，但可以通过运行进行验证：
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron 示例具有测试基础设施：
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## 测试说明

### 内容验证

资源库使用自动化翻译工作流。翻译无需手动测试。

**内容更改的手动验证：**
1. 通过预览 `.md` 文件检查 Markdown 渲染效果
2. 验证所有链接指向有效目标
3. 测试文档中包含的代码片段
4. 确保图片加载正确

### 示例应用测试

**模块08/示例/08（Electron 应用）具有全面测试：**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python 示例需要手动测试：**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## 代码风格指南

### Markdown 内容

- 使用一致的标题层级（# 用于标题，## 用于主要部分，### 用于子部分）
- 包含带语言说明符的代码块：```python, ```bash, ```javascript
- 遵循现有的表格、列表和强调格式
- 保持行可读性（目标约 80-100 字符，但不严格）
- 对内部引用使用相对链接

### Python 代码风格

- 遵循 PEP 8 规范
- 适当使用类型提示
- 为函数和类添加文档字符串
- 使用有意义的变量名
- 保持函数专注且简洁

### JavaScript/Node.js 代码风格

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**关键约定：**
- 示例08中提供了 ESLint 配置
- 使用 Prettier 进行代码格式化
- 使用现代 ES6+ 语法
- 遵循代码库中的现有模式

## 拉取请求指南

### 标题格式
```
[ModuleXX] Brief description of change
```
或
```
[Module08/samples/XX] Description for sample changes
```

### 提交前

**对于内容更改：**
- 预览所有修改的 Markdown 文件
- 验证链接和图片是否正常
- 检查拼写和语法错误

**对于示例代码更改（模块08/示例/08）：**
```bash
npm run lint
npm test
```

**对于 Python 示例更改：**
- 测试示例是否成功运行
- 验证错误处理是否正常
- 检查与 Foundry Local 的兼容性

### 审核流程

- 教育内容更改需审核准确性和清晰度
- 代码示例需测试功能性
- 翻译更新由 GitHub Actions 自动处理

## 翻译系统

**重要说明：** 此资源库使用 GitHub Actions 自动翻译。

- 翻译文件位于 `/translations/` 目录（支持 50+ 种语言）
- 通过 `co-op-translator.yml` 工作流自动化
- **请勿手动编辑翻译文件** - 它们会被覆盖
- 仅编辑根目录和模块目录中的英文源文件
- 推送到 `main` 分支时会自动生成翻译

## Foundry Local 集成

大多数模块08示例需要运行 Microsoft Foundry Local：

### 启动 Foundry Local
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### 验证 Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### 示例环境变量

大多数示例使用以下环境变量：
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## 构建与部署

### 内容部署

此资源库主要是文档内容 - 无需构建过程。

### 示例应用构建

**Electron 应用（模块08/示例/08）：**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python 示例：**
无需构建过程 - 示例直接使用 Python 解释器运行。

## 常见问题与故障排除

### Foundry Local 未运行
**问题：** 示例因连接错误而失败

**解决方案：**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Python 虚拟环境问题
**问题：** 模块导入错误

**解决方案：**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Electron 构建问题
**问题：** npm 安装或构建失败

**解决方案：**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### 翻译工作流冲突
**问题：** 翻译 PR 与您的更改发生冲突

**解决方案：**
- 仅编辑英文源文件
- 让自动化翻译工作流处理翻译
- 如果发生冲突，在翻译合并后将 `main` 分支合并到您的分支

## 其他资源

### 学习路径
- **初学者路径：** 模块01-02（7-9小时）
- **中级路径：** 模块03-04（9-11小时）
- **高级路径：** 模块05-07（12-15小时）
- **专家路径：** 模块08（8-10小时）

### 关键模块内容
- **模块01：** EdgeAI 基础知识和实际案例研究
- **模块02：** 小型语言模型（SLM）家族和架构
- **模块03：** 本地和云部署策略
- **模块04：** 使用多种框架进行模型优化
- **模块05：** SLMOps - 生产操作
- **模块06：** AI 代理和函数调用
- **模块07：** 平台特定实现
- **模块08：** Foundry Local 工具包及 10 个综合示例

### 外部依赖
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - 本地 AI 模型运行时
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - 优化框架
- [Microsoft Olive](https://microsoft.github.io/Olive/) - 模型优化工具包
- [OpenVINO](https://docs.openvino.ai/) - Intel 的优化工具包

## 项目特定说明

### 模块08示例应用

资源库包含 10 个综合示例应用：

1. **01-REST Chat Quickstart** - 基本的 OpenAI SDK 集成
2. **02-OpenAI SDK Integration** - 高级 SDK 功能
3. **03-Model Discovery & Benchmarking** - 模型比较工具
4. **04-Chainlit RAG Application** - 检索增强生成
5. **05-Multi-Agent Orchestration** - 基本代理协调
6. **06-Models-as-Tools Router** - 智能模型路由
7. **07-Direct API Client** - 低级 API 集成
8. **08-Windows 11 Chat App** - 原生 Electron 桌面应用
9. **09-Advanced Multi-Agent System** - 复杂代理协调
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel 集成

每个示例展示了使用 Foundry Local 进行边缘 AI 开发的不同方面。

### 性能考虑

- SLMs 针对边缘部署进行了优化（2-16GB RAM）
- 本地推理提供 50-500ms 响应时间
- 量化技术实现 75% 的大小缩减，同时保留 85% 的性能
- 使用本地模型实现实时对话功能

### 安全性与隐私

- 所有处理均在本地完成 - 无数据发送到云端
- 适用于隐私敏感型应用（医疗、金融）
- 满足数据主权要求
- Foundry Local 完全在本地硬件上运行

---

**这是一个专注于教授边缘 AI 开发的教育资源库。主要贡献模式是改进教育内容以及添加/增强示例应用，以展示边缘 AI 概念。**

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。