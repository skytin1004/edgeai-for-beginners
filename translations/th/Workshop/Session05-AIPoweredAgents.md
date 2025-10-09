<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aee170a832b8870fc6eea546aa544bdb",
  "translation_date": "2025-10-09T12:52:51+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "th"
}
-->
# Session 5: สร้างตัวแทน AI ที่ทรงพลังได้อย่างรวดเร็วด้วย Foundry Local

## บทคัดย่อ

ออกแบบและจัดการตัวแทน AI หลายบทบาทโดยใช้ Foundry Local ที่มีการประมวลผลแบบความหน่วงต่ำและรักษาความเป็นส่วนตัว คุณจะได้กำหนดบทบาทของตัวแทน กลยุทธ์การจดจำรูปแบบ การเรียกใช้เครื่องมือ และกราฟการดำเนินการ เซสชันนี้จะแนะนำรูปแบบการสร้างโครงสร้างที่คุณสามารถขยายได้ด้วย Chainlit หรือ LangGraph โครงการเริ่มต้นจะขยายตัวอย่างสถาปัตยกรรมตัวแทนที่มีอยู่เพื่อเพิ่มการบันทึกความจำและตัวประเมินผล

## วัตถุประสงค์การเรียนรู้

- **กำหนดบทบาท**: คำสั่งระบบและขอบเขตความสามารถ
- **นำการจดจำมาใช้**: ระยะสั้น (การสนทนา), ระยะยาว (เวกเตอร์ / ไฟล์), สมุดบันทึกชั่วคราว
- **สร้างโครงสร้างการทำงาน**: ขั้นตอนตัวแทนแบบลำดับ, แตกแขนง, และขนาน
- **ผสานเครื่องมือ**: รูปแบบการเรียกใช้ฟังก์ชันเครื่องมือที่เบา
- **ประเมินผล**: การติดตามพื้นฐาน + การให้คะแนนผลลัพธ์ตามเกณฑ์

## ข้อกำหนดเบื้องต้น

- ผ่านเซสชัน 1–4 แล้ว
- Python พร้อม `foundry-local-sdk`, `openai`, และ `chainlit` (ไม่บังคับ)
- โมเดลที่ทำงานในเครื่อง (อย่างน้อย `phi-4-mini`)

### ตัวอย่างการตั้งค่าสภาพแวดล้อมข้ามแพลตฟอร์ม

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

หากเรียกใช้ตัวแทนจาก macOS กับบริการโฮสต์ Windows ระยะไกล:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## ลำดับการสาธิต (30 นาที)

### 1. กำหนดบทบาทตัวแทนและความจำ (7 นาที)

สร้าง `samples/05-agents/agents_core.py`:

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


### 2. รูปแบบการสร้างโครงสร้าง CLI (3 นาที)

```powershell
python samples/05-agents/agents_core.py
```


### 3. เพิ่มการเรียกใช้เครื่องมือ (7 นาที)

ขยายด้วย `samples/05-agents/tools.py`:

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

ปรับ `agents_core.py` เพื่อให้รองรับไวยากรณ์เครื่องมือแบบง่าย: ผู้ใช้เขียน `#tool:get_time` และตัวแทนจะขยายผลลัพธ์ของเครื่องมือเข้าไปในบริบทก่อนการสร้างข้อความ

### 4. การจัดการโครงสร้างการทำงาน (6 นาที)

สร้าง `samples/05-agents/orchestrator.py`:

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


### 5. โครงการเริ่มต้น: ขยาย `05-agent-architecture` (7 นาที)

เพิ่ม:
1. ชั้นความจำที่คงอยู่ (เช่น การเพิ่มบรรทัด JSON ของการสนทนา)
2. เกณฑ์การประเมินผลแบบง่าย: ความถูกต้อง / ความชัดเจน / สไตล์
3. ส่วนหน้าของ Chainlit (สองแท็บ: การสนทนา & การติดตาม)
4. สไตล์เครื่องจักรสถานะ LangGraph (ถ้าเพิ่มการพึ่งพา) สำหรับการตัดสินใจแบบแตกแขนง

## รายการตรวจสอบการตรวจสอบ

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

คาดหวังผลลัพธ์ของกระบวนการที่มีการบันทึกการฉีดเครื่องมือ

## ภาพรวมกลยุทธ์การจดจำ

| ชั้น | วัตถุประสงค์ | ตัวอย่าง |
|------|---------------|----------|
| ระยะสั้น | ความต่อเนื่องของการสนทนา | ข้อความ N ล่าสุด |
| ระยะตอน | การเรียกคืนเซสชัน | JSON ต่อเซสชัน |
| ระยะความหมาย | การเรียกคืนระยะยาว | เวกเตอร์สโตร์ของบทสรุป |
| สมุดบันทึก | ขั้นตอนการให้เหตุผล | การคิดแบบลำดับในตัว (ส่วนตัว) |

## ตัวประเมินผล (แนวคิด)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## การแก้ไขปัญหา

| ปัญหา | สาเหตุ | วิธีแก้ไข |
|-------|--------|-----------|
| คำตอบซ้ำ | หน้าต่างบริบทใหญ่/เล็กเกินไป | ปรับพารามิเตอร์หน้าต่างความจำ |
| เครื่องมือไม่ได้ถูกเรียกใช้ | ไวยากรณ์ผิด | ใช้รูปแบบ `#tool:tool_name` |
| การจัดการช้า | โมเดลเย็นหลายตัว | เริ่มต้นคำสั่งอุ่นเครื่องล่วงหน้า |

## อ้างอิง

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (แนวคิดไม่บังคับ): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**ระยะเวลาเซสชัน**: 30 นาที  
**ระดับความยาก**: ขั้นสูง

## ตัวอย่างสถานการณ์และการจับคู่เวิร์กช็อป

| สคริปต์เวิร์กช็อป | สถานการณ์ | วัตถุประสงค์ | ตัวอย่างคำสั่ง |
|--------------------|------------|---------------|-----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | บอทวิจัยความรู้ที่สร้างบทสรุปที่เหมาะกับผู้บริหาร | ท่อส่งตัวแทนสองตัว (วิจัย → ขัดเกลาเนื้อหา) พร้อมโมเดลที่แตกต่างกัน (ไม่บังคับ) | อธิบายว่าทำไมการอนุมานขอบจึงสำคัญสำหรับการปฏิบัติตามข้อกำหนด |
| (ขยาย) แนวคิด `tools.py` | เพิ่มเครื่องมือประมาณเวลาและโทเค็น | สาธิตรูปแบบการเรียกใช้เครื่องมือที่เบา | #tool:get_time |

### เรื่องราวสถานการณ์
ทีมเอกสารการปฏิบัติตามข้อกำหนดต้องการบทสรุปภายในที่รวดเร็วจากความรู้ในเครื่องโดยไม่ส่งร่างไปยังบริการคลาวด์ ตัวแทนวิจัยรวบรวมข้อมูลข้อเท็จจริงที่กระชับ; ตัวแทนบรรณาธิการเขียนใหม่ให้เหมาะกับผู้บริหาร สามารถกำหนดชื่อโมเดลที่แตกต่างกันเพื่อเพิ่มประสิทธิภาพความหน่วง (SLM ที่เร็ว) กับการปรับแต่งสไตล์ (โมเดลที่ใหญ่กว่าเมื่อจำเป็น)

### ตัวอย่างสภาพแวดล้อมหลายโมเดล
```powershell
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python Workshop\samples\session05\agents_orchestrator.py
```


### โครงสร้างการติดตาม (ไม่บังคับ)
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

บันทึกแต่ละขั้นตอนลงในไฟล์ JSONL เพื่อการให้คะแนนตามเกณฑ์ในภายหลัง

### การปรับปรุงเพิ่มเติม (ไม่บังคับ)

| ธีม | การปรับปรุง | ประโยชน์ | โครงร่างการดำเนินการ |
|-----|-------------|----------|-----------------------|
| บทบาทหลายโมเดล | โมเดลที่แตกต่างกันต่อตัวแทน (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | ความเชี่ยวชาญและความเร็ว | เลือกตัวแปรสภาพแวดล้อมชื่อ, เรียก `chat_once` ด้วยชื่อโมเดลต่อบทบาท |
| การติดตามที่มีโครงสร้าง | การติดตาม JSON ของแต่ละการกระทำ (เครื่องมือ, อินพุต, ความหน่วง, โทเค็น) | การแก้ไขข้อผิดพลาดและการประเมินผล | เพิ่ม dict ลงในรายการ; เขียน `.jsonl` เมื่อสิ้นสุด |
| ความจำที่คงอยู่ | บริบทการสนทนาที่โหลดใหม่ได้ | ความต่อเนื่องของเซสชัน | บันทึก `Agent.memory` ลงใน `sessions/<ts>.json` |
| การลงทะเบียนเครื่องมือ | การค้นพบเครื่องมือแบบไดนามิก | ความสามารถในการขยาย | รักษา dict `TOOLS` และตรวจสอบชื่อ/คำอธิบาย |
| การลองใหม่และการถอยหลัง | โซ่ยาวที่แข็งแกร่ง | ลดความล้มเหลวชั่วคราว | ห่อ `act` ด้วย try/except + การถอยหลังแบบเอ็กซ์โพเนนเชียล |
| การให้คะแนนตามเกณฑ์ | ป้ายกำกับเชิงคุณภาพอัตโนมัติ | ติดตามการปรับปรุง | การแจ้งโมเดลรอบที่สอง: "ให้คะแนนความชัดเจน 1-5" |
| ความจำแบบเวกเตอร์ | การเรียกคืนเชิงความหมาย | บริบทระยะยาวที่สมบูรณ์ | ฝังบทสรุป, เรียกคืน top-k เข้าไปในข้อความระบบ |
| การตอบกลับแบบสตรีม | การตอบสนองที่เร็วขึ้น | การปรับปรุง UX | ใช้การสตรีมเมื่อพร้อมใช้งานและล้างโทเค็นบางส่วน |
| การทดสอบแบบกำหนด | การควบคุมการถดถอย | CI ที่เสถียร | เรียกใช้ด้วย `temperature=0`, เมล็ดคำสั่งคงที่ |
| การแตกแขนงแบบขนาน | การสำรวจที่เร็วขึ้น | ปริมาณงาน | ใช้ `concurrent.futures` สำหรับขั้นตอนตัวแทนที่เป็นอิสระ |

#### ตัวอย่างบันทึกการติดตาม

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### คำสั่งประเมินผลแบบง่าย

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

บันทึกคู่ (`answer`, `rating`) เพื่อสร้างกราฟคุณภาพในอดีต

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้