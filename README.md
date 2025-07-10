# EdgeAI for Beginners 

An in-depth educational journey through Edge AI technologies, structured across three comprehensive modules: EdgeAI Fundamentals, Small Language Model Foundations, and Practical Deployment Strategies. This course guides learners from basic concepts through advanced implementations, featuring real-world case studies, hands-on exercises, and deployment examples that demonstrate how to effectively run AI models directly on edge devices for enhanced privacy, reduced latency, and improved efficiency.

![Course cover image](./imgs/cover.png)

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
    - Phi Silica: Windows AI integration
    - Mu models: task-specific micro language models
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
  - Open source excellence (Qwen 1.0 to Qwen3)
  - Advanced reasoning architecture
  - Scalable deployment options (0.5B-235B parameters)

- [**Section 3: Gemma Family Fundamentals**](./Module02/03.GemmaFamily.md)
  - Research-driven innovation (Gemma 3 & 3n)
  - Multimodal excellence
  - Mobile-first architecture

- [**Section 4: BitNET Family Fundamentals**](./Module02/04.BitNETFamily.md)
  - Revolutionary quantization technology (1.58-bit)
  - Optimized inference framework
  - Sustainable AI leadership

- [**Section 5: Microsoft Mu Model Fundamentals**](./Module02/05.mumodel.md)
  - Device-first architecture for Windows
  - System integration with Windows Settings
  - Privacy-preserving offline operation

- [**Section 6: Phi-Silica Fundamentals**](./Module02/06.phisilica.md)
  - NPU-optimized architecture for Windows Copilot+ PCs
  - Exceptional efficiency (650 tokens/second at 1.5W)
  - Developer integration with Windows App SDK

---

### [Module 03: Small Language Model Deployment](./Module03/README.md)
**Theme**: Complete SLM lifecycle deployment, from theory to production environment

#### Chapter Structure:
- [**Section 1: SLM Advanced Learning**](./Module03/01.SLMAdvancedLearning.md)
  - Parameter classification framework (Micro SLM 100M-1.4B, Medium SLM 14B-30B)
  - Advanced optimization techniques (quantization methods, BitNET 1-bit quantization)
  - Model acquisition strategies (Hugging Face, Azure AI Foundry)

- [**Section 2: Local Environment Deployment**](./Module03/02.DeployingSLMinLocalEnv.md)
  - Ollama universal platform deployment
  - Microsoft Foundry local enterprise-grade solutions
  - Framework comparative analysis

- [**Section 3: Containerized Cloud Deployment**](./Module03/03.DeployingSLMinCloud.md)
  - vLLM high-performance inference deployment
  - Ollama container orchestration
  - ONNX Runtime edge-optimized implementation

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

Each module is designed to be independently complete, but sequential learning will provide the best results.

## Study Guide

A comprehensive [Study Guide](./studyguide.md) is available to help you maximize your learning experience. The study guide provides:

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