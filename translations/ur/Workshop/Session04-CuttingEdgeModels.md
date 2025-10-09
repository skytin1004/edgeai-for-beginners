<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d1b3c0fecfd713c2df903a0633249dc9",
  "translation_date": "2025-10-09T06:42:27+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "ur"
}
-->
# سیشن 4: جدید ماڈلز کا جائزہ – LLMs، SLMs اور آن ڈیوائس انفرنس

## خلاصہ

بڑے زبان ماڈلز (LLMs) اور چھوٹے زبان ماڈلز (SLMs) کا مقامی اور کلاؤڈ انفرنس کے منظرناموں میں موازنہ کریں۔ ONNX Runtime کی تیز رفتاری، WebGPU کی عمل درآمد، اور ہائبرڈ RAG تجربات کے استعمال کے طریقے سیکھیں۔ اس میں Chainlit RAG ڈیمو شامل ہے جس میں ایک مقامی ماڈل اور اختیاری OpenWebUI کی تلاش شامل ہے۔ آپ WebGPU انفرنس اسٹارٹر کو اپنائیں گے اور Phi بمقابلہ GPT-OSS-20B کی صلاحیت اور لاگت/کارکردگی کے موازنہ کا جائزہ لیں گے۔

## سیکھنے کے مقاصد

- **موازنہ کریں** SLM اور LLM کو لیٹینسی، میموری، اور معیار کے پہلوؤں پر
- **ماڈلز کو نافذ کریں** ONNXRuntime اور (جہاں دستیاب ہو) WebGPU کے ساتھ
- **چلائیں** براؤزر پر مبنی انفرنس (پرائیویسی کو محفوظ رکھنے والا انٹرایکٹو ڈیمو)
- **ضم کریں** Chainlit RAG پائپ لائن کو مقامی SLM بیک اینڈ کے ساتھ
- **جائزہ لیں** ہلکے معیار + لاگت کے اصولوں کا استعمال کرتے ہوئے

## ضروریات

- سیشنز 1–3 مکمل کیے گئے ہوں
- `chainlit` انسٹال ہو (پہلے سے `requirements.txt` میں Module08 کے لیے شامل ہے)
- WebGPU کے قابل براؤزر (Edge / Chrome ونڈوز 11 پر تازہ ترین)
- Foundry Local چل رہا ہو (`foundry status`)

### کراس پلیٹ فارم نوٹس

ونڈوز بنیادی ہدف ماحول ہے۔ macOS ڈویلپرز جو مقامی بائنریز کے منتظر ہیں:
1. Foundry Local کو ونڈوز 11 VM (Parallels / UTM) یا ریموٹ ونڈوز ورک اسٹیشن میں چلائیں۔
2. سروس کو ظاہر کریں (ڈیفالٹ پورٹ 5273) اور macOS پر سیٹ کریں:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. وہی Python ورچوئل ماحول کے اقدامات استعمال کریں جو پہلے سیشنز میں کیے گئے تھے۔

Chainlit انسٹال (دونوں پلیٹ فارمز):
```bash
pip install chainlit
```

## ڈیمو فلو (30 منٹ)

### 1. Phi (SLM) بمقابلہ GPT-OSS-20B (LLM) کا موازنہ کریں (6 منٹ)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

ٹریک کریں: جواب کی گہرائی، حقائق کی درستگی، اسلوب کی خوبصورتی، لیٹینسی۔

### 2. ONNX Runtime کی تیز رفتاری (5 منٹ)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   set BENCH_MODELS=phi-4-mini
#   python Workshop\samples\session03\benchmark_oss_models.py
```

GPU کو فعال کرنے کے بعد تھروپٹ میں تبدیلی کا مشاہدہ کریں بمقابلہ صرف CPU۔

### 3. براؤزر میں WebGPU انفرنس (6 منٹ)

اسٹارٹر `04-webgpu-inference` کو اپنائیں (بنائیں `samples/04-cutting-edge/webgpu_demo.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

فائل کو براؤزر میں کھولیں؛ کم لیٹینسی مقامی راؤنڈ ٹرپ کا مشاہدہ کریں۔

### 4. Chainlit RAG چیٹ ایپ (7 منٹ)

کم سے کم `samples/04-cutting-edge/chainlit_app.py`:

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

چلائیں:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. اسٹارٹر پروجیکٹ: `04-webgpu-inference` کو اپنائیں (6 منٹ)

ڈیلیورایبلز:
- پلیس ہولڈر fetch لاجک کو اسٹریمنگ ٹوکنز کے ساتھ تبدیل کریں (جب `stream=True` اینڈ پوائنٹ ویریئنٹ فعال ہو)
- لیٹینسی چارٹ شامل کریں (کلائنٹ سائیڈ) phi بمقابلہ gpt-oss-20b ٹوگلز کے لیے
- RAG سیاق و سباق کو ان لائن شامل کریں (ریفرنس ڈاکس کے لیے textarea)

## جائزہ لینے کے اصول

| زمرہ | Phi-4-mini | GPT-OSS-20B | مشاہدہ |
|----------|------------|-------------|-------------|
| لیٹینسی (کولڈ) | تیز | سست | SLM جلدی گرم ہوتا ہے |
| میموری | کم | زیادہ | ڈیوائس کی قابلیت |
| سیاق و سباق کی پابندی | اچھا | مضبوط | بڑا ماڈل زیادہ تفصیلی ہو سکتا ہے |
| لاگت (مقامی) | کم سے کم | زیادہ (وسائل) | توانائی/وقت کا موازنہ |
| بہترین استعمال کا کیس | ایج ایپس | گہری استدلال | ہائبرڈ پائپ لائن ممکن |

## ماحول کی تصدیق

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python Workshop\samples\session03\benchmark_oss_models.py
```

## مسائل کا حل

| علامت | وجہ | عمل |
|---------|-------|--------|
| ویب صفحہ fetch ناکام | CORS یا سروس بند | اینڈ پوائنٹ کی تصدیق کے لیے `curl` استعمال کریں؛ اگر ضرورت ہو تو CORS پراکسی فعال کریں |
| Chainlit خالی | ماحول فعال نہیں | venv کو فعال کریں اور دوبارہ dependencies انسٹال کریں |
| زیادہ لیٹینسی | ماڈل ابھی لوڈ ہوا | چھوٹے پرامپٹ سیکوئنس کے ساتھ گرم کریں |

## حوالہ جات

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Docs: https://docs.chainlit.io
- RAG جائزہ (Ragas): https://docs.ragas.io

---

**سیشن کا دورانیہ**: 30 منٹ  
**مشکل**: اعلیٰ درجے کا

## نمونہ منظرنامہ اور ورکشاپ میپنگ

| ورکشاپ آرٹفیکٹس | منظرنامہ | مقصد | ڈیٹا / پرامپٹ سورس |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | آرکیٹیکچر ٹیم جو ایگزیکٹو سمری جنریٹر کے لیے SLM بمقابلہ LLM کا جائزہ لے رہی ہے | لیٹینسی + ٹوکن کے استعمال کے فرق کو مقدار میں ظاہر کریں | سنگل `COMPARE_PROMPT` env var |
| `chainlit_app.py` (RAG ڈیمو) | اندرونی علم معاون پروٹوٹائپ | مختصر جوابات کو کم سے کم لغوی بازیافت کے ساتھ بنیاد فراہم کریں | فائل میں ان لائن `DOCS` لسٹ |
| `webgpu_demo.html` | مستقبل کی آن ڈیوائس براؤزر انفرنس پیش نظارہ | کم لیٹینسی مقامی راؤنڈ ٹرپ + UX بیانیہ دکھائیں | صرف لائیو یوزر پرامپٹ |

### منظرنامہ بیانیہ
پروڈکٹ آرگنائزیشن ایک ایگزیکٹو بریفنگ جنریٹر چاہتی ہے۔ ایک ہلکا SLM (phi‑4‑mini) خلاصے تیار کرتا ہے؛ ایک بڑا LLM (gpt‑oss‑20b) صرف اعلیٰ ترجیحی رپورٹس کو بہتر بنا سکتا ہے۔ سیشن اسکرپٹس تجرباتی لیٹینسی اور ٹوکن میٹرکس کو ہائبرڈ ڈیزائن کو جواز فراہم کرنے کے لیے پکڑتے ہیں، جبکہ Chainlit ڈیمو یہ ظاہر کرتا ہے کہ کس طرح بنیاد فراہم کردہ بازیافت چھوٹے ماڈل کے جوابات کو حقائق پر مبنی رکھتی ہے۔ WebGPU تصوراتی صفحہ مکمل طور پر کلائنٹ سائیڈ پروسیسنگ کے لیے وژن کا راستہ فراہم کرتا ہے جب براؤزر کی تیز رفتاری پختہ ہو جائے۔

### کم سے کم RAG سیاق و سباق (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### ہائبرڈ ڈرافٹ→ریفائن فلو (پسیوڈو)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

دونوں لیٹینسی اجزاء کو ٹریک کریں تاکہ مخلوط اوسط لاگت کی رپورٹ دی جا سکے۔

### اختیاری بہتریاں

| فوکس | بہتری | کیوں | عمل درآمد کا اشارہ |
|-------|------------|-----|---------------------|
| تقابلی میٹرکس | ٹوکن کے استعمال + پہلے ٹوکن کی لیٹینسی کو ٹریک کریں | جامع کارکردگی کا جائزہ | بہتر بینچ مارک اسکرپٹ استعمال کریں (سیشن 3) کے ساتھ `BENCH_STREAM=1` |
| ہائبرڈ پائپ لائن | SLM ڈرافٹ → LLM ریفائن | لیٹینسی اور لاگت کو کم کریں | phi-4-mini کے ساتھ تیار کریں، خلاصہ gpt-oss-20b کے ساتھ بہتر بنائیں |
| اسٹریمنگ UI | Chainlit میں بہتر UX | انکریمنٹل فیڈبیک | جب مقامی اسٹریمنگ ظاہر ہو تو `stream=True` استعمال کریں؛ چنکس جمع کریں |
| WebGPU کیشنگ | JS کی تیز تر شروعات | دوبارہ کمپائل اوور ہیڈ کو کم کریں | مرتب شدہ شیڈر آرٹفیکٹس کو کیش کریں (مستقبل کی رن ٹائم صلاحیت) |
| تعین شدہ QA سیٹ | منصفانہ ماڈل موازنہ | تغیر کو ختم کریں | فکسڈ پرامپٹ لسٹ + `temperature=0` جائزہ لینے کے لیے |
| آؤٹ پٹ اسکورنگ | ساختی معیار کا عدسہ | کہانیوں سے آگے بڑھیں | سادہ پیمانہ: ہم آہنگی / حقائق / اختصار (1–5) |
| توانائی / وسائل کے نوٹس | کلاس روم بحث | تجارتی مواقع دکھائیں | OS مانیٹرز (`foundry system info`, Task Manager, `nvidia-smi`) + بینچ مارک اسکرپٹ آؤٹ پٹس استعمال کریں |
| لاگت کی نقل | پری کلاؤڈ جواز | اسکیلنگ کی منصوبہ بندی | ٹوکنز کو فرضی کلاؤڈ قیمتوں سے نقش کریں TCO بیانیہ کے لیے |
| لیٹینسی کی تقسیم | رکاوٹوں کی شناخت کریں | اصلاحات کو ہدف بنائیں | پرامپٹ تیاری، درخواست بھیجنا، پہلا ٹوکن، مکمل تکمیل کی پیمائش کریں |
| RAG + LLM فال بیک | معیار کی حفاظتی جال | مشکل سوالات کو بہتر بنائیں | اگر SLM جواب کی لمبائی < حد یا کم اعتماد → بڑھائیں |

#### ہائبرڈ ڈرافٹ/ریفائن پیٹرن کی مثال

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### لیٹینسی بریک ڈاؤن خاکہ

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

ماڈلز کے درمیان منصفانہ موازنہ کے لیے مستقل پیمائش کے ڈھانچے کا استعمال کریں۔

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔