<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb6eadc312d5658a0cd71c0085b43742",
  "translation_date": "2025-09-23T00:24:52+00:00",
  "source_file": "Module07/README.md",
  "language_code": "my"
}
-->
# အခန်း ၀၇ : EdgeAI နမူနာများ

Edge AI သည် အတန်းမြင့် ဉာဏ်ရည်တုနှင့် edge computing တို့ပေါင်းစပ်မှုကို ကိုယ်စားပြုပြီး cloud ချိတ်ဆက်မှုမရှိဘဲ စက်ပစ္စည်းများပေါ်တွင် တိုက်ရိုက် အတန်းမြင့် အချက်အလက်များကို အဆင့်မြင့်လုပ်ဆောင်နိုင်စေသည်။ ဒီအခန်းမှာ EdgeAI ကို အခြေခံပြီး platform နှင့် framework များအမျိုးမျိုးတွင် အသုံးပြုထားသော နမူနာ ၅ ခုကို လေ့လာမည်ဖြစ်ပြီး edge တွင် AI မော်ဒယ်များကို အတန်းမြင့်အောင် လုပ်ဆောင်နိုင်မှုနှင့် အကျိုးကျေးဇူးများကို ပြသထားသည်။

## ၁။ NVIDIA Jetson Orin Nano တွင် EdgeAI

NVIDIA Jetson Orin Nano သည် edge AI computing အတွက် အရေးပါသော တိုးတက်မှုတစ်ခုကို ကိုယ်စားပြုပြီး 67 TOPS အထိ AI စွမ်းဆောင်ရည်ကို credit-card အရွယ်အစားဖြင့် ပေးစွမ်းနိုင်သည်။ ဒီအတန်းမြင့် edge AI platform သည် hobbyist, ကျောင်းသားများနှင့် professional developer များအတွက် Generative AI ဖွံ့ဖြိုးတိုးတက်မှုကို ပိုမိုလွယ်ကူစေသည်။

### အဓိက အင်္ဂါရပ်များ
- 67 TOPS အထိ AI စွမ်းဆောင်ရည်ပေးစွမ်းခြင်း—ယခင်မော်ဒယ်ထက် 1.7X တိုးတက်မှု
- AI လုပ်ဆောင်မှုအတွက် 1024 CUDA cores နှင့် 32 Tensor Cores အထိ
- 6-core Arm Cortex-A78AE v8.2 64-bit CPU (1.5 GHz အမြင့်ဆုံး frequency)
- $249 သာရှိသော စျေးနှုန်းဖြင့် developer, ကျောင်းသားများနှင့် maker များအတွက် အလွယ်တကူရရှိနိုင်သော platform

### အသုံးချမှုများ
Jetson Orin Nano သည် vision transformers, large language models, vision-language models အပါအဝင် ယနေ့ခေတ် Generative AI မော်ဒယ်များကို အထူးကောင်းမွန်စွာ လုပ်ဆောင်နိုင်သည်။ GenAI အသုံးချမှုများအတွက် အထူးဒီဇိုင်းပြုလုပ်ထားပြီး palm device ပေါ်တွင် LLM များစွာကို လုပ်ဆောင်နိုင်သည်။ အထူးအသုံးချမှုများမှာ AI-powered robotics, smart drones, intelligent cameras, autonomous edge devices တို့ဖြစ်သည်။

**ပိုမိုလေ့လာရန်**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## ၂။ .NET MAUI နှင့် ONNX Runtime GenAI ဖြင့် Mobile Applications တွင် EdgeAI

ဒီနမူနာသည် Generative AI နှင့် Large Language Models (LLMs) ကို .NET MAUI (Multi-platform App UI) နှင့် ONNX Runtime GenAI အသုံးပြု၍ cross-platform mobile applications တွင် ပေါင်းစပ်အသုံးပြုနည်းကို ပြသသည်။ ဒီနည်းလမ်းသည် .NET developer များအတွက် Android နှင့် iOS စက်ပစ္စည်းများပေါ်တွင် native အတန်းမြင့် AI-powered mobile applications ဖန်တီးနိုင်စေသည်။

### အဓိက အင်္ဂါရပ်များ
- .NET MAUI framework အပေါ် အခြေခံပြီး Android နှင့် iOS application များအတွက် single codebase ပေးစွမ်းခြင်း
- ONNX Runtime GenAI ပေါင်းစပ်မှုသည် mobile devices ပေါ်တွင် Generative AI မော်ဒယ်များကို တိုက်ရိုက် လုပ်ဆောင်နိုင်စေသည်
- CPU, GPU နှင့် mobile AI processor အထူးပြု hardware accelerators များကို ပံ့ပိုးပေးခြင်း
- ONNX Runtime မှတဆင့် iOS အတွက် CoreML နှင့် Android အတွက် NNAPI ကဲ့သို့သော platform-specific optimizations
- Generative AI loop အပြည့်အစုံကို pre/post processing, inference, logits processing, search and sampling, KV cache management အပါအဝင် လုပ်ဆောင်နိုင်ခြင်း

### ဖွံ့ဖြိုးတိုးတက်မှု အကျိုးကျေးဇူးများ
.NET MAUI နည်းလမ်းသည် developer များအတွက် ရှိပြီးသား C# နှင့် .NET ကျွမ်းကျင်မှုများကို အသုံးပြု၍ cross-platform AI applications ဖန်တီးနိုင်စေသည်။ ONNX Runtime GenAI framework သည် Llama, Mistral, Phi, Gemma အပါအဝင် မော်ဒယ် architecture များစွာကို ပံ့ပိုးပေးသည်။ ARM64 kernels များကို optimize လုပ်ခြင်းဖြင့် INT4 quantized matrix multiplication ကို မြန်ဆန်စွာ လုပ်ဆောင်နိုင်စေပြီး mobile hardware ပေါ်တွင် စွမ်းဆောင်ရည်မြင့်မားစေသည်။

### အသုံးချမှုများ
ဒီနည်းလမ်းသည် .NET နည်းပညာများကို အသုံးပြု၍ AI-powered mobile applications ဖန်တီးလိုသော developer များအတွက် အထူးသင့်လျော်သည်။ intelligent chatbots, image recognition apps, language translation tools, personalized recommendation systems တို့ကို offline အခြေအနေတွင် privacy မြင့်မားစွာ လုပ်ဆောင်နိုင်စေသည်။

**ပိုမိုလေ့လာရန်**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## ၃။ Azure EdgeAI နှင့် Small Language Models Engine

Microsoft ၏ Azure-based EdgeAI ဖြေရှင်းနည်းသည် Small Language Models (SLMs) များကို cloud-edge hybrid ပတ်ဝန်းကျင်တွင် ထိရောက်စွာ အသုံးချနိုင်ရန် အဓိကထားသည်။ ဒီနည်းလမ်းသည် cloud-scale AI services နှင့် edge deployment လိုအပ်ချက်များအကြား ချိတ်ဆက်မှုကို ပံ့ပိုးပေးသည်။

### Architecture အကျိုးကျေးဇူးများ
- Azure AI services နှင့် seamless integration
- ONNX Runtime ဖြင့် SLMs/LLMs နှင့် multi-modal models ကို စက်ပစ္စည်းပေါ်တွင်နှင့် cloud တွင် လုပ်ဆောင်နိုင်ခြင်း
- Enterprise-scale deployment အတွက် optimize လုပ်ထားခြင်း
- မော်ဒယ်များကို ဆက်လက် update နှင့် စီမံခန့်ခွဲနိုင်ခြင်း

### အသုံးချမှုများ
Azure EdgeAI implementation သည် enterprise-grade AI deployment လိုအပ်ချက်များနှင့် cloud management capabilities ရှိသော အခြေအနေများတွင် အထူးကောင်းမွန်သည်။ intelligent document processing, real-time analytics, hybrid AI workflows တို့ကို cloud နှင့် edge computing resources နှစ်ခုလုံးကို အသုံးပြု၍ လုပ်ဆောင်နိုင်သည်။

**ပိုမိုလေ့လာရန်**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## ၄။ Windows ML ဖြင့် EdgeAI

Windows ML သည် Microsoft ၏ cutting-edge runtime ဖြစ်ပြီး on-device model inference ကို အထူး optimize လုပ်ထားပြီး deployment ကို လွယ်ကူစေသည်။ Windows AI Foundry ၏ အခြေခံအဆောက်အအုံအဖြစ် တည်ရှိသည်။ ဒီ platform သည် PC hardware အပြည့်အဝကို အသုံးပြုနိုင်သော AI-powered Windows applications ဖန်တီးရန် developer များကို အခွင့်အရေးပေးသည်။

### Platform စွမ်းဆောင်ရည်များ
- Windows 11 PCs (version 24H2, build 26100) အထက်တွင် အလုပ်လုပ်နိုင်ခြင်း
- x64 နှင့် ARM64 PC hardware အားလုံးတွင် အလုပ်လုပ်နိုင်ခြင်း၊ NPU/GPU မရှိသော PCs တွင်ပါ အလုပ်လုပ်နိုင်ခြင်း
- Developer များအတွက် မော်ဒယ်များကို ကိုယ်ပိုင်ဖန်တီးပြီး AMD, Intel, NVIDIA, Qualcomm စသည်တို့၏ silicon partner ecosystem အတွင်း အထိရောက်ဆုံး deployment လုပ်နိုင်ခြင်း
- Infrastructure APIs ကို အသုံးပြု၍ silicon မျိုးစုံ targeting အတွက် app builds များကို မတည်ဆောက်ရတော့ပဲ လွယ်ကူစေခြင်း

### Developer အကျိုးကျေးဇူးများ
Windows ML သည် hardware နှင့် execution providers ကို abstract လုပ်ပေးပြီး developer များအတွက် code ရေးသားခြင်းကို အလွယ်ကူစေသည်။ Windows ML သည် NPU, GPU, CPU များကို အဆက်မပြတ် update လုပ်ပေးပြီး အသစ်ထွက်လာသော hardware များကို support လုပ်ပေးသည်။ Windows hardware ecosystem အတွင်း AI development အတွက် unified framework ကို ပံ့ပိုးပေးသည်။

**ပိုမိုလေ့လာရန်**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](../windowdeveloper.md) - Windows Edge AI ဖွံ့ဖြိုးတိုးတက်မှုအတွက် လမ်းညွှန်ချက်

## ၅။ Foundry Local Applications ဖြင့် EdgeAI

Foundry Local သည် Retrieval Augmented Generation (RAG) applications များကို .NET အသုံးပြု၍ local resources တွင် ဖန်တီးနိုင်စေသည်။ ဒီနည်းလမ်းသည် local language models နှင့် semantic search capabilities ကို ပေါင်းစပ်ထားပြီး privacy-focused AI solutions များကို local infrastructure ပေါ်တွင် လုပ်ဆောင်နိုင်စေသည်။

### Technical Architecture
- Phi language model, Local Embeddings, Semantic Kernel တို့ကို ပေါင်းစပ်၍ RAG scenario ဖန်တီးခြင်း
- Embeddings ကို floating-point values (vectors) အဖြစ် အသုံးပြု၍ content နှင့် semantic meaning ကို ကိုယ်စားပြုခြင်း
- Semantic Kernel သည် Phi နှင့် Smart Components ကို ပေါင်းစပ်၍ seamless RAG pipeline ဖန်တီးရန် အဓိက orchestrator အဖြစ် လုပ်ဆောင်ခြင်း
- SQLite နှင့် Qdrant ကဲ့သို့သော local vector databases များကို ပံ့ပိုးပေးခြင်း

### Implementation အကျိုးကျေးဇူးများ
RAG သည် "အချက်အလက်များကို ရှာဖွေပြီး prompt ထဲသို့ ထည့်ခြင်း" ဆိုသော အလွယ်ကူဆုံးနည်းလမ်းဖြစ်သည်။ ဒီ local implementation သည် data privacy ကို အထူးကောင်းမွန်စွာ ထိန်းသိမ်းပေးပြီး custom knowledge bases အပေါ် အခြေခံထားသော intelligent responses ကို ပေးစွမ်းနိုင်သည်။ ဒီနည်းလမ်းသည် data sovereignty နှင့် offline operation လိုအပ်သော enterprise scenarios များအတွက် အထူးတန်ဖိုးရှိသည်။

**ပိုမိုလေ့လာရန်**: [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local သည် ONNX Runtime powered OpenAI-compatible REST server ကို Windows ပေါ်တွင် local မော်ဒယ်များကို run လုပ်ရန် ပံ့ပိုးပေးသည်။ အောက်တွင် validated အကျဉ်းချုပ်ကို ဖော်ပြထားပြီး အပြည့်အစုံကို official docs တွင် ကြည့်ရှုနိုင်သည်။

- စတင်အသုံးပြုရန်: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architecture: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI reference: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Windows အတွက် လမ်းညွှန်ချက်: [foundrylocal.md](./foundrylocal.md)

Windows (cmd.exe) တွင် install သို့မဟုတ် upgrade:
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

မော်ဒယ် run လုပ်ပြီး dynamic endpoint ကို ရှာဖွေရန်:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

REST check ကို models list လုပ်ရန် (status မှ PORT ကို အစားထိုးပါ):
```cmd
curl -s http://localhost:PORT/v1/models
```

Tips:
- SDK integration: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- ကိုယ်ပိုင်မော်ဒယ် (compile): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI Development Resources

Windows platform ကို အထူးပစ်မှတ်ထားသော developer များအတွက် Windows EdgeAI ecosystem အပြည့်အစုံကို ဖော်ပြထားသော လမ်းညွှန်ချက်ကို ဖန်တီးထားသည်။ ဒီ resource သည် Windows AI Foundry အပါအဝင် APIs, tools, EdgeAI ဖွံ့ဖြိုးတိုးတက်မှုအတွက် အကောင်းဆုံးနည်းလမ်းများကို အသေးစိတ်ဖော်ပြထားသည်။

### Windows AI Foundry Platform
Windows AI Foundry platform သည် Windows စက်ပစ္စည်းများပေါ်တွင် Edge AI ဖွံ့ဖြိုးတိုးတက်မှုအတွက် အထူးဒီဇိုင်းပြုလုပ်ထားသော tools နှင့် APIs များကို ပံ့ပိုးပေးသည်။ NPU-accelerated hardware, Windows ML integration, platform-specific optimization techniques အထူးပံ့ပိုးပေးထားသည်။

**Comprehensive Guide**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

ဒီလမ်းညွှန်ချက်တွင် ပါဝင်သည်-
- Windows AI Foundry platform overview နှင့် components
- NPU hardware ပေါ်တွင် အထိရောက်ဆုံး inference အတွက် Phi Silica API
- Computer Vision APIs (image processing နှင့် OCR)
- Windows ML runtime integration နှင့် optimization
- Foundry Local CLI (local development နှင့် testing)
- Windows devices အတွက် hardware optimization strategies
- Practical implementation examples နှင့် အကောင်းဆုံးနည်းလမ်းများ

### Edge AI Development အတွက် AI Toolkit
Visual Studio Code ကို အသုံးပြုသော developer များအတွက် AI Toolkit extension သည် Edge AI applications ဖန်တီးခြင်း, စမ်းသပ်ခြင်း, deployment အတွက် အထူးဒီဇိုင်းပြုလုပ်ထားသော development environment ကို ပံ့ပိုးပေးသည်။ ဒီ toolkit သည် Edge AI development workflow အားလုံးကို VS Code အတွင်း streamline လုပ်ပေးသည်။

**Development Guide**: [AI Toolkit for Edge AI Development](../aitoolkit.md)

AI Toolkit လမ်းညွှန်ချက်တွင် ပါဝင်သည်-
- Edge deployment အတွက် မော်ဒယ် ရှာဖွေခြင်းနှင့် ရွေးချယ်ခြင်း
- Local testing နှင့် optimization workflows
- Edge မော်ဒယ်များအတွက် ONNX နှင့် Ollama integration
- မော်ဒယ် conversion နှင့် quantization techniques
- Edge scenarios အတွက် agent development
- စွမ်းဆောင်ရည် အကဲဖြတ်ခြင်းနှင့် monitoring
- Deployment ပြင်ဆင်ခြင်းနှင့် အကောင်းဆုံးနည်းလမ်းများ

## နိဂုံး

ဒီ EdgeAI implementation ၅ ခုသည် ယနေ့ခေတ် Edge AI ဖြေရှင်းနည်းများ၏ အဆင့်မြင့်မှုနှင့် အမျိုးမျိုးသော diversity ကို ပြသသည်။ Jetson Orin Nano ကဲ့သို့ hardware-accelerated edge devices မှ ONNX Runtime GenAI နှင့် Windows ML ကဲ့သို့ software frameworks အထိ developer များအတွက် edge တွင် intelligent applications ဖန်တီးရန် များစွာသော ရွေးချယ်မှုများကို ပေးစွမ်းသည်။

ဒီ platform များအားလုံးတွင် AI စွမ်းရည်များကို democratize လုပ်ခြင်းသည် အဓိကဖြစ်ပြီး developer များအတွက် skill level မျိုးစုံနှင့် use case မျိုးစုံအတွက် sophisticated machine learning ကို လွယ်ကူစွာ အသုံးပြုနိုင်စေသည်။ Mobile applications, desktop software, embedded systems တို့ကို ဖန်တီးလိုသော developer များအတွက် ဒီ EdgeAI solutions များသည် edge တွင် privacy နှင့် efficiency ရှိသော next-generation intelligent applications ဖန်တီးရန် အခြေခံအဆောက်အအုံကို ပံ့ပိုးပေးသည်။

Jetson Orin Nano သည် hardware-accelerated edge computing အတွက် အထူးကောင်းမွန်ပြီး ONNX Runtime GenAI သည် cross-platform mobile development အတွက် အထူးသင့်လျော်သည်။ Azure EdgeAI သည် enterprise cloud-edge integration အတွက် အထူးကောင်းမွန်ပြီး Windows ML သည် Windows-native applications အတွက် အထူးသင့်လျော်သည်။ Foundry Local သည် privacy-focused RAG implementations အတွက် အထူးတန်ဖိုးရှိသည်။ EdgeAI development အတွက် comprehensive ecosystem ကို ပေါင်းစပ်ထားသော platform များဖြစ်သည်။

---

