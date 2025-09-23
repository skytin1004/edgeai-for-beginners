<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-23T00:52:07+00:00",
  "source_file": "Module08/README.md",
  "language_code": "my"
}
-->
# အပိုင်း 08: Microsoft Foundry Local - အပြည့်အစုံ Developer Toolkit ကို လက်တွေ့ကျကျ လေ့လာခြင်း

## အကျဉ်းချုပ်

Microsoft Foundry Local သည် edge AI ဖွံ့ဖြိုးတိုးတက်မှု၏ နောက်ဆုံးမျိုးဆက်ကို ကိုယ်စားပြုသည်။ ဒါဟာ developer များအတွက် Azure AI Foundry နှင့် အဆက်မပြတ် ပေါင်းစည်းမှုကို ထိန်းသိမ်းထားပြီး၊ AI application များကို ဒေသတွင်းတွင် ဖန်တီး၊ တင်သွင်း၊ နှင့် အတိုင်းအတာချဲ့ထွင်နိုင်ရန် အင်အားကြီး tools များကို ပေးစွမ်းသည်။ ဒီ module မှာ Foundry Local ကို installation မှ စ၍ အဆင့်မြင့် agent ဖွံ့ဖြိုးတိုးတက်မှုအထိ အကျယ်အဝန်းကို ဖော်ပြထားသည်။

**အဓိကနည်းပညာများ:**
- Microsoft Foundry Local CLI နှင့် SDK
- Azure AI Foundry integration
- On-device model inference
- Local model caching နှင့် optimization
- Agent-based architectures

## Module Learning Objectives

ဒီ module ကို ပြီးမြောက်စွာ လေ့လာပြီးနောက်၊ သင်သည်:

- **Foundry Local Setup ကို ကျွမ်းကျင်စွာ လုပ်ဆောင်နိုင်မည်**: Windows 11 အတွက် Foundry Local ကို install, configure, နှင့် optimize လုပ်ခြင်း
- **မတူကွဲပြားသော Models များကို Deploy လုပ်ခြင်း**: phi, qwen, deepseek, နှင့် GPT-OSS-20B models များကို CLI commands ဖြင့် ဒေသတွင်းတွင် run လုပ်ခြင်း
- **Production Solutions ဖန်တီးခြင်း**: Prompt engineering နှင့် data integration ကို အသုံးပြု၍ AI applications ဖန်တီးခြင်း
- **Open-Source Ecosystem ကို အသုံးချခြင်း**: Hugging Face models နှင့် community-driven additions များကို ပေါင်းစည်းခြင်း
- **AI Architectures များကို နှိုင်းယှဉ်ခြင်း**: LLMs နှင့် SLMs အကြား trade-offs နှင့် deployment strategies ကို နားလည်ခြင်း
- **AI Agents ဖွံ့ဖြိုးတိုးတက်မှု**: Foundry Local ၏ architecture နှင့် grounding capabilities ကို အသုံးပြု၍ intelligent agents ဖန်တီးခြင်း
- **Models ကို Tools အဖြစ် အသုံးချခြင်း**: Enterprise applications အတွက် modular, customizable AI solutions ဖန်တီးခြင်း

## Session Structure

### [1: Foundry Local ကို စတင်အသုံးပြုခြင်း](./01.FoundryLocalSetup.md)
**အဓိကအချက်**: Installation, CLI setup, model caching, နှင့် hardware acceleration

**သင်လေ့လာမည့်အရာများ:**
- Windows 11 တွင် Foundry Local ကို အပြည့်အစုံ install လုပ်ခြင်း
- CLI configuration နှင့် command structure
- Model caching strategies များကို အသုံးပြု၍ performance ကို အကောင်းဆုံးဖြစ်စေရန်
- Hardware acceleration setup နှင့် optimization
- phi, qwen, deepseek, နှင့် GPT-OSS-20B models များကို လက်တွေ့ deploy လုပ်ခြင်း

**ကြာမြင့်ချိန်**: 2-3 နာရီ  
**လိုအပ်ချက်များ**: Windows 11, basic command line knowledge

---

### [2: Azure AI Foundry ဖြင့် AI Solutions ဖန်တီးခြင်း](./02.AzureAIFoundryIntegration.md)
**အဓိကအချက်**: Advanced prompt engineering, data integration, နှင့် actionable tasks

**သင်လေ့လာမည့်အရာများ:**
- Advanced prompt engineering techniques
- Data integration patterns နှင့် အကောင်းဆုံး လုပ်ဆောင်နည်းများ
- Foundry Local ဖြင့် actionable AI tasks ဖန်တီးခြင်း
- Azure AI Foundry integration workflows ကို seamless အဖြစ်လုပ်ဆောင်ခြင်း
- Performance optimization နှင့် monitoring

**ကြာမြင့်ချိန်**: 2-3 နာရီ  
**လိုအပ်ချက်များ**: Session 1 ကို ပြီးမြောက်ထားရမည်၊ Azure account (optional)

---

### [3: Open-Source Models Foundry Local](./03.OpenSourceModels.md)
**အဓိကအချက်**: Hugging Face integration, model selection strategies, နှင့် community-driven additions

**သင်လေ့လာမည့်အရာများ:**
- Hugging Face model integration ကို Foundry Local နှင့် ပေါင်းစည်းခြင်း
- Bring-your-own-model (BYOM) strategies နှင့် implementation
- Model Mondays series insights နှင့် community contributions
- Custom model deployment နှင့် optimization
- Community model များကို အကဲဖြတ်ခြင်းနှင့် ရွေးချယ်ခြင်း criteria

**ကြာမြင့်ချိန်**: 2-3 နာရီ  
**လိုအပ်ချက်များ**: Session 1-2 ကို ပြီးမြောက်ထားရမည်၊ Hugging Face account

---

### [4: Cutting-Edge Models - LLMs, SLMs, နှင့် On-Device Inference ကို လေ့လာခြင်း](./04.CuttingEdgeModels.md)
**အဓိကအချက်**: Model comparison, EdgeAI with Phi နှင့် ONNX Runtime, advanced demos

**သင်လေ့လာမည့်အရာများ:**
- LLMs နှင့် SLMs အကြား အပြည့်အစုံ နှိုင်းယှဉ်ခြင်းနှင့် အသုံးပြုမှုများ
- Local နှင့် cloud inference trade-offs နှင့် decision frameworks
- EdgeAI implementation ကို Phi နှင့် ONNX Runtime ဖြင့် လုပ်ဆောင်ခြင်း
- Chainlit RAG Chat App ဖန်တီးခြင်းနှင့် deploy လုပ်ခြင်း
- WebGPU inference optimization techniques
- AI PC SDK integration နှင့် capabilities

**ကြာမြင့်ချိန်**: 3-4 နာရီ  
**လိုအပ်ချက်များ**: Session 1-3 ကို ပြီးမြောက်ထားရမည်၊ inference concepts ကို နားလည်ထားရမည်

---

### [5: Foundry Local ဖြင့် AI-Powered Agents ကို အလျင်အမြန် ဖန်တီးခြင်း](./05.AIPoweredAgents.md)
**အဓိကအချက်**: Rapid GenAI app development, system prompts, grounding, နှင့် agent architectures

**သင်လေ့လာမည့်အရာများ:**
- Foundry Local agent architecture နှင့် design patterns
- Agent behavior အတွက် system prompt engineering
- Agent responses အတွက် grounding techniques
- Rapid GenAI application development workflows
- Agent orchestration နှင့် multi-agent systems
- Production deployment strategies for AI agents

**ကြာမြင့်ချိန်**: 3-4 နာရီ  
**လိုအပ်ချက်များ**: Session 1-4 ကို ပြီးမြောက်ထားရမည်၊ AI agents ကို အခြေခံနားလည်ထားရမည်

---

### [6: Foundry Local - Models as Tools](./06.ModelsAsTools.md)
**အဓိကအချက်**: Modular AI solutions, on-device deployment, နှင့် enterprise scaling

**သင်လေ့လာမည့်အရာများ:**
- AI models ကို modular, customizable tools အဖြစ် အသုံးချခြင်း
- Cloud မလိုအပ်သော on-device deployment
- Low-latency, cost-efficient, နှင့် privacy-preserving inference
- SDK, API, နှင့် CLI integration patterns
- Specific use cases အတွက် model customization
- Local မှ Azure AI Foundry အထိ scaling strategies
- Enterprise-ready AI application architectures

**ကြာမြင့်ချိန်**: 3-4 နာရီ  
**လိုအပ်ချက်များ**: အရင် session များအားလုံးကို ပြီးမြောက်ထားရမည်၊ enterprise development အတွေ့အကြုံရှိရမည် (optional)

## Prerequisites

### System Requirements
- **Operating System**: Windows 11 (22H2 or later)
- **Memory**: 16GB RAM (32GB recommended for larger models)
- **Storage**: Model caching အတွက် 50GB free space
- **Hardware**: NPU-enabled device (Copilot+ PC) အကြံပြုထားသည်၊ GPU optional
- **Network**: Model များကို download လုပ်ရန် အတွက် high-speed internet

### Development Environment
- Visual Studio Code with AI Toolkit extension
- Python 3.10+ နှင့် pip
- Git for version control
- PowerShell or Command Prompt
- Azure CLI (optional for cloud integration)

### Knowledge Prerequisites
- AI/ML concepts အခြေခံနားလည်မှု
- Command line အသုံးပြုမှု
- Python programming အခြေခံ
- REST API concepts
- Prompting နှင့် model inference အခြေခံနားလည်မှု

## Module Timeline

**စုစုပေါင်း ခန့်မှန်းကြာမြင့်ချိန်**: 15-20 နာရီ

| Session | အဓိကအချက် | ကြာမြင့်ချိန် | အဆင့် |
|---------|------------|------|------------|
|  1 | Setup & Basics | 2-3 နာရီ | Beginner |
|  2 | AI Solutions | 2-3 နာရီ | Intermediate |
|  3 | Open Source | 2-3 နာရီ | Intermediate |
|  4 | Advanced Models | 3-4 နာရီ | Advanced |
|  5 | AI Agents | 3-4 နာရီ | Advanced |
|  6 | Enterprise Tools | 3-4 နာရီ | Expert |

## Key Resources

### Primary Documentation
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays Series](https://aka.ms/model-mondays)

### Community Resources
- [Foundry Local Community Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry Samples](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence)

## Learning Outcomes

ဒီ module ကို ပြီးမြောက်ပြီးနောက်၊ သင်သည်:

### Technical Mastery
- **Deploy နှင့် Manage**: Development နှင့် production environments များတွင် Foundry Local installations ကို လုပ်ဆောင်ခြင်း
- **Integrate Models**: Microsoft, Hugging Face, နှင့် community sources မှ model များကို seamless အဖြစ် အသုံးပြုခြင်း
- **Build Applications**: Advanced features နှင့် optimizations ဖြင့် production-ready AI applications ဖန်တီးခြင်း
- **Develop Agents**: Grounding, reasoning, နှင့် tool integration ဖြင့် sophisticated AI agents ဖန်တီးခြင်း

### Strategic Understanding
- **Architecture Decisions**: Local နှင့် cloud deployment အကြား informed choices လုပ်ဆောင်နိုင်ခြင်း
- **Performance Optimization**: Hardware configurations များအတွက် inference performance ကို optimize လုပ်ခြင်း
- **Enterprise Scaling**: Local prototypes မှ enterprise deployments အထိ scale လုပ်နိုင်သော applications ကို design လုပ်ခြင်း
- **Privacy နှင့် Security**: Local inference ဖြင့် privacy-preserving AI solutions ကို implement လုပ်ခြင်း

### Innovation Capabilities
- **Rapid Prototyping**: AI application concepts များကို အလျင်အမြန် ဖန်တီးနှင့် စမ်းသပ်ခြင်း
- **Community Integration**: Open-source models ကို အသုံးချခြင်းနှင့် ecosystem ကို အထောက်အကူပြုခြင်း
- **Advanced Patterns**: RAG, agents, နှင့် tool integration အပါအဝင် cutting-edge AI patterns များကို implement လုပ်ခြင်း
- **Future-Ready Development**: ပေါ်ပေါက်လာမည့် AI technologies နှင့် patterns များအတွက် အသင့်ဖြစ်သော applications ကို ဖန်တီးခြင်း

## Getting Started

1. **Prepare Your Environment**: Windows 11 နှင့် အကြံပြုထားသော hardware specifications ကို အဆင်သင့်ဖြစ်စေရန်
2. **Install Prerequisites**: Development tools နှင့် dependencies များကို install လုပ်ခြင်း
3. **Begin with Session 1**: Foundry Local installation နှင့် basic setup ကို စတင်ခြင်း
4. **Progress Sequentially**: အကောင်းဆုံး learning progression အတွက် sessions များကို အစဉ်လိုက် ပြီးမြောက်စွာ လုပ်ဆောင်ခြင်း
5. **Practice Continuously**: Hands-on exercises နှင့် projects များကို အသုံးပြု၍ concepts များကို လေ့ကျင့်ခြင်း

## Success Metrics

Module ၏ progress ကို အောက်ပါအတိုင်း tracking လုပ်ပါ:

- [ ] Foundry Local ကို အောင်မြင်စွာ install နှင့် configure လုပ်ခြင်း
- [ ] Model families 4 ခုကို အနည်းဆုံး deploy နှင့် run လုပ်ခြင်း
- [ ] Data integration ဖြင့် အပြည့်အစုံ AI solution တစ်ခုကို ဖန်တီးခြင်း
- [ ] Open-source models 2 ခုကို အနည်းဆုံး integrate လုပ်ခြင်း
- [ ] Functional RAG chat application တစ်ခုကို ဖန်တီးခြင်း
- [ ] AI agent တစ်ခုကို ဖန်တီးနှင့် deploy လုပ်ခြင်း
- [ ] Models-as-tools architecture ကို implement လုပ်ခြင်း

## Quick Start for Samples

### 1) Environment setup (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Start a local model (new terminal)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Run the Chainlit demo (Session 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Run the multi-agent coordinator (Session 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Connection errors တွေ့ရင် Foundry Local ကို validate လုပ်ပါ:
```cmd
curl http://localhost:8000/v1/models
```

### Router configuration (Session 6)
Router သည် quick health check ကို လုပ်ဆောင်ပြီး env-based config ကို support လုပ်ပါသည်:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

ဒီ module သည် edge AI development ၏ cutting edge ကို ကိုယ်စားပြုသည်။ ဒါဟာ Microsoft's enterprise-grade tools များနှင့် open-source ecosystem ၏ flexibility နှင့် innovation ကို ပေါင်းစည်းထားသည်။ Foundry Local ကို ကျွမ်းကျင်စွာ လေ့လာခြင်းဖြင့် သင်သည် AI application development ၏ အရှေ့တန်းတွင် ရပ်တည်နိုင်မည်ဖြစ်သည်။

Azure OpenAI (Session 2) အတွက် လိုအပ်သော environment variables နှင့် API version settings များကို sample README တွင် ကြည့်ပါ။

## Samples Overview

- `samples/01`: Foundry Local သို့ Quick REST chat (`chat_quickstart.py`)။
- `samples/02`: OpenAI SDK integration (`sdk_quickstart.py`)။
- `samples/03`: Model discovery + quick bench (`list_and_bench.cmd`)။
- `samples/04`: Chainlit RAG demo (`app.py`)။
- `samples/05`: Multi-agent orchestration (`python -m samples.05.agents.coordinator`)။
- `samples/06`: Models-as-Tools router (`python samples\06\router.py`)။

---

