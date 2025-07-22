<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "64a53ca0c6f9d7f6d3620adfd1dd1e6e",
  "translation_date": "2025-07-22T02:41:39+00:00",
  "source_file": "README.md",
  "language_code": "zh"
}
-->
# 初学者的边缘AI课程

通过三个全面模块——边缘AI基础、小型语言模型基础和实用部署策略，深入学习边缘AI技术。本课程从基本概念到高级实现，涵盖真实案例研究、动手练习和部署示例，展示如何在边缘设备上直接运行AI模型，以增强隐私、降低延迟和提高效率。

![课程封面图片](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.zh.png)

## 课程架构

### [模块01：边缘AI基础与转型](./Module01/README.md)
**主题**：边缘AI部署的变革性转变

#### 章节结构：
- [**第1节：边缘AI基础**](./Module01/01.EdgeAIFundamentals.md)
  - 传统云AI与边缘AI的比较
  - 边缘计算的挑战与限制
  - 核心技术：模型量化、压缩优化、小型语言模型（SLM）
  - 硬件加速：NPU、GPU优化、CPU优化
  - 优势：隐私安全、低延迟、离线能力、成本效率

- [**第2节：真实案例研究**](./Module01/02.RealWorldCaseStudies.md)
  - Microsoft Phi & Mu模型生态系统
    - Phi Silica：Windows AI集成
    - Mu模型：任务专用微型语言模型
  - 日本航空AI报告系统案例研究
  - 市场影响与未来方向
  - 部署考虑与最佳实践

- [**第3节：实用实施指南**](./Module01/03.PracticalImplementationGuide.md)
  - 开发环境设置（Python 3.10+，.NET 8+）
  - 硬件要求与推荐配置
  - 核心模型家族资源
  - 量化与优化工具（Llama.cpp、Microsoft Olive、Apple MLX）
  - 评估与验证清单

- [**第4节：边缘AI部署硬件平台**](./Module01/04.EdgeDeployment.md)
  - 边缘AI部署的考虑与要求
  - Intel边缘AI硬件与优化技术
  - Qualcomm移动与嵌入式系统AI解决方案
  - NVIDIA Jetson与边缘计算平台
  - Windows AI PC平台与NPU加速
  - 硬件特定优化策略

---

### [模块02：小型语言模型基础](./Module02/README.md)
**主题**：SLM理论原理、实施策略与生产部署

#### 章节结构：
- [**第1节：Microsoft Phi模型家族基础**](./Module02/01.PhiFamily.md)
  - 设计理念演变（Phi-1到Phi-4）
  - 以效率为先的架构设计
  - 专业能力（推理、多模态、边缘部署）

- [**第2节：Qwen模型家族基础**](./Module02/02.QwenFamily.md)
  - 开源卓越（Qwen 1.0到Qwen3）——可通过Hugging Face获取
  - 先进的推理架构与思维模式能力
  - 可扩展部署选项（0.5B-235B参数）

- [**第3节：Gemma模型家族基础**](./Module02/03.GemmaFamily.md)
  - 以研究为驱动的创新（Gemma 3 & 3n）
  - 多模态卓越
  - 移动优先架构

- [**第4节：BitNET模型家族基础**](./Module02/04.BitNETFamily.md)
  - 革命性的量化技术（1.58-bit）
  - 专用推理框架：https://github.com/microsoft/BitNet
  - 通过极高效率实现可持续AI领导力

- [**第5节：Microsoft Mu模型基础**](./Module02/05.mumodel.md)
  - 设备优先架构，内置于Windows 11
  - 与Windows 11设置的系统集成
  - 隐私保护的离线操作

- [**第6节：Phi-Silica基础**](./Module02/06.phisilica.md)
  - 针对NPU优化的架构，内置于Windows 11 Copilot+ PC
  - 卓越效率（650 tokens/second，功耗1.5W）
  - 开发者集成与Windows App SDK

---

### [模块03：小型语言模型部署](./Module03/README.md)
**主题**：完整的SLM生命周期部署，从理论到生产环境

#### 章节结构：
- [**第1节：SLM高级学习**](./Module03/01.SLMAdvancedLearning.md)
  - 参数分类框架（微型SLM 100M-1.4B，中型SLM 14B-30B）
  - 高级优化技术（量化方法、BitNET 1-bit量化）
  - 模型获取策略（Azure AI Foundry获取Phi模型，Hugging Face获取选定模型）

- [**第2节：本地环境部署**](./Module03/02.DeployingSLMinLocalEnv.md)
  - Ollama通用平台部署
  - Microsoft Foundry本地企业级解决方案
  - 框架比较分析

- [**第3节：容器化云部署**](./Module03/03.DeployingSLMinCloud.md)
  - vLLM高性能推理部署
  - Ollama容器编排
  - ONNX Runtime边缘优化实现

---

### [模块04：模型格式转换与量化](./Module04/README.md)
**主题**：跨平台边缘部署的完整模型优化工具包

#### 章节结构：
- [**第1节：模型格式转换与量化基础**](./Module04/01.Introduce.md)
  - 精度分类框架（超低、低、中精度）
  - GGUF与ONNX格式的优势与使用场景
  - 量化对操作效率的益处
  - 性能基准与内存占用比较

- [**第2节：Llama.cpp实施指南**](./Module04/02.Llamacpp.md)
  - 跨平台安装（Windows、macOS、Linux）
  - GGUF格式转换与量化级别（Q2_K到Q8_0）
  - 硬件加速（CUDA、Metal、OpenCL、Vulkan）
  - Python集成与REST API部署

- [**第3节：Microsoft Olive优化套件**](./Module04/03.MicrosoftOlive.md)
  - 硬件感知模型优化，内置40+组件
  - 动态与静态量化的自动优化
  - 与Azure ML工作流的企业集成
  - 支持的流行模型（Llama、Phi、选定Qwen模型、Gemma）

- [**第4节：Apple MLX框架深度解析**](./Module04/04.AppleMLX.md)
  - Apple Silicon的统一内存架构
  - 支持LLaMA、Mistral、Phi-3、选定Qwen模型
  - LoRA微调与模型定制
  - Hugging Face集成，支持4-bit/8-bit量化

---

### [模块05：SLMOps - 小型语言模型操作](./Module05/README.md)
**主题**：从蒸馏到生产部署的完整SLM生命周期操作

#### 章节结构：
- [**第1节：SLMOps简介**](./Module05/01.IntroduceSLMOps.md)
  - SLMOps在AI操作中的范式转变
  - 成本效率与隐私优先架构
  - 战略业务影响与竞争优势
  - 真实实施中的挑战与解决方案

- [**第2节：模型蒸馏——从理论到实践**](./Module05/02.SLMOps-Distillation.md)
  - 从教师模型到学生模型的知识转移
  - 两阶段蒸馏过程实施
  - Azure ML蒸馏工作流与实际示例
  - 推理时间减少85%，准确率保留92%

- [**第3节：微调——为特定任务定制模型**](./Module05/03.SLMOps-Finetuing.md)
  - 参数高效微调（PEFT）技术
  - LoRA与QLoRA高级方法
  - Microsoft Olive微调实施
  - 多适配器训练与超参数优化

- [**第4节：部署——生产就绪实施**](./Module05/04.SLMOps.Deployment.md)
  - 模型转换与量化以适应生产
  - Foundry Local部署配置
  - 性能基准测试与质量验证
  - 减少75%模型大小并进行生产监控

---

### [模块06：SLM代理系统——AI代理与函数调用](./Module06/README.md)
**主题**：从基础到高级函数调用与模型上下文协议集成的SLM代理系统实施

#### 章节结构：
- [**第1节：AI代理与小型语言模型基础**](./Module06/01.IntroduceAgent.md)
  - 代理分类框架（反射型、基于模型、基于目标、学习型代理）
  - SLM基础与优化策略（GGUF、量化、边缘框架）
  - SLM与LLM的权衡分析（成本减少10-30倍，任务有效性70-80%）
  - 实际部署（Ollama、VLLM、Microsoft边缘解决方案）

- [**第2节：小型语言模型中的函数调用**](./Module06/02.FunctionCalling.md)
  - 系统化工作流实施（意图检测、JSON输出、外部执行）
  - 平台特定实施（Phi-4-mini、选定Qwen模型、Microsoft Foundry Local）
  - 高级示例（多代理协作、动态工具选择）
  - 生产考虑（速率限制、审计日志、安全措施）

- [**第3节：模型上下文协议（MCP）集成**](./Module06/03.IntroduceMCP.md)
  - 协议架构与分层系统设计
  - 多后端支持（Ollama用于开发，vLLM用于生产）
  - 连接协议（STDIO与SSE模式）
  - 真实应用（网页自动化、数据处理、API集成）

---

### [模块07：边缘AI实施示例](./Module07/README.md)
**主题**：跨多平台与框架的全面边缘AI实施

#### 章节结构：
- [**NVIDIA Jetson Orin Nano上的边缘AI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 信用卡大小的设备提供67 TOPS AI性能
  - 支持生成式AI模型（视觉变换器、LLM、视觉语言模型）
  - 应用于机器人、无人机、智能摄像头、自动化设备
  - 价格实惠的$249平台，推动AI开发普及

- [**使用.NET MAUI和ONNX Runtime GenAI的移动应用边缘AI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - 单一C#代码库实现跨平台移动AI
  - 硬件加速支持（CPU、GPU、移动AI处理器）
  - 平台特定优化（iOS的CoreML，Android的NNAPI）
  - 完整的生成式AI循环实施

- [**Azure中的边缘AI与小型语言模型引擎**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - 云-边缘混合部署架构
  - Azure AI服务与ONNX Runtime集成
  - 企业级部署与持续模型管理
  - 智能文档处理的混合AI工作流

- [**Windows ML上的边缘AI**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Windows AI Foundry为设备上的高性能推理提供基础
  - 通用硬件支持（AMD、Intel、NVIDIA、Qualcomm芯片）
  - 自动硬件抽象与优化
  - 为多样化Windows硬件生态系统提供统一框架

- [**Foundry Local应用中的边缘AI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - 隐私优先的RAG实施，使用本地资源
  - Phi-3语言模型与语义搜索集成（仅支持Phi模型）
  - 本地向量数据库支持（SQLite、Qdrant）
  - 数据主权与离线操作能力

## 学习成果概览

### 模块01学习成果：
- 理解云AI与边缘AI架构的基本差异
- 掌握边缘部署的核心优化技术
- 识别真实应用与成功案例
- 获得实施边缘AI解决方案的实用技能

### 模块02学习成果：
- 深入理解不同SLM设计理念及其部署影响
- 掌握基于计算约束与性能需求的战略决策能力
- 理解部署灵活性的权衡
- 拥有面向未来的高效AI架构洞察力

### 模块03学习成果：
- 战略模型选择能力
- 优化技术掌握
- 部署灵活性掌握
- 生产就绪配置能力

### 模块04学习成果：
- 深入理解量化边界与实际应用
- 掌握多种优化框架的实践经验（Llama.cpp、Olive、MLX）
- 硬件感知优化选择能力
- 跨平台边缘计算环境的生产部署技能

### 模块05学习成果：
- 掌握SLMOps范式与操作原则
- 实施模型蒸馏以实现知识转移与效率优化
- 应用微调技术进行领域特定模型定制
- 部署生产就绪的SLM解决方案，并制定监控与维护策略
### 第六模块学习成果：
- 理解AI代理和小型语言模型架构的基础概念  
- 掌握跨多个平台和框架的函数调用实现  
- 集成模型上下文协议（MCP），实现标准化的外部工具交互  
- 构建复杂的代理系统，减少对人工干预的需求  

### 第七模块学习成果：
- 获得多种EdgeAI平台和实施策略的实践经验  
- 掌握针对硬件的优化技术，包括NVIDIA、移动设备、Azure和Windows平台  
- 理解性能、成本和隐私需求之间的部署权衡  
- 开发构建不同生态系统中真实EdgeAI应用的实用技能  

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

## 课程特点

- **渐进式学习**：从基础概念逐步深入到高级部署  
- **理论与实践结合**：每个模块包含理论基础和实际操作  
- **真实案例研究**：基于微软、阿里巴巴、谷歌等公司的实际案例  
- **动手实践**：完整的配置文件、API测试流程和部署脚本  
- **性能基准**：详细比较推理速度、内存使用和资源需求  
- **企业级考量**：安全实践、合规框架和数据保护策略  

## 入门指南

推荐学习路径：  
1. 从 **Module01** 开始，建立EdgeAI的基础理解  
2. 继续学习 **Module02**，深入了解各种SLM模型家族  
3. 学习 **Module03**，掌握实际部署技能  
4. 学习 **Module04**，进行高级模型优化和格式转换  
5. 完成 **Module05**，掌握生产级SLMOps实施能力  
6. 探索 **Module06**，理解SLM代理系统和函数调用功能  
7. 最后学习 **Module07**，获得多样化EdgeAI实施样例的实践经验  

每个模块都设计为独立完整，但按顺序学习效果最佳。  

## 学习指南

一份全面的[学习指南](STUDY_GUIDE.md)可帮助您最大化学习体验。学习指南提供：  

- **结构化学习路径**：优化的课程完成时间表（20小时）  
- **时间分配建议**：针对阅读、练习和项目的具体推荐  
- **关键概念聚焦**：每个模块的优先学习目标  
- **自我评估工具**：测试理解的题目和练习  
- **迷你项目创意**：强化学习的实际应用  

学习指南适合密集学习（1周）和兼职学习（3周），即使您只能投入10小时，也有明确的时间分配建议。  

---

**EdgeAI的未来在于持续改进模型架构、量化技术和部署策略，优先考虑效率和专业化而非通用能力。拥抱这一范式转变的组织将能够充分利用AI的变革潜力，同时保持对数据和运营的控制。**

## 其他课程

我们的团队还制作了其他课程！查看以下内容：  

- [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners)  
- [AI Agents For Beginners](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
- [Generative AI for Beginners using JavaScript](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)  
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [ML for Beginners](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
- [Data Science for Beginners](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
- [AI for Beginners](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)  
- [Web Dev for Beginners](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
- [IoT for Beginners](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
- [XR Development for Beginners](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [Mastering GitHub Copilot for AI Paired Programming](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
- [Mastering GitHub Copilot for C#/.NET Developers](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
- [Choose Your Own Copilot Adventure](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言版本的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。