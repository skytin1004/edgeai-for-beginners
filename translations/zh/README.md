<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0f8da2fde263594c60dab5c40e0fffc",
  "translation_date": "2025-07-22T07:44:48+00:00",
  "source_file": "README.md",
  "language_code": "zh"
}
-->
# EdgeAI 初学者指南

通过三个全面模块（EdgeAI 基础知识、小型语言模型基础和实践部署策略）深入学习 Edge AI 技术。本课程从基础概念到高级实现，涵盖真实案例研究、动手练习和部署示例，展示如何在边缘设备上高效运行 AI 模型，从而增强隐私、降低延迟并提高效率。

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
1. **Fork 仓库**：点击 [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/mcp-for-beginners/fork)  
2. **克隆仓库**：`git clone https://github.com/microsoft/edgeai-for-beginners.git`  
3. [**加入 Azure AI Foundry Discord，与专家和开发者交流**](https://discord.com/invite/ByRwuEEgH4)  

### 🌐 多语言支持

#### 通过 GitHub Action 支持（自动化且始终保持最新）

[法语](../fr/README.md) | [西班牙语](../es/README.md) | [简体中文](./README.md) | [繁体中文（澳门）](../mo/README.md) | [繁体中文（香港）](../hk/README.md) | [繁体中文（台湾）](../tw/README.md) | [日语](../ja/README.md) | [韩语](../ko/README.md) |  

欢迎来到 EdgeAI 初学者指南，在这里语言模型的强大功能与本地设备的高效性相结合。本课程介绍了如何在边缘硬件（如智能手机、物联网板卡和小型服务器）上直接运行小型优化语言模型（SLMs），无需依赖云端访问。您将探索实时、注重隐私的 AI 推理如何通过轻量化部署彻底改变智能家居、工业监控和离线应用，兼顾速度、安全性和模块化。

**Edge AI**

Edge AI 是指在本地硬件上运行 AI 算法和语言模型——靠近数据生成的位置——而无需依赖云资源进行推理。它减少了延迟、增强了隐私，并支持实时决策。

核心原则：
- **设备端推理**：AI 模型在边缘设备（手机、路由器、微控制器、工业 PC）上运行。
- **离线能力**：无需持续联网即可运行。
- **低延迟**：适合实时系统的即时响应。
- **数据主权**：敏感数据保留在本地，提高安全性和合规性。

**小型语言模型（SLMs）**

像 Phi-4、Mistral-7B 或 Gemma 这样的 SLM 是更大 LLM 的优化版本，通过训练或蒸馏实现：
- 更小的内存占用
- 更低的计算需求
- 更快的启动时间

它们在以下场景中提供强大的 NLP 功能，同时满足约束条件：
- 嵌入式系统
- 移动设备
- 物联网设备
- GPU 资源有限的边缘服务器
- 个人电脑

## 课程架构

### [模块 01：EdgeAI 基础知识与变革](./Module01/README.md)
**主题**：边缘 AI 部署的变革性转变

#### 章节结构：
- [**第 1 节：EdgeAI 基础知识**](./Module01/01.EdgeAIFundamentals.md)
  - 传统云 AI 与边缘 AI 的对比
  - 边缘计算的挑战与限制
  - 关键技术：模型量化、压缩优化、小型语言模型（SLMs）
  - 硬件加速：NPU、GPU 优化、CPU 优化
  - 优势：隐私安全、低延迟、离线能力、成本效益

- [**第 2 节：真实案例研究**](./Module01/02.RealWorldCaseStudies.md)
  - Microsoft Phi 和 Mu 模型生态系统
    - Phi Silica：Windows AI 集成
    - Mu 模型：任务特定的微型语言模型
  - 日本航空 AI 报告系统案例研究
  - 市场影响与未来方向
  - 部署注意事项与最佳实践

- [**第 3 节：实践实施指南**](./Module01/03.PracticalImplementationGuide.md)
  - 开发环境设置（Python 3.10+，.NET 8+）
  - 硬件要求与推荐配置
  - 核心模型家族资源
  - 量化与优化工具（Llama.cpp、Microsoft Olive、Apple MLX）
  - 评估与验证清单

- [**第 4 节：边缘 AI 部署硬件平台**](./Module01/04.EdgeDeployment.md)
  - 边缘 AI 部署的注意事项与要求
  - Intel 边缘 AI 硬件与优化技术
  - Qualcomm 移动与嵌入式系统 AI 解决方案
  - NVIDIA Jetson 与边缘计算平台
  - Windows AI PC 平台与 NPU 加速
  - 硬件特定的优化策略

---

### [模块 02：小型语言模型基础](./Module02/README.md)
**主题**：SLM 理论原理、实施策略与生产部署

#### 章节结构：
- [**第 1 节：Microsoft Phi 模型家族基础**](./Module02/01.PhiFamily.md)
  - 设计理念演变（Phi-1 到 Phi-4）
  - 以效率为先的架构设计
  - 专业能力（推理、多模态、边缘部署）

- [**第 2 节：Qwen 模型家族基础**](./Module02/02.QwenFamily.md)
  - 开源卓越（Qwen 1.0 到 Qwen3）——可通过 Hugging Face 获取
  - 具有思维模式能力的高级推理架构
  - 可扩展部署选项（0.5B-235B 参数）

- [**第 3 节：Gemma 模型家族基础**](./Module02/03.GemmaFamily.md)
  - 以研究为驱动的创新（Gemma 3 和 3n）
  - 多模态卓越
  - 移动优先架构

- [**第 4 节：BitNET 模型家族基础**](./Module02/04.BitNETFamily.md)
  - 革命性的量化技术（1.58-bit）
  - 专用推理框架：https://github.com/microsoft/BitNet
  - 通过极致效率实现可持续 AI 领导力

- [**第 5 节：Microsoft Mu 模型基础**](./Module02/05.mumodel.md)
  - 面向设备的架构，内置于 Windows 11
  - 与 Windows 11 设置集成
  - 注重隐私的离线操作

- [**第 6 节：Phi-Silica 基础**](./Module02/06.phisilica.md)
  - 针对 NPU 优化的架构，内置于 Windows 11 Copilot+ PC
  - 卓越效率（650 tokens/second，功耗仅 1.5W）
  - 开发者可通过 Windows App SDK 集成

---

### [模块 03：小型语言模型部署](./Module03/README.md)
**主题**：从理论到生产环境的完整 SLM 生命周期部署

#### 章节结构：
- [**第 1 节：SLM 高级学习**](./Module03/01.SLMAdvancedLearning.md)
  - 参数分类框架（微型 SLM 100M-1.4B，中型 SLM 14B-30B）
  - 高级优化技术（量化方法、BitNET 1-bit 量化）
  - 模型获取策略（Azure AI Foundry 提供 Phi 模型，Hugging Face 提供精选模型）

- [**第 2 节：本地环境部署**](./Module03/02.DeployingSLMinLocalEnv.md)
  - Ollama 通用平台部署
  - Microsoft Foundry 本地企业级解决方案
  - 框架对比分析

- [**第 3 节：容器化云部署**](./Module03/03.DeployingSLMinCloud.md)
  - vLLM 高性能推理部署
  - Ollama 容器编排
  - ONNX Runtime 边缘优化实现

---

### [模块 04：模型格式转换与量化](./Module04/README.md)
**主题**：跨平台边缘部署的完整模型优化工具包

#### 章节结构：
- [**第 1 节：模型格式转换与量化基础**](./Module04/01.Introduce.md)
  - 精度分类框架（超低、低、中精度）
  - GGUF 和 ONNX 格式的优势与使用场景
  - 量化对操作效率的好处
  - 性能基准与内存占用对比

- [**第 2 节：Llama.cpp 实施指南**](./Module04/02.Llamacpp.md)
  - 跨平台安装（Windows、macOS、Linux）
  - GGUF 格式转换与量化级别（Q2_K 到 Q8_0）
  - 硬件加速（CUDA、Metal、OpenCL、Vulkan）
  - Python 集成与 REST API 部署

- [**第 3 节：Microsoft Olive 优化套件**](./Module04/03.MicrosoftOlive.md)
  - 硬件感知模型优化，内置 40+ 组件
  - 动态与静态量化的自动优化
  - 与 Azure ML 工作流的企业集成
  - 支持的热门模型（Llama、Phi、精选 Qwen 模型、Gemma）

- [**第 4 节：Apple MLX 框架深度解析**](./Module04/04.AppleMLX.md)
  - 针对 Apple Silicon 的统一内存架构
  - 支持 LLaMA、Mistral、Phi-3、精选 Qwen 模型
  - LoRA 微调与模型定制
  - 与 Hugging Face 集成，支持 4-bit/8-bit 量化

---

### [模块 05：SLMOps - 小型语言模型运维](./Module05/README.md)
**主题**：从蒸馏到生产部署的完整 SLM 生命周期运维

#### 章节结构：
- [**第 1 节：SLMOps 简介**](./Module05/01.IntroduceSLMOps.md)
  - SLMOps 在 AI 运维中的范式转变
  - 成本效益与隐私优先架构
  - 战略性商业影响与竞争优势
  - 真实实施中的挑战与解决方案

- [**第 2 节：模型蒸馏——从理论到实践**](./Module05/02.SLMOps-Distillation.md)
  - 从教师模型到学生模型的知识转移
  - 两阶段蒸馏过程实施
  - Azure ML 蒸馏工作流与实践示例
  - 推理时间减少 85%，准确率保持 92%

- [**第 3 节：微调——为特定任务定制模型**](./Module05/03.SLMOps-Finetuing.md)
  - 参数高效微调（PEFT）技术
  - LoRA 和 QLoRA 高级方法
  - Microsoft Olive 微调实施
  - 多适配器训练与超参数优化

- [**第 4 节：部署——生产就绪实施**](./Module05/04.SLMOps.Deployment.md)
  - 面向生产的模型转换与量化
  - Foundry Local 部署配置
  - 性能基准测试与质量验证
  - 减少 75% 的模型大小并进行生产监控

---

### [模块 06：SLM Agentic 系统——AI 代理与函数调用](./Module06/README.md)
**主题**：从基础到高级函数调用与模型上下文协议集成的 SLM Agentic 系统实施

#### 章节结构：
- [**第 1 节：AI 代理与小型语言模型基础**](./Module06/01.IntroduceAgent.md)  
- 智能体分类框架（反射型、基于模型、基于目标、学习型智能体）  
- SLM 基础知识与优化策略（GGUF、量化、边缘框架）  
- SLM 与 LLM 的权衡分析（成本降低 10-30 倍，任务有效性达 70-80%）  
- 使用 Ollama、VLLM 和 Microsoft 边缘解决方案的实际部署  

- [**第 2 节：小型语言模型中的函数调用**](./Module06/02.FunctionCalling.md)  
  - 系统化工作流实现（意图检测、JSON 输出、外部执行）  
  - 特定平台实现（Phi-4-mini、精选 Qwen 模型、Microsoft Foundry Local）  
  - 高级示例（多智能体协作、动态工具选择）  
  - 生产环境注意事项（速率限制、审计日志、安全措施）  

- [**第 3 节：模型上下文协议（MCP）集成**](./Module06/03.IntroduceMCP.md)  
  - 协议架构与分层系统设计  
  - 多后端支持（开发使用 Ollama，生产使用 vLLM）  
  - 连接协议（STDIO 和 SSE 模式）  
  - 实际应用（网页自动化、数据处理、API 集成）  

---

### [模块 07：EdgeAI 实现示例](./Module07/README.md)  
**主题**：跨多种平台和框架的全面 EdgeAI 实现  

#### 章节结构：  
- [**NVIDIA Jetson Orin Nano 的 EdgeAI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)  
  - 信用卡大小的设备中实现 67 TOPS 的 AI 性能  
  - 支持生成式 AI 模型（视觉变换器、LLM、视觉语言模型）  
  - 应用于机器人、无人机、智能摄像头、自主设备  
  - 价格仅 $249 的平台，推动 AI 开发普及化  

- [**使用 .NET MAUI 和 ONNX Runtime GenAI 的移动应用 EdgeAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)  
  - 单一 C# 代码库实现跨平台移动 AI  
  - 硬件加速支持（CPU、GPU、移动 AI 处理器）  
  - 特定平台优化（iOS 的 CoreML，Android 的 NNAPI）  
  - 完整的生成式 AI 循环实现  

- [**在 Azure 中使用小型语言模型引擎的 EdgeAI**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)  
  - 云-边缘混合部署架构  
  - Azure AI 服务与 ONNX Runtime 集成  
  - 企业级部署与持续模型管理  
  - 智能文档处理的混合 AI 工作流  

- [**使用 Windows ML 的 EdgeAI**](./Module07/README.md#4-edgeai-with-windows-ml)  
  - 基于 Windows AI Foundry 的高性能设备端推理  
  - 通用硬件支持（AMD、Intel、NVIDIA、Qualcomm 芯片）  
  - 自动硬件抽象与优化  
  - 适用于多样化 Windows 硬件生态系统的统一框架  

- [**使用 Foundry Local 应用的 EdgeAI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)  
  - 注重隐私的 RAG 实现，利用本地资源  
  - 集成 Phi-3 语言模型与语义搜索（仅限 Phi 模型）  
  - 支持本地向量数据库（SQLite、Qdrant）  
  - 数据主权与离线操作能力  

## 学习成果概览  

### 模块 01 学习成果：  
- 理解云端与边缘 AI 架构的基本差异  
- 掌握边缘部署的核心优化技术  
- 识别实际应用与成功案例  
- 获得实施 EdgeAI 解决方案的实践技能  

### 模块 02 学习成果：  
- 深入理解不同 SLM 设计理念及其部署影响  
- 掌握基于计算约束和性能需求的战略决策能力  
- 理解部署灵活性的权衡  
- 拥有面向未来的高效 AI 架构洞察力  

### 模块 03 学习成果：  
- 战略性模型选择能力  
- 优化技术掌握  
- 部署灵活性掌握  
- 生产就绪配置能力  

### 模块 04 学习成果：  
- 深入理解量化边界及实际应用  
- 掌握多种优化框架的实践经验（Llama.cpp、Olive、MLX）  
- 硬件感知的优化选择能力  
- 跨平台边缘计算环境的生产部署技能  

### 模块 05 学习成果：  
- 掌握 SLMOps 范式与操作原则  
- 实现模型蒸馏以进行知识转移和效率优化  
- 应用微调技术进行领域特定模型定制  
- 部署生产就绪的 SLM 解决方案，并制定监控与维护策略  

### 模块 06 学习成果：  
- 理解 AI 智能体和小型语言模型架构的基础概念  
- 掌握跨多个平台和框架的函数调用实现  
- 集成模型上下文协议（MCP），实现标准化的外部工具交互  
- 构建复杂的智能体系统，最大限度减少人工干预需求  

### 模块 07 学习成果：  
- 获得多样化 EdgeAI 平台和实现策略的实践经验  
- 掌握 NVIDIA、移动设备、Azure 和 Windows 平台的硬件特定优化技术  
- 理解性能、成本和隐私需求之间的部署权衡  
- 开发跨不同生态系统的实际 EdgeAI 应用的实践技能  

## 文件结构树形图  

```
edgeai-for-beginners/
├── imgs/
│   └── cover.png
├── Module01/ (EdgeAI Fundamentals and Transformation)
│   ├── 01.EdgeAIFundamentals.md
│   ├── 02.RealWorldCaseStudies.md
│   ├── 03.PracticalImplementationGuide.md
│   ├── 04.EdgeDeployment.md
│   └── README.md
├── Module02/ (Small Language Model Foundations)
│   ├── 01.PhiFamily.md
│   ├── 02.QwenFamily.md
│   ├── 03.GemmaFamily.md
│   ├── 04.BitNETFamily.md
│   ├── 05.mumodel.md
│   ├── 06.phisilica.md
│   └── README.md
├── Module03/ (SLM Deployment Practice)
│   ├── 01.SLMAdvancedLearning.md
│   ├── 02.DeployingSLMinLocalEnv.md
│   ├── 03.DeployingSLMinCloud.md
│   └── README.md
├── Module04/ (Model Format Conversion and Quantization)
│   ├── 01.Introduce.md
│   ├── 02.Llamacpp.md
│   ├── 03.MicrosoftOlive.md
│   ├── 04.AppleMLX.md
│   └── README.md
├── Module05/ (SLMOps - Small Language Model Operations)
│   ├── 01.IntroduceSLMOps.md
│   ├── 02.SLMOps-Distillation.md
│   ├── 03.SLMOps-Finetuing.md
│   ├── 04.SLMOps.Deployment.md
│   └── README.md
├── Module06/ (SLM Agentic Systems)
│   ├── 01.IntroduceAgent.md
│   ├── 02.FunctionCalling.md
│   ├── 03.IntroduceMCP.md
│   └── README.md
├── Module07/ (EdgeAI Implementation Samples)
│   └── README.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md (This file)
├── SECURITY.md
├── STUDY_GUIDE.md
└── SUPPORT.md
```  

## 课程特色  

- **渐进式学习**：从基础概念逐步深入到高级部署  
- **理论与实践结合**：每个模块包含理论基础和实际操作  
- **真实案例研究**：基于 Microsoft、阿里巴巴、Google 等实际案例  
- **动手实践**：完整的配置文件、API 测试流程和部署脚本  
- **性能基准**：详细比较推理速度、内存使用和资源需求  
- **企业级考量**：安全实践、合规框架和数据保护策略  

## 入门指南  

推荐学习路径：  
1. 从 **模块 01** 开始，建立 EdgeAI 的基础理解  
2. 继续学习 **模块 02**，深入了解各种 SLM 模型家族  
3. 学习 **模块 03**，掌握实际部署技能  
4. 继续学习 **模块 04**，了解高级模型优化和格式转换  
5. 完成 **模块 05**，掌握 SLMOps 的生产就绪实现  
6. 探索 **模块 06**，理解 SLM 智能体系统和函数调用能力  
7. 最后学习 **模块 07**，获得多样化 EdgeAI 实现示例的实践经验  

每个模块都设计为独立完整，但按顺序学习效果最佳。  

## 学习指南  

一份全面的 [学习指南](STUDY_GUIDE.md) 可帮助您最大化学习体验。学习指南提供：  

- **结构化学习路径**：优化的时间表，20 小时完成课程  
- **时间分配建议**：具体建议，平衡阅读、练习和项目  
- **关键概念聚焦**：每个模块的优先学习目标  
- **自我评估工具**：测试理解的题目和练习  
- **小型项目创意**：强化学习的实际应用  

学习指南适合密集学习（1 周）和兼职学习（3 周），即使您只能投入 10 小时，也有明确的时间分配建议。  

---

**EdgeAI 的未来在于持续改进模型架构、量化技术和部署策略，优先考虑效率和专业化，而非通用能力。拥抱这一范式转变的组织将能够充分利用 AI 的变革潜力，同时保持对数据和运营的控制。**  

## 其他课程  

我们的团队还制作了其他课程！查看以下内容：  

- [MCP 初学者教程](https://github.com/microsoft/mcp-for-beginners)  
- [AI 智能体初学者教程](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [使用 .NET 的生成式 AI 初学者教程](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
- [使用 JavaScript 的生成式 AI 初学者教程](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)  
- [生成式 AI 初学者教程](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [机器学习初学者教程](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
- [数据科学初学者教程](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
- [AI 初学者教程](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
- [网络安全初学者教程](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)  
- [Web 开发初学者教程](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
- [物联网初学者教程](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
- [XR 开发初学者教程](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [掌握 GitHub Copilot 的 AI 配对编程](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
- [掌握 GitHub Copilot 的 C#/.NET 开发](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
- [选择你的 Copilot 冒险](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。