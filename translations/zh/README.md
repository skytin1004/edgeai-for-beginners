<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e73444e4fc8f1931ac3979dbd7785e2",
  "translation_date": "2025-09-15T16:35:10+00:00",
  "source_file": "README.md",
  "language_code": "zh"
}
-->
# 初学者的边缘AI课程

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

[法语](../fr/README.md) | [西班牙语](../es/README.md) | [中文（简体）](./README.md) | [中文（繁体，澳门）](../mo/README.md) | [中文（繁体，香港）](../hk/README.md) | [中文（繁体，台湾）](../tw/README.md) | [日语](../ja/README.md) | [韩语](../ko/README.md)  
**如果您希望支持其他语言，支持的语言列表请参见 [这里](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## 课程简介

欢迎来到 **边缘AI初学者课程**——这是您探索边缘人工智能变革世界的全面旅程。本课程将强大的AI能力与实际的边缘设备部署相结合，使您能够直接在数据生成和决策发生的地方释放AI的潜力。

### 您将掌握的内容

本课程从基础概念到生产级实现，涵盖以下内容：
- **小型语言模型（SLMs）**，优化用于边缘部署  
- **硬件优化**，适用于多种平台  
- **实时推理**，具备隐私保护功能  
- **生产部署**，面向企业应用的策略  

### 为什么边缘AI很重要

边缘AI代表了一种解决现代关键问题的范式转变：
- **隐私与安全**：在本地处理敏感数据，无需上传到云端  
- **实时性能**：消除网络延迟，适用于时间敏感的应用  
- **成本效益**：减少带宽和云计算开销  
- **可靠性**：在网络中断时仍能保持功能  
- **法规遵从**：满足数据主权要求  

### 边缘AI

边缘AI指的是在硬件本地运行AI算法和语言模型——靠近数据生成的地方——无需依赖云资源进行推理。它减少了延迟，增强了隐私，并支持实时决策。

### 核心原则：
- **设备端推理**：AI模型在边缘设备（手机、路由器、微控制器、工业PC）上运行  
- **离线能力**：无需持续的互联网连接即可运行  
- **低延迟**：适用于实时系统的即时响应  
- **数据主权**：将敏感数据保留在本地，提高安全性和合规性  

### 小型语言模型（SLMs）

SLMs，如 Phi-4、Mistral-7B 和 Gemma，是经过优化的较大语言模型版本——通过训练或蒸馏实现：
- **减少内存占用**：高效利用边缘设备有限的内存  
- **降低计算需求**：优化CPU和边缘GPU性能  
- **更快的启动时间**：快速初始化，适用于响应式应用  

它们在以下场景中释放强大的自然语言处理能力，同时满足约束条件：
- **嵌入式系统**：物联网设备和工业控制器  
- **移动设备**：具备离线能力的智能手机和平板电脑  
- **物联网设备**：资源有限的传感器和智能设备  
- **边缘服务器**：具有有限GPU资源的本地处理单元  
- **个人电脑**：桌面和笔记本电脑的部署场景  

## 课程架构

### [模块 01：边缘AI基础与变革](./Module01/README.md)  
**主题**：边缘AI部署的变革性转变  

#### 章节结构：
- [**第1节：边缘AI基础**](./Module01/01.EdgeAIFundamentals.md)  
  - 传统云AI与边缘AI的比较  
  - 边缘计算的挑战与限制  
  - 关键技术：模型量化、压缩优化、小型语言模型（SLMs）  
  - 硬件加速：NPU、GPU优化、CPU优化  
  - 优势：隐私安全、低延迟、离线能力、成本效益  

- [**第2节：真实案例研究**](./Module01/02.RealWorldCaseStudies.md)  
  - Microsoft Phi 和 Mu 模型生态系统  
  - 日本航空AI报告系统案例研究  
  - 市场影响与未来方向  
  - 部署考虑与最佳实践  

- [**第3节：实践实施指南**](./Module01/03.PracticalImplementationGuide.md)  
  - 开发环境设置（Python 3.10+，.NET 8+）  
  - 硬件要求与推荐配置  
  - 核心模型家族资源  
  - 量化与优化工具（Llama.cpp、Microsoft Olive、Apple MLX）  
  - 评估与验证清单  

- [**第4节：边缘AI部署硬件平台**](./Module01/04.EdgeDeployment.md)  
  - 边缘AI部署的考虑与要求  
  - Intel 边缘AI硬件与优化技术  
  - Qualcomm 移动与嵌入式系统AI解决方案  
  - NVIDIA Jetson 和边缘计算平台  
  - Windows AI PC平台与NPU加速  
  - 硬件特定的优化策略  

---

### [模块 02：小型语言模型基础](./Module02/README.md)  
**主题**：SLM理论原理、实施策略与生产部署  

#### 章节结构：
- [**第1节：Microsoft Phi 模型家族基础**](./Module02/01.PhiFamily.md)  
  - 设计理念演变（Phi-1到Phi-4）  
  - 以效率为先的架构设计  
  - 专业能力（推理、多模态、边缘部署）  

- [**第2节：Qwen 模型家族基础**](./Module02/02.QwenFamily.md)  
  - 开源卓越（Qwen 1.0到Qwen3）——可通过 Hugging Face 获取  
  - 先进的推理架构与思维模式能力  
  - 可扩展部署选项（0.5B-235B 参数）  

- [**第3节：Gemma 模型家族基础**](./Module02/03.GemmaFamily.md)  
  - 以研究为驱动的创新（Gemma 3 和 3n）  
  - 多模态卓越  
  - 移动优先架构  

- [**第4节：BitNET 模型家族基础**](./Module02/04.BitNETFamily.md)  
  - 革命性的量化技术（1.58-bit）  
  - 专用推理框架：https://github.com/microsoft/BitNet  
  - 通过极高效率实现可持续AI领导力  

- [**第5节：Microsoft Mu 模型基础**](./Module02/05.mumodel.md)  
  - 设备优先架构，内置于 Windows 11  
  - 与 Windows 11 设置的系统集成  
  - 隐私保护的离线操作  

- [**第6节：Phi-Silica 基础**](./Module02/06.phisilica.md)  
  - 为 Windows 11 Copilot+ PC 优化的 NPU 架构  
  - 卓越效率（650 tokens/second，功耗仅 1.5W）  
  - 开发者可通过 Windows App SDK 集成  

---

### [模块 03：小型语言模型部署](./Module03/README.md)  
**主题**：从理论到生产环境的完整SLM生命周期部署  

#### 章节结构：
- [**第1节：SLM高级学习**](./Module03/01.SLMAdvancedLearning.md)  
  - 参数分类框架（微型SLM 100M-1.4B，中型SLM 14B-30B）  
  - 高级优化技术（量化方法，BitNET 1-bit量化）  
  - 模型获取策略（Azure AI Foundry 提供 Phi 模型，Hugging Face 提供选定模型）  

- [**第2节：本地环境部署**](./Module03/02.DeployingSLMinLocalEnv.md)  
  - Ollama 通用平台部署  
  - Microsoft Foundry 本地企业级解决方案  
  - 框架对比分析  

- [**第3节：容器化云部署**](./Module03/03.DeployingSLMinCloud.md)  
  - vLLM 高性能推理部署  
  - Ollama 容器编排  
  - ONNX Runtime 边缘优化实现  

---

### [模块 04：模型格式转换与量化](./Module04/README.md)  
**主题**：跨平台边缘部署的完整模型优化工具包  

#### 章节结构：
- [**第1节：模型格式转换与量化基础**](./Module04/01.Introduce.md)  
  - 精度分类框架（超低、低、中精度）  
  - GGUF 和 ONNX 格式的优势与使用场景  
  - 量化对操作效率的好处  
  - 性能基准与内存占用比较  

- [**第2节：Llama.cpp 实施指南**](./Module04/02.Llamacpp.md)  
  - 跨平台安装（Windows、macOS、Linux）  
  - GGUF 格式转换与量化级别（Q2_K到Q8_0）  
  - 硬件加速（CUDA、Metal、OpenCL、Vulkan）  
  - Python 集成与 REST API 部署  

- [**第3节：Microsoft Olive 优化套件**](./Module04/03.MicrosoftOlive.md)  
  - 硬件感知模型优化，内置40+组件  
  - 动态与静态量化的自动优化  
  - 与 Azure ML 工作流的企业集成  
  - 支持的流行模型（Llama、Phi、选定的 Qwen 模型、Gemma）  

- [**第4节：OpenVINO 工具包优化套件**](./Module04/04.openvino.md)  
  - Intel 的开源工具包，用于跨平台AI部署  
  - 神经网络压缩框架（NNCF）实现高级优化  
  - OpenVINO GenAI 用于大语言模型部署  
  - 硬件加速覆盖 CPU、GPU、VPU 和 AI 加速器  

- [**第5节：Apple MLX 框架深度解析**](./Module04/05.AppleMLX.md)  
  - Apple Silicon 的统一内存架构  
  - 支持 LLaMA、Mistral、Phi-3、选定的 Qwen 模型  
  - LoRA 微调与模型定制  
  - 与 Hugging Face 集成，支持4-bit/8-bit量化  

- [**第6节：边缘AI开发工作流综合**](./Module04/06.workflow-synthesis.md)  
  - 综合工作流架构，整合多种优化框架  
  - 框架选择决策树与性能权衡分析  
  - 生产准备验证与全面部署策略  
  - 面向新兴硬件与模型架构的未来保障策略  

---

### [模块 05：SLMOps - 小型语言模型操作](./Module05/README.md)  
**主题**：从蒸馏到生产部署的完整SLM生命周期操作  

#### 章节结构：
- [**第1节：SLMOps简介**](./Module05/01.IntroduceSLMOps.md)  
  - SLMOps 在AI操作中的范式转变  
  - 成本效益与隐私优先架构  
  - 战略业务影响与竞争优势  
  - 真实世界实施的挑战与解决方案  
- [**第2节：模型蒸馏 - 从理论到实践**](./Module05/02.SLMOps-Distillation.md)
  - 从教师模型向学生模型的知识传递
  - 两阶段蒸馏过程的实现
  - Azure ML蒸馏工作流及实际案例
  - 推理时间减少85%，准确率保持92%

- [**第3节：微调 - 为特定任务定制模型**](./Module05/03.SLMOps-Finetuing.md)
  - 参数高效微调（PEFT）技术
  - LoRA和QLoRA高级方法
  - Microsoft Olive微调实现
  - 多适配器训练和超参数优化

- [**第4节：部署 - 面向生产的实现**](./Module05/04.SLMOps.Deployment.md)
  - 模型转换和量化以适应生产环境
  - Foundry Local部署配置
  - 性能基准测试和质量验证
  - 减少75%模型大小并进行生产监控

---

### [模块06：SLM代理系统 - AI代理与函数调用](./Module06/README.md)
**主题**：从基础到高级函数调用及模型上下文协议（MCP）集成的SLM代理系统实现

#### 章节结构：
- [**第1节：AI代理与小型语言模型基础**](./Module06/01.IntroduceAgent.md)
  - 代理分类框架（反射型、基于模型、基于目标、学习型代理）
  - SLM基础知识及优化策略（GGUF、量化、边缘框架）
  - SLM与LLM的权衡分析（成本降低10-30倍，任务有效性70-80%）
  - 使用Ollama、VLLM和Microsoft边缘解决方案进行实际部署

- [**第2节：小型语言模型中的函数调用**](./Module06/02.FunctionCalling.md)
  - 系统化工作流实现（意图检测、JSON输出、外部执行）
  - 平台特定实现（Phi-4-mini、选定的Qwen模型、Microsoft Foundry Local）
  - 高级案例（多代理协作、动态工具选择）
  - 生产环境注意事项（速率限制、审计日志、安全措施）

- [**第3节：模型上下文协议（MCP）集成**](./Module06/03.IntroduceMCP.md)
  - 协议架构及分层系统设计
  - 多后端支持（开发使用Ollama，生产使用vLLM）
  - 连接协议（STDIO和SSE模式）
  - 实际应用案例（网页自动化、数据处理、API集成）

---

### [模块07：EdgeAI实现样例](./Module07/README.md)
**主题**：跨多平台和框架的全面EdgeAI实现

#### 章节结构：
- [**Visual Studio Code的AI工具包**](./Module07/aitoolkit.md)
  - 在VS Code中构建全面的Edge AI开发环境
  - 模型目录及边缘部署发现
  - 本地测试、优化及代理开发工作流
  - 边缘场景的性能监控与评估

- [**Windows EdgeAI开发指南**](./Module07/windowdeveloper.md)
  - Windows AI Foundry平台全面概述
  - Phi Silica API用于高效NPU推理
  - 计算机视觉API用于图像处理和OCR
  - Foundry Local CLI用于本地开发和测试

- [**NVIDIA Jetson Orin Nano上的EdgeAI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 信用卡大小设备上的67 TOPS AI性能
  - 支持生成式AI模型（视觉变换器、LLM、视觉语言模型）
  - 应用于机器人、无人机、智能摄像头、自动化设备
  - 经济实惠的$249平台，推动AI开发普及化

- [**使用.NET MAUI和ONNX Runtime GenAI的移动应用EdgeAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - 单一C#代码库实现跨平台移动AI
  - 硬件加速支持（CPU、GPU、移动AI处理器）
  - 平台特定优化（iOS的CoreML，Android的NNAPI）
  - 完整的生成式AI循环实现

- [**Azure中的EdgeAI与小型语言模型引擎**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - 云-边缘混合部署架构
  - Azure AI服务与ONNX Runtime集成
  - 企业级部署及持续模型管理
  - 智能文档处理的混合AI工作流

- [**使用Windows ML的EdgeAI**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Windows AI Foundry基础，用于高效的设备端推理
  - 通用硬件支持（AMD、Intel、NVIDIA、Qualcomm芯片）
  - 自动硬件抽象和优化
  - 适用于多样化Windows硬件生态系统的统一框架

- [**使用Foundry Local应用的EdgeAI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - 注重隐私的RAG实现，使用本地资源
  - Phi-3语言模型与语义搜索集成（仅支持Phi模型）
  - 本地向量数据库支持（SQLite、Qdrant）
  - 数据主权及离线操作能力

## 课程学习目标

通过完成这门全面的EdgeAI课程，您将掌握设计、实现和部署生产级EdgeAI解决方案的专业技能。我们的结构化方法确保您既掌握理论基础，又具备实践操作能力。

### 技术能力

**基础知识**
- 理解基于云和基于边缘的AI架构的基本差异
- 掌握模型量化、压缩和优化的原则，以适应资源受限环境
- 理解硬件加速选项（NPU、GPU、CPU）及其部署影响

**实施技能**
- 在多样化的边缘平台（移动设备、嵌入式设备、物联网、边缘服务器）上部署小型语言模型
- 应用优化框架，包括Llama.cpp、Microsoft Olive、ONNX Runtime和Apple MLX
- 实现具有亚秒级响应要求的实时推理系统

**生产能力**
- 设计可扩展的EdgeAI架构以适应企业应用
- 实施已部署系统的监控、维护和更新策略
- 应用隐私保护EdgeAI实现的安全最佳实践

### 战略能力

**决策框架**
- 评估EdgeAI机会并识别适合的业务应用场景
- 权衡模型准确性、推理速度、功耗和硬件成本之间的取舍
- 根据具体部署限制选择合适的SLM系列和配置

**系统架构**
- 设计与现有基础设施集成的端到端EdgeAI解决方案
- 规划混合边缘-云架构以实现最佳性能和成本效率
- 实现实时AI应用的数据流和处理管道

### 行业应用

**实际部署场景**
- **制造业**：质量控制系统、预测性维护和流程优化
- **医疗**：隐私保护诊断工具和患者监控系统
- **交通**：自动驾驶决策和交通管理
- **智慧城市**：智能基础设施和资源管理系统
- **消费电子**：AI驱动的移动应用和智能家居设备

## 学习成果概览

### 模块01学习成果：
- 理解云AI架构与边缘AI架构的基本差异
- 掌握边缘部署的核心优化技术
- 识别实际应用案例和成功故事
- 获得实施EdgeAI解决方案的实践技能

### 模块02学习成果：
- 深刻理解不同SLM设计理念及其部署影响
- 掌握基于计算约束和性能需求的战略决策能力
- 理解部署灵活性权衡
- 拥有面向未来的高效AI架构洞察力

### 模块03学习成果：
- 战略模型选择能力
- 优化技术掌握
- 部署灵活性掌握
- 生产级配置能力

### 模块04学习成果：
- 深刻理解量化边界及实际应用
- 掌握多种优化框架的实际操作（Llama.cpp、Olive、OpenVINO、MLX）
- 精通使用OpenVINO和NNCF进行Intel硬件优化
- 跨多平台选择硬件感知优化的能力
- 生产部署技能，适用于跨平台边缘计算环境
- 战略框架选择及工作流综合能力，以实现最佳EdgeAI解决方案

### 模块05学习成果：
- 掌握SLMOps范式及操作原则
- 实现模型蒸馏以进行知识传递和效率优化
- 应用微调技术进行领域特定模型定制
- 部署生产级SLM解决方案并实施监控和维护策略

### 模块06学习成果：
- 理解AI代理和小型语言模型架构的基础概念
- 掌握跨多个平台和框架的函数调用实现
- 集成模型上下文协议（MCP），实现标准化的外部工具交互
- 构建复杂的代理系统，减少人工干预需求

### 模块07学习成果：
- 掌握Visual Studio Code的AI工具包，用于全面的Edge AI开发工作流
- 熟悉Windows AI Foundry平台及NPU优化策略
- 获得多样化EdgeAI平台和实现策略的实际操作经验
- 掌握针对NVIDIA、移动设备、Azure和Windows平台的硬件特定优化技术
- 理解性能、成本和隐私要求之间的部署权衡
- 开发跨不同生态系统的实际EdgeAI应用技能

## 预期课程成果

成功完成本课程后，您将具备知识、技能和信心，在专业环境中领导EdgeAI项目。

### 职业准备

**技术领导力**
- **解决方案架构**：设计满足企业需求的全面EdgeAI系统
- **性能优化**：在准确性、速度和资源消耗之间实现最佳平衡
- **跨平台部署**：在Windows、Linux、移动设备和嵌入式平台上实施解决方案
- **生产运营**：维护和扩展具有企业级可靠性的EdgeAI系统

**行业专业知识**
- **技术评估**：评估并推荐适合特定业务挑战的EdgeAI解决方案
- **实施规划**：为EdgeAI项目制定现实的时间表和资源需求
- **风险管理**：识别并减轻EdgeAI部署中的技术和运营风险
- **ROI优化**：展示EdgeAI实施带来的可衡量业务价值

### 职业发展机会

**专业角色**
- EdgeAI解决方案架构师
- 机器学习工程师（边缘方向）
- 物联网AI开发者
- 移动AI应用开发者
- 企业AI顾问

**行业领域**
- 智能制造与工业4.0
- 自动驾驶与交通运输
- 医疗技术与医疗设备
- 金融科技与安全
- 消费电子与移动应用

### 认证与验证

**作品集开发**
- 完成端到端EdgeAI项目，展示实际能力
- 在多个硬件平台上部署生产级解决方案
- 记录优化策略及实现的性能提升

**持续学习路径**
- 为高级AI专业化奠定基础
- 为云-边缘混合架构做好准备
- 为新兴AI技术和框架提供入门途径

本课程将您定位于AI技术部署的前沿，将智能能力无缝集成到现代生活所依赖的设备和系统中。

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
- **真实案例研究**：基于Microsoft、阿里巴巴、Google等实际案例
- **动手实践**：完整的配置文件、API测试流程和部署脚本
- **性能基准**：详细比较推理速度、内存使用和资源需求
- **企业级考虑**：安全实践、合规框架和数据保护策略

## 入门指南

推荐学习路径：
1. 从**模块01**开始，建立EdgeAI的基础理解
2. 继续学习**模块02**，深入了解各种SLM模型系列
3. 学习**模块03**，掌握实际部署技能
4. 学习**模块04**，了解高级模型优化、格式转换和框架综合
5. 完成**模块05**，掌握SLMOps以实现生产级部署
6. 探索**模块06**，理解SLM代理系统和函数调用能力
7. 最后完成**模块07**，获得AI工具包和多样化EdgeAI实现样例的实践经验

每个模块都设计为独立完整，但按顺序学习将获得最佳效果。

## 学习指南

一份全面的[学习指南](STUDY_GUIDE.md)可帮助您最大化学习体验。学习指南提供：

- **结构化学习路径**：优化的时间表，20小时内完成课程
- **时间分配建议**：具体推荐如何平衡阅读、练习和项目
- **关键概念重点**：每个模块的优先学习目标
- **自我评估工具**：测试理解的题目和练习
- **迷你项目创意**：强化学习的实际应用

学习指南适合密集学习（1周）和兼职学习（3周），即使您只能投入10小时，也有明确的时间分配建议。

---
**EdgeAI的未来在于持续改进模型架构、量化技术以及部署策略，这些策略优先考虑效率和专业化，而非通用能力。那些能够接受这一范式转变的组织，将能够充分利用人工智能的变革潜力，同时保持对其数据和运营的掌控。**

## 其他课程

我们的团队还制作了其他课程！查看以下内容：

- [MCP入门课程](https://github.com/microsoft/mcp-for-beginners)
- [AI代理入门课程](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [使用.NET的生成式AI入门课程](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [使用JavaScript的生成式AI入门课程](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [生成式AI入门课程](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [机器学习入门课程](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [数据科学入门课程](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [人工智能入门课程](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [网络安全入门课程](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [Web开发入门课程](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [物联网入门课程](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [XR开发入门课程](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [掌握GitHub Copilot进行AI配对编程](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [掌握GitHub Copilot为C#/.NET开发者服务](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [选择你的Copilot冒险之旅](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。