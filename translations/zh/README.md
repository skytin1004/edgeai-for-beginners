<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ff006cd813df4152f5036e7b2bc5ed32",
  "translation_date": "2025-09-24T09:31:20+00:00",
  "source_file": "README.md",
  "language_code": "zh"
}
-->
# EdgeAI 初学者指南

![课程封面图片](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.zh.png)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

按照以下步骤开始使用这些资源：

1. **Fork 仓库**：点击 [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **克隆仓库**：`git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**加入 Azure AI Foundry Discord，与专家和开发者交流**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 多语言支持

#### 通过 GitHub Action 支持（自动化且始终保持最新）

[阿拉伯语](../ar/README.md) | [孟加拉语](../bn/README.md) | [保加利亚语](../bg/README.md) | [缅甸语](../my/README.md) | [中文（简体）](./README.md) | [中文（繁体，香港）](../hk/README.md) | [中文（繁体，澳门）](../mo/README.md) | [中文（繁体，台湾）](../tw/README.md) | [克罗地亚语](../hr/README.md) | [捷克语](../cs/README.md) | [丹麦语](../da/README.md) | [荷兰语](../nl/README.md) | [芬兰语](../fi/README.md) | [法语](../fr/README.md) | [德语](../de/README.md) | [希腊语](../el/README.md) | [希伯来语](../he/README.md) | [印地语](../hi/README.md) | [匈牙利语](../hu/README.md) | [印尼语](../id/README.md) | [意大利语](../it/README.md) | [日语](../ja/README.md) | [韩语](../ko/README.md) | [马来语](../ms/README.md) | [马拉地语](../mr/README.md) | [尼泊尔语](../ne/README.md) | [挪威语](../no/README.md) | [波斯语](../fa/README.md) | [波兰语](../pl/README.md) | [葡萄牙语（巴西）](../br/README.md) | [葡萄牙语（葡萄牙）](../pt/README.md) | [旁遮普语](../pa/README.md) | [罗马尼亚语](../ro/README.md) | [俄语](../ru/README.md) | [塞尔维亚语（西里尔字母）](../sr/README.md) | [斯洛伐克语](../sk/README.md) | [斯洛文尼亚语](../sl/README.md) | [西班牙语](../es/README.md) | [斯瓦希里语](../sw/README.md) | [瑞典语](../sv/README.md) | [他加禄语（菲律宾语）](../tl/README.md) | [泰语](../th/README.md) | [土耳其语](../tr/README.md) | [乌克兰语](../uk/README.md) | [乌尔都语](../ur/README.md) | [越南语](../vi/README.md)

**如果您希望支持其他语言，支持的语言列表请参见 [这里](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## 介绍

欢迎来到 **EdgeAI 初学者指南**——这是您探索边缘人工智能变革世界的全面旅程。本课程将强大的 AI 能力与实际的边缘设备部署相结合，帮助您直接在数据生成和决策需要的地方释放 AI 的潜力。

### 您将掌握的内容

本课程从基础概念到生产级实现，涵盖以下内容：
- **小型语言模型（SLMs）**，优化用于边缘部署
- **硬件优化**，适用于多种平台
- **实时推理**，具备隐私保护功能
- **生产部署**，面向企业应用的策略

### 为什么边缘 AI 很重要

边缘 AI 是一种解决现代关键问题的范式转变：
- **隐私与安全**：在本地处理敏感数据，无需上传到云端
- **实时性能**：消除网络延迟，适用于时间敏感的应用
- **成本效益**：减少带宽和云计算费用
- **弹性操作**：在网络中断时仍能保持功能
- **法规遵从**：满足数据主权要求

### 边缘 AI

边缘 AI 指的是在硬件设备上本地运行 AI 算法和语言模型，靠近数据生成的地方，无需依赖云资源进行推理。它减少了延迟，增强了隐私，并支持实时决策。

### 核心原则：
- **设备端推理**：AI 模型在边缘设备（手机、路由器、微控制器、工业 PC）上运行
- **离线能力**：无需持续的互联网连接即可运行
- **低延迟**：适合实时系统的即时响应
- **数据主权**：将敏感数据保留在本地，提高安全性和合规性

### 小型语言模型（SLMs）

SLMs 如 Phi-4、Mistral-7B 和 Gemma 是大型语言模型的优化版本——通过训练或蒸馏实现：
- **减少内存占用**：高效利用边缘设备有限的内存
- **降低计算需求**：优化 CPU 和边缘 GPU 性能
- **更快的启动时间**：快速初始化，适用于响应式应用

它们在以下场景中满足约束条件的同时，释放强大的自然语言处理能力：
- **嵌入式系统**：物联网设备和工业控制器
- **移动设备**：支持离线功能的智能手机和平板电脑
- **物联网设备**：资源有限的传感器和智能设备
- **边缘服务器**：具有有限 GPU 资源的本地处理单元
- **个人电脑**：桌面和笔记本电脑的部署场景

## 课程模块与导航

| 模块 | 主题 | 重点领域 | 关键内容 | 难度 | 时长 |
|------|------|----------|----------|------|------|
| [📚 01](../../Module01) | [边缘 AI 基础](./Module01/README.md) | 云与边缘 AI 比较 | 边缘 AI 基础 • 实际案例研究 • 实现指南 • 边缘部署 | 初级 | 3-4 小时 |
| [🧠 02](../../Module02) | [SLM 模型基础](./Module02/README.md) | 模型家族与架构 | Phi 家族 • Qwen 家族 • Gemma 家族 • BitNET • μModel • Phi-Silica | 初级 | 4-5 小时 |
| [🚀 03](../../Module03) | [SLM 部署实践](./Module03/README.md) | 本地与云部署 | 高级学习 • 本地环境 • 云部署 | 中级 | 4-5 小时 |
| [⚙️ 04](../../Module04) | [模型优化工具包](./Module04/README.md) | 跨平台优化 | 介绍 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • 工作流合成 | 中级 | 5-6 小时 |
| [🔧 05](../../Module05) | [SLMOps 生产](./Module05/README.md) | 生产操作 | SLMOps 介绍 • 模型蒸馏 • 微调 • 生产部署 | 高级 | 5-6 小时 |
| [🤖 06](../../Module06) | [AI 代理与函数调用](./Module06/README.md) | 代理框架与 MCP | 代理介绍 • 函数调用 • 模型上下文协议 | 高级 | 4-5 小时 |
| [💻 07](../../Module07) | [平台实现](./Module07/README.md) | 跨平台示例 | AI 工具包 • Foundry Local • Windows 开发 | 高级 | 3-4 小时 |
| [🏭 08](../../Module08) | [Foundry Local 工具包](./Module08/README.md) | 生产级示例 | 示例应用（详见下方） | 专家 | 8-10 小时 |

### 🏭 **模块 08：示例应用**

- [01: REST 聊天快速入门](./Module08/samples/01/README.md)
- [02: OpenAI SDK 集成](./Module08/samples/02/README.md)
- [03: 模型发现与基准测试](./Module08/samples/03/README.md)
- [04: Chainlit RAG 应用](./Module08/samples/04/README.md)
- [05: 多代理编排](./Module08/samples/05/README.md)
- [06: 模型工具路由器](./Module08/samples/06/README.md)
- [07: 直接 API 客户端](./Module08/samples/07/README.md)
- [08: Windows 11 聊天应用](./Module08/samples/08/README.md)
- [09: 高级多代理系统](./Module08/samples/09/README.md)
- [10: Foundry 工具框架](./Module08/samples/10/README.md)

### 📊 **学习路径总结**
- **总时长**：36-45 小时
- **初级路径**：模块 01-02（7-9 小时）  
- **中级路径**：模块 03-04（9-11 小时）
- **高级路径**：模块 05-07（12-15 小时）
- **专家路径**：模块 08（8-10 小时）

## 您将构建的内容

### 🎯 核心能力
- **边缘 AI 架构**：设计本地优先的 AI 系统并集成云端
- **模型优化**：量化和压缩模型以适应边缘部署（速度提升 85%，大小减少 75%）
- **多平台部署**：支持 Windows、移动设备、嵌入式设备和云边缘混合系统
- **生产操作**：监控、扩展和维护生产中的边缘 AI

### 🏗️ 实践项目
- **Foundry Local 聊天应用**：支持模型切换的 Windows 11 原生应用
- **多代理系统**：协调复杂工作流的专家代理
- **RAG 应用**：本地文档处理与向量搜索
- **模型路由器**：基于任务分析的智能模型选择
- **API 框架**：具备流式处理和健康监控的生产级客户端
- **跨平台工具**：LangChain/Semantic Kernel 集成模式

### 🏢 行业应用
**制造业** • **医疗健康** • **自动驾驶** • **智慧城市** • **移动应用**

## 快速入门

**推荐学习路径**（总计 20-30 小时）：

1. **📚 基础**（模块 01-02）：边缘 AI 概念 + SLM 模型家族
2. **⚙️ 优化**（模块 03-04）：部署 + 量化框架  
3. **🚀 生产**（模块 05-06）：SLMOps + AI 代理 + 函数调用
4. **💻 实现**（模块 07-08）：平台示例 + Foundry Local 工具包

每个模块都包含理论、实践练习和生产级代码示例。

## 职业影响
**技术角色**：EdgeAI解决方案架构师 • 机器学习工程师（边缘） • IoT AI开发者 • 移动AI开发者

**行业领域**：工业4.0 • 医疗科技 • 自主系统 • 金融科技 • 消费电子

**项目组合**：多代理系统 • 生产级RAG应用 • 跨平台部署 • 性能优化

## 仓库结构

```
edgeai-for-beginners/
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## 课程亮点

✅ **渐进式学习**：理论 → 实践 → 生产部署  
✅ **真实案例研究**：微软、日本航空、企业级实施案例  
✅ **动手实践样例**：50+示例，10个全面的Foundry Local演示  
✅ **性能优化**：提升速度85%，减少体积75%  
✅ **多平台支持**：Windows、移动端、嵌入式、云边混合架构  
✅ **生产级准备**：监控、扩展、安全性、合规框架

📖 **[学习指南可用](STUDY_GUIDE.md)**：结构化的20小时学习路径，包含时间分配建议和自我评估工具。

---

**EdgeAI代表了AI部署的未来**：本地优先、隐私保护、高效。掌握这些技能，构建下一代智能应用。

## 其他课程

我们的团队还制作了其他课程！查看以下内容：

- [MCP入门课程](https://github.com/microsoft/mcp-for-beginners)
- [AI代理入门课程](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [使用.NET的生成式AI入门课程](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [使用JavaScript的生成式AI入门课程](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [生成式AI入门课程](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [机器学习入门课程](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [数据科学入门课程](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [AI入门课程](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [网络安全入门课程](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [Web开发入门课程](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [IoT入门课程](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [XR开发入门课程](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [掌握GitHub Copilot进行AI配对编程](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [掌握GitHub Copilot为C#/.NET开发者服务](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [选择你的Copilot冒险之旅](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

---

