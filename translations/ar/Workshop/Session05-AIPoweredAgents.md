<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aee170a832b8870fc6eea546aa544bdb",
  "translation_date": "2025-10-09T06:44:46+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "ar"
}
-->
# الجلسة الخامسة: بناء وكلاء مدعومين بالذكاء الاصطناعي بسرعة باستخدام Foundry Local

## الملخص

صمم ونظم وكلاء ذكاء اصطناعي متعددين الأدوار باستخدام بيئة التشغيل Foundry Local التي تتميز بزمن استجابة منخفض وحفاظها على الخصوصية. ستقوم بتحديد أدوار الوكلاء، استراتيجيات الذاكرة، أنماط استدعاء الأدوات، ورسوم التنفيذ البيانية. تقدم الجلسة أنماط هيكلية يمكنك توسيعها باستخدام Chainlit أو LangGraph. المشروع المبدئي يوسع نموذج بنية الوكيل الحالي لإضافة استمرارية الذاكرة وخطافات التقييم.

## أهداف التعلم

- **تحديد الأدوار**: مطالبات النظام وحدود القدرات  
- **تنفيذ الذاكرة**: قصيرة المدى (المحادثة)، طويلة المدى (متجه / ملف)، دفاتر مؤقتة  
- **بناء سير العمل**: خطوات الوكيل المتسلسلة، المتفرعة، والمتوازية  
- **دمج الأدوات**: نمط استدعاء الأدوات الوظيفية الخفيفة  
- **التقييم**: تتبع أساسي + تقييم النتائج بناءً على معايير محددة  

## المتطلبات الأساسية

- إكمال الجلسات من 1 إلى 4  
- Python مع `foundry-local-sdk`، `openai`، و `chainlit` اختياري  
- تشغيل النماذج المحلية (على الأقل `phi-4-mini`)  

### مقتطف بيئة متعددة الأنظمة

Windows:  
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```
  
macOS:  
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```
  
إذا كنت تقوم بتشغيل الوكلاء من macOS ضد خدمة مضيفة عن بُعد على Windows:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## تدفق العرض التوضيحي (30 دقيقة)

### 1. تحديد أدوار الوكلاء والذاكرة (7 دقائق)

إنشاء `samples/05-agents/agents_core.py`:

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```
  

### 2. نمط الهيكلة عبر CLI (3 دقائق)

```powershell
python samples/05-agents/agents_core.py
```
  

### 3. إضافة استدعاء الأدوات (7 دقائق)

قم بالتوسيع باستخدام `samples/05-agents/tools.py`:

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```
  
قم بتعديل `agents_core.py` للسماح بصيغة أدوات بسيطة: يكتب المستخدم `#tool:get_time` ويقوم الوكيل بتوسيع مخرجات الأداة في السياق قبل التوليد.

### 4. سير العمل المنظم (6 دقائق)

إنشاء `samples/05-agents/orchestrator.py`:

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```
  

### 5. المشروع المبدئي: توسيع `05-agent-architecture` (7 دقائق)

أضف:  
1. طبقة ذاكرة مستمرة (مثل إضافة خطوط JSON للمحادثات)  
2. معيار تقييم بسيط: حقائق / وضوح / أسلوب  
3. واجهة أمامية اختيارية باستخدام Chainlit (علامتان: المحادثة والتتبع)  
4. آلة حالة بأسلوب LangGraph (اختياري إذا تمت إضافة التبعية) لاتخاذ قرارات متفرعة  

## قائمة التحقق من التحقق

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```
  
توقع إخراج خط أنابيب منظم مع ملاحظة إدخال الأداة.

## نظرة عامة على استراتيجيات الذاكرة

| الطبقة | الغرض | المثال |
|--------|-------|--------|
| قصيرة المدى | استمرارية الحوار | آخر N رسالة |
| الحلقية | استدعاء الجلسة | JSON لكل جلسة |
| الدلالية | استرجاع طويل المدى | مخزن متجه للملخصات |
| دفتر مؤقت | خطوات التفكير | سلسلة أفكار داخلية (خاصة) |

## خطافات التقييم (مفهومي)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```
  

## استكشاف الأخطاء وإصلاحها

| المشكلة | السبب | الحل |
|---------|-------|------|
| إجابات متكررة | نافذة السياق كبيرة جدًا/صغيرة جدًا | ضبط معلمة نافذة الذاكرة |
| الأداة لم تُستدعى | صيغة خاطئة | استخدم صيغة `#tool:tool_name` |
| بطء في التنظيم | نماذج باردة متعددة | قم بتشغيل مطالبات الإحماء مسبقًا |

## المراجع

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- LangGraph (مفهوم اختياري): https://github.com/langchain-ai/langgraph  
- Chainlit: https://docs.chainlit.io  

---

**مدة الجلسة**: 30 دقيقة  
**الصعوبة**: متقدمة  

## سيناريو العينة وخريطة ورشة العمل

| نص ورشة العمل | السيناريو | الهدف | مثال على الطلب |
|---------------|-----------|-------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | روبوت بحث معرفي ينتج ملخصات مناسبة للإدارة التنفيذية | خط أنابيب من وكيلين (بحث → تنقيح تحرير) مع نماذج مميزة اختيارية | اشرح لماذا يعتبر الاستدلال المحلي مهمًا للامتثال. |
| (مفهوم موسع) `tools.py` | إضافة أدوات تقدير الوقت والرموز | توضيح نمط استدعاء الأدوات الخفيفة | #tool:get_time |

### سرد السيناريو
فريق توثيق الامتثال يحتاج إلى ملخصات داخلية سريعة مستمدة من المعرفة المحلية دون إرسال المسودات إلى خدمات السحابة. يقوم وكيل الباحث بجمع نقاط حقائق موجزة؛ يقوم وكيل المحرر بإعادة صياغتها لتكون واضحة للإدارة التنفيذية. يمكن تخصيص أسماء مستعارة لنماذج مميزة لتحسين زمن الاستجابة (نموذج سريع SLM) مقابل تحسين الأسلوب (نموذج أكبر عند الحاجة فقط).

### بيئة متعددة النماذج كمثال
```powershell
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python Workshop\samples\session05\agents_orchestrator.py
```
  

### هيكل التتبع (اختياري)
```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```
  
قم بحفظ كل خطوة في ملف JSONL للتقييم لاحقًا بناءً على المعايير.

### تحسينات اختيارية

| الموضوع | التحسين | الفائدة | مخطط التنفيذ |
|---------|---------|---------|--------------|
| أدوار متعددة النماذج | نماذج مميزة لكل وكيل (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | التخصص والسرعة | اختيار متغيرات البيئة المستعارة، استدعاء `chat_once` مع اسم مستعار لكل دور |
| تتبع منظم | تتبع JSON لكل فعل (أداة، إدخال، زمن استجابة، رموز) | التصحيح والتقييم | إضافة قاموس إلى قائمة؛ كتابة `.jsonl` في النهاية |
| استمرارية الذاكرة | سياق حوار قابل لإعادة التحميل | استمرارية الجلسة | حفظ `Agent.memory` في `sessions/<ts>.json` |
| سجل الأدوات | اكتشاف الأدوات الديناميكي | التوسع | الحفاظ على قاموس `TOOLS` واستكشاف الأسماء/الوصف |
| إعادة المحاولة والتراجع | سلاسل طويلة قوية | تقليل الأخطاء المؤقتة | تغليف `act` مع try/except + تراجع أسي |
| تقييم المعايير | تسميات نوعية تلقائية | تتبع التحسينات | تمرير ثانوي لنموذج التوجيه: "قيم الوضوح من 1-5" |
| ذاكرة المتجهات | استرجاع دلالي | سياق طويل المدى غني | تضمين الملخصات، استرجاع أفضل k إلى رسالة النظام |
| الردود المتدفقة | استجابة أسرع | تحسين تجربة المستخدم | استخدام التدفق عند توفره وتحديث الرموز الجزئية |
| اختبارات حتمية | التحكم في التراجع | CI مستقر | التشغيل مع `temperature=0`، بذور مطالبات ثابتة |
| التفرع المتوازي | استكشاف أسرع | زيادة الإنتاجية | استخدام `concurrent.futures` لخطوات الوكيل المستقلة |

#### مثال على سجل التتبع

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```
  

#### طلب تقييم بسيط

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```
  
قم بحفظ أزواج (`answer`, `rating`) لبناء رسم بياني تاريخي للجودة.

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.