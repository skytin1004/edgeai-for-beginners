<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec281a7cf06deda1f29140a2959ef0d2",
  "translation_date": "2025-10-09T09:42:09+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "bn"
}
-->
# Foundry Local SDK মাইগ্রেশন নোটস

## সংক্ষিপ্ত বিবরণ

Workshop ফোল্ডারের সমস্ত Python ফাইল আপডেট করা হয়েছে যাতে তারা অফিসিয়াল [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local)-এর সর্বশেষ প্যাটার্ন অনুসরণ করে।

## পরিবর্তনের সারসংক্ষেপ

### মূল অবকাঠামো (`workshop_utils.py`)

#### উন্নত বৈশিষ্ট্যসমূহ:
- **এন্ডপয়েন্ট ওভাররাইড সাপোর্ট**: `FOUNDRY_LOCAL_ENDPOINT` পরিবেশ ভেরিয়েবল সাপোর্ট যোগ করা হয়েছে
- **উন্নত ত্রুটি পরিচালনা**: বিস্তারিত ত্রুটি বার্তাসহ আরও ভালো এক্সসেপশন হ্যান্ডলিং
- **উন্নত ক্যাশিং**: মাল্টি-এন্ডপয়েন্ট পরিস্থিতির জন্য ক্যাশ কী-তে এন্ডপয়েন্ট অন্তর্ভুক্ত করা হয়েছে
- **এক্সপোনেনশিয়াল ব্যাকঅফ**: আরও নির্ভরযোগ্যতার জন্য পুনরায় চেষ্টা করার লজিক এক্সপোনেনশিয়াল ব্যাকঅফ ব্যবহার করে
- **টাইপ অ্যানোটেশন**: আরও ভালো IDE সাপোর্টের জন্য ব্যাপক টাইপ হিন্ট যোগ করা হয়েছে

#### নতুন সক্ষমতা:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### নমুনা অ্যাপ্লিকেশন

#### সেশন ০১: চ্যাট বুটস্ট্র্যাপ (`chat_bootstrap.py`)
- ডিফল্ট মডেল `phi-3.5-mini` থেকে `phi-4-mini`-এ আপডেট করা হয়েছে
- এন্ডপয়েন্ট ওভাররাইড সাপোর্ট যোগ করা হয়েছে
- SDK রেফারেন্স সহ ডকুমেন্টেশন উন্নত করা হয়েছে

#### সেশন ০২: RAG পাইপলাইন (`rag_pipeline.py`)
- ডিফল্ট হিসেবে `phi-4-mini` ব্যবহার করার জন্য আপডেট করা হয়েছে
- এন্ডপয়েন্ট ওভাররাইড সাপোর্ট যোগ করা হয়েছে
- পরিবেশ ভেরিয়েবল সম্পর্কিত বিস্তারিত সহ ডকুমেন্টেশন উন্নত করা হয়েছে

#### সেশন ০২: RAG মূল্যায়ন (`rag_eval_ragas.py`)
- মডেল ডিফল্ট আপডেট করা হয়েছে
- এন্ডপয়েন্ট কনফিগারেশন যোগ করা হয়েছে
- ত্রুটি পরিচালনা উন্নত করা হয়েছে

#### সেশন ০৩: বেঞ্চমার্কিং (`benchmark_oss_models.py`)
- ডিফল্ট মডেল তালিকায় `phi-4-mini` অন্তর্ভুক্ত করা হয়েছে
- পরিবেশ ভেরিয়েবল সম্পর্কিত ব্যাপক ডকুমেন্টেশন যোগ করা হয়েছে
- ফাংশন ডকুমেন্টেশন উন্নত করা হয়েছে
- পুরো জুড়ে এন্ডপয়েন্ট ওভাররাইড সাপোর্ট যোগ করা হয়েছে

#### সেশন ০৪: মডেল তুলনা (`model_compare.py`)
- ডিফল্ট LLM `gpt-oss-20b` থেকে `qwen2.5-7b`-এ আপডেট করা হয়েছে
- এন্ডপয়েন্ট কনফিগারেশন যোগ করা হয়েছে
- ডকুমেন্টেশন উন্নত করা হয়েছে

#### সেশন ০৫: মাল্টি-এজেন্ট অর্কেস্ট্রেশন (`agents_orchestrator.py`)
- টাইপ হিন্ট যোগ করা হয়েছে (যেমন `str | None` পরিবর্তন করে `Optional[str]`)
- Agent ক্লাসের ডকুমেন্টেশন উন্নত করা হয়েছে
- এন্ডপয়েন্ট ওভাররাইড সাপোর্ট যোগ করা হয়েছে
- ইনিশিয়ালাইজেশন প্যাটার্ন উন্নত করা হয়েছে

#### সেশন ০৬: মডেল রাউটার (`models_router.py`)
- এন্ডপয়েন্ট কনফিগারেশন যোগ করা হয়েছে
- ইন্টেন্ট ডিটেকশন ডকুমেন্টেশন উন্নত করা হয়েছে
- রাউটিং লজিক ডকুমেন্টেশন উন্নত করা হয়েছে

#### সেশন ০৬: পাইপলাইন (`models_pipeline.py`)
- ব্যাপক ফাংশন ডকুমেন্টেশন যোগ করা হয়েছে
- ধাপে ধাপে ডকুমেন্টেশন উন্নত করা হয়েছে
- ত্রুটি পরিচালনা উন্নত করা হয়েছে

### স্ক্রিপ্ট

#### বেঞ্চমার্ক এক্সপোর্ট (`export_benchmark_markdown.py`)
- এন্ডপয়েন্ট ওভাররাইড সাপোর্ট যোগ করা হয়েছে
- ডিফল্ট মডেল আপডেট করা হয়েছে
- ফাংশন ডকুমেন্টেশন উন্নত করা হয়েছে
- ত্রুটি পরিচালনা উন্নত করা হয়েছে

#### CLI লিন্টার (`lint_markdown_cli.py`)
- SDK রেফারেন্স লিঙ্ক যোগ করা হয়েছে
- ব্যবহার সম্পর্কিত ডকুমেন্টেশন উন্নত করা হয়েছে

### টেস্ট

#### স্মোক টেস্ট (`smoke.py`)
- এন্ডপয়েন্ট ওভাররাইড সাপোর্ট যোগ করা হয়েছে
- ডকুমেন্টেশন উন্নত করা হয়েছে
- টেস্ট কেস ডকুমেন্টেশন উন্নত করা হয়েছে
- আরও ভালো ত্রুটি রিপোর্টিং

## পরিবেশ ভেরিয়েবল

সমস্ত নমুনা এখন এই পরিবেশ ভেরিয়েবলগুলো সাপোর্ট করে:

### মূল কনফিগারেশন
- `FOUNDRY_LOCAL_ALIAS` - ব্যবহৃত মডেলের উপনাম (ডিফল্ট নমুনা অনুযায়ী পরিবর্তিত হয়)
- `FOUNDRY_LOCAL_ENDPOINT` - সার্ভিস এন্ডপয়েন্ট ওভাররাইড (ঐচ্ছিক)
- `SHOW_USAGE` - টোকেন ব্যবহারের পরিসংখ্যান দেখান (ডিফল্ট: "0")
- `RETRY_ON_FAIL` - পুনরায় চেষ্টা করার লজিক সক্রিয় করুন (ডিফল্ট: "1")
- `RETRY_BACKOFF` - পুনরায় চেষ্টা করার প্রাথমিক বিলম্ব সেকেন্ডে (ডিফল্ট: "1.0")

### নমুনা-নির্দিষ্ট
- `EMBED_MODEL` - RAG নমুনার জন্য এমবেডিং মডেল
- `BENCH_MODELS` - বেঞ্চমার্কিংয়ের জন্য কমা-আলাদা মডেল
- `BENCH_ROUNDS` - বেঞ্চমার্ক রাউন্ডের সংখ্যা
- `BENCH_PROMPT` - বেঞ্চমার্কের জন্য টেস্ট প্রম্পট
- `BENCH_STREAM` - প্রথম টোকেন লেটেন্সি পরিমাপ করুন
- `RAG_QUESTION` - RAG নমুনার জন্য টেস্ট প্রশ্ন
- `AGENT_MODEL_PRIMARY` - প্রাইমারি এজেন্ট মডেল
- `AGENT_MODEL_EDITOR` - এডিটর এজেন্ট মডেল
- `SLM_ALIAS` - ছোট ভাষার মডেলের উপনাম
- `LLM_ALIAS` - বড় ভাষার মডেলের উপনাম

## SDK সেরা অনুশীলন বাস্তবায়ন

### ১. সঠিক ক্লায়েন্ট ইনিশিয়ালাইজেশন
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### ২. মডেল তথ্য পুনরুদ্ধার
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### ৩. ত্রুটি পরিচালনা
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### ৪. এক্সপোনেনশিয়াল ব্যাকঅফ সহ পুনরায় চেষ্টা করার লজিক
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### ৫. স্ট্রিমিং সাপোর্ট
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## কাস্টম নমুনার জন্য মাইগ্রেশন গাইড

যদি আপনি নতুন নমুনা তৈরি করেন বা বিদ্যমান নমুনা আপডেট করেন:

1. **`workshop_utils.py` হেল্পার ব্যবহার করুন**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **এন্ডপয়েন্ট ওভাররাইড সাপোর্ট করুন**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **ব্যাপক ডকুমেন্টেশন যোগ করুন**:
   - পরিবেশ ভেরিয়েবল ডকস্ট্রিং-এ
   - SDK রেফারেন্স লিঙ্ক
   - ব্যবহার উদাহরণ

4. **টাইপ হিন্ট ব্যবহার করুন**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **সঠিক ত্রুটি পরিচালনা বাস্তবায়ন করুন**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## টেস্টিং

সমস্ত নমুনা পরীক্ষা করা যেতে পারে:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
python Workshop/samples/session01/chat_bootstrap.py "Test question"
python Workshop/samples/session02/rag_pipeline.py

# Run benchmark
python Workshop/samples/session03/benchmark_oss_models.py

# Run smoke tests
python -m Workshop.tests.smoke
```

## SDK ডকুমেন্টেশন রেফারেন্স

- **মূল রিপোজিটরি**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API ডকুমেন্টেশন**: সর্বশেষ API ডকসের জন্য SDK রিপোজিটরি দেখুন

## ব্রেকিং পরিবর্তন

### কোনো প্রত্যাশিত নয়
সমস্ত পরিবর্তন ব্যাকওয়ার্ড কম্প্যাটিবল। আপডেটগুলো মূলত:
- নতুন ঐচ্ছিক বৈশিষ্ট্য যোগ করে (এন্ডপয়েন্ট ওভাররাইড)
- ত্রুটি পরিচালনা উন্নত করে
- ডকুমেন্টেশন উন্নত করে
- ডিফল্ট মডেল নাম বর্তমান সুপারিশ অনুযায়ী আপডেট করে

### ঐচ্ছিক উন্নতি
আপনার কোড আপডেট করতে চাইতে পারেন:
- `FOUNDRY_LOCAL_ENDPOINT` স্পষ্ট এন্ডপয়েন্ট নিয়ন্ত্রণের জন্য
- `SHOW_USAGE=1` টোকেন ব্যবহারের দৃশ্যমানতার জন্য
- আপডেট করা মডেল ডিফল্ট (`phi-4-mini` পরিবর্তে `phi-3.5-mini`)

## সাধারণ সমস্যা ও সমাধান

### সমস্যা: "ক্লায়েন্ট ইনিশিয়ালাইজেশন ব্যর্থ হয়েছে"
**সমাধান**: নিশ্চিত করুন Foundry Local সার্ভিস চালু আছে:
```bash
foundry service start
foundry model run phi-4-mini
```

### সমস্যা: "মডেল পাওয়া যায়নি"
**সমাধান**: উপলব্ধ মডেল চেক করুন:
```bash
foundry model list
```

### সমস্যা: এন্ডপয়েন্ট সংযোগ ত্রুটি
**সমাধান**: এন্ডপয়েন্ট যাচাই করুন:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## পরবর্তী পদক্ষেপ

1. **Module08 নমুনা আপডেট করুন**: Module08/samples-এ অনুরূপ প্যাটার্ন প্রয়োগ করুন
2. **ইন্টিগ্রেশন টেস্ট যোগ করুন**: ব্যাপক টেস্ট স্যুট তৈরি করুন
3. **পারফরম্যান্স বেঞ্চমার্কিং**: পূর্বের এবং পরবর্তী পারফরম্যান্স তুলনা করুন
4. **ডকুমেন্টেশন আপডেট**: নতুন প্যাটার্ন সহ প্রধান README আপডেট করুন

## কন্ট্রিবিউশন নির্দেশিকা

নতুন নমুনা যোগ করার সময়:
1. সামঞ্জস্যের জন্য `workshop_utils.py` ব্যবহার করুন
2. বিদ্যমান নমুনার প্যাটার্ন অনুসরণ করুন
3. ব্যাপক ডকস্ট্রিং যোগ করুন
4. SDK রেফারেন্স লিঙ্ক অন্তর্ভুক্ত করুন
5. এন্ডপয়েন্ট ওভাররাইড সাপোর্ট করুন
6. সঠিক টাইপ হিন্ট যোগ করুন
7. ডকস্ট্রিং-এ ব্যবহার উদাহরণ অন্তর্ভুক্ত করুন

## সংস্করণ সামঞ্জস্যতা

এই আপডেটগুলো সামঞ্জস্যপূর্ণ:
- `foundry-local-sdk` (সর্বশেষ)
- `openai>=1.30.0`
- Python 3.8+

---

**শেষ আপডেট**: ২০২৫-০১-০৮  
**রক্ষণাবেক্ষণকারী**: EdgeAI Workshop টিম  
**SDK সংস্করণ**: Foundry Local SDK (সর্বশেষ 0.7.117+67073234e7)

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।