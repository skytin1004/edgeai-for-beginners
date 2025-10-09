<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d1b3c0fecfd713c2df903a0633249dc9",
  "translation_date": "2025-10-09T06:42:04+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "ar"
}
-->
# الجلسة 4: استكشاف النماذج المتطورة – LLMs، SLMs والاستدلال على الجهاز

## الملخص

قارن بين النماذج اللغوية الكبيرة (LLMs) والنماذج اللغوية الصغيرة (SLMs) في سيناريوهات الاستدلال المحلي مقابل السحابي. تعلم أنماط النشر باستخدام تسريع ONNX Runtime، تنفيذ WebGPU، وتجارب RAG الهجينة. تتضمن الجلسة عرضًا توضيحيًا باستخدام Chainlit RAG مع نموذج محلي بالإضافة إلى استكشاف اختياري لـ OpenWebUI. ستقوم بتكييف مشروع بدء تشغيل الاستدلال باستخدام WebGPU وتقييم القدرات والتكاليف/الأداء بين Phi وGPT-OSS-20B.

## أهداف التعلم

- **المقارنة** بين SLM وLLM من حيث التأخير، الذاكرة، والجودة
- **نشر** النماذج باستخدام ONNXRuntime و(عند الدعم) WebGPU
- **تشغيل** الاستدلال عبر المتصفح (عرض تفاعلي يحافظ على الخصوصية)
- **دمج** خط أنابيب Chainlit RAG مع نموذج SLM محلي
- **التقييم** باستخدام معايير جودة وتكلفة خفيفة

## المتطلبات الأساسية

- إكمال الجلسات 1–3
- تثبيت `chainlit` (موجود بالفعل في `requirements.txt` لـ Module08)
- متصفح يدعم WebGPU (Edge / Chrome أحدث إصدار على Windows 11)
- تشغيل Foundry Local (`foundry status`)

### ملاحظات عبر الأنظمة

Windows يظل البيئة المستهدفة الأساسية. بالنسبة لمطوري macOS الذين ينتظرون الثنائيات الأصلية:
1. قم بتشغيل Foundry Local في جهاز افتراضي Windows 11 (Parallels / UTM) أو محطة عمل Windows عن بُعد.
2. قم بفتح الخدمة (المنفذ الافتراضي 5273) وقم بالإعداد على macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. استخدم نفس خطوات البيئة الافتراضية لـ Python كما في الجلسات السابقة.

تثبيت Chainlit (كلا النظامين):
```bash
pip install chainlit
```

## تدفق العرض التوضيحي (30 دقيقة)

### 1. مقارنة Phi (SLM) مقابل GPT-OSS-20B (LLM) (6 دقائق)

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

تتبع: عمق الاستجابة، دقة الحقائق، ثراء الأسلوب، التأخير.

### 2. تسريع ONNX Runtime (5 دقائق)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   set BENCH_MODELS=phi-4-mini
#   python Workshop\samples\session03\benchmark_oss_models.py
```

لاحظ تغييرات الإنتاجية بعد تمكين GPU مقابل CPU فقط.

### 3. استدلال WebGPU في المتصفح (6 دقائق)

قم بتكييف مشروع البدء `04-webgpu-inference` (إنشاء `samples/04-cutting-edge/webgpu_demo.html`):

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

افتح الملف في المتصفح؛ لاحظ جولة محلية منخفضة التأخير.

### 4. تطبيق دردشة Chainlit RAG (7 دقائق)

`samples/04-cutting-edge/chainlit_app.py` بسيط:

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

تشغيل:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. مشروع البدء: تكييف `04-webgpu-inference` (6 دقائق)

المخرجات:
- استبدال منطق الجلب المؤقت بتدفق الرموز (استخدام متغير نقطة النهاية `stream=True` بمجرد التمكين)
- إضافة مخطط التأخير (على الجانب العميل) لتبديل بين phi وgpt-oss-20b
- تضمين سياق RAG داخلي (منطقة نصية للمستندات المرجعية)

## معايير التقييم

| الفئة | Phi-4-mini | GPT-OSS-20B | الملاحظة |
|-------|------------|-------------|-----------|
| التأخير (بارد) | سريع | أبطأ | SLM يسخن بسرعة |
| الذاكرة | منخفضة | عالية | جدوى الجهاز |
| الالتزام بالسياق | جيد | قوي | النموذج الأكبر قد يكون أكثر تفصيلاً |
| التكلفة (محلي) | ضئيلة | أعلى (الموارد) | توازن الطاقة/الوقت |
| أفضل حالة استخدام | تطبيقات الحافة | التفكير العميق | خط أنابيب هجين ممكن |

## التحقق من البيئة

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python Workshop\samples\session03\benchmark_oss_models.py
```

## استكشاف الأخطاء وإصلاحها

| العرض | السبب | الإجراء |
|-------|-------|--------|
| فشل جلب صفحة الويب | CORS أو الخدمة معطلة | استخدم `curl` للتحقق من نقطة النهاية؛ قم بتمكين وكيل CORS إذا لزم الأمر |
| Chainlit فارغ | البيئة غير نشطة | قم بتنشيط البيئة الافتراضية وأعد تثبيت التبعيات |
| تأخير عالي | النموذج تم تحميله للتو | قم بتسخينه بتسلسل مطالبات صغيرة |

## المراجع

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- وثائق Chainlit: https://docs.chainlit.io
- تقييم RAG (Ragas): https://docs.ragas.io

---

**مدة الجلسة**: 30 دقيقة  
**الصعوبة**: متقدمة

## سيناريو العينة وتخطيط ورشة العمل

| مواد ورشة العمل | السيناريو | الهدف | مصدر البيانات / المطالبات |
|------------------|----------|-------|---------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | فريق الهندسة المعمارية يقيم SLM مقابل LLM لتوليد ملخصات تنفيذية | قياس الفرق في التأخير + استخدام الرموز | متغير بيئة `COMPARE_PROMPT` واحد |
| `chainlit_app.py` (عرض RAG) | نموذج مساعد داخلي للمعرفة | تقديم إجابات قصيرة مع استرجاع لغوي ضئيل | قائمة `DOCS` مضمنة في الملف |
| `webgpu_demo.html` | معاينة استدلال مستقبلي على الجهاز عبر المتصفح | عرض جولة محلية منخفضة التأخير + سرد تجربة المستخدم | مطالبة المستخدم الحية فقط |

### سرد السيناريو
تريد منظمة المنتج مولد ملخصات تنفيذية. يقوم نموذج SLM خفيف الوزن (phi‑4‑mini) بصياغة الملخصات؛ قد يقوم نموذج LLM أكبر (gpt‑oss‑20b) بتحسين التقارير ذات الأولوية العالية فقط. تسجل نصوص الجلسة مقاييس التأخير والرموز التجريبية لتبرير تصميم هجين، بينما يوضح عرض Chainlit كيف يحافظ الاسترجاع الموجه على إجابات النموذج الصغير دقيقة. توفر صفحة مفهوم WebGPU مسار رؤية للمعالجة الكاملة على العميل عندما ينضج تسريع المتصفح.

### سياق RAG الأدنى (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### تدفق الهجين: صياغة → تحسين (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

تتبع كلا مكوني التأخير للإبلاغ عن متوسط التكلفة المدمجة.

### تحسينات اختيارية

| التركيز | التحسين | السبب | تلميح التنفيذ |
|---------|---------|-------|---------------|
| المقاييس المقارنة | تتبع استخدام الرموز + تأخير أول رمز | عرض أداء شامل | استخدم نص تحسين القياس (الجلسة 3) مع `BENCH_STREAM=1` |
| خط أنابيب هجين | صياغة SLM → تحسين LLM | تقليل التأخير والتكلفة | توليد باستخدام phi-4-mini، تحسين الملخص باستخدام gpt-oss-20b |
| واجهة مستخدم متدفقة | تجربة مستخدم أفضل في Chainlit | ردود فعل تدريجية | استخدم `stream=True` بمجرد تمكين التدفق المحلي؛ اجمع الأجزاء |
| تخزين مؤقت WebGPU | بدء تشغيل JS أسرع | تقليل عبء إعادة الترجمة | تخزين مؤقت للقطع الشيفرة المترجمة (قدرة تشغيل مستقبلية) |
| مجموعة أسئلة محددة | مقارنة عادلة للنماذج | إزالة التباين | قائمة مطالبات ثابتة + `temperature=0` لتشغيلات التقييم |
| تسجيل النتائج | عدسة جودة منظمة | تجاوز الحكايات | معيار بسيط: التماسك / الحقائق / الإيجاز (1–5) |
| ملاحظات الطاقة / الموارد | مناقشة صفية | عرض التوازنات | استخدم مراقبي النظام (`foundry system info`, Task Manager, `nvidia-smi`) + مخرجات نص القياس |
| محاكاة التكلفة | تبرير ما قبل السحابة | تخطيط التوسع | قم بتعيين الرموز إلى تسعير السحابة الافتراضي لرواية TCO |
| تحليل التأخير | تحديد نقاط الاختناق | استهداف التحسينات | قياس إعداد المطالبات، إرسال الطلب، أول رمز، الإكمال الكامل |
| RAG + LLM احتياطي | شبكة أمان الجودة | تحسين الاستفسارات الصعبة | إذا كان طول إجابة SLM < العتبة أو الثقة منخفضة → تصعيد |

#### نمط صياغة/تحسين الهجين

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### مخطط تفصيلي لتحليل التأخير

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

استخدم هيكل قياس متسق عبر النماذج للمقارنات العادلة.

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.