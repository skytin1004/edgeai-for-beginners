<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aee170a832b8870fc6eea546aa544bdb",
  "translation_date": "2025-10-09T06:45:24+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "ur"
}
-->
# سیشن 5: فاؤنڈری لوکل کے ساتھ تیزی سے AI پاورڈ ایجنٹس بنائیں

## خلاصہ

فاؤنڈری لوکل کے کم لیٹینسی اور پرائیویسی محفوظ رن ٹائم کا استعمال کرتے ہوئے ملٹی رول AI ایجنٹس کو ڈیزائن اور آرکیسٹریٹ کریں۔ آپ ایجنٹس کے کردار، میموری کی حکمت عملی، ٹول انووکیشن پیٹرنز، اور ایکزیکیوشن گرافز کی تعریف کریں گے۔ یہ سیشن اسکیفولڈنگ پیٹرنز کا تعارف کراتا ہے جنہیں آپ چینلٹ یا لینگ گراف کے ساتھ بڑھا سکتے ہیں۔ اسٹارٹر پروجیکٹ موجودہ ایجنٹ آرکیٹیکچر سیمپل کو میموری پرسسٹنس اور ایویلیوایشن ہکس شامل کرنے کے لیے بڑھاتا ہے۔

## سیکھنے کے مقاصد

- **کردار کی تعریف کریں**: سسٹم پرامپٹس اور صلاحیت کی حدود
- **میموری نافذ کریں**: قلیل مدتی (گفتگو)، طویل مدتی (ویکٹر / فائل)، عارضی اسکریچ پیڈز
- **ورک فلو اسکیفولڈ کریں**: ترتیب وار، شاخ دار، اور متوازی ایجنٹ کے مراحل
- **ٹولز کو ضم کریں**: ہلکے وزن کے فنکشن ٹول کالنگ پیٹرن
- **تشخیص کریں**: بنیادی ٹریس + روبریک پر مبنی نتائج کی اسکورنگ

## ضروریات

- سیشنز 1–4 مکمل کیے گئے ہوں
- Python کے ساتھ `foundry-local-sdk`, `openai`, اختیاری `chainlit`
- لوکل ماڈلز چل رہے ہوں (کم از کم `phi-4-mini`)

### کراس پلیٹ فارم انوائرمنٹ اسنیپٹ

ونڈوز:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

میک او ایس:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

اگر ایجنٹس کو میک او ایس سے ریموٹ ونڈوز ہوسٹ سروس کے خلاف چلایا جا رہا ہو:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## ڈیمو فلو (30 منٹ)

### 1. ایجنٹ کے کردار اور میموری کی تعریف کریں (7 منٹ)

`samples/05-agents/agents_core.py` بنائیں:

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


### 2. CLI اسکیفولڈنگ پیٹرن (3 منٹ)

```powershell
python samples/05-agents/agents_core.py
```


### 3. ٹول انووکیشن شامل کریں (7 منٹ)

`samples/05-agents/tools.py` کے ساتھ توسیع کریں:

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


`agents_core.py` میں ترمیم کریں تاکہ سادہ ٹول سینٹیکس کی اجازت دی جا سکے: صارف لکھتا ہے `#tool:get_time` اور ایجنٹ جنریشن سے پہلے کانٹیکسٹ میں ٹول آؤٹ پٹ کو شامل کرتا ہے۔

### 4. آرکیسٹریٹڈ ورک فلو (6 منٹ)

`samples/05-agents/orchestrator.py` بنائیں:

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


### 5. اسٹارٹر پروجیکٹ: `05-agent-architecture` کو بڑھائیں (7 منٹ)

شامل کریں:
1. مستقل میموری لیئر (مثلاً، گفتگو کے JSON لائنز اپینڈ)
2. سادہ ایویلیوایشن روبریک: حقائق، وضاحت، اسٹائل پلیس ہولڈرز
3. اختیاری چینلٹ فرنٹ اینڈ (دو ٹیبز: گفتگو اور ٹریسز)
4. اختیاری لینگ گراف اسٹائل اسٹیٹ مشین (اگر ڈیپینڈنسی شامل کر رہے ہیں) شاخ دار فیصلوں کے لیے

## ویلیڈیشن چیک لسٹ

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```


ٹول انجیکشن نوٹ کے ساتھ ساختی پائپ لائن آؤٹ پٹ کی توقع کریں۔

## میموری حکمت عملی کا جائزہ

| لیئر | مقصد | مثال |
|------|-------|-------|
| قلیل مدتی | گفتگو کا تسلسل | آخری N پیغامات |
| ایپیسوڈک | سیشن کی یاد دہانی | ہر سیشن کے لیے JSON |
| سیمانٹک | طویل مدتی بازیافت | خلاصوں کا ویکٹر اسٹور |
| اسکریچ پیڈ | استدلال کے مراحل | ان لائن چین آف تھوٹ (نجی) |

## ایویلیوایشن ہکس (تصوراتی)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## مسائل کا حل

| مسئلہ | وجہ | حل |
|-------|------|-----|
| بار بار جوابات | کانٹیکسٹ ونڈو بہت بڑی/چھوٹی | میموری ونڈو پیرامیٹر کو ایڈجسٹ کریں |
| ٹول انووک نہیں ہوا | غلط سینٹیکس | `#tool:tool_name` فارمیٹ استعمال کریں |
| سست آرکیسٹریشن | متعدد کولڈ ماڈلز | پری رن وارم اپ پرامپٹس استعمال کریں |

## حوالہ جات

- فاؤنڈری لوکل SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- لینگ گراف (اختیاری تصور): https://github.com/langchain-ai/langgraph
- چینلٹ: https://docs.chainlit.io

---

**سیشن کا دورانیہ**: 30 منٹ  
**مشکل سطح**: ایڈوانسڈ

## نمونہ منظر نامہ اور ورکشاپ میپنگ

| ورکشاپ اسکرپٹ | منظر نامہ | مقصد | مثال پرامپٹ |
|---------------|-----------|-------|-------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | ایگزیکٹو فرینڈلی خلاصے تیار کرنے والا نالج ریسرچ بوٹ | دو ایجنٹ پائپ لائن (ریسرچ → ایڈیٹوریل پولش) اختیاری مختلف ماڈلز کے ساتھ | وضاحت کریں کہ کمپلائنس کے لیے ایج انفرنس کیوں اہم ہے۔ |
| (توسیع شدہ) `tools.py` تصور | وقت اور ٹوکن تخمینہ ٹولز شامل کریں | ہلکے وزن کے ٹول انووکیشن پیٹرن کا مظاہرہ کریں | #tool:get_time |

### منظر نامہ کی کہانی

کمپلائنس ڈاکیومنٹیشن ٹیم کو لوکل نالج سے حاصل کردہ تیز اندرونی بریفز کی ضرورت ہے بغیر ڈرافٹس کو کلاؤڈ سروسز پر بھیجے۔ ایک ریسرچر ایجنٹ مختصر حقائق جمع کرتا ہے؛ ایک ایڈیٹر ایجنٹ ایگزیکٹو وضاحت کے لیے دوبارہ لکھتا ہے۔ لیٹینسی کو بہتر بنانے کے لیے مختلف ماڈل عرفیتیں تفویض کی جا سکتی ہیں (تیز SLM) بمقابلہ اسٹائلسٹک ریفائنمنٹ (بڑے ماڈل صرف ضرورت کے وقت)۔

### مثال ملٹی ماڈل انوائرمنٹ

```powershell
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python Workshop\samples\session05\agents_orchestrator.py
```


### ٹریس اسٹرکچر (اختیاری)

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


ہر مرحلے کو JSONL فائل میں محفوظ کریں تاکہ بعد میں روبریک اسکورنگ کی جا سکے۔

### اختیاری بہتریاں

| تھیم | بہتری | فائدہ | نفاذ کا خاکہ |
|------|-------|-------|-------------|
| ملٹی ماڈل کردار | ہر ایجنٹ کے لیے مختلف ماڈلز (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | مہارت اور رفتار | عرفیت انوائرمنٹ ویریبلز منتخب کریں، ہر کردار کے لیے `chat_once` کال کریں |
| ساختی ٹریسز | ہر ایکٹ (ٹول، ان پٹ، لیٹینسی، ٹوکنز) کا JSON ٹریس | ڈیبگ اور ایویلیوایشن | ڈکشنری کو ایک لسٹ میں شامل کریں؛ آخر میں `.jsonl` لکھیں |
| میموری پرسسٹنس | دوبارہ لوڈ ہونے والا ڈائیلاگ کانٹیکسٹ | سیشن تسلسل | `Agent.memory` کو `sessions/<ts>.json` میں ڈمپ کریں |
| ٹول رجسٹری | ڈائنامک ٹول دریافت | توسیع پذیری | `TOOLS` ڈکشنری برقرار رکھیں اور نام/تفصیل کا جائزہ لیں |
| ریٹری اور بیک آف | مضبوط طویل چینز | عارضی ناکامیوں کو کم کریں | `act` کو try/except + ایکسپونینشل بیک آف کے ساتھ لپیٹیں |
| روبریک اسکورنگ | خودکار معیاری لیبلز | بہتری کا ٹریک رکھیں | ماڈل کو سیکنڈری پاس پرامپٹ کریں: "وضاحت کو 1-5 تک ریٹ کریں" |
| ویکٹر میموری | سیمانٹک بازیافت | بھرپور طویل مدتی کانٹیکسٹ | خلاصے ایمبیڈ کریں، سسٹم میسج میں ٹاپ-k بازیافت کریں |
| اسٹریمنگ جوابات | تیز محسوس ہونے والا ردعمل | UX میں بہتری | اسٹریمنگ دستیاب ہونے پر استعمال کریں اور جزوی ٹوکنز کو فلش کریں |
| ڈیٹرمینیٹک ٹیسٹس | ریگریشن کنٹرول | مستحکم CI | `temperature=0`، فکسڈ پرامپٹ سیڈز کے ساتھ چلائیں |
| متوازی شاخیں | تیز تر دریافت | تھروپٹ | آزاد ایجنٹ مراحل کے لیے `concurrent.futures` استعمال کریں |

#### ٹریس ریکارڈ مثال

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### سادہ ایویلیوایشن پرامپٹ

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```


(`answer`, `rating`) جوڑوں کو محفوظ کریں تاکہ تاریخی معیار کا گراف بنایا جا سکے۔

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔