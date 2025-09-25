<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50d80c321803b5170d9a9cd9bbfb37a3",
  "translation_date": "2025-09-25T02:18:49+00:00",
  "source_file": "Module08/README.md",
  "language_code": "my"
}
-->
# အပိုင်း 08: Microsoft Foundry Local - အပြည့်အစုံ Developer Toolkit ကို လက်တွေ့ကျကျ လေ့လာခြင်း

## အကျဉ်းချုပ်

Microsoft Foundry Local သည် edge AI ဖွံ့ဖြိုးတိုးတက်မှု၏ နောက်ဆုံးမျိုးဆက်ကို ကိုယ်စားပြုသည်။ ဒါဟာ developer များအတွက် Azure AI Foundry နှင့် seamless integration ကို ထိန်းသိမ်းထားပြီး၊ AI application များကို ဒေသတွင်းတွင် ဖန်တီး၊ တင်သွင်း၊ နှင့် အတိုင်းအတာချဲ့ထွင်နိုင်ရန် အင်အားကြီး tools များကို ပေးစွမ်းသည်။ ဒီ module မှာ Foundry Local ကို installation မှ advanced agent ဖွံ့ဖြိုးတိုးတက်မှုအထိ အပြည့်အစုံကို ဖော်ပြထားပါတယ်။

**အဓိကနည်းပညာများ:**
- Microsoft Foundry Local CLI နှင့် SDK
- Azure AI Foundry integration
- On-device model inference
- Local model caching နှင့် optimization
- Agent-based architectures

## သင်ယူရမည့်ရည်ရွယ်ချက်များ

ဒီ module ကို ပြီးမြောက်ပါက၊ သင်သည် -

- **Foundry Local ကို ကျွမ်းကျင်စွာ အသုံးပြုနိုင်မည်**: Windows 11 development အတွက် install, configure, နှင့် optimize လုပ်ခြင်း
- **မတူကွဲပြားသော Models များကို Deploy လုပ်နိုင်မည်**: phi, qwen, deepseek, နှင့် GPT models များကို CLI commands ဖြင့် ဒေသတွင်းတွင် run လုပ်ခြင်း
- **Production Solutions ဖန်တီးနိုင်မည်**: Advanced prompt engineering နှင့် data integration ဖြင့် AI applications ဖန်တီးခြင်း
- **Open-Source Ecosystem ကို အသုံးချနိုင်မည်**: Hugging Face models နှင့် community contributions များကို ပေါင်းစပ်ခြင်း
- **AI Agents ဖွံ့ဖြိုးတိုးတက်မှု**: Grounding နှင့် orchestration capabilities ဖြင့် intelligent agents ဖန်တီးခြင်း
- **Enterprise Patterns ကို အကောင်အထည်ဖော်နိုင်မည်**: Modular, scalable AI solutions များကို production deployment အတွက် ဖန်တီးခြင်း

## အစီအစဉ်ဖွဲ့စည်းမှု

### [1: Foundry Local ကို စတင်အသုံးပြုခြင်း](./01.FoundryLocalSetup.md)
**အဓိကအချက်**: Installation, CLI setup, model deployment, နှင့် hardware optimization

**အဓိကအကြောင်းအရာများ**: Complete installation • CLI commands • Model caching • Hardware acceleration • Multi-model deployment

**နမူနာ**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK Integration](./samples/02/README.md) • [Model Discovery & Benchmarking](./samples/03/README.md)

**ကြာမြင့်ချိန်**: 2-3 နာရီ | **အဆင့်**: Beginner

---

### [2: Azure AI Foundry ဖြင့် AI Solutions ဖန်တီးခြင်း](./02.AzureAIFoundryIntegration.md)
**အဓိကအချက်**: Advanced prompt engineering, data integration, နှင့် cloud connectivity

**အဓိကအကြောင်းအရာများ**: Prompt engineering • Data integration • Azure workflows • Performance optimization • Monitoring

**နမူနာ**: [Chainlit RAG Application](./samples/04/README.md)

**ကြာမြင့်ချိန်**: 2-3 နာရီ | **အဆင့်**: Intermediate

---

### [3: Open-Source Models Foundry Local](./03.OpenSourceModels.md)
**အဓိကအချက်**: Hugging Face integration, BYOM strategies, နှင့် community models

**အဓိကအကြောင်းအရာများ**: HuggingFace integration • Bring-your-own-model • Model Mondays insights • Community contributions • Model selection

**နမူနာ**: [Multi-Agent Orchestration](./samples/05/README.md)

**ကြာမြင့်ချိန်**: 2-3 နာရီ | **အဆင့်**: Intermediate

---

### [4: Cutting-Edge Models ကို ရှာဖွေခြင်း](./04.CuttingEdgeModels.md)
**အဓိကအချက်**: LLMs vs SLMs, EdgeAI implementation, နှင့် advanced demos

**အဓိကအကြောင်းအရာများ**: Model comparison • Edge vs cloud inference • Phi + ONNX Runtime • Chainlit RAG app • WebGPU optimization

**နမူနာ**: [Models-as-Tools Router](./samples/06/README.md)

**ကြာမြင့်ချိန်**: 3-4 နာရီ | **အဆင့်**: Advanced

---

### [5: AI-Powered Agents ကို အလျင်အမြန် ဖန်တီးခြင်း](./05.AIPoweredAgents.md)
**အဓိကအချက်**: Agent architectures, system prompts, grounding, နှင့် orchestration

**အဓိကအကြောင်းအရာများ**: Agent design patterns • System prompt engineering • Grounding techniques • Multi-agent systems • Production deployment

**နမူနာ**: [Multi-Agent Orchestration](./samples/05/README.md) • [Advanced Multi-Agent System](./samples/09/README.md)

**ကြာမြင့်ချိန်**: 3-4 နာရီ | **အဆင့်**: Advanced

---

### [6: Foundry Local - Models as Tools](./06.ModelsAsTools.md)
**အဓိကအချက်**: Modular AI solutions, enterprise scaling, နှင့် production patterns

**အဓိကအကြောင်းအရာများ**: Models as tools • On-device deployment • SDK/API integration • Enterprise architectures • Scaling strategies

**နမူနာ**: [Models-as-Tools Router](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**ကြာမြင့်ချိန်**: 3-4 နာရီ | **အဆင့်**: Expert

---

### [7: Direct API Integration Patterns](./samples/07/README.md)
**အဓိကအချက်**: SDK မလိုအပ်သော REST API integration ကို အမြင့်ဆုံးထိန်းချုပ်မှုအတွက် အသုံးပြုခြင်း

**အဓိကအကြောင်းအရာများ**: HTTP client implementation • Custom authentication • Model health monitoring • Streaming responses • Production error handling

**နမူနာ**: [Direct API Client](./samples/07/README.md)

**ကြာမြင့်ချိန်**: 2-3 နာရီ | **အဆင့်**: Intermediate

---

### [8: Windows 11 Native Chat Application](./samples/08/README.md)
**အဓိကအချက်**: Foundry Local integration ဖြင့် modern native chat applications ဖန်တီးခြင်း

**အဓိကအကြောင်းအရာများ**: Electron development • Fluent Design System • Native Windows integration • Real-time streaming • Chat interface design

**နမူနာ**: [Windows 11 Chat Application](./samples/08/README.md)

**ကြာမြင့်ချိန်**: 3-4 နာရီ | **အဆင့်**: Advanced

---

### [9: Advanced Multi-Agent Orchestration](./samples/09/README.md)
**အဓိကအချက်**: Agent များကို စနစ်တကျ ပေါင်းစပ်ခြင်း၊ အထူးလုပ်ငန်းတာဝန်များကို ခွဲဝေခြင်း၊ နှင့် AI workflows တွင် ပူးပေါင်းဆောင်ရွက်ခြင်း

**အဓိကအကြောင်းအရာများ**: Intelligent agent coordination • Function calling patterns • Cross-agent communication • Workflow orchestration • Quality assurance mechanisms

**နမူနာ**: [Advanced Multi-Agent System](./samples/09/README.md)

**ကြာမြင့်ချိန်**: 4-5 နာရီ | **အဆင့်**: Expert

---

### [10: Foundry Local as Tools Framework](./samples/10/README.md)
**အဓိကအချက်**: Foundry Local ကို ရှိပြီးသား applications နှင့် frameworks များတွင် ပေါင်းစပ်ရန် tool-first architecture

**အဓိကအကြောင်းအရာများ**: LangChain integration • Semantic Kernel functions • REST API frameworks • CLI tools • Jupyter integration • Production deployment patterns

**နမူနာ**: [Foundry Tools Framework](./samples/10/README.md)

**ကြာမြင့်ချိန်**: 4-5 နာရီ | **အဆင့်**: Expert

## လိုအပ်ချက်များ

### System Requirements
- **Operating System**: Windows 11 (22H2 or later)
- **Memory**: 16GB RAM (32GB recommended for larger models)
- **Storage**: 50GB free space for model caching
- **Hardware**: NPU-enabled device recommended (Copilot+ PC), GPU optional
- **Network**: High-speed internet for initial model downloads

### Development Environment
- Visual Studio Code with AI Toolkit extension
- Python 3.10+ and pip
- Git for version control
- PowerShell or Command Prompt
- Azure CLI (optional for cloud integration)

### Knowledge Prerequisites
- AI/ML အခြေခံအကြောင်းအရာများကို နားလည်ထားခြင်း
- Command line အသုံးပြုမှုအတွေ့အကြုံရှိခြင်း
- Python programming အခြေခံများ
- REST API အကြောင်းအရာများ
- Prompting နှင့် model inference အခြေခံများကို နားလည်ထားခြင်း

## Module Timeline

**စုစုပေါင်း ခန့်မှန်းချိန်**: 30-38 နာရီ

| Session | အဓိကအချက် | နမူနာများ | ကြာမြင့်ချိန် | အဆင့် |
|---------|------------|---------|------|------------|
|  1 | Setup & Basics | 01, 02, 03 | 2-3 နာရီ | Beginner |
|  2 | AI Solutions | 04 | 2-3 နာရီ | Intermediate |
|  3 | Open Source | 05 | 2-3 နာရီ | Intermediate |
|  4 | Advanced Models | 06 | 3-4 နာရီ | Advanced |
|  5 | AI Agents | 05, 09 | 3-4 နာရီ | Advanced |
|  6 | Enterprise Tools | 06, 10 | 3-4 နာရီ | Expert |
|  7 | Direct API Integration | 07 | 2-3 နာရီ | Intermediate |
|  8 | Windows 11 Chat App | 08 | 3-4 နာရီ | Advanced |
|  9 | Advanced Multi-Agent | 09 | 4-5 နာရီ | Expert |
| 10 | Tools Framework | 10 | 4-5 နာရီ | Expert |

## အဓိကအရင်းအမြစ်များ

**Official Documentation:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Source code နှင့် official samples
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Complete setup နှင့် usage guide
- [Model Mondays Series](https://aka.ms/model-mondays) - Weekly model highlights နှင့် tutorials

**Community & Support:**
- [Foundry Local Discussions](https://github.com/microsoft/Foundry-Local/discussions) - Community Q&A နှင့် feature requests
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence) - နောက်ဆုံးရသတင်းများနှင့် အကောင်းဆုံးအလေ့အကျင့်များ

## သင်ယူပြီးရလဒ်များ

ဒီ module ကို ပြီးမြောက်ပါက၊ သင်သည် -

### Technical Mastery
- **Deploy နှင့် Manage**: Development နှင့် production environments များတွင် Foundry Local installations ကို စနစ်တကျ ထိန်းချုပ်နိုင်ခြင်း
- **Integrate Models**: Microsoft, Hugging Face, နှင့် community sources မှ မတူကွဲပြားသော model families များနှင့် seamless အလုပ်လုပ်နိုင်ခြင်း
- **Build Applications**: Advanced features နှင့် optimizations ဖြင့် production-ready AI applications ဖန်တီးနိုင်ခြင်း
- **Develop Agents**: Grounding, reasoning, နှင့် tool integration ဖြင့် sophisticated AI agents များကို အကောင်အထည်ဖော်နိုင်ခြင်း

### Strategic Understanding
- **Architecture Decisions**: Local vs cloud deployment အကြား အကောင်းဆုံးရွေးချယ်မှုများကို ဆုံးဖြတ်နိုင်ခြင်း
- **Performance Optimization**: Hardware configurations များအကြား inference performance ကို optimize လုပ်နိုင်ခြင်း
- **Enterprise Scaling**: Local prototypes မှ enterprise deployments အထိ applications များကို design လုပ်နိုင်ခြင်း
- **Privacy နှင့် Security**: Local inference ဖြင့် privacy-preserving AI solutions များကို အကောင်အထည်ဖော်နိုင်ခြင်း

### Innovation Capabilities
- **Rapid Prototyping**: AI application concepts များကို အလျင်အမြန် ဖန်တီးပြီး စမ်းသပ်နိုင်ခြင်း
- **Community Integration**: Open-source models ကို အသုံးချပြီး ecosystem ကို ပံ့ပိုးနိုင်ခြင်း
- **Advanced Patterns**: RAG, agents, နှင့် tool integration အပါအဝင် cutting-edge AI patterns များကို အကောင်အထည်ဖော်နိုင်ခြင်း
- **Framework Mastery**: LangChain, Semantic Kernel, Chainlit, နှင့် Electron တို့နှင့် expert-level integration
- **Production Deployment**: Local prototypes မှ enterprise systems အထိ scalable AI solutions များကို deploy လုပ်နိုင်ခြင်း
- **Future-Ready Development**: ပေါ်ပေါက်လာမည့် AI technologies နှင့် patterns များအတွက် အသင့်ဖြစ်စေခြင်း

## စတင်အသုံးပြုခြင်း

1. **Environment Setup**: Windows 11 နှင့် recommend hardware (Prerequisites ကို ကြည့်ပါ)
2. **Foundry Local ကို Install လုပ်ပါ**: Session 1 ကို လိုက်နာပြီး installation နှင့် configuration ကို ပြီးမြောက်ပါစေ
3. **Sample 01 ကို Run လုပ်ပါ**: Basic REST API integration ဖြင့် setup ကို စစ်ဆေးပါ
4. **Samples များကို ဆက်လက်လုပ်ဆောင်ပါ**: Comprehensive mastery အတွက် samples 01-10 ကို ပြီးမြောက်ပါစေ

## Success Metrics

10 ခုလုံးကို အပြည့်အဝ စမ်းသပ်ပြီး သင်၏ progress ကို tracking လုပ်ပါ:

### Foundation Level (Samples 01-03)
- [ ] Foundry Local ကို install နှင့် configure လုပ်ပြီးစီးခြင်း
- [ ] REST API integration ကို ပြီးမြောက်စွာ လုပ်ဆောင်ခြင်း (Sample 01)
- [ ] OpenAI SDK compatibility ကို အကောင်အထည်ဖော်ခြင်း (Sample 02)
- [ ] Model discovery နှင့် benchmarking ကို ပြုလုပ်ခြင်း (Sample 03)

### Application Level (Samples 04-06)
- [ ] မတူကွဲပြားသော model families 4 ခုကို deploy နှင့် run လုပ်ခြင်း
- [ ] Functional RAG chat application ကို ဖန်တီးခြင်း (Sample 04)
- [ ] Multi-agent orchestration system ကို ဖန်တီးခြင်း (Sample 05)
- [ ] Intelligent model routing ကို အကောင်အထည်ဖော်ခြင်း (Sample 06)

### Advanced Integration Level (Samples 07-10)
- [ ] Production-ready API client ကို ဖန်တီးခြင်း (Sample 07)
- [ ] Windows 11 native chat application ကို ဖွံ့ဖြိုးတိုးတက်စေခြင်း (Sample 08)
- [ ] Advanced multi-agent system ကို အကောင်အထည်ဖော်ခြင်း (Sample 09)
- [ ] Comprehensive tools framework ကို ဖန်တီးခြင်း (Sample 10)

### Mastery Indicators
- [ ] Samples 10 ခုလုံးကို error မရှိဘဲ run လုပ်နိုင်ခြင်း
- [ ] Specific use cases အတွက် samples 3 ခုကို customize လုပ်နိုင်ခြင်း
- [ ] Production-like environments တွင် samples 2+ ခုကို deploy လုပ်နိုင်ခြင်း
- [ ] Sample code ကို တိုးတက်မှုများ သို့မဟုတ် extension များဖြင့် ပံ့ပိုးနိုင်ခြင်း
- [ ] Foundry Local patterns များကို ကိုယ်ပိုင်/ပရော်ဖက်ရှင်နယ် project များတွင် ပေါင်းစပ်နိုင်ခြင်း

## Quick Start Guide - All 10 Samples

### Environment Setup (Required for All Samples)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Core Foundation Samples (01-06)

**Sample 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Sample 02: OpenAI SDK Integration**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Sample 03: Model Discovery & Benchmarking**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Sample 04: Chainlit RAG Application**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Sample 05: Multi-Agent Orchestration**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Sample 06: Models-as-Tools Router**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b-instruct

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Advanced Integration Samples (07-10)

**Sample 07: Direct API Client**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**Sample 08: Windows 11 Chat Application**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**Sample 09: Advanced Multi-Agent System**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**Sample 10: Foundry Tools Framework**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### Troubleshooting Common Issues

**Foundry Local Connection Errors**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Model Loading Issues**
```powershell
# Check available models
foundry model list --cached

# Download missing models
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Force reload if needed
foundry model unload --all
foundry model run phi-4-mini
```

**Dependency Issues**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## အကျဉ်းချုပ်
ဤမော်ဂျူးသည် အနာဂတ် Edge AI ဖွံ့ဖြိုးတိုးတက်မှုကို ကိုယ်စားပြုပြီး Microsoft ၏ စီးပွားရေးအဆင့်မြင့် tools များနှင့် အခွင့်အလမ်းများနှင့် ဖန်တီးမှုများကို ပေါင်းစပ်ထားသော open-source ecosystem ၏ အကျိုးကျေးဇူးများကို ပေါင်းစပ်ထားသည်။ Foundry Local ၏ ၁၀ ခုလုံးသော စုံလင်သော နမူနာများကို ကျွမ်းကျင်စွာ လေ့လာပြီးနောက်၊ သင်သည် AI အက်ပလီကေးရှင်း ဖွံ့ဖြိုးတိုးတက်မှု၏ အရှေ့တန်းတွင် ရပ်တည်နိုင်မည်ဖြစ်သည်။

**လေ့လာမှု လမ်းကြောင်း အပြည့်အစုံ:**
- **အခြေခံ** (နမူနာ 01-03): API ပေါင်းစည်းမှုနှင့် မော်ဒယ် စီမံခန့်ခွဲမှု
- **အက်ပလီကေးရှင်းများ** (နမူနာ 04-06): RAG, agents, နှင့် အာရုံစိုက်မှု လမ်းကြောင်းချမှတ်ခြင်း
- **အဆင့်မြင့်** (နမူနာ 07-10): ထုတ်လုပ်မှု ဖွဲ့စည်းမှုများနှင့် စီးပွားရေး ပေါင်းစည်းမှု

Azure OpenAI ပေါင်းစည်းမှု (Session 2) အတွက် လိုအပ်သော ပတ်ဝန်းကျင် variable များနှင့် API version အပြင်အဆင်များကို တစ်ခုချင်း README ဖိုင်များတွင် ကြည့်ရှုပါ။

---

