# EdgeAI for Beginners 


![Course cover image](./imgs/cover.png)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Follow these steps to get started using these resources:

1. **Fork the Repository**: Click [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clone the Repository**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Join The Azure AI Foundry Discord and meet experts and fellow developers**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Multi-Language Support

#### Supported via GitHub Action (Automated & Always Up-to-Date)

[French](./translations/fr/README.md) | [Spanish](./translations/es/README.md) |  [Chinese (Simplified)](./translations/zh/README.md) | [Chinese (Traditional, Macau)](./translations/mo/README.md) | [Chinese (Traditional, Hong Kong)](./translations/hk/README.md) | [Chinese (Traditional, Taiwan)](./translations/tw/README.md) | [Japanese](./translations/ja/README.md) | [Korean](./translations/ko/README.md) | 
**If you wish to have additional translations languages supported are listed [here](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Introduction

Welcome to **EdgeAI for Beginners** – your comprehensive journey into the transformative world of Edge Artificial Intelligence. This course bridges the gap between powerful AI capabilities and practical, real-world deployment on edge devices, empowering you to harness AI's potential directly where data is generated and decisions need to be made.

### What You'll Master

This course takes you from fundamental concepts to production-ready implementations, covering:
- **Small Language Models (SLMs)** optimized for edge deployment
- **Hardware-aware optimization** across diverse platforms
- **Real-time inference** with privacy-preserving capabilities
- **Production deployment** strategies for enterprise applications

### Why EdgeAI Matters

Edge AI represents a paradigm shift that addresses critical modern challenges:
- **Privacy & Security**: Process sensitive data locally without cloud exposure
- **Real-time Performance**: Eliminate network latency for time-critical applications
- **Cost Efficiency**: Reduce bandwidth and cloud computing expenses
- **Resilient Operations**: Maintain functionality during network outages
- **Regulatory Compliance**: Meet data sovereignty requirements

### Edge AI

Edge AI refers to running AI algorithms and language models locally on hardware—close to where data is generated—without relying on cloud resources for inference. It reduces latency, enhances privacy, and enables real-time decision-making.

### Core Principles:
- **On-device inference**: AI models run on edge devices (phones, routers, microcontrollers, industrial PCs)
- **Offline capability**: Functions without persistent internet connectivity
- **Low latency**: Immediate responses suited for real-time systems
- **Data sovereignty**: Keeps sensitive data local, improving security and compliance

### Small Language Models (SLMs)

SLMs like Phi-4, Mistral-7B, and Gemma are optimized versions of larger LLMs—trained or distilled for:
- **Reduced memory footprint**: Efficient use of limited edge device memory
- **Lower compute demand**: Optimized for CPU and edge GPU performance
- **Faster startup times**: Quick initialization for responsive applications

They unlock powerful NLP capabilities while meeting the constraints of:
- **Embedded systems**: IoT devices and industrial controllers
- **Mobile devices**: Smartphones and tablets with offline capabilities
- **IoT Devices**: Sensors and smart devices with limited resources
- **Edge servers**: Local processing units with limited GPU resources
- **Personal Computers**: Desktop and laptop deployment scenarios

## Course Architecture

### [Module 01: EdgeAI Fundamentals and Transformation](./Module01/README.md)
**Theme**: The transformative shift of edge AI deployment

#### Chapter Structure:
- [**Section 1: EdgeAI Fundamentals**](./Module01/01.EdgeAIFundamentals.md)
  - Traditional cloud AI vs edge AI comparison
  - Edge computing challenges and constraints
  - Key technologies: model quantization, compression optimization, Small Language Models (SLMs)
  - Hardware acceleration: NPUs, GPU optimization, CPU optimization
  - Advantages: privacy security, low latency, offline capabilities, cost efficiency

- [**Section 2: Real-World Case Studies**](./Module01/02.RealWorldCaseStudies.md)
  - Microsoft Phi & Mu model ecosystem
  - Japan Airlines AI reporting system case study
  - Market impact and future directions
  - Deployment considerations and best practices

- [**Section 3: Practical Implementation Guide**](./Module01/03.PracticalImplementationGuide.md)
  - Development environment setup (Python 3.10+, .NET 8+)
  - Hardware requirements and recommended configurations
  - Core model family resources
  - Quantization and optimization tools (Llama.cpp, Microsoft Olive, Apple MLX)
  - Assessment and verification checklist

- [**Section 4: Edge AI Deployment Hardware Platforms**](./Module01/04.EdgeDeployment.md)
  - Edge AI deployment considerations and requirements
  - Intel edge AI hardware and optimization techniques
  - Qualcomm AI solutions for mobile and embedded systems
  - NVIDIA Jetson and edge computing platforms
  - Windows AI PC platforms with NPU acceleration
  - Hardware-specific optimization strategies

---

### [Module 02: Small Language Model Foundations](./Module02/README.md)
**Theme**: SLM theoretical principles, implementation strategies, and production deployment

#### Chapter Structure:
- [**Section 1: Microsoft Phi Model Family Fundamentals**](./Module02/01.PhiFamily.md)
  - Design philosophy evolution (Phi-1 to Phi-4)
  - Efficiency-first architecture design
  - Specialized capabilities (reasoning, multimodal, edge deployment)

- [**Section 2: Qwen Family Fundamentals**](./Module02/02.QwenFamily.md)
  - Open source excellence (Qwen 1.0 to Qwen3) - available through Hugging Face
  - Advanced reasoning architecture with thinking mode capabilities
  - Scalable deployment options (0.5B-235B parameters)

- [**Section 3: Gemma Family Fundamentals**](./Module02/03.GemmaFamily.md)
  - Research-driven innovation (Gemma 3 & 3n)
  - Multimodal excellence
  - Mobile-first architecture

- [**Section 4: BitNET Family Fundamentals**](./Module02/04.BitNETFamily.md)
  - Revolutionary quantization technology (1.58-bit)
  - Specialized inference framework from https://github.com/microsoft/BitNet
  - Sustainable AI leadership through extreme efficiency

- [**Section 5: Microsoft Mu Model Fundamentals**](./Module02/05.mumodel.md)
  - Device-first architecture built into Windows 11
  - System integration with Windows 11 Settings
  - Privacy-preserving offline operation

- [**Section 6: Phi-Silica Fundamentals**](./Module02/06.phisilica.md)
  - NPU-optimized architecture built into Windows 11 Copilot+ PCs
  - Exceptional efficiency (650 tokens/second at 1.5W)
  - Developer integration with Windows App SDK

---

### [Module 03: Small Language Model Deployment](./Module03/README.md)
**Theme**: Complete SLM lifecycle deployment, from theory to production environment

#### Chapter Structure:
- [**Section 1: SLM Advanced Learning**](./Module03/01.SLMAdvancedLearning.md)
  - Parameter classification framework (Micro SLM 100M-1.4B, Medium SLM 14B-30B)
  - Advanced optimization techniques (quantization methods, BitNET 1-bit quantization)
  - Model acquisition strategies (Azure AI Foundry for Phi models, Hugging Face for selected models)

- [**Section 2: Local Environment Deployment**](./Module03/02.DeployingSLMinLocalEnv.md)
  - Ollama universal platform deployment
  - Microsoft Foundry local enterprise-grade solutions
  - Framework comparative analysis

- [**Section 3: Containerized Cloud Deployment**](./Module03/03.DeployingSLMinCloud.md)
  - vLLM high-performance inference deployment
  - Ollama container orchestration
  - ONNX Runtime edge-optimized implementation

---

### [Module 04: Model Format Conversion and Quantization](./Module04/README.md)
**Theme**: Complete model optimization toolkit for edge deployment across platforms

#### Chapter Structure:
- [**Section 1: Model Format Conversion and Quantization Foundations**](./Module04/01.Introduce.md)
  - Precision classification framework (ultra-low, low, medium precision)
  - GGUF and ONNX format advantages and use cases
  - Quantization benefits for operational efficiency
  - Performance benchmarks and memory footprint comparisons

- [**Section 2: Llama.cpp Implementation Guide**](./Module04/02.Llamacpp.md)
  - Cross-platform installation (Windows, macOS, Linux)
  - GGUF format conversion and quantization levels (Q2_K to Q8_0)
  - Hardware acceleration (CUDA, Metal, OpenCL, Vulkan)
  - Python integration and REST API deployment

- [**Section 3: Microsoft Olive Optimization Suite**](./Module04/03.MicrosoftOlive.md)
  - Hardware-aware model optimization with 40+ built-in components
  - Auto-optimization with dynamic and static quantization
  - Enterprise integration with Azure ML workflows
  - Popular model support (Llama, Phi, selected Qwen models, Gemma)

- [**Section 4: OpenVINO Toolkit Optimization Suite**](./Module04/04.openvino.md)
  - Intel's open-source toolkit for cross-platform AI deployment
  - Neural Network Compression Framework (NNCF) for advanced optimization
  - OpenVINO GenAI for large language model deployment
  - Hardware acceleration across CPU, GPU, VPU, and AI accelerators

- [**Section 5: Apple MLX Framework Deep Dive**](./Module04/05.AppleMLX.md)
  - Unified memory architecture for Apple Silicon
  - Support for LLaMA, Mistral, Phi-3, selected Qwen models
  - LoRA fine-tuning and model customization
  - Hugging Face integration with 4-bit/8-bit quantization

- [**Section 6: Edge AI Development Workflow Synthesis**](./Module04/06.workflow-synthesis.md)
  - Unified workflow architecture integrating multiple optimization frameworks
  - Framework selection decision trees and performance trade-off analysis
  - Production readiness validation and comprehensive deployment strategies
  - Future-proofing strategies for emerging hardware and model architectures

---

### [Module 05: SLMOps - Small Language Model Operations](./Module05/README.md)
**Theme**: Complete SLM lifecycle operations from distillation to production deployment

#### Chapter Structure:
- [**Section 1: Introduction to SLMOps**](./Module05/01.IntroduceSLMOps.md)
  - SLMOps paradigm shift in AI operations
  - Cost efficiency and privacy-first architecture
  - Strategic business impact and competitive advantages
  - Real-world implementation challenges and solutions

- [**Section 2: Model Distillation - From Theory to Practice**](./Module05/02.SLMOps-Distillation.md)
  - Knowledge transfer from teacher to student models
  - Two-stage distillation process implementation
  - Azure ML distillation workflows with practical examples
  - 85% inference time reduction with 92% accuracy retention

- [**Section 3: Fine-Tuning - Customizing Models for Specific Tasks**](./Module05/03.SLMOps-Finetuing.md)
  - Parameter-efficient fine-tuning (PEFT) techniques
  - LoRA and QLoRA advanced methods
  - Microsoft Olive fine-tuning implementation
  - Multi-adapter training and hyperparameter optimization

- [**Section 4: Deployment - Production-Ready Implementation**](./Module05/04.SLMOps.Deployment.md)
  - Model conversion and quantization for production
  - Foundry Local deployment configuration
  - Performance benchmarking and quality validation
  - 75% size reduction with production monitoring

---

### [Module 06: SLM Agentic Systems - AI Agents and Function Calling](./Module06/README.md)
**Theme**: SLM agentic systems implementation from foundation to advanced function calling and Model Context Protocol integration

#### Chapter Structure:
- [**Section 1: AI Agents and Small Language Models Foundation**](./Module06/01.IntroduceAgent.md)
  - Agent classification framework (reflex, model-based, goal-based, learning agents)
  - SLM fundamentals and optimization strategies (GGUF, quantization, edge frameworks)
  - SLM vs LLM trade-offs analysis (10-30× cost reduction, 70-80% task effectiveness)
  - Practical deployment with Ollama, VLLM, and Microsoft edge solutions

- [**Section 2: Function Calling in Small Language Models**](./Module06/02.FunctionCalling.md)
  - Systematic workflow implementation (intent detection, JSON output, external execution)
  - Platform-specific implementations (Phi-4-mini, selected Qwen models, Microsoft Foundry Local)
  - Advanced examples (multi-agent collaboration, dynamic tool selection)
  - Production considerations (rate limiting, audit logging, security measures)

- [**Section 3: Model Context Protocol (MCP) Integration**](./Module06/03.IntroduceMCP.md)
  - Protocol architecture and layered system design
  - Multi-backend support (Ollama for development, vLLM for production)
  - Connection protocols (STDIO and SSE modes)
  - Real-world applications (web automation, data processing, API integration)

---

### [Module 07: EdgeAI Implementation Samples](./Module07/README.md)
**Theme**: Comprehensive EdgeAI implementations across diverse platforms and frameworks

#### Chapter Structure:
- [**AI Toolkit for Visual Studio Code**](./Module07/aitoolkit.md)
  - Comprehensive Edge AI development environment within VS Code
  - Model catalog and discovery for edge deployment
  - Local testing, optimization, and agent development workflows
  - Performance monitoring and evaluation for edge scenarios

- [**Windows EdgeAI Development Guide**](./Module07/windowdeveloper.md)
  - Windows AI Foundry platform comprehensive overview
  - Phi Silica API for efficient NPU inference
  - Computer Vision APIs for image processing and OCR
  - Foundry Local CLI for local development and testing

- [**EdgeAI in NVIDIA Jetson Orin Nano**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 67 TOPS AI performance in credit-card-sized form factor
  - Generative AI models support (vision transformers, LLMs, vision-language models)
  - Applications in robotics, drones, intelligent cameras, autonomous devices
  - Affordable $249 platform for democratized AI development

- [**EdgeAI in Mobile Applications with .NET MAUI and ONNX Runtime GenAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - Cross-platform mobile AI with single C# codebase
  - Hardware acceleration support (CPU, GPU, mobile AI processors)
  - Platform-specific optimizations (CoreML for iOS, NNAPI for Android)
  - Complete generative AI loop implementation

- [**EdgeAI in Azure with Small Language Models Engine**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - Cloud-edge hybrid deployment architecture
  - Azure AI services integration with ONNX Runtime
  - Enterprise-scale deployment and continuous model management
  - Hybrid AI workflows for intelligent document processing

- [**EdgeAI with Windows ML**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Windows AI Foundry foundation for performant on-device inference
  - Universal hardware support (AMD, Intel, NVIDIA, Qualcomm silicon)
  - Automatic hardware abstraction and optimization
  - Unified framework for diverse Windows hardware ecosystem

- [**EdgeAI with Foundry Local Applications**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - Privacy-focused RAG implementation with local resources
  - Phi-3 language model integration with semantic search (Phi models only)
  - Local vector databases support (SQLite, Qdrant)
  - Data sovereignty and offline operation capabilities

## Course Learning Objectives

By completing this comprehensive EdgeAI course, you will develop the expertise to design, implement, and deploy production-ready EdgeAI solutions. Our structured approach ensures you master both theoretical foundations and practical implementation skills.

### Technical Competencies

**Foundation Knowledge**
- Understand the fundamental differences between cloud-based and edge-based AI architectures
- Master the principles of model quantization, compression, and optimization for resource-constrained environments
- Comprehend hardware acceleration options (NPUs, GPUs, CPUs) and their deployment implications

**Implementation Skills**
- Deploy Small Language Models across diverse edge platforms (mobile, embedded, IoT, edge servers)
- Apply optimization frameworks including Llama.cpp, Microsoft Olive, ONNX Runtime, and Apple MLX
- Implement real-time inference systems with sub-second response requirements

**Production Expertise**
- Design scalable EdgeAI architectures for enterprise applications
- Implement monitoring, maintenance, and updating strategies for deployed systems
- Apply security best practices for privacy-preserving EdgeAI implementations

### Strategic Capabilities

**Decision-Making Framework**
- Evaluate EdgeAI opportunities and identify suitable use cases for business applications
- Assess trade-offs between model accuracy, inference speed, power consumption, and hardware costs
- Select appropriate SLM families and configurations based on specific deployment constraints

**System Architecture**
- Design end-to-end EdgeAI solutions that integrate with existing infrastructure
- Plan hybrid edge-cloud architectures for optimal performance and cost efficiency
- Implement data flow and processing pipelines for real-time AI applications

### Industry Applications

**Practical Deployment Scenarios**
- **Manufacturing**: Quality control systems, predictive maintenance, and process optimization
- **Healthcare**: Privacy-preserving diagnostic tools and patient monitoring systems
- **Transportation**: Autonomous vehicle decision-making and traffic management
- **Smart Cities**: Intelligent infrastructure and resource management systems
- **Consumer Electronics**: AI-powered mobile applications and smart home devices

## Learning Outcomes Overview

### Module 01 Learning Outcomes:
- Understand the fundamental differences between cloud and edge AI architectures
- Master core optimization techniques for edge deployment
- Recognize real-world applications and success stories
- Acquire practical skills for implementing EdgeAI solutions

### Module 02 Learning Outcomes:
- Deep understanding of different SLM design philosophies and their deployment implications
- Master strategic decision-making capabilities based on computational constraints and performance requirements
- Understand deployment flexibility trade-offs
- Possess future-ready insights into efficient AI architecture

### Module 03 Learning Outcomes:
- Strategic model selection capabilities
- Optimization technique mastery
- Deployment flexibility mastery
- Production-ready configuration capabilities

### Module 04 Learning Outcomes:
- Deep understanding of quantization boundaries and practical applications
- Hands-on experience with multiple optimization frameworks (Llama.cpp, Olive, OpenVINO, MLX)
- Master Intel hardware optimization with OpenVINO and NNCF
- Hardware-aware optimization selection capabilities across diverse platforms
- Production deployment skills for cross-platform edge computing environments
- Strategic framework selection and workflow synthesis for optimal Edge AI solutions

### Module 05 Learning Outcomes:
- Master SLMOps paradigm and operational principles
- Implement model distillation for knowledge transfer and efficiency optimization
- Apply fine-tuning techniques for domain-specific model customization
- Deploy production-ready SLM solutions with monitoring and maintenance strategies

### Module 06 Learning Outcomes:
- Understand foundational concepts of AI agents and Small Language Models architecture
- Master function calling implementation across multiple platforms and frameworks
- Integrate Model Context Protocol (MCP) for standardized external tool interaction
- Build sophisticated agentic systems with minimal human intervention requirements

### Module 07 Learning Outcomes:
- Master AI Toolkit for Visual Studio Code for comprehensive Edge AI development workflows
- Gain expertise in Windows AI Foundry platform and NPU optimization strategies
- Acquire hands-on experience with diverse EdgeAI platforms and implementation strategies
- Master hardware-specific optimization techniques across NVIDIA, mobile, Azure, and Windows platforms
- Understand deployment trade-offs between performance, cost, and privacy requirements
- Develop practical skills for building real-world EdgeAI applications across different ecosystems

## Expected Course Outcomes

Upon successful completion of this course, you will be equipped with the knowledge, skills, and confidence to lead EdgeAI initiatives in professional environments.

### Professional Readiness

**Technical Leadership**
- **Solution Architecture**: Design comprehensive EdgeAI systems that meet enterprise requirements
- **Performance Optimization**: Achieve optimal balance between accuracy, speed, and resource consumption
- **Cross-Platform Deployment**: Implement solutions across Windows, Linux, mobile, and embedded platforms
- **Production Operations**: Maintain and scale EdgeAI systems with enterprise-grade reliability

**Industry Expertise**
- **Technology Evaluation**: Assess and recommend EdgeAI solutions for specific business challenges
- **Implementation Planning**: Develop realistic timelines and resource requirements for EdgeAI projects
- **Risk Management**: Identify and mitigate technical and operational risks in EdgeAI deployments
- **ROI Optimization**: Demonstrate measurable business value from EdgeAI implementations

### Career Advancement Opportunities

**Professional Roles**
- EdgeAI Solutions Architect
- Machine Learning Engineer (Edge Specialization)
- IoT AI Developer
- Mobile AI Application Developer
- Enterprise AI Consultant

**Industry Sectors**
- Smart Manufacturing and Industry 4.0
- Autonomous Vehicles and Transportation
- Healthcare Technology and Medical Devices
- Financial Technology and Security
- Consumer Electronics and Mobile Applications

### Certification and Validation

**Portfolio Development**
- Complete end-to-end EdgeAI projects demonstrating practical competency
- Deploy production-ready solutions across multiple hardware platforms
- Document optimization strategies and performance improvements achieved

**Continuous Learning Path**
- Foundation for advanced AI specializations
- Preparation for cloud-edge hybrid architectures
- Gateway to emerging AI technologies and frameworks

This course positions you at the forefront of AI technology deployment, where intelligent capabilities are seamlessly integrated into the devices and systems that power modern life.

## File Structure Tree Diagram

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

## Course Features

- **Progressive Learning**: Gradually advance from basic concepts to advanced deployment
- **Theory and Practice Integration**: Each module contains both theoretical foundations and practical operations
- **Real Case Studies**: Based on actual cases from Microsoft, Alibaba, Google, and others
- **Hands-on Practice**: Complete configuration files, API testing procedures, and deployment scripts
- **Performance Benchmarks**: Detailed comparisons of inference speed, memory usage, and resource requirements
- **Enterprise-grade Considerations**: Security practices, compliance frameworks, and data protection strategies

## Getting Started

Recommended Learning Path:
1. Start with **Module01** to build fundamental understanding of EdgeAI
2. Proceed to **Module02** to deeply understand various SLM model families
3. Learn **Module03** to master practical deployment skills
4. Continue with **Module04** for advanced model optimization, format conversion, and framework synthesis
5. Complete **Module05** to master SLMOps for production-ready implementations
6. Explore **Module06** to understand SLM agentic systems and function calling capabilities
7. Finish with **Module07** to gain practical experience with AI Toolkit and diverse EdgeAI implementation samples

Each module is designed to be independently complete, but sequential learning will provide the best results.

## Study Guide

A comprehensive [Study Guide](STUDY_GUIDE.md) is available to help you maximize your learning experience. The study guide provides:

- **Structured Learning Paths**: Optimized schedules for completing the course in 20 hours
- **Time Allocation Guidance**: Specific recommendations for balancing reading, exercises, and projects
- **Key Concept Focus**: Prioritized learning objectives for each module
- **Self-Assessment Tools**: Questions and exercises to test your understanding
- **Mini-Project Ideas**: Practical applications to reinforce your learning

The study guide is designed to accommodate both intensive learning (1 week) and part-time study (3 weeks), with clear guidance on how to allocate your time effectively even if you can only dedicate 10 hours to the course.

---

**The future of EdgeAI lies in continuous improvement of model architectures, quantization techniques, and deployment strategies that prioritize efficiency and specialization over general-purpose capabilities. Organizations that embrace this paradigm shift will be well-positioned to leverage AI's transformative potential while maintaining control over their data and operations.**

## Other Courses

Our team produces other courses! Check out:

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
