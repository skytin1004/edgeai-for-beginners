<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T09:17:02+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "bn"
}
-->
# ফাউন্ড্রি লোকাল SDK আপডেট

## ওভারভিউ

**অফিশিয়াল ফাউন্ড্রি লোকাল পাইথন SDK** এর প্যাটার্ন অনুসরণ করে ওয়ার্কশপ নোটবুক এবং ইউটিলিটিগুলি সঠিকভাবে আপডেট করা হয়েছে:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## পরিবর্তিত ফাইলসমূহ

### ১. `Workshop/samples/workshop_utils.py`

**পরিবর্তনসমূহ:**
- ✅ `foundry-local-sdk` প্যাকেজের জন্য ইমপোর্ট ত্রুটি হ্যান্ডলিং যোগ করা হয়েছে
- ✅ অফিসিয়াল SDK প্যাটার্নের সাথে ডকুমেন্টেশন উন্নত করা হয়েছে
- ✅ ইউনিকোড প্রতীক (✓, ✗, ⚠) সহ লগিং উন্নত করা হয়েছে
- ✅ উদাহরণ সহ বিস্তৃত ডকস্ট্রিং যোগ করা হয়েছে
- ✅ CLI কমান্ড রেফারেন্স সহ উন্নত ত্রুটি বার্তা
- ✅ অফিসিয়াল SDK ডকুমেন্টেশনের সাথে মিল রেখে মন্তব্য আপডেট করা হয়েছে

**মূল উন্নতিসমূহ:**

#### ইমপোর্ট ত্রুটি হ্যান্ডলিং
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### উন্নত `get_client()` ফাংশন
- SDK ইনিশিয়ালাইজেশন প্যাটার্ন সম্পর্কে বিস্তারিত ডকুমেন্টেশন যোগ করা হয়েছে
- ব্যাখ্যা করা হয়েছে যে `FoundryLocalManager` স্বয়ংক্রিয়ভাবে সার্ভিস শুরু করে
- মডেল অ্যালিয়াস হার্ডওয়্যার-অপ্টিমাইজড ভ্যারিয়েন্টে রেজলভ করার প্রক্রিয়া ব্যাখ্যা করা হয়েছে
- এন্ডপয়েন্ট তথ্য সহ লগিং উন্নত করা হয়েছে
- সমস্যা সমাধানের পরামর্শ সহ উন্নত ত্রুটি বার্তা

#### উন্নত `chat_once()` ফাংশন
- ব্যবহারের উদাহরণ সহ বিস্তৃত ডকস্ট্রিং যোগ করা হয়েছে
- OpenAI SDK সামঞ্জস্যতা স্পষ্ট করা হয়েছে
- স্ট্রিমিং সাপোর্ট (kwargs এর মাধ্যমে) ডকুমেন্ট করা হয়েছে
- CLI কমান্ডের পরামর্শ সহ উন্নত ত্রুটি বার্তা
- মডেল উপলব্ধতা যাচাই সম্পর্কে নোট যোগ করা হয়েছে

### ২. `Workshop/notebooks/session06_models_router.ipynb`

**পরিবর্তনসমূহ:**
- ✅ SDK রেফারেন্স সহ সমস্ত মার্কডাউন সেল আপডেট করা হয়েছে
- ✅ SDK প্যাটার্ন ব্যাখ্যা সহ কোড মন্তব্য উন্নত করা হয়েছে
- ✅ সেল ডকুমেন্টেশন এবং ব্যাখ্যা উন্নত করা হয়েছে
- ✅ সমস্যা সমাধানের নির্দেশিকা যোগ করা হয়েছে
- ✅ মডেল ক্যাটালগ আপডেট করা হয়েছে ('gpt-oss-20b' এর পরিবর্তে 'phi-3.5-mini' যোগ করা হয়েছে)
- ✅ ভিজ্যুয়াল ইন্ডিকেটর সহ আউটপুট ফরম্যাটিং উন্নত করা হয়েছে
- ✅ SDK লিঙ্ক এবং রেফারেন্স সর্বত্র যোগ করা হয়েছে

**সেল-বাই-সেল আপডেট:**

#### সেল ১ (শিরোনাম)
- SDK ডকুমেন্টেশনের লিঙ্ক যোগ করা হয়েছে
- অফিসিয়াল গিটহাব রিপোজিটরির রেফারেন্স দেওয়া হয়েছে

#### সেল ২ (সিনারিও)
- নম্বরযুক্ত ধাপ সহ পুনরায় ফরম্যাট করা হয়েছে
- উদ্দেশ্য-ভিত্তিক রাউটিং প্যাটার্ন স্পষ্ট করা হয়েছে
- লোকাল এক্সিকিউশনের সুবিধাগুলি জোর দেওয়া হয়েছে

#### সেল ৩ (ডিপেন্ডেন্সি ইনস্টলেশন)
- প্রতিটি প্যাকেজ কী প্রদান করে তার ব্যাখ্যা যোগ করা হয়েছে
- SDK এর ক্ষমতাগুলি ডকুমেন্ট করা হয়েছে (অ্যালিয়াস রেজল্যুশন, হার্ডওয়্যার অপ্টিমাইজেশন)

#### সেল ৪ (এনভায়রনমেন্ট সেটআপ)
- ফাংশন ডকস্ট্রিং উন্নত করা হয়েছে
- SDK প্যাটার্ন ব্যাখ্যা করে ইনলাইন মন্তব্য যোগ করা হয়েছে
- মডেল ক্যাটালগ স্ট্রাকচার ডকুমেন্ট করা হয়েছে
- অগ্রাধিকার/ক্ষমতা মিল সম্পর্কে স্পষ্ট করা হয়েছে

#### সেল ৫ (ক্যাটালগ চেক)
- ভিজ্যুয়াল চেকমার্ক (✓) যোগ করা হয়েছে
- আউটপুট আরও ভালোভাবে ফরম্যাট করা হয়েছে

#### সেল ৬ (ইনটেন্ট ডিটেকশন টেস্ট)
- আউটপুট টেবিল-স্টাইল হিসাবে পুনরায় ফরম্যাট করা হয়েছে
- উভয় ইনটেন্ট এবং নির্বাচিত মডেল দেখানো হয়েছে

#### সেল ৭ (রাউটিং ফাংশন)
- বিস্তৃত SDK প্যাটার্ন ব্যাখ্যা
- ইনিশিয়ালাইজেশন ফ্লো ডকুমেন্ট করা হয়েছে
- সমস্ত ফিচার তালিকাভুক্ত করা হয়েছে (রিট্রাই, ট্র্যাকিং, ত্রুটি)
- SDK রেফারেন্স লিঙ্ক যোগ করা হয়েছে

#### সেল ৮ (ব্যাচ ডেমো)
- কী আশা করা উচিত তার ব্যাখ্যা উন্নত করা হয়েছে
- সমস্যা সমাধানের বিভাগ যোগ করা হয়েছে
- ডিবাগিংয়ের জন্য CLI কমান্ড অন্তর্ভুক্ত করা হয়েছে
- আউটপুট ডিসপ্লে আরও ভালোভাবে ফরম্যাট করা হয়েছে

### ৩. `Workshop/notebooks/session06_README.md` (নতুন ফাইল)

**বিস্তারিত ডকুমেন্টেশন তৈরি করা হয়েছে যা অন্তর্ভুক্ত করে:**

1. **ওভারভিউ**: আর্কিটেকচার ডায়াগ্রাম এবং উপাদান ব্যাখ্যা
2. **SDK ইন্টিগ্রেশন**: অফিসিয়াল প্যাটার্ন অনুসরণ করে কোড উদাহরণ
3. **প্রয়োজনীয়তা**: ধাপে ধাপে সেটআপ নির্দেশিকা
4. **ব্যবহার**: নোটবুক চালানো এবং কাস্টমাইজ করার পদ্ধতি
5. **মডেল অ্যালিয়াস**: হার্ডওয়্যার-অপ্টিমাইজড ভ্যারিয়েন্টের ব্যাখ্যা
6. **সমস্যা সমাধান**: সাধারণ সমস্যা এবং সমাধান
7. **বিস্তারণ**: ইনটেন্ট, মডেল এবং কাস্টম লজিক যোগ করার পদ্ধতি
8. **পারফরম্যান্স টিপস**: প্রোডাকশন ব্যবহারের জন্য সেরা পদ্ধতি
9. **রিসোর্স**: অফিসিয়াল ডকস এবং কমিউনিটির লিঙ্ক

## SDK প্যাটার্ন ইমপ্লিমেন্টেশন

### অফিসিয়াল প্যাটার্ন (ফাউন্ড্রি লোকাল ডকস থেকে)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### আমাদের ইমপ্লিমেন্টেশন (workshop_utils এ)

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**আমাদের পদ্ধতির সুবিধাসমূহ:**
- ✅ অফিসিয়াল SDK প্যাটার্ন সঠিকভাবে অনুসরণ করে
- ✅ পুনরায় ইনিশিয়ালাইজেশন এড়াতে ক্যাশিং যোগ করা হয়েছে
- ✅ প্রোডাকশন রোবাস্টনেসের জন্য রিট্রাই লজিক অন্তর্ভুক্ত
- ✅ টোকেন ব্যবহারের ট্র্যাকিং সাপোর্ট করে
- ✅ উন্নত ত্রুটি বার্তা প্রদান করে
- ✅ অফিসিয়াল উদাহরণের সাথে সামঞ্জস্যপূর্ণ

## মডেল ক্যাটালগ পরিবর্তন

### পূর্বে
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### পরে
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**কারণ:** 'gpt-oss-20b' (নন-স্ট্যান্ডার্ড অ্যালিয়াস) এর পরিবর্তে 'phi-3.5-mini' (অফিশিয়াল ফাউন্ড্রি লোকাল অ্যালিয়াস) যোগ করা হয়েছে।

## ডিপেন্ডেন্সি

### আপডেটেড requirements.txt

ওয়ার্কশপের requirements.txt ইতিমধ্যেই অন্তর্ভুক্ত:
```
foundry-local-sdk
openai>=1.30.0
```

ফাউন্ড্রি লোকাল ইন্টিগ্রেশনের জন্য এগুলোই প্রয়োজনীয় প্যাকেজ।

## আপডেট পরীক্ষা

### ১. ফাউন্ড্রি লোকাল চালু আছে কিনা যাচাই করুন

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### ২. উপলব্ধ মডেল চেক করুন

```bash
foundry model ls
```

নিশ্চিত করুন যে এই মডেলগুলি উপলব্ধ বা স্বয়ংক্রিয়ভাবে ডাউনলোড হবে:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### ৩. নোটবুক চালান

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

অথবা VS Code এ খুলে সমস্ত সেল চালান।

### ৪. প্রত্যাশিত আচরণ

**সেল ১ (ইনস্টল):** সফলভাবে প্যাকেজ ইনস্টল করে
**সেল ২ (সেটআপ):** কোনো ত্রুটি ছাড়াই কাজ করে
**সেল ৩ (যাচাই):** ✓ সহ মডেল তালিকা দেখায়
**সেল ৪ (ইনটেন্ট টেস্ট):** ইনটেন্ট ডিটেকশন ফলাফল দেখায়
**সেল ৫ (রাউটার):** ✓ রাউট ফাংশন প্রস্তুত দেখায়
**সেল ৬ (এক্সিকিউট):** প্রম্পট মডেলে রাউট করে, ফলাফল দেখায়

### ৫. সংযোগ ত্রুটি সমাধান

যদি আপনি `APIConnectionError: Connection error` দেখেন:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## পরিবেশ ভেরিয়েবল

নিম্নলিখিত পরিবেশ ভেরিয়েবলগুলি সমর্থিত:

| ভেরিয়েবল | ডিফল্ট | বর্ণনা |
|-----------|--------|---------|
| `SHOW_USAGE` | `0` | টোকেন ব্যবহারের তথ্য প্রদর্শনের জন্য `1` সেট করুন |
| `RETRY_ON_FAIL` | `1` | রিট্রাই লজিক সক্রিয় করুন |
| `RETRY_BACKOFF` | `1.0` | প্রাথমিক রিট্রাই বিলম্ব (সেকেন্ডে) |
| `FOUNDRY_LOCAL_ENDPOINT` | অটো | সার্ভিস এন্ডপয়েন্ট ওভাররাইড করুন |

### ব্যবহারের উদাহরণ

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## পুরনো প্যাটার্ন থেকে মাইগ্রেশন

যদি আপনার বিদ্যমান কোড সরাসরি API কল ব্যবহার করে, তাহলে কীভাবে মাইগ্রেট করবেন:

### পূর্বে (ডিরেক্ট API)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### পরে (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### মাইগ্রেশনের সুবিধাসমূহ
- ✅ স্বয়ংক্রিয় সার্ভিস ম্যানেজমেন্ট
- ✅ মডেল অ্যালিয়াস রেজল্যুশন
- ✅ হার্ডওয়্যার অপ্টিমাইজেশন নির্বাচন
- ✅ উন্নত ত্রুটি হ্যান্ডলিং
- ✅ OpenAI SDK সামঞ্জস্যতা
- ✅ স্ট্রিমিং সাপোর্ট

## রেফারেন্স

### অফিসিয়াল ডকুমেন্টেশন
- **ফাউন্ড্রি লোকাল গিটহাব**: https://github.com/microsoft/Foundry-Local
- **পাইথন SDK সোর্স**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI রেফারেন্স**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **সমস্যা সমাধান**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### ওয়ার্কশপ রিসোর্স
- **সেশন ০৬ README**: `Workshop/notebooks/session06_README.md`
- **ওয়ার্কশপ ইউটিলস**: `Workshop/samples/workshop_utils.py`
- **নমুনা নোটবুক**: `Workshop/notebooks/session06_models_router.ipynb`

### কমিউনিটি
- **ডিসকর্ড**: https://aka.ms/foundry-local-discord
- **গিটহাব ইস্যু**: https://github.com/microsoft/Foundry-Local/issues

## পরবর্তী পদক্ষেপ

1. **পরিবর্তন পর্যালোচনা করুন**: আপডেট করা ফাইলগুলি পড়ুন
2. **নোটবুক পরীক্ষা করুন**: session06_models_router.ipynb চালান
3. **SDK যাচাই করুন**: নিশ্চিত করুন যে foundry-local-sdk ইনস্টল করা আছে
4. **সার্ভিস চেক করুন**: নিশ্চিত করুন যে ফাউন্ড্রি লোকাল চালু আছে
5. **ডকস অন্বেষণ করুন**: নতুন session06_README.md পড়ুন

## সারসংক্ষেপ

এই আপডেটগুলি নিশ্চিত করে যে ওয়ার্কশপের উপকরণগুলি **অফিশিয়াল ফাউন্ড্রি লোকাল SDK প্যাটার্ন** এর সাথে সঠিকভাবে সামঞ্জস্যপূর্ণ। সমস্ত কোড উদাহরণ, ডকুমেন্টেশন এবং ইউটিলিটি এখন মাইক্রোসফটের স্থানীয় AI মডেল ডিপ্লয়মেন্টের জন্য প্রস্তাবিত সেরা পদ্ধতির সাথে সামঞ্জস্যপূর্ণ।

এই পরিবর্তনগুলি উন্নত করে:
- ✅ **সঠিকতা**: অফিসিয়াল SDK প্যাটার্ন ব্যবহার
- ✅ **ডকুমেন্টেশন**: বিস্তৃত ব্যাখ্যা এবং উদাহরণ
- ✅ **ত্রুটি হ্যান্ডলিং**: উন্নত বার্তা এবং সমস্যা সমাধানের নির্দেশিকা
- ✅ **রক্ষণাবেক্ষণযোগ্যতা**: অফিসিয়াল কনভেনশন অনুসরণ
- ✅ **ব্যবহারকারীর অভিজ্ঞতা**: আরও পরিষ্কার নির্দেশনা এবং ডিবাগিং সহায়তা

---

**আপডেট করা হয়েছে:** ৮ অক্টোবর, ২০২৫  
**SDK সংস্করণ:** foundry-local-sdk (সর্বশেষ)  
**ওয়ার্কশপ শাখা:** Reactor

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।