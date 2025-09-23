<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-22T17:48:18+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "bn"
}
-->
# Windows-এ Foundry Local (যাচাই করা হয়েছে)

এই গাইডটি আপনাকে Windows-এ Microsoft Foundry Local ইনস্টল, চালানো এবং ইন্টিগ্রেট করতে সাহায্য করবে। সমস্ত ধাপ এবং কমান্ড Microsoft Learn ডকুমেন্টেশনের সাথে যাচাই করা হয়েছে।

- শুরু করুন: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- আর্কিটেকচার: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI রেফারেন্স: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKs ইন্টিগ্রেট করুন: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF মডেল কম্পাইল করুন (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Local বনাম Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## ১) Windows-এ ইনস্টল / আপগ্রেড

- ইনস্টল:
```cmd
winget install Microsoft.FoundryLocal
```
- আপগ্রেড:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- ভার্সন চেক:
```cmd
foundry --version
```

## ২) CLI বেসিকস (তিনটি বিভাগ)

- মডেল:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- সার্ভিস:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- ক্যাশ:
```cmd
foundry cache --help
foundry cache list
```

মন্তব্য:
- সার্ভিসটি একটি OpenAI-সামঞ্জস্যপূর্ণ REST API প্রকাশ করে। এন্ডপয়েন্ট পোর্টটি ডাইনামিকভাবে বরাদ্দ করা হয়; এটি খুঁজে পেতে `foundry service status` ব্যবহার করুন।
- SDKs ব্যবহার করুন সুবিধার জন্য; এটি যেখানে সমর্থিত, এন্ডপয়েন্ট ডিসকভারি স্বয়ংক্রিয়ভাবে পরিচালনা করে।

## ৩) লোকাল এন্ডপয়েন্ট আবিষ্কার করুন (ডাইনামিক পোর্ট)

Foundry Local প্রতিবার সার্ভিস শুরু হলে একটি ডাইনামিক পোর্ট বরাদ্দ করে:
```cmd
foundry service status
```
প্রতিবেদন করা `http://localhost:<PORT>` ব্যবহার করুন আপনার `base_url` হিসেবে OpenAI-সামঞ্জস্যপূর্ণ পাথগুলির সাথে (যেমন, `/v1/chat/completions`)।

## ৪) OpenAI Python SDK দিয়ে দ্রুত পরীক্ষা

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
রেফারেন্স:
- SDK ইন্টিগ্রেশন: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## ৫) আপনার নিজস্ব মডেল আনুন (Olive দিয়ে কম্পাইল করুন)

যদি আপনি ক্যাটালগে থাকা মডেলগুলির বাইরে কিছু প্রয়োজন হয়, তাহলে Olive ব্যবহার করে এটি ONNX-এ কম্পাইল করুন Foundry Local-এর জন্য।

উচ্চ-স্তরের ফ্লো (ধাপগুলির জন্য ডক দেখুন):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
ডক:
- BYOM কম্পাইল: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## ৬) সমস্যা সমাধান

- সার্ভিস স্ট্যাটাস এবং লগ চেক করুন:
```cmd
foundry service status
foundry service diag
```
- ক্যাশ ক্লিয়ার বা সরান:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- সর্বশেষ প্রিভিউতে আপডেট করুন:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## ৭) সংশ্লিষ্ট Windows ডেভেলপার অভিজ্ঞতা

- Windows লোকাল বনাম ক্লাউড AI পছন্দগুলি, যার মধ্যে Foundry Local এবং Windows ML অন্তর্ভুক্ত:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit Foundry Local-এর সাথে (চ্যাট এন্ডপয়েন্ট URL পেতে `foundry service status` ব্যবহার করুন):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

