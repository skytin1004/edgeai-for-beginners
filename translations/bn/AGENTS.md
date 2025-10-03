<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:28:28+00:00",
  "source_file": "AGENTS.md",
  "language_code": "bn"
}
-->
# AGENTS.md

## প্রকল্পের সংক্ষিপ্ত বিবরণ

EdgeAI for Beginners একটি বিস্তৃত শিক্ষামূলক সংগ্রহশালা যা ছোট ভাষার মডেল (SLMs) ব্যবহার করে Edge AI উন্নয়ন শেখায়। এই কোর্সে EdgeAI এর মৌলিক বিষয়, মডেল ডিপ্লয়মেন্ট, অপ্টিমাইজেশন কৌশল এবং Microsoft Foundry Local এবং বিভিন্ন AI ফ্রেমওয়ার্ক ব্যবহার করে প্রোডাকশন-রেডি ইমপ্লিমেন্টেশন অন্তর্ভুক্ত রয়েছে।

**মূল প্রযুক্তি:**
- Python 3.8+ (AI/ML নমুনার জন্য প্রধান ভাষা)
- .NET C# (AI/ML নমুনা)
- JavaScript/Node.js এবং Electron (ডেস্কটপ অ্যাপ্লিকেশনের জন্য)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI ফ্রেমওয়ার্ক: LangChain, Semantic Kernel, Chainlit
- মডেল অপ্টিমাইজেশন: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**সংগ্রহশালার ধরন:** ৮টি মডিউল এবং ১০টি বিস্তৃত নমুনা অ্যাপ্লিকেশন সহ শিক্ষামূলক বিষয়বস্তু সংগ্রহশালা

**আর্কিটেকচার:** মাল্টি-মডিউল লার্নিং পাথ যা Edge AI ডিপ্লয়মেন্ট প্যাটার্ন প্রদর্শন করে

## সংগ্রহশালার কাঠামো

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## সেটআপ কমান্ড

### সংগ্রহশালা সেটআপ

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python নমুনা সেটআপ (Module08 এবং Python নমুনা)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Node.js নমুনা সেটআপ (নমুনা 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Local সেটআপ

Module08 নমুনা চালানোর জন্য Foundry Local প্রয়োজন:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## উন্নয়ন কর্মপ্রবাহ

### বিষয়বস্তু উন্নয়ন

এই সংগ্রহশালায় প্রধানত **Markdown শিক্ষামূলক বিষয়বস্তু** রয়েছে। পরিবর্তন করার সময়:

1. সংশ্লিষ্ট মডিউল ডিরেক্টরিতে `.md` ফাইল সম্পাদনা করুন
2. বিদ্যমান ফরম্যাটিং প্যাটার্ন অনুসরণ করুন
3. কোড উদাহরণগুলি সঠিক এবং পরীক্ষিত কিনা নিশ্চিত করুন
4. প্রয়োজন হলে সংশ্লিষ্ট অনুবাদিত বিষয়বস্তু আপডেট করুন (অথবা অটোমেশনকে এটি করতে দিন)

### নমুনা অ্যাপ্লিকেশন উন্নয়ন

Python নমুনার জন্য (নমুনা 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electron নমুনার জন্য (নমুনা 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### নমুনা অ্যাপ্লিকেশন পরীক্ষা

Python নমুনার জন্য স্বয়ংক্রিয় পরীক্ষা নেই তবে সেগুলি চালিয়ে যাচাই করা যেতে পারে:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron নমুনার জন্য পরীক্ষার অবকাঠামো রয়েছে:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## পরীক্ষার নির্দেশনা

### বিষয়বস্তু যাচাই

সংগ্রহশালায় স্বয়ংক্রিয় অনুবাদ কর্মপ্রবাহ ব্যবহার করা হয়। অনুবাদের জন্য ম্যানুয়াল পরীক্ষা প্রয়োজন নেই।

**বিষয়বস্তু পরিবর্তনের জন্য ম্যানুয়াল যাচাই:**
1. `.md` ফাইল প্রিভিউ করে Markdown রেন্ডারিং পর্যালোচনা করুন
2. নিশ্চিত করুন যে সমস্ত লিঙ্ক বৈধ লক্ষ্যবস্তুতে নির্দেশ করে
3. ডকুমেন্টেশনে অন্তর্ভুক্ত কোড স্নিপেট পরীক্ষা করুন
4. নিশ্চিত করুন যে চিত্রগুলি সঠিকভাবে লোড হচ্ছে

### নমুনা অ্যাপ্লিকেশন পরীক্ষা

**Module08/samples/08 (Electron অ্যাপ) এর বিস্তৃত পরীক্ষা রয়েছে:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python নমুনাগুলি ম্যানুয়ালি পরীক্ষা করা উচিত:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## কোড স্টাইল নির্দেশিকা

### Markdown বিষয়বস্তু

- ধারাবাহিক শিরোনাম শ্রেণিবিন্যাস ব্যবহার করুন (# শিরোনামের জন্য, ## প্রধান বিভাগগুলির জন্য, ### উপবিভাগগুলির জন্য)
- ভাষা নির্দিষ্টকারী সহ কোড ব্লক অন্তর্ভুক্ত করুন: ```python, ```bash, ```javascript
- টেবিল, তালিকা এবং জোর দেওয়ার জন্য বিদ্যমান ফরম্যাটিং অনুসরণ করুন
- লাইনগুলি পাঠযোগ্য রাখুন (~80-100 অক্ষর লক্ষ্য করুন, তবে কঠোর নয়)
- অভ্যন্তরীণ রেফারেন্সের জন্য আপেক্ষিক লিঙ্ক ব্যবহার করুন

### Python কোড স্টাইল

- PEP 8 কনভেনশন অনুসরণ করুন
- যেখানে প্রয়োজন টাইপ হিন্ট ব্যবহার করুন
- ফাংশন এবং ক্লাসের জন্য ডকস্ট্রিং অন্তর্ভুক্ত করুন
- অর্থপূর্ণ ভেরিয়েবল নাম ব্যবহার করুন
- ফাংশনগুলিকে ফোকাসড এবং সংক্ষিপ্ত রাখুন

### JavaScript/Node.js কোড স্টাইল

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**মূল কনভেনশন:**
- নমুনা 08-এ ESLint কনফিগারেশন প্রদান করা হয়েছে
- কোড ফরম্যাটিংয়ের জন্য Prettier ব্যবহার করুন
- আধুনিক ES6+ সিনট্যাক্স ব্যবহার করুন
- কোডবেসে বিদ্যমান প্যাটার্ন অনুসরণ করুন

## পুল রিকোয়েস্ট নির্দেশিকা

### শিরোনাম ফরম্যাট
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### জমা দেওয়ার আগে

**বিষয়বস্তু পরিবর্তনের জন্য:**
- সমস্ত পরিবর্তিত Markdown ফাইল প্রিভিউ করুন
- লিঙ্ক এবং চিত্র কাজ করছে কিনা যাচাই করুন
- টাইপো এবং ব্যাকরণগত ত্রুটি পরীক্ষা করুন

**নমুনা কোড পরিবর্তনের জন্য (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python নমুনা পরিবর্তনের জন্য:**
- নমুনাটি সফলভাবে চালানো যাচাই করুন
- ত্রুটি পরিচালনা কাজ করছে কিনা যাচাই করুন
- Foundry Local এর সাথে সামঞ্জস্য পরীক্ষা করুন

### পর্যালোচনা প্রক্রিয়া

- শিক্ষামূলক বিষয়বস্তু পরিবর্তনগুলি সঠিকতা এবং স্পষ্টতার জন্য পর্যালোচনা করা হয়
- কোড নমুনাগুলি কার্যকারিতার জন্য পরীক্ষা করা হয়
- অনুবাদ আপডেটগুলি GitHub Actions দ্বারা স্বয়ংক্রিয়ভাবে পরিচালিত হয়

## অনুবাদ ব্যবস্থা

**গুরুত্বপূর্ণ:** এই সংগ্রহশালা GitHub Actions এর মাধ্যমে স্বয়ংক্রিয় অনুবাদ ব্যবহার করে।

- অনুবাদগুলি `/translations/` ডিরেক্টরিতে রয়েছে (৫০+ ভাষা)
- `co-op-translator.yml` কর্মপ্রবাহের মাধ্যমে স্বয়ংক্রিয়
- **অনুবাদ ফাইলগুলি ম্যানুয়ালি সম্পাদনা করবেন না** - সেগুলি ওভাররাইট করা হবে
- মূল ইংরেজি সোর্স ফাইলগুলি শুধুমাত্র রুট এবং মডিউল ডিরেক্টরিতে সম্পাদনা করুন
- `main` ব্রাঞ্চে পুশ করার সময় অনুবাদগুলি স্বয়ংক্রিয়ভাবে তৈরি হয়

## Foundry Local ইন্টিগ্রেশন

Module08 এর বেশিরভাগ নমুনা চালানোর জন্য Microsoft Foundry Local চালু থাকা প্রয়োজন:

### Foundry Local শুরু করা
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### Foundry Local যাচাই করা
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### নমুনার জন্য পরিবেশ ভেরিয়েবল

বেশিরভাগ নমুনা এই পরিবেশ ভেরিয়েবলগুলি ব্যবহার করে:
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## বিল্ড এবং ডিপ্লয়মেন্ট

### বিষয়বস্তু ডিপ্লয়মেন্ট

এই সংগ্রহশালা প্রধানত ডকুমেন্টেশন - বিষয়বস্তু জন্য কোনো বিল্ড প্রক্রিয়া প্রয়োজন নেই।

### নমুনা অ্যাপ্লিকেশন বিল্ডিং

**Electron অ্যাপ্লিকেশন (Module08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python নমুনা:**
কোনো বিল্ড প্রক্রিয়া নেই - নমুনাগুলি সরাসরি Python ইন্টারপ্রেটার দিয়ে চালানো হয়।

## সাধারণ সমস্যা এবং সমাধান

### Foundry Local চালু নেই
**সমস্যা:** নমুনাগুলি সংযোগ ত্রুটির সাথে ব্যর্থ হয়

**সমাধান:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Python ভার্চুয়াল পরিবেশ সমস্যা
**সমস্যা:** মডিউল ইমপোর্ট ত্রুটি

**সমাধান:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Electron বিল্ড সমস্যা
**সমস্যা:** npm install বা বিল্ড ব্যর্থতা

**সমাধান:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### অনুবাদ কর্মপ্রবাহের দ্বন্দ্ব
**সমস্যা:** অনুবাদ PR আপনার পরিবর্তনের সাথে দ্বন্দ্ব করছে

**সমাধান:**
- শুধুমাত্র ইংরেজি সোর্স ফাইল সম্পাদনা করুন
- স্বয়ংক্রিয় অনুবাদ কর্মপ্রবাহকে অনুবাদ পরিচালনা করতে দিন
- যদি দ্বন্দ্ব ঘটে, অনুবাদগুলি মার্জ হওয়ার পরে `main` আপনার ব্রাঞ্চে মার্জ করুন

## অতিরিক্ত সম্পদ

### লার্নিং পাথ
- **বিগিনার পাথ:** মডিউল 01-02 (৭-৯ ঘণ্টা)
- **ইন্টারমিডিয়েট পাথ:** মডিউল 03-04 (৯-১১ ঘণ্টা)
- **অ্যাডভান্সড পাথ:** মডিউল 05-07 (১২-১৫ ঘণ্টা)
- **এক্সপার্ট পাথ:** মডিউল 08 (৮-১০ ঘণ্টা)

### মূল মডিউল বিষয়বস্তু
- **Module01:** EdgeAI এর মৌলিক বিষয় এবং বাস্তব জীবনের কেস স্টাডি
- **Module02:** ছোট ভাষার মডেল (SLM) পরিবার এবং আর্কিটেকচার
- **Module03:** স্থানীয় এবং ক্লাউড ডিপ্লয়মেন্ট কৌশল
- **Module04:** একাধিক ফ্রেমওয়ার্ক দিয়ে মডেল অপ্টিমাইজেশন
- **Module05:** SLMOps - প্রোডাকশন অপারেশন
- **Module06:** AI এজেন্ট এবং ফাংশন কলিং
- **Module07:** প্ল্যাটফর্ম-নির্দিষ্ট ইমপ্লিমেন্টেশন
- **Module08:** Foundry Local টুলকিট সহ ১০টি বিস্তৃত নমুনা

### বাহ্যিক নির্ভরতা
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - স্থানীয় AI মডেল রানটাইম
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - অপ্টিমাইজেশন ফ্রেমওয়ার্ক
- [Microsoft Olive](https://microsoft.github.io/Olive/) - মডেল অপ্টিমাইজেশন টুলকিট
- [OpenVINO](https://docs.openvino.ai/) - Intel এর অপ্টিমাইজেশন টুলকিট

## প্রকল্প-নির্দিষ্ট নোট

### Module08 নমুনা অ্যাপ্লিকেশন

সংগ্রহশালায় ১০টি বিস্তৃত নমুনা অ্যাপ্লিকেশন অন্তর্ভুক্ত রয়েছে:

1. **01-REST Chat Quickstart** - OpenAI SDK এর মৌলিক ইন্টিগ্রেশন
2. **02-OpenAI SDK Integration** - উন্নত SDK বৈশিষ্ট্য
3. **03-Model Discovery & Benchmarking** - মডেল তুলনা সরঞ্জাম
4. **04-Chainlit RAG Application** - রিট্রিভাল-অগমেন্টেড জেনারেশন
5. **05-Multi-Agent Orchestration** - মৌলিক এজেন্ট সমন্বয়
6. **06-Models-as-Tools Router** - বুদ্ধিমান মডেল রাউটিং
7. **07-Direct API Client** - নিম্ন-স্তরের API ইন্টিগ্রেশন
8. **08-Windows 11 Chat App** - নেটিভ Electron ডেস্কটপ অ্যাপ্লিকেশন
9. **09-Advanced Multi-Agent System** - জটিল এজেন্ট সমন্বয়
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel ইন্টিগ্রেশন

প্রতিটি নমুনা Foundry Local দিয়ে Edge AI উন্নয়নের বিভিন্ন দিক প্রদর্শন করে।

### কর্মক্ষমতা বিবেচনা

- SLMs Edge ডিপ্লয়মেন্টের জন্য অপ্টিমাইজ করা হয়েছে (২-১৬GB RAM)
- স্থানীয় ইনফারেন্স ৫০-৫০০ms প্রতিক্রিয়া সময় প্রদান করে
- কোয়ান্টাইজেশন কৌশল ৭৫% আকার হ্রাস এবং ৮৫% কর্মক্ষমতা ধরে রাখে
- স্থানীয় মডেল দিয়ে রিয়েল-টাইম কথোপকথন সক্ষমতা

### নিরাপত্তা এবং গোপনীয়তা

- সমস্ত প্রসেসিং স্থানীয়ভাবে ঘটে - কোনো ডেটা ক্লাউডে পাঠানো হয় না
- গোপনীয়তা-সংবেদনশীল অ্যাপ্লিকেশনের জন্য উপযুক্ত (স্বাস্থ্যসেবা, অর্থনীতি)
- ডেটা সার্বভৌমত্বের প্রয়োজনীয়তা পূরণ করে
- Foundry Local সম্পূর্ণরূপে স্থানীয় হার্ডওয়্যারে চলে

---

**এটি একটি শিক্ষামূলক সংগ্রহশালা যা Edge AI উন্নয়ন শেখানোর উপর কেন্দ্রীভূত। প্রধান অবদান প্যাটার্ন হল শিক্ষামূলক বিষয়বস্তু উন্নত করা এবং Edge AI ধারণাগুলি প্রদর্শন করে এমন নমুনা অ্যাপ্লিকেশন যোগ করা/উন্নত করা।**

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।