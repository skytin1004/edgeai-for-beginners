# Module 08 Samples: Foundry Local Development Guide

## Overview

This comprehensive collection demonstrates both **Foundry Local SDK** and **Shell Command** approaches for building production-ready AI applications. Each sample showcases different aspects of edge AI development, from basic REST integration to advanced multi-agent systems.

## Development Approach: SDK vs Shell Commands

### Use Foundry Local SDK When:

- **Programmatic Control**: You need full control over agent lifecycle, evaluation, or deployment workflows
- **Custom Tooling**: Building automation around Foundry Local (CI/CD integration, multi-agent orchestration)
- **Fine-Grained Access**: Requiring detailed agent metadata, versioning, or evaluation runner control
- **Python Integration**: Working in Python-heavy environments or embedding Foundry logic into broader applications
- **Enterprise Workflows**: Implementing modular workflows and reproducible evaluation pipelines aligned with Microsoft reference architectures

### Use Shell Commands When:

- **Quick Testing**: Performing rapid local testing, manual agent launches, or setup verification
- **CLI Simplicity**: Need straightforward CLI operations for starting/stopping agents, checking logs, or basic evaluations
- **Lightweight Automation**: Scripting simple automation without full SDK integration requirements
- **Rapid Iteration**: Debugging and development cycles, especially in constrained environments or resource group-level deployments
- **Setup & Validation**: Initial environment configuration and quick verification tasks

## Best Practices & Recommended Workflow

Based on agent lifecycle management, dependency tracking, and least-privilege reproducibility principles:

### Phase 1: Foundation & Setup
1. **Start with Shell Commands** for initial setup and quick validation
2. **Verify Environment** using CLI tools and basic model deployment
3. **Test Connectivity** with simple REST calls and health checks

### Phase 2: Development & Integration
1. **Transition to SDK** for scalable, traceable workflows
2. **Implement Programmatic Control** for complex agent interactions
3. **Build Custom Tools** for community-ready templates and Azure OpenAI integration

### Phase 3: Production & Scale
1. **Hybrid Approach** combining CLI for ops and SDK for application logic
2. **Enterprise Integration** with monitoring, logging, and deployment pipelines
3. **Community Contribution** through reusable templates and best practices
