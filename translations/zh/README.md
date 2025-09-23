<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a189d7d9d47816a518ca119d79dc19b",
  "translation_date": "2025-09-22T11:24:57+00:00",
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

[阿拉伯语](../ar/README.md) | [孟加拉语](../bn/README.md) | [保加利亚语](../bg/README.md) | [缅甸语](../my/README.md) | [中文（简体）](./README.md) | [中文（繁体，香港）](../hk/README.md) | [中文（繁体，澳门）](../mo/README.md) | [中文（繁体，台湾）](../tw/README.md) | [克罗地亚语](../hr/README.md) | [捷克语](../cs/README.md) | [丹麦语](../da/README.md) | [荷兰语](../nl/README.md) | [芬兰语](../fi/README.md) | [法语](../fr/README.md) | [德语](../de/README.md) | [希腊语](../el/README.md) | [希伯来语](../he/README.md) | [印地语](../hi/README.md) | [匈牙利语](../hu/README.md) | [印尼语](../id/README.md) | [意大利语](../it/README.md) | [日语](../ja/README.md) | [韩语](../ko/README.md) | [马来语](../ms/README.md) | [马拉地语](../mr/README.md) | [尼泊尔语](../ne/README.md) | [挪威语](../no/README.md) | [波斯语（法尔西语）](../fa/README.md) | [波兰语](../pl/README.md) | [葡萄牙语（巴西）](../br/README.md) | [葡萄牙语（葡萄牙）](../pt/README.md) | [旁遮普语（古木基文）](../pa/README.md) | [罗马尼亚语](../ro/README.md) | [俄语](../ru/README.md) | [塞尔维亚语（西里尔文）](../sr/README.md) | [斯洛伐克语](../sk/README.md) | [斯洛文尼亚语](../sl/README.md) | [西班牙语](../es/README.md) | [斯瓦希里语](../sw/README.md) | [瑞典语](../sv/README.md) | [他加禄语（菲律宾语）](../tl/README.md) | [泰语](../th/README.md) | [土耳其语](../tr/README.md) | [乌克兰语](../uk/README.md) | [乌尔都语](../ur/README.md) | [越南语](../vi/README.md)

**如果您希望支持其他语言，支持的语言列表请参考[这里](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## 课程简介

欢迎来到 **EdgeAI 初学者指南**——一场全面探索边缘人工智能（Edge AI）变革世界的旅程。本课程将强大的 AI 能力与实际应用部署相结合，帮助您在数据生成和决策发生的地方直接利用 AI 的潜力。

### 您将掌握的内容

本课程从基础概念到生产级实现，涵盖以下内容：
- **小型语言模型（SLMs）**，优化用于边缘部署
- **硬件感知优化**，适配多种平台
- **实时推理**，兼顾隐私保护
- **生产部署策略**，面向企业应用

### 为什么边缘 AI 很重要

边缘 AI 是一种解决现代关键问题的范式转变：
- **隐私与安全**：本地处理敏感数据，无需上传云端
- **实时性能**：消除网络延迟，适用于时间敏感的应用
- **成本效益**：降低带宽和云计算成本
- **高可靠性**：网络中断时仍能保持功能
- **合规性**：满足数据主权要求

### 什么是边缘 AI

边缘 AI 是指在本地硬件上运行 AI 算法和语言模型——靠近数据生成的地方——无需依赖云资源进行推理。它减少了延迟，增强了隐私，并支持实时决策。

### 核心原则：
- **设备端推理**：AI 模型运行在边缘设备上（如手机、路由器、微控制器、工业 PC）
- **离线能力**：无需持续的互联网连接即可运行
- **低延迟**：即时响应，适合实时系统
- **数据主权**：本地保存敏感数据，提高安全性和合规性

### 小型语言模型（SLMs）

像 Phi-4、Mistral-7B 和 Gemma 这样的 SLM 是大型语言模型（LLMs）的优化版本，通过训练或蒸馏实现：
- **内存占用更小**：高效利用边缘设备有限的内存
- **计算需求更低**：优化 CPU 和边缘 GPU 的性能
- **启动速度更快**：快速初始化，适应响应式应用

它们在以下场景中释放强大的自然语言处理能力，同时满足资源限制：
- **嵌入式系统**：物联网设备和工业控制器
- **移动设备**：支持离线功能的智能手机和平板电脑
- **物联网设备**：资源有限的传感器和智能设备
- **边缘服务器**：具有有限 GPU 资源的本地处理单元
- **个人电脑**：桌面和笔记本部署场景

## 课程架构

### [模块 01：边缘 AI 基础与变革](./Module01/README.md)
**主题**：边缘 AI 部署的变革性转变

#### 章节结构：
- [**第 1 节：边缘 AI 基础**](./Module01/01.EdgeAIFundamentals.md)
  - 传统云 AI 与边缘 AI 的对比
  - 边缘计算的挑战与限制
  - 关键技术：模型量化、压缩优化、小型语言模型（SLMs）
  - 硬件加速：NPU、GPU 优化、CPU 优化
  - 优势：隐私安全、低延迟、离线能力、成本效益

- [**第 2 节：真实案例研究**](./Module01/02.RealWorldCaseStudies.md)
  - Microsoft Phi 和 Mu 模型生态系统
  - 日本航空 AI 报告系统案例研究
  - 市场影响与未来方向
  - 部署注意事项与最佳实践

- [**第 3 节：实践实施指南**](./Module01/03.PracticalImplementationGuide.md)
  - 开发环境设置（Python 3.10+，.NET 8+）
  - 硬件需求与推荐配置
  - 核心模型家族资源
  - 量化与优化工具（Llama.cpp、Microsoft Olive、Apple MLX）
  - 评估与验证清单

- [**第 4 节：边缘 AI 部署硬件平台**](./Module01/04.EdgeDeployment.md)
  - 边缘 AI 部署的注意事项与要求
  - Intel 边缘 AI 硬件与优化技术
  - Qualcomm 移动与嵌入式系统 AI 解决方案
  - NVIDIA Jetson 与边缘计算平台
  - Windows AI PC 平台与 NPU 加速
  - 硬件特定优化策略

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
  - 内置于 Windows 11 的设备优先架构
  - 与 Windows 11 设置的系统集成
  - 隐私保护的离线操作

- [**第 6 节：Phi-Silica 基础**](./Module02/06.phisilica.md)
  - 内置于 Windows 11 Copilot+ PC 的 NPU 优化架构
  - 卓越效率（650 tokens/second，功耗仅 1.5W）
  - 与 Windows App SDK 的开发者集成

---

### [模块 03：小型语言模型部署](./Module03/README.md)
**主题**：从理论到生产环境的完整 SLM 生命周期部署

#### 章节结构：
- [**第 1 节：SLM 高级学习**](./Module03/01.SLMAdvancedLearning.md)
  - 参数分类框架（微型 SLM 100M-1.4B，中型 SLM 14B-30B）
  - 高级优化技术（量化方法、BitNET 1-bit 量化）
  - 模型获取策略（Azure AI Foundry 获取 Phi 模型，Hugging Face 获取精选模型）

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
- [**第2节：Llama.cpp 实现指南**](./Module04/02.Llamacpp.md)
  - 跨平台安装（Windows、macOS、Linux）
  - GGUF格式转换及量化级别（Q2_K到Q8_0）
  - 硬件加速（CUDA、Metal、OpenCL、Vulkan）
  - Python集成及REST API部署

- [**第3节：Microsoft Olive 优化套件**](./Module04/03.MicrosoftOlive.md)
  - 基于硬件的模型优化，包含40+内置组件
  - 动态和静态量化的自动优化
  - 与Azure ML工作流的企业级集成
  - 支持热门模型（Llama、Phi、部分Qwen模型、Gemma）

- [**第4节：OpenVINO工具包优化套件**](./Module04/04.openvino.md)
  - Intel开源工具包，用于跨平台AI部署
  - 神经网络压缩框架（NNCF）实现高级优化
  - OpenVINO GenAI用于大语言模型部署
  - 支持CPU、GPU、VPU及AI加速器的硬件加速

- [**第5节：Apple MLX框架深度解析**](./Module04/05.AppleMLX.md)
  - Apple Silicon的统一内存架构
  - 支持LLaMA、Mistral、Phi及部分Qwen模型
  - LoRA微调及模型定制化
  - 与Hugging Face集成，支持4位/8位量化

- [**第6节：边缘AI开发工作流综合**](./Module04/06.workflow-synthesis.md)
  - 集成多种优化框架的统一工作流架构
  - 框架选择决策树及性能权衡分析
  - 生产就绪验证及全面部署策略
  - 针对新兴硬件和模型架构的未来规划策略

---

### [模块05：SLMOps - 小型语言模型操作](./Module05/README.md)
**主题**：从模型蒸馏到生产部署的完整SLM生命周期操作

#### 章节结构：
- [**第1节：SLMOps简介**](./Module05/01.IntroduceSLMOps.md)
  - SLMOps在AI操作中的范式转变
  - 成本效率及隐私优先架构
  - 战略性业务影响及竞争优势
  - 实际实施中的挑战及解决方案

- [**第2节：模型蒸馏——从理论到实践**](./Module05/02.SLMOps-Distillation.md)
  - 从教师模型到学生模型的知识转移
  - 两阶段蒸馏过程的实施
  - Azure ML蒸馏工作流及实际案例
  - 推理时间减少85%，准确率保留92%

- [**第3节：微调——为特定任务定制模型**](./Module05/03.SLMOps-Finetuing.md)
  - 参数高效微调（PEFT）技术
  - LoRA及QLoRA高级方法
  - Microsoft Olive微调实施
  - 多适配器训练及超参数优化

- [**第4节：部署——生产就绪实施**](./Module05/04.SLMOps.Deployment.md)
  - 模型转换及量化以适应生产需求
  - Foundry Local部署配置
  - 性能基准测试及质量验证
  - 实现75%模型大小缩减及生产监控

---

### [模块06：SLM智能系统——AI代理及函数调用](./Module06/README.md)
**主题**：从基础到高级函数调用及模型上下文协议集成的SLM智能系统实施

#### 章节结构：
- [**第1节：AI代理及小型语言模型基础**](./Module06/01.IntroduceAgent.md)
  - 代理分类框架（反射型、基于模型、目标导向型、学习型代理）
  - SLM基础及优化策略（GGUF、量化、边缘框架）
  - SLM与LLM的权衡分析（成本降低10-30倍，任务有效性70-80%）
  - 使用Ollama、VLLM及Microsoft边缘解决方案的实际部署

- [**第2节：小型语言模型中的函数调用**](./Module06/02.FunctionCalling.md)
  - 系统化工作流实施（意图检测、JSON输出、外部执行）
  - 平台特定实现（Phi-4-mini、部分Qwen模型、Microsoft Foundry Local）
  - 高级示例（多代理协作、动态工具选择）
  - 生产考虑（速率限制、审计日志、安全措施）

- [**第3节：模型上下文协议（MCP）集成**](./Module06/03.IntroduceMCP.md)
  - 协议架构及分层系统设计
  - 多后端支持（开发用Ollama，生产用vLLM）
  - 连接协议（STDIO及SSE模式）
  - 实际应用（网页自动化、数据处理、API集成）

---

### [模块07：边缘AI实施示例](./Module07/README.md)
**主题**：跨多平台及框架的全面边缘AI实施

#### 章节结构：
- [**Visual Studio Code的AI工具包**](./Module07/aitoolkit.md)
  - 在VS Code中构建全面的边缘AI开发环境
  - 模型目录及边缘部署发现
  - 本地测试、优化及代理开发工作流
  - 边缘场景的性能监控及评估

- [**Windows边缘AI开发指南**](./Module07/windowdeveloper.md)
  - Windows AI Foundry平台全面概述
  - Phi Silica API实现高效NPU推理
  - 计算机视觉API用于图像处理及OCR
  - Foundry Local CLI用于本地开发及测试

- [**NVIDIA Jetson Orin Nano上的边缘AI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 信用卡大小的设备实现67 TOPS AI性能
  - 支持生成式AI模型（视觉变换器、LLM、视觉语言模型）
  - 应用于机器人、无人机、智能摄像头、自动化设备
  - 经济实惠的$249平台，推动AI开发普及化

- [**使用.NET MAUI和ONNX Runtime GenAI的移动应用边缘AI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - 单一C#代码库实现跨平台移动AI
  - 硬件加速支持（CPU、GPU、移动AI处理器）
  - 平台特定优化（iOS的CoreML，Android的NNAPI）
  - 完整的生成式AI循环实施

- [**Azure中的边缘AI与小型语言模型引擎**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - 云-边缘混合部署架构
  - Azure AI服务与ONNX Runtime集成
  - 企业级部署及持续模型管理
  - 智能文档处理的混合AI工作流

- [**使用Windows ML的边缘AI**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Windows AI Foundry基础实现高效设备端推理
  - 通用硬件支持（AMD、Intel、NVIDIA、Qualcomm芯片）
  - 自动硬件抽象及优化
  - 适用于多样化Windows硬件生态系统的统一框架

- [**使用Foundry Local应用的边缘AI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - 隐私优先的RAG实施，利用本地资源
  - Phi-4语言模型与语义搜索集成（仅支持Phi模型）
  - 支持本地向量数据库（SQLite、Qdrant）
  - 数据主权及离线操作能力

### [模块08：Microsoft Foundry Local——完整开发工具包](./Module08/README.md)
**主题**：使用Foundry Local构建、运行及集成AI；通过Azure AI Foundry实现扩展及混合化

#### 章节结构：
- [**1：Foundry Local入门**](./Module08/01.FoundryLocalSetup.md)
- [**2：使用Azure AI Foundry构建AI解决方案**](./Module08/02.AzureAIFoundryIntegration.md)
- [**3：开源模型Foundry Local**](./Module08/03.OpenSourceModels.md)
- [**4：尖端模型及设备端推理**](./Module08/04.CuttingEdgeModels.md)
- [**5：使用Foundry Local的AI驱动代理**](./Module08/05.AIPoweredAgents.md)
- [**6：模型作为工具**](./Module08/06.ModelsAsTools.md)

## 课程学习目标

通过完成这门全面的边缘AI课程，您将掌握设计、实施及部署生产就绪边缘AI解决方案的专业技能。我们的结构化方法确保您既能掌握理论基础，又能熟练应用实践技能。

### 技术能力

**基础知识**
- 理解云端与边缘AI架构的基本差异
- 掌握模型量化、压缩及优化的原则，适用于资源受限环境
- 理解硬件加速选项（NPUs、GPUs、CPUs）及其部署影响

**实施技能**
- 在多样化边缘平台（移动设备、嵌入式设备、物联网、边缘服务器）上部署小型语言模型
- 应用优化框架，包括Llama.cpp、Microsoft Olive、ONNX Runtime及Apple MLX
- 实现具有亚秒级响应要求的实时推理系统

**生产专业知识**
- 设计可扩展的边缘AI架构，用于企业应用
- 实施已部署系统的监控、维护及更新策略
- 应用隐私保护边缘AI实施的安全最佳实践

### 战略能力

**决策框架**
- 评估边缘AI机会并识别适合的业务应用场景
- 权衡模型准确性、推理速度、功耗及硬件成本之间的取舍
- 根据具体部署限制选择合适的SLM系列及配置

**系统架构**
- 设计端到端边缘AI解决方案，与现有基础设施集成
- 规划混合边缘-云架构，以实现最佳性能及成本效率
- 实施实时AI应用的数据流及处理管道

### 行业应用

**实际部署场景**
- **制造业**：质量控制系统、预测性维护及流程优化
- **医疗**：隐私保护诊断工具及患者监测系统
- **交通**：自动驾驶决策及交通管理
- **智慧城市**：智能基础设施及资源管理系统
- **消费电子**：AI驱动的移动应用及智能家居设备

## 学习成果概览

### 模块01学习成果：
- 理解云端与边缘AI架构的基本差异
- 掌握边缘部署的核心优化技术
- 识别实际应用及成功案例
- 获得实施边缘AI解决方案的实践技能

### 模块02学习成果：
- 深刻理解不同SLM设计理念及其部署影响
- 掌握基于计算约束及性能需求的战略决策能力
- 理解部署灵活性的权衡
- 拥有面向未来的高效AI架构洞察力

### 模块03学习成果：
- 战略性模型选择能力
- 优化技术掌握
- 部署灵活性掌握
- 生产就绪配置能力

### 模块04学习成果：
- 深刻理解量化边界及实际应用
- 掌握多种优化框架的实践经验（Llama.cpp、Olive、OpenVINO、MLX）
- 精通使用OpenVINO及NNCF进行Intel硬件优化
- 在多样化平台上选择硬件感知优化的能力
- 跨平台边缘计算环境的生产部署技能
- 针对最佳边缘AI解决方案的战略框架选择及工作流综合能力

### 模块05学习成果：
- 掌握SLMOps范式及操作原则
- 实施模型蒸馏以实现知识转移及效率优化
- 应用微调技术进行领域特定模型定制
- 部署生产就绪的SLM解决方案，并实施监控及维护策略

### 模块06学习成果：
- 理解AI代理及小型语言模型架构的基础概念
- 掌握跨多个平台及框架的函数调用实施
- 集成模型上下文协议（MCP），实现标准化外部工具交互
- 构建复杂的智能系统，减少人工干预需求

### 模块07学习成果：
- 掌握Visual Studio Code的AI工具包，用于全面的边缘AI开发工作流
- 熟悉Windows AI Foundry平台及NPU优化策略
- 获得多样化边缘AI平台及实施策略的实践经验
- 掌握针对NVIDIA、移动设备、Azure及Windows平台的硬件特定优化技术
- 理解性能、成本及隐私需求之间的部署权衡
- 开发跨不同生态系统的实际边缘AI应用的实践技能

## 预期课程成果

成功完成本课程后，您将具备知识、技能及信心，在专业环境中领导边缘AI项目。

### 职业准备

**技术领导力**
- **解决方案架构**：设计满足企业需求的全面边缘AI系统
- **性能优化**：在准确性、速度及资源消耗之间实现最佳平衡
- **跨平台部署**：在Windows、Linux、移动及嵌入式平台上实施解决方案
- **生产操作**：维护及扩展具有企业级可靠性的边缘AI系统

**行业专业知识**
- **技术评估**：评估并推荐适合特定业务挑战的边缘AI解决方案
- **实施规划**：为边缘AI项目制定现实的时间表及资源需求
- **风险管理**：识别并减轻EdgeAI部署中的技术和运营风险  
- **投资回报优化**：展示EdgeAI实施带来的可量化业务价值  

### 职业发展机会  

**专业角色**  
- EdgeAI解决方案架构师  
- 机器学习工程师（Edge方向）  
- IoT AI开发者  
- 移动AI应用开发者  
- 企业AI顾问  

**行业领域**  
- 智能制造与工业4.0  
- 自动驾驶与交通运输  
- 医疗科技与医疗设备  
- 金融科技与安全  
- 消费电子与移动应用  

### 认证与验证  

**作品集开发**  
- 完成端到端的EdgeAI项目，展示实际能力  
- 在多个硬件平台上部署生产级解决方案  
- 记录优化策略及实现的性能提升  

**持续学习路径**  
- 为高级AI专业方向打下基础  
- 为云-边混合架构做好准备  
- 通向新兴AI技术与框架的入口  

本课程将您定位于AI技术部署的前沿，智能功能将无缝集成到驱动现代生活的设备和系统中。  

## 文件结构树图  

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
│   ├── 04.openvino.md
│   ├── 05.AppleMLX.md
│   ├── 06.workflow-synthesis.md
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
│   ├── aitoolkit.md
│   ├── windowdeveloper.md
│   └── README.md
├── Module08/ (Hands on with Foundry Local)
│   ├── 01.FoundryLocalSetup.md
│   ├── 02.AzureAIFoundryIntegration.md
│   ├── 03.OpenSourceModels.md
│   ├── 04.CuttingEdgeModels.md
│   ├── 05.AIPoweredAgents.md
│   ├── 06.ModelsAsTools.md
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
- **真实案例研究**：基于微软、阿里巴巴、谷歌等实际案例  
- **动手实践**：完成配置文件、API测试流程和部署脚本  
- **性能基准**：详细比较推理速度、内存使用和资源需求  
- **企业级考量**：安全实践、合规框架和数据保护策略  

## 入门指南  

推荐学习路径：  
1. 从**Module01**开始，建立EdgeAI的基础理解  
2. 进入**Module02**，深入了解各种SLM模型家族  
3. 学习**Module03**，掌握实际部署技能  
4. 继续**Module04**，学习高级模型优化、格式转换和框架整合  
5. 完成**Module05**，掌握SLMOps以实现生产级部署  
6. 探索**Module06**，了解SLM代理系统和函数调用能力  
7. 完成**Module07**，获得AI工具包和多样化EdgeAI实施样例的实践经验  
8. 探索**Module08**，全面了解Foundry Local开发工具包（以本地为主的开发与混合Azure集成）  

每个模块都设计为独立完整，但按顺序学习将获得最佳效果。  

## 学习指南  

一份全面的[学习指南](STUDY_GUIDE.md)可帮助您最大化学习体验。学习指南提供：  

- **结构化学习路径**：优化的课程完成时间表（20小时）  
- **时间分配建议**：针对阅读、练习和项目的具体建议  
- **关键概念重点**：每个模块的优先学习目标  
- **自我评估工具**：测试理解的题目和练习  
- **迷你项目创意**：强化学习的实际应用  

学习指南适合密集学习（1周）和兼职学习（3周），即使您只能投入10小时，也有明确的时间分配建议。  

---

**EdgeAI的未来在于持续改进模型架构、量化技术和部署策略，优先考虑效率和专业化而非通用能力。拥抱这一范式转变的组织将能够充分利用AI的变革潜力，同时保持对数据和运营的控制。**  

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

