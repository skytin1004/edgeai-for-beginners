<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e9e31a2b5ff0f6a682a258fa859a8ff5",
  "translation_date": "2025-09-26T19:20:16+00:00",
  "source_file": "Module07/README.md",
  "language_code": "en"
}
-->
# Chapter 07: EdgeAI Samples

Edge AI combines artificial intelligence with edge computing, enabling smart processing directly on devices without relying on cloud connectivity. This chapter showcases five distinct EdgeAI implementations across various platforms and frameworks, highlighting the flexibility and power of running AI models at the edge.

## 1. EdgeAI on NVIDIA Jetson Orin Nano

The NVIDIA Jetson Orin Nano is a groundbreaking edge AI computing platform, offering up to 67 TOPS of AI performance in a compact, credit-card-sized design. This powerful platform makes generative AI development accessible to hobbyists, students, and professional developers.

### Key Features
- Provides up to 67 TOPS of AI performance—a 1.7X improvement over its predecessor
- Features 1024 CUDA cores and up to 32 Tensor Cores for AI processing
- Includes a 6-core Arm Cortex-A78AE v8.2 64-bit CPU with a maximum frequency of 1.5 GHz
- Priced at $249, making it an affordable and accessible option for developers, students, and makers

### Applications
The Jetson Orin Nano is ideal for running modern generative AI models, such as vision transformers, large language models, and vision-language models. Designed for GenAI use cases, it enables running several LLMs on a palm-sized device. Common applications include AI-powered robotics, smart drones, intelligent cameras, and autonomous edge devices.

**Learn More**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI in Mobile Applications with .NET MAUI and ONNX Runtime GenAI

This solution demonstrates how to integrate Generative AI and Large Language Models (LLMs) into cross-platform mobile applications using .NET MAUI (Multi-platform App UI) and ONNX Runtime GenAI. It enables .NET developers to create advanced AI-powered mobile apps that run natively on Android and iOS devices.

### Key Features
- Built on the .NET MAUI framework, allowing a single codebase for both Android and iOS apps
- ONNX Runtime GenAI integration enables generative AI models to run directly on mobile devices
- Supports various hardware accelerators tailored for mobile devices, including CPU, GPU, and specialized mobile AI processors
- Offers platform-specific optimizations like CoreML for iOS and NNAPI for Android via ONNX Runtime
- Implements the full generative AI workflow, including pre/post-processing, inference, logits processing, search and sampling, and KV cache management

### Development Benefits
The .NET MAUI approach lets developers use their existing C# and .NET skills to build cross-platform AI applications. ONNX Runtime GenAI supports multiple model architectures, such as Llama, Mistral, Phi, Gemma, and others. Optimized ARM64 kernels accelerate INT4 quantized matrix multiplication, ensuring efficient performance on mobile hardware while maintaining the familiar .NET development experience.

### Use Cases
This solution is perfect for developers building AI-powered mobile apps using .NET technologies, such as intelligent chatbots, image recognition tools, language translation apps, and personalized recommendation systems that operate entirely on-device for enhanced privacy and offline functionality.

**Learn More**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI in Azure with Small Language Models Engine

Microsoft's Azure-based EdgeAI solution focuses on deploying Small Language Models (SLMs) efficiently in cloud-edge hybrid environments. This approach bridges the gap between cloud-scale AI services and edge deployment needs.

### Architecture Advantages
- Seamless integration with Azure AI services
- Supports running SLMs/LLMs and multi-modal models on-device and in the cloud using ONNX Runtime
- Optimized for enterprise-scale deployment
- Enables continuous model updates and management

### Use Cases
The Azure EdgeAI implementation is ideal for enterprise-grade AI deployments with cloud management capabilities. Applications include intelligent document processing, real-time analytics, and hybrid AI workflows that utilize both cloud and edge computing resources.

**Learn More**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI with Windows ML](./windowdeveloper.md)

Windows ML is Microsoft's advanced runtime optimized for efficient on-device model inference and simplified deployment, forming the foundation of Windows AI Foundry. It allows developers to create AI-powered Windows applications that leverage the full range of PC hardware.

### Platform Capabilities
- Compatible with all Windows 11 PCs running version 24H2 (build 26100) or later
- Works on all x64 and ARM64 PC hardware, even devices without NPUs or GPUs
- Enables developers to bring their own models and deploy them efficiently across the silicon partner ecosystem, including AMD, Intel, NVIDIA, and Qualcomm, spanning CPU, GPU, and NPU
- Infrastructure APIs eliminate the need for multiple app builds targeting different hardware

### Developer Benefits
Windows ML abstracts hardware and execution providers, allowing developers to focus on coding. It automatically updates to support the latest NPUs, GPUs, and CPUs as they are released. The platform offers a unified framework for AI development across the diverse Windows hardware ecosystem.

**Learn More**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](./windowdeveloper.md) - Comprehensive guide for Windows Edge AI development

## [5. EdgeAI with Foundry Local Applications](./foundrylocal.md)

Foundry Local enables Windows and Mac developers to create Retrieval Augmented Generation (RAG) applications using local resources in .NET, combining local language models with semantic search capabilities. This approach delivers privacy-focused AI solutions that operate entirely on local infrastructure.

### Technical Architecture
- Integrates the Phi language model, Local Embeddings, and Semantic Kernel to build a RAG scenario
- Uses embeddings as vectors (arrays) of floating-point values representing content and its semantic meaning
- Semantic Kernel acts as the main orchestrator, combining Phi and Smart Components to create a seamless RAG pipeline
- Supports local vector databases like SQLite and Qdrant

### Implementation Benefits
RAG, or Retrieval Augmented Generation, essentially means "retrieving relevant information and incorporating it into the prompt." This local implementation ensures data privacy while providing intelligent responses based on custom knowledge bases. It's particularly useful for enterprise scenarios requiring data sovereignty and offline functionality.

**Learn More**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local offers an OpenAI-compatible REST server powered by ONNX Runtime for running models locally on Windows. Below is a quick summary; refer to the official documentation for full details.

- Get started: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architecture: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI reference: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Full Windows guide in this repo: [foundrylocal.md](./foundrylocal.md)

Install or upgrade on Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Explore CLI categories:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Run a model and discover the dynamic endpoint:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Quick REST check to list models (replace PORT from status):
```cmd
curl -s http://localhost:PORT/v1/models
```

Tips:
- SDK integration: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Bring your own model (compile): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI Development Resources

For developers targeting the Windows platform, we've created a detailed guide covering the complete Windows EdgeAI ecosystem. This resource provides in-depth information about Windows AI Foundry, including APIs, tools, and best practices for EdgeAI development on Windows.

### Windows AI Foundry Platform
The Windows AI Foundry platform offers a comprehensive suite of tools and APIs specifically designed for Edge AI development on Windows devices. It includes specialized support for NPU-accelerated hardware, Windows ML integration, and platform-specific optimization techniques.

**Comprehensive Guide**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

This guide covers:
- Overview and components of the Windows AI Foundry platform
- Phi Silica API for efficient inference on NPU hardware
- Computer Vision APIs for image processing and OCR
- Windows ML runtime integration and optimization
- Foundry Local CLI for local development and testing
- Hardware optimization strategies for Windows devices
- Practical implementation examples and best practices

### [AI Toolkit for Edge AI Development](./aitoolkit.md)
For developers using Visual Studio Code, the AI Toolkit extension provides a complete development environment for building, testing, and deploying Edge AI applications. This toolkit simplifies the entire Edge AI development workflow within VS Code.

**Development Guide**: [AI Toolkit for Edge AI Development](./aitoolkit.md)

The AI Toolkit guide covers:
- Model discovery and selection for edge deployment
- Local testing and optimization workflows
- ONNX and Ollama integration for edge models
- Model conversion and quantization techniques
- Agent development for edge scenarios
- Performance evaluation and monitoring
- Deployment preparation and best practices

## Conclusion

These five EdgeAI implementations highlight the maturity and diversity of edge AI solutions available today. From hardware-accelerated devices like the Jetson Orin Nano to software frameworks like ONNX Runtime GenAI and Windows ML, developers have unprecedented options for deploying intelligent applications at the edge.

The common theme across all these platforms is the democratization of AI capabilities, making advanced machine learning accessible to developers of varying skill levels and use cases. Whether you're building mobile apps, desktop software, or embedded systems, these EdgeAI solutions provide the foundation for the next generation of intelligent applications that operate efficiently and privately at the edge.

Each platform offers unique strengths: Jetson Orin Nano for hardware-accelerated edge computing, ONNX Runtime GenAI for cross-platform mobile development, Azure EdgeAI for enterprise cloud-edge integration, Windows ML for Windows-native applications, and Foundry Local for privacy-focused RAG implementations. Together, they form a comprehensive ecosystem for EdgeAI development.

---

