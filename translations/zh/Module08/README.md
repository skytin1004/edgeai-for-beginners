<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T11:41:28+00:00",
  "source_file": "Module08/README.md",
  "language_code": "zh"
}
-->
# 第08模块：深入体验Microsoft Foundry Local - 完整开发者工具包

## 概述

Microsoft Foundry Local代表了边缘AI开发的下一代技术，为开发者提供强大的工具，用于本地构建、部署和扩展AI应用，同时与Azure AI Foundry保持无缝集成。本模块全面覆盖了Foundry Local的安装到高级代理开发的全过程。

**关键技术：**
- Microsoft Foundry Local CLI和SDK
- Azure AI Foundry集成
- 设备上的模型推理
- 本地模型缓存与优化
- 基于代理的架构

## 模块学习目标

完成本模块后，您将能够：

- **掌握Foundry Local设置**：安装、配置并优化Foundry Local以支持Windows 11开发
- **部署多样化模型**：使用CLI命令本地运行phi、qwen、deepseek和GPT-OSS-20B模型
- **构建生产级解决方案**：通过高级提示工程和数据集成创建AI应用
- **利用开源生态系统**：集成Hugging Face模型和社区驱动的扩展
- **比较AI架构**：理解LLM与SLM的权衡及部署策略
- **开发AI代理**：使用Foundry Local的架构和基础能力构建智能代理
- **实现模型工具化**：创建模块化、可定制的企业级AI解决方案

## 课程结构

### [1: 开始使用Foundry Local](./01.FoundryLocalSetup.md)
**重点**：安装、CLI设置、模型缓存和硬件加速

**您将学到：**
- 在Windows 11上完成Foundry Local安装
- CLI配置和命令结构
- 优化性能的模型缓存策略
- 硬件加速设置与优化
- 实践部署phi、qwen、deepseek和GPT-OSS-20B模型

**时长**：2-3小时  
**前置条件**：Windows 11，基本命令行知识

---

### [2: 使用Azure AI Foundry构建AI解决方案](./02.AzureAIFoundryIntegration.md)
**重点**：高级提示工程、数据集成和可操作任务

**您将学到：**
- 高级提示工程技术
- 数据集成模式和最佳实践
- 使用Foundry Local构建可操作的AI任务
- 无缝的Azure AI Foundry集成工作流
- 性能优化与监控

**时长**：2-3小时  
**前置条件**：完成第1节，Azure账户（可选）

---

### [3: Foundry Local中的开源模型](./03.OpenSourceModels.md)
**重点**：Hugging Face集成、模型选择策略和社区驱动的扩展

**您将学到：**
- Hugging Face模型与Foundry Local的集成
- 自带模型（BYOM）策略与实现
- Model Mondays系列的见解和社区贡献
- 自定义模型部署与优化
- 社区模型评估与选择标准

**时长**：2-3小时  
**前置条件**：完成第1-2节，Hugging Face账户

---

### [4: 探索前沿模型 - LLMs、SLMs和设备上的推理](./04.CuttingEdgeModels.md)
**重点**：模型比较、使用Phi和ONNX Runtime的EdgeAI、高级演示

**您将学到：**
- 全面的LLM与SLM比较及应用场景
- 本地与云推理的权衡及决策框架
- 使用Phi和ONNX Runtime实现EdgeAI
- Chainlit RAG聊天应用开发与部署
- WebGPU推理优化技术
- AI PC SDK集成与功能

**时长**：3-4小时  
**前置条件**：完成第1-3节，理解推理概念

---

### [5: 使用Foundry Local快速构建AI驱动代理](./05.AIPoweredAgents.md)
**重点**：快速生成式AI应用开发、系统提示、基础能力和代理架构

**您将学到：**
- Foundry Local代理架构与设计模式
- 系统提示工程以定义代理行为
- 可靠代理响应的基础技术
- 快速生成式AI应用开发工作流
- 代理编排与多代理系统
- AI代理的生产部署策略

**时长**：3-4小时  
**前置条件**：完成第1-4节，基本了解AI代理

---

### [6: Foundry Local - 模型工具化](./06.ModelsAsTools.md)
**重点**：模块化AI解决方案、设备上的部署和企业级扩展

**您将学到：**
- 将AI模型视为模块化、可定制的工具
- 无需云依赖的设备部署
- 低延迟、成本高效且隐私保护的推理
- SDK、API和CLI集成模式
- 针对特定用例的模型定制
- 从本地到Azure AI Foundry的扩展策略
- 企业级AI应用架构

**时长**：3-4小时  
**前置条件**：完成所有前置课程，有企业开发经验更佳

## 前置条件

### 系统要求
- **操作系统**：Windows 11（22H2或更高版本）
- **内存**：16GB RAM（建议32GB以支持更大的模型）
- **存储**：50GB可用空间用于模型缓存
- **硬件**：建议使用支持NPU的设备（如Copilot+ PC），GPU可选
- **网络**：高速互联网用于初始模型下载

### 开发环境
- Visual Studio Code及AI Toolkit扩展
- Python 3.10+及pip
- Git用于版本控制
- PowerShell或命令提示符
- Azure CLI（可选，用于云集成）

### 知识要求
- 基本了解AI/ML概念
- 熟悉命令行操作
- Python编程基础
- REST API概念
- 基本提示工程和模型推理知识

## 模块时间表

**总预计时间**：15-20小时

| 课程 | 重点领域 | 时间 | 难度 |
|------|----------|------|------|
|  1 | 设置与基础 | 2-3小时 | 初级 |
|  2 | AI解决方案 | 2-3小时 | 中级 |
|  3 | 开源模型 | 2-3小时 | 中级 |
|  4 | 高级模型 | 3-4小时 | 高级 |
|  5 | AI代理 | 3-4小时 | 高级 |
|  6 | 企业工具 | 3-4小时 | 专家 |

## 关键资源

### 主要文档
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local文档](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays系列](https://aka.ms/model-mondays)

### 社区资源
- [Foundry Local社区讨论](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry示例](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI开发者社区](https://techcommunity.microsoft.com/category/artificialintelligence)

## 学习成果

完成本模块后，您将具备以下能力：

### 技术掌握
- **部署与管理**：在开发和生产环境中安装和管理Foundry Local
- **集成模型**：无缝使用来自Microsoft、Hugging Face和社区的多样化模型
- **构建应用**：创建具有高级功能和优化的生产级AI应用
- **开发代理**：实现具有基础能力、推理和工具集成的复杂AI代理

### 战略理解
- **架构决策**：在本地与云部署之间做出明智选择
- **性能优化**：优化不同硬件配置下的推理性能
- **企业扩展**：设计从本地原型到企业部署的应用
- **隐私与安全**：实现隐私保护的AI解决方案，支持本地推理

### 创新能力
- **快速原型**：快速构建和测试AI应用概念
- **社区集成**：利用开源模型并为生态系统做出贡献
- **高级模式**：实现包括RAG、代理和工具集成在内的前沿AI模式
- **面向未来开发**：构建适应新兴AI技术和模式的应用

## 开始学习

1. **准备环境**：确保Windows 11符合推荐硬件规格
2. **安装前置条件**：设置开发工具和依赖项
3. **从第1节开始**：从Foundry Local安装和基础设置入手
4. **按顺序学习**：按顺序完成课程以获得最佳学习效果
5. **持续实践**：通过实践练习和项目应用所学概念

## 成功指标

通过以下指标跟踪您的学习进度：

- [ ] 成功安装并配置Foundry Local
- [ ] 部署并运行至少4个不同的模型系列
- [ ] 构建一个完整的AI解决方案并实现数据集成
- [ ] 集成至少2个开源模型
- [ ] 创建一个功能性RAG聊天应用
- [ ] 开发并部署一个AI代理
- [ ] 实现一个模型工具化架构

## 示例快速启动

### 1) 环境设置（Windows cmd.exe）
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) 启动本地模型（新终端）
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) 运行Chainlit演示（第4节）
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) 运行多代理协调器（第5节）
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

如果出现连接错误，请验证Foundry Local：
```cmd
curl http://localhost:8000/v1/models
```

### 路由器配置（第6节）
路由器执行快速健康检查并支持基于环境的配置：
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

本模块代表了边缘AI开发的前沿技术，将Microsoft的企业级工具与开源生态系统的灵活性和创新性相结合。通过掌握Foundry Local，您将站在AI应用开发的最前沿。

有关Azure OpenAI（第2节），请参阅示例README以获取所需的环境变量和API版本设置。

## 示例概览

- `samples/01`：快速REST聊天到Foundry Local（`chat_quickstart.py`）。
- `samples/02`：OpenAI SDK集成（`sdk_quickstart.py`）。
- `samples/03`：模型发现+快速基准测试（`list_and_bench.cmd`）。
- `samples/04`：Chainlit RAG演示（`app.py`）。
- `samples/05`：多代理编排（`python -m samples.05.agents.coordinator`）。
- `samples/06`：模型工具化路由器（`python samples\06\router.py`）。

---

