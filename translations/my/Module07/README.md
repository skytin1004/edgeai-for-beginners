<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e9e31a2b5ff0f6a682a258fa859a8ff5",
  "translation_date": "2025-09-26T19:46:28+00:00",
  "source_file": "Module07/README.md",
  "language_code": "my"
}
-->
# အခန်း ၀၇ : EdgeAI နမူနာများ

Edge AI သည် အတန်းမြင့် ဉာဏ်ရည်တုကို edge computing နှင့် ပေါင်းစပ်ထားသော နည်းပညာဖြစ်ပြီး၊ cloud ချိတ်ဆက်မှုမရှိဘဲ စက်ပစ္စည်းပေါ်တွင် တိုက်ရိုက် အဆင့်မြင့် အချက်အလက်များကို အဆင်ပြေစွာ ဆောင်ရွက်နိုင်စေသည်။ ဒီအခန်းမှာ EdgeAI ကို အခြေခံပြီး မတူကွဲပြားတဲ့ ပလက်ဖောင်းနဲ့ framework များပေါ်မှာ AI မော်ဒယ်များကို edge မှာ အကောင်းဆုံး အသုံးချနိုင်မှုကို ပြသထားတဲ့ နမူနာ ၅ ခုကို လေ့လာပါမည်။

## ၁။ NVIDIA Jetson Orin Nano တွင် EdgeAI

NVIDIA Jetson Orin Nano သည် edge AI computing အတွက် အရေးပါသော တိုးတက်မှုတစ်ခုဖြစ်ပြီး၊ 67 TOPS အထိ AI စွမ်းဆောင်ရည်ကို credit-card အရွယ်အစားဖြင့် ပေးစွမ်းနိုင်သည်။ ဒီ platform သည် hobbyists, ကျောင်းသားများနှင့် professional developers အတွက် Generative AI ဖွံ့ဖြိုးတိုးတက်မှုကို ပိုမိုလွယ်ကူစေသည်။

### အဓိက အင်္ဂါရပ်များ
- 67 TOPS အထိ AI စွမ်းဆောင်ရည်ပေးစွမ်းခြင်း—ယခင်မော်ဒယ်ထက် 1.7X တိုးတက်မှု
- AI စွမ်းဆောင်ရည်အတွက် 1024 CUDA cores နှင့် 32 Tensor Cores
- 6-core Arm Cortex-A78AE v8.2 64-bit CPU (1.5 GHz အမြင့်ဆုံး frequency)
- $249 တန်ဖိုးဖြင့် developer, ကျောင်းသားများနှင့် maker များအတွက် အလွယ်တကူရရှိနိုင်သော platform

### အသုံးချမှုများ
Jetson Orin Nano သည် vision transformers, large language models, vision-language models စသည့် GenAI မော်ဒယ်များကို palm device ပေါ်တွင် run လုပ်နိုင်သည်။ AI-powered robotics, smart drones, intelligent cameras, autonomous edge devices စသည့် နေရာများတွင် အထူးကောင်းမွန်သည်။

**ပိုမိုလေ့လာရန်**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## ၂။ .NET MAUI နှင့် ONNX Runtime GenAI ဖြင့် Mobile EdgeAI

ဒီ solution သည် .NET MAUI (Multi-platform App UI) နှင့် ONNX Runtime GenAI ကို အသုံးပြု၍ Generative AI နှင့် Large Language Models (LLMs) ကို cross-platform mobile applications တွင် ပေါင်းစပ်အသုံးချပုံကို ပြသသည်။ Android နှင့် iOS devices ပေါ်တွင် native အနေဖြင့် AI-powered mobile applications ဖန်တီးရန် .NET developer များအတွက် အခွင့်အရေးပေးသည်။

### အဓိက အင်္ဂါရပ်များ
- .NET MAUI framework အပေါ် အခြေခံပြီး Android နှင့် iOS applications အတွက် single codebase
- ONNX Runtime GenAI ဖြင့် mobile devices ပေါ်တွင် generative AI မော်ဒယ်များ run လုပ်နိုင်ခြင်း
- CPU, GPU, mobile AI processors စသည့် hardware accelerators များကို ထောက်ပံ့ခြင်း
- iOS အတွက် CoreML နှင့် Android အတွက် NNAPI အထူး optimize လုပ်ထားခြင်း
- Generative AI loop အပြည့်အစုံကို implement လုပ်ထားခြင်း (pre/post processing, inference, logits processing, search/sampling, KV cache management)

### ဖွံ့ဖြိုးတိုးတက်မှု အကျိုးကျေးဇူးများ
.NET MAUI သည် C# နှင့် .NET အတတ်ပညာရှိ developer များအတွက် cross-platform AI applications ဖန်တီးရန် အခွင့်အရေးပေးသည်။ ONNX Runtime GenAI သည် Llama, Mistral, Phi, Gemma စသည့် မော်ဒယ်များကို support လုပ်ပြီး ARM64 kernels ကို optimize လုပ်ထားသည်။

### အသုံးချမှုများ
ဒီ solution သည် intelligent chatbots, image recognition apps, language translation tools, personalized recommendation systems စသည့် mobile applications ဖန်တီးရန် အထူးသင့်လျော်သည်။

**ပိုမိုလေ့လာရန်**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## ၃။ Azure EdgeAI နှင့် Small Language Models Engine

Microsoft Azure EdgeAI သည် Small Language Models (SLMs) ကို cloud-edge hybrid ပုံစံတွင် ထိရောက်စွာ deploy လုပ်ရန် အထူးအာရုံစိုက်ထားသည်။ Cloud-scale AI services နှင့် edge deployment အကြားကွာဟချက်ကို ဖြည့်ဆည်းပေးသည်။

### Architecture အကျိုးကျေးဇူးများ
- Azure AI services နှင့် seamless integration
- ONNX Runtime ဖြင့် SLMs/LLMs နှင့် multi-modal models ကို cloud နှင့် edge ပေါ်တွင် run လုပ်နိုင်ခြင်း
- Enterprise-scale deployment အတွက် optimize လုပ်ထားခြင်း
- မော်ဒယ်များကို ဆက်လက် update နှင့် စီမံခန့်ခွဲနိုင်ခြင်း

### အသုံးချမှုများ
Azure EdgeAI သည် enterprise-grade AI deployment အတွက် အထူးသင့်လျော်ပြီး intelligent document processing, real-time analytics, hybrid AI workflows စသည့် နေရာများတွင် အထူးကောင်းမွန်သည်။

**ပိုမိုလေ့လာရန်**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [၄။ Windows ML ဖြင့် EdgeAI](./windowdeveloper.md)

Windows ML သည် Microsoft ရဲ့ cutting-edge runtime ဖြစ်ပြီး၊ on-device model inference ကို အထူး optimize လုပ်ထားသည်။ Windows AI Foundry အခြေခံအနေဖြင့် AI-powered Windows applications ဖန်တီးရန် developer များအတွက် အခွင့်အရေးပေးသည်။

### Platform စွမ်းရည်များ
- Windows 11 PCs (version 24H2 build 26100) အထက်တွင် run လုပ်နိုင်ခြင်း
- x64 နှင့် ARM64 PC hardware အားလုံးတွင် အလုပ်လုပ်နိုင်ခြင်း
- Developer များအတွက် မော်ဒယ်များကို အလွယ်တကူ deploy လုပ်နိုင်ခြင်း
- Hardware အမျိုးမျိုးကို target လုပ်ရန် app builds များကို မလိုအပ်တော့ခြင်း

### Developer အကျိုးကျေးဇူးများ
Windows ML သည် hardware နှင့် execution providers ကို abstract လုပ်ထားပြီး developer များအတွက် coding အပေါ် အာရုံစိုက်နိုင်စေသည်။ Windows ML သည် NPU, GPU, CPU များကို အဆင့်မြှင့်တင်ပြီး အဆင်ပြေစွာ update လုပ်ပေးသည်။

**ပိုမိုလေ့လာရန်**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](./windowdeveloper.md)

## [၅။ Foundry Local Applications ဖြင့် EdgeAI](./foundrylocal.md)

Foundry Local သည် Windows နှင့် Mac developer များအတွက် Retrieval Augmented Generation (RAG) applications ကို local resources အသုံးပြု၍ ဖန်တီးရန် အခွင့်အရေးပေးသည်။ ဒီနည်းလမ်းသည် privacy-focused AI solutions ကို local infrastructure ပေါ်တွင် run လုပ်နိုင်စေသည်။

### Technical Architecture
- Phi language model, Local Embeddings, Semantic Kernel ကို ပေါင်းစပ်ထားခြင်း
- Embeddings ကို floating-point values (vectors) အဖြစ် represent လုပ်ထားခြင်း
- Semantic Kernel သည် RAG pipeline ကို seamless အဖြစ် integrate လုပ်ထားခြင်း
- SQLite နှင့် Qdrant စသည့် local vector databases ကို support လုပ်ထားခြင်း

### Implementation အကျိုးကျေးဇူးများ
RAG သည် "အချက်အလက်များကို ရှာဖွေပြီး prompt ထဲထည့်ခြင်း" ကို privacy-focused နည်းလမ်းဖြင့် local infrastructure ပေါ်တွင် run လုပ်နိုင်စေသည်။

**ပိုမိုလေ့လာရန်**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local သည် ONNX Runtime ကို အသုံးပြု၍ Windows ပေါ်တွင် OpenAI-compatible REST server ကို run လုပ်နိုင်စေသည်။

- စတင်အသုံးပြုရန်: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architecture: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI reference: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Full Windows guide: [foundrylocal.md](./foundrylocal.md)

Windows တွင် install/upgrade (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

CLI categories ကို explore လုပ်ရန်:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

မော်ဒယ် run လုပ်ပြီး dynamic endpoint ကို ရှာဖွေပါ:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

REST check (PORT ကို status မှာပြောင်းပါ):
```cmd
curl -s http://localhost:PORT/v1/models
```

Tips:
- SDK integration: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- မော်ဒယ်ကို compile လုပ်ရန်: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI Development Resources

Windows platform ကို target လုပ်သော developer များအတွက် Windows EdgeAI ecosystem အပြည့်အစုံကို လေ့လာရန် guide တစ်ခုကို ဖန်တီးထားသည်။

### Windows AI Foundry Platform
Windows AI Foundry platform သည် Edge AI development အတွက် tools နှင့် APIs များကို အပြည့်အစုံပေးစွမ်းသည်။

**Comprehensive Guide**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

ဒီ guide တွင် ပါဝင်သည်:
- Windows AI Foundry platform overview
- Phi Silica API
- Computer Vision APIs
- Windows ML runtime integration
- Foundry Local CLI
- Hardware optimization strategies
- Implementation examples

### [AI Toolkit for Edge AI Development](./aitoolkit.md)
Visual Studio Code အသုံးပြု developer များအတွက် AI Toolkit extension သည် Edge AI applications ဖန်တီးရန် အထူး designed လုပ်ထားသည်။

**Development Guide**: [AI Toolkit for Edge AI Development](./aitoolkit.md)

AI Toolkit guide တွင် ပါဝင်သည်:
- Model discovery
- Local testing
- ONNX နှင့် Ollama integration
- Model conversion
- Agent development
- Performance evaluation
- Deployment preparation

## နိဂုံး

ဒီ EdgeAI နမူနာ ၅ ခုသည် edge AI solutions များ၏ maturity နှင့် diversity ကို ပြသသည်။ Hardware-accelerated edge devices, cross-platform mobile development, enterprise cloud-edge integration, Windows-native applications, privacy-focused RAG implementations စသည့် နေရာများတွင် developer များအတွက် အခွင့်အရေးပေးသည်။

Jetson Orin Nano, ONNX Runtime GenAI, Azure EdgeAI, Windows ML, Foundry Local တို့သည် EdgeAI development အတွက် အပြည့်အစုံ ecosystem ကို ဖန်တီးပေးသည်။

---

