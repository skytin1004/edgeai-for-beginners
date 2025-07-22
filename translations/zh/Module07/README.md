<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f921854683b0ba903972831f6e61c28f",
  "translation_date": "2025-07-22T05:22:30+00:00",
  "source_file": "Module07/README.md",
  "language_code": "zh"
}
-->
# 第七章：EdgeAI 示例

Edge AI 是人工智能与边缘计算的结合，使得设备能够直接进行智能处理，而无需依赖云端连接。本章将探讨五种不同平台和框架上的 EdgeAI 实现，展示在边缘运行 AI 模型的多样性和强大功能。

## 1. NVIDIA Jetson Orin Nano 的 EdgeAI

NVIDIA Jetson Orin Nano 是边缘 AI 计算领域的一次突破，提供高达 67 TOPS 的 AI 性能，体积仅有信用卡大小。这款强大的边缘 AI 平台让生成式 AI 的开发变得更加普及，无论是爱好者、学生还是专业开发者都能轻松使用。

### 主要特点
- 提供高达 67 TOPS 的 AI 性能，比前代产品提升 1.7 倍
- 配备 1024 个 CUDA 核心和最多 32 个 Tensor 核心，用于 AI 处理
- 6 核 Arm Cortex-A78AE v8.2 64 位 CPU，最高频率 1.5 GHz
- 售价仅 $249，为开发者、学生和创客提供最实惠且易用的平台

### 应用场景
Jetson Orin Nano 擅长运行现代生成式 AI 模型，包括视觉变换器、大型语言模型和视觉-语言模型。它专为生成式 AI（GenAI）用例设计，现在可以在掌上设备上运行多个 LLM。常见应用包括 AI 驱动的机器人、智能无人机、智能摄像头和自主边缘设备。

**了解更多**：[NVIDIA 的 Jetson Orin Nano 超级计算机：EdgeAI 的下一次飞跃](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. 使用 .NET MAUI 和 ONNX Runtime GenAI 的移动应用 EdgeAI

该解决方案展示了如何使用 .NET MAUI（多平台应用 UI）和 ONNX Runtime GenAI 将生成式 AI 和大型语言模型（LLMs）集成到跨平台移动应用中。这种方法使 .NET 开发者能够构建运行于 Android 和 iOS 设备上的复杂 AI 驱动移动应用。

### 主要特点
- 基于 .NET MAUI 框架，提供单一代码库支持 Android 和 iOS 应用
- 集成 ONNX Runtime GenAI，可直接在移动设备上运行生成式 AI 模型
- 支持多种针对移动设备的硬件加速器，包括 CPU、GPU 和专用移动 AI 处理器
- 通过 ONNX Runtime 实现平台特定优化，例如 iOS 的 CoreML 和 Android 的 NNAPI
- 实现完整的生成式 AI 流程，包括预处理和后处理、推理、logits 处理、搜索和采样以及 KV 缓存管理

### 开发优势
使用 .NET MAUI 方法，开发者可以利用现有的 C# 和 .NET 技能构建跨平台 AI 应用。ONNX Runtime GenAI 框架支持多种模型架构，包括 Llama、Mistral、Phi、Gemma 等。优化的 ARM64 内核加速了 INT4 量化矩阵乘法，确保在移动硬件上高效运行，同时保持熟悉的 .NET 开发体验。

### 应用场景
该解决方案非常适合希望使用 .NET 技术构建 AI 驱动移动应用的开发者，包括智能聊天机器人、图像识别应用、语言翻译工具和个性化推荐系统，这些应用完全在设备上运行，增强了隐私性和离线能力。

**了解更多**：[.NET MAUI ONNX Runtime GenAI 示例](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. Azure 中的小型语言模型引擎 EdgeAI

微软基于 Azure 的 EdgeAI 解决方案专注于在云-边缘混合环境中高效部署小型语言模型（SLMs）。这种方法弥合了云规模 AI 服务与边缘部署需求之间的差距。

### 架构优势
- 与 Azure AI 服务无缝集成
- 使用 ONNX Runtime 在设备和云端运行 SLMs/LLMs 以及多模态模型
- 针对企业级部署进行了优化
- 支持持续的模型更新和管理

### 应用场景
Azure EdgeAI 实现非常适合需要企业级 AI 部署和云管理能力的场景，包括智能文档处理、实时分析以及结合云和边缘计算资源的混合 AI 工作流。

**了解更多**：[Azure EdgeAI SLM 引擎](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. 使用 Windows ML 的 EdgeAI

Windows ML 是微软优化的运行时，专为高效的设备端模型推理和简化部署而设计，是 Windows AI Foundry 的基础。该平台使开发者能够创建利用 PC 硬件全能力的 AI 驱动 Windows 应用。

### 平台能力
- 适用于所有运行 Windows 11 版本 24H2（构建 26100）或更高版本的 PC
- 支持所有 x64 和 ARM64 PC 硬件，即使是没有 NPU 或 GPU 的 PC
- 开发者可以自带模型，并高效部署到包括 AMD、Intel、NVIDIA 和 Qualcomm 在内的硅片合作伙伴生态系统中，涵盖 CPU、GPU 和 NPU
- 借助基础设施 API，开发者无需为不同的硅片目标创建多个应用构建版本

### 开发者优势
Windows ML 抽象了硬件和执行提供程序，因此开发者可以专注于编写代码。此外，Windows ML 会自动更新以支持最新的 NPU、GPU 和 CPU。该平台为跨 Windows 硬件生态系统的 AI 开发提供了统一框架。

**了解更多**：[Windows ML 概述](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)

## 5. 使用 Foundry Local 应用的 EdgeAI

Foundry Local 使开发者能够使用本地资源在 .NET 中构建检索增强生成（RAG）应用，将本地语言模型与语义搜索功能结合。这种方法提供了完全基于本地基础设施运行的隐私保护 AI 解决方案。

### 技术架构
- 结合 Phi-3 语言模型、本地嵌入和语义内核，创建 RAG 场景
- 使用嵌入作为浮点值数组（向量），表示内容及其语义含义
- 语义内核作为主要协调器，集成 Phi-3 和智能组件，创建无缝的 RAG 管道
- 支持包括 SQLite 和 Qdrant 在内的本地向量数据库

### 实现优势
RAG（检索增强生成）实际上就是“查找一些内容并将其放入提示中”的一种方式。这种本地实现确保了数据隐私，同时提供基于自定义知识库的智能响应。该方法在需要数据主权和离线操作能力的企业场景中尤为有价值。

**了解更多**：[Foundry Local RAG 示例](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## 结论

这五种 EdgeAI 实现展示了当前边缘 AI 解决方案的成熟度和多样性。从像 Jetson Orin Nano 这样的硬件加速边缘设备，到像 ONNX Runtime GenAI 和 Windows ML 这样的软件框架，开发者拥有了前所未有的选择，可以在边缘部署智能应用。

这些平台的共同点在于 AI 能力的普及化，使得不同技能水平和用例的开发者都能轻松使用先进的机器学习技术。无论是构建移动应用、桌面软件还是嵌入式系统，这些 EdgeAI 解决方案为下一代高效且私密的边缘智能应用奠定了基础。

每个平台都有其独特优势：Jetson Orin Nano 专注于硬件加速边缘计算，ONNX Runtime GenAI 支持跨平台移动开发，Azure EdgeAI 提供企业级云-边缘集成，Windows ML 面向 Windows 原生应用，Foundry Local 则专注于隐私保护的 RAG 实现。它们共同构成了一个全面的 EdgeAI 开发生态系统。

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文档的原始语言版本为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而引起的任何误解或误读不承担责任。