<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e9e31a2b5ff0f6a682a258fa859a8ff5",
  "translation_date": "2025-09-26T19:24:40+00:00",
  "source_file": "Module07/README.md",
  "language_code": "zh"
}
-->
# 第七章：EdgeAI 示例

边缘人工智能（Edge AI）是人工智能与边缘计算的结合，使设备能够直接进行智能处理，而无需依赖云连接。本章将探讨五种不同平台和框架上的EdgeAI实现，展示在边缘运行AI模型的多样性和强大功能。

## 1. NVIDIA Jetson Orin Nano上的EdgeAI

NVIDIA Jetson Orin Nano是边缘AI计算领域的一次突破，提供高达67 TOPS的AI性能，体积仅有信用卡大小。这款强大的边缘AI平台让生成式AI开发变得触手可及，无论是爱好者、学生还是专业开发者都能轻松使用。

### 主要特点
- 提供高达67 TOPS的AI性能，比前代产品提升1.7倍
- 配备1024个CUDA核心和最多32个Tensor核心用于AI处理
- 6核Arm Cortex-A78AE v8.2 64位CPU，最高频率1.5 GHz
- 售价仅为249美元，为开发者、学生和创客提供最实惠且易于使用的平台

### 应用场景
Jetson Orin Nano擅长运行现代生成式AI模型，包括视觉变换器、大型语言模型和视觉语言模型。它专为生成式AI（GenAI）用例设计，现在可以在掌上设备上运行多个LLM。常见应用包括AI驱动的机器人、智能无人机、智能摄像头和自主边缘设备。

**了解更多**：[NVIDIA的Jetson Orin Nano超级计算机：边缘AI的下一大趋势](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. 使用.NET MAUI和ONNX Runtime GenAI的移动应用EdgeAI

此解决方案展示了如何将生成式AI和大型语言模型（LLMs）集成到跨平台移动应用中，使用.NET MAUI（多平台应用UI）和ONNX Runtime GenAI。这种方法使.NET开发者能够构建在Android和iOS设备上原生运行的复杂AI驱动移动应用。

### 主要特点
- 基于.NET MAUI框架，提供单一代码库支持Android和iOS应用
- 集成ONNX Runtime GenAI，可直接在移动设备上运行生成式AI模型
- 支持针对移动设备的各种硬件加速器，包括CPU、GPU和专用移动AI处理器
- 通过ONNX Runtime实现平台特定优化，例如iOS的CoreML和Android的NNAPI
- 实现完整的生成式AI流程，包括预处理和后处理、推理、logits处理、搜索和采样以及KV缓存管理

### 开发优势
.NET MAUI方法允许开发者利用现有的C#和.NET技能，同时构建跨平台AI应用。ONNX Runtime GenAI框架支持多种模型架构，包括Llama、Mistral、Phi、Gemma等。优化的ARM64内核加速INT4量化矩阵乘法，确保在移动硬件上高效运行，同时保持熟悉的.NET开发体验。

### 应用场景
此解决方案非常适合希望使用.NET技术构建AI驱动移动应用的开发者，包括智能聊天机器人、图像识别应用、语言翻译工具以及完全在设备上运行的个性化推荐系统，增强隐私性和离线能力。

**了解更多**：[.NET MAUI ONNX Runtime GenAI 示例](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. 使用Azure的小型语言模型引擎的EdgeAI

微软基于Azure的EdgeAI解决方案专注于在云边混合环境中高效部署小型语言模型（SLMs）。这种方法弥合了云规模AI服务与边缘部署需求之间的差距。

### 架构优势
- 与Azure AI服务无缝集成
- 使用ONNX Runtime在设备和云端运行SLMs/LLMs以及多模态模型
- 针对企业级部署进行优化
- 支持持续的模型更新和管理

### 应用场景
Azure EdgeAI实现擅长需要企业级AI部署和云管理能力的场景，包括智能文档处理、实时分析以及结合云和边缘计算资源的混合AI工作流。

**了解更多**：[Azure EdgeAI SLM引擎](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. 使用Windows ML的EdgeAI](./windowdeveloper.md)

Windows ML是微软优化的运行时，专为高效的设备端模型推理和简化部署而设计，是Windows AI Foundry的基础。该平台使开发者能够创建利用PC硬件的AI驱动Windows应用。

### 平台能力
- 适用于所有运行版本24H2（构建26100）或更高版本的Windows 11 PC
- 适用于所有x64和ARM64 PC硬件，即使是没有NPU或GPU的PC
- 允许开发者使用自己的模型，并高效部署到包括AMD、Intel、NVIDIA和Qualcomm在内的硅合作伙伴生态系统，涵盖CPU、GPU、NPU
- 利用基础设施API，开发者无需为不同的硅目标创建多个应用构建版本

### 开发者优势
Windows ML抽象了硬件和执行提供者，因此开发者可以专注于编写代码。此外，Windows ML会自动更新以支持最新的NPU、GPU和CPU。该平台为跨Windows硬件生态系统的AI开发提供了统一框架。

**了解更多**：
- [Windows ML概述](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI开发指南](./windowdeveloper.md) - Windows Edge AI开发的全面指南

## [5. 使用Foundry Local应用的EdgeAI](./foundrylocal.md)

Foundry Local使Windows和Mac开发者能够使用本地资源在.NET中构建检索增强生成（RAG）应用，将本地语言模型与语义搜索功能相结合。这种方法提供了完全基于本地基础设施运行的隐私保护AI解决方案。

### 技术架构
- 结合Phi语言模型、本地嵌入和语义内核创建RAG场景
- 使用嵌入作为浮点值数组（向量），表示内容及其语义含义
- 语义内核作为主要协调器，集成Phi和智能组件以创建无缝的RAG管道
- 支持本地向量数据库，包括SQLite和Qdrant

### 实现优势
RAG，即检索增强生成，本质上是“查找一些内容并将其放入提示中”。这种本地实现确保数据隐私，同时提供基于自定义知识库的智能响应。该方法在需要数据主权和离线操作能力的企业场景中尤为有价值。

**了解更多**：
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG示例](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

微软Foundry Local提供了一个OpenAI兼容的REST服务器，由ONNX Runtime驱动，可在Windows本地运行模型。以下是快速验证的摘要；完整细节请参阅官方文档。

- 入门指南：https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- 架构概述：https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI参考：https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- 本仓库中的完整Windows指南：[foundrylocal.md](./foundrylocal.md)

在Windows上安装或升级（cmd.exe）：
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

探索CLI类别：
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

运行模型并发现动态端点：
```cmd
foundry model run gpt-oss-20b
foundry service status
```

快速REST检查列出模型（替换状态中的PORT）：
```cmd
curl -s http://localhost:PORT/v1/models
```

提示：
- SDK集成：https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- 使用自己的模型（编译）：https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI开发资源

针对专门面向Windows平台的开发者，我们创建了一份全面指南，涵盖完整的Windows EdgeAI生态系统。该资源提供了关于Windows AI Foundry的详细信息，包括API、工具和Windows EdgeAI开发的最佳实践。

### Windows AI Foundry平台
Windows AI Foundry平台提供了一整套专为Windows设备上的Edge AI开发设计的工具和API。这包括对NPU加速硬件的专门支持、Windows ML集成以及平台特定的优化技术。

**全面指南**：[Windows EdgeAI开发指南](../windowdeveloper.md)

本指南涵盖：
- Windows AI Foundry平台概述及组件
- Phi Silica API，用于NPU硬件上的高效推理
- 计算机视觉API，用于图像处理和OCR
- Windows ML运行时集成与优化
- Foundry Local CLI，用于本地开发和测试
- Windows设备的硬件优化策略
- 实际实施示例和最佳实践

### [Edge AI开发的AI工具包](./aitoolkit.md)
对于使用Visual Studio Code的开发者，AI工具包扩展提供了一个专门为构建、测试和部署Edge AI应用设计的全面开发环境。该工具包简化了整个Edge AI开发工作流。

**开发指南**：[Edge AI开发的AI工具包](./aitoolkit.md)

AI工具包指南涵盖：
- 边缘部署的模型发现与选择
- 本地测试与优化工作流
- ONNX和Ollama集成用于边缘模型
- 模型转换与量化技术
- 边缘场景的代理开发
- 性能评估与监控
- 部署准备与最佳实践

## 结论

这五种EdgeAI实现展示了当前边缘AI解决方案的成熟度和多样性。从像Jetson Orin Nano这样的硬件加速边缘设备到像ONNX Runtime GenAI和Windows ML这样的软件框架，开发者拥有了前所未有的选择，可以在边缘部署智能应用。

这些平台的共同点是AI能力的普及，使复杂的机器学习对不同技能水平和用例的开发者都变得触手可及。无论是构建移动应用、桌面软件还是嵌入式系统，这些EdgeAI解决方案都为下一代高效且隐私友好的边缘智能应用奠定了基础。

每个平台都有其独特优势：Jetson Orin Nano适用于硬件加速边缘计算，ONNX Runtime GenAI适用于跨平台移动开发，Azure EdgeAI适用于企业云边集成，Windows ML适用于Windows原生应用，Foundry Local适用于隐私保护的RAG实现。它们共同构成了一个全面的EdgeAI开发生态系统。

---

