<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec281a7cf06deda1f29140a2959ef0d2",
  "translation_date": "2025-10-09T13:12:52+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "th"
}
-->
# หมายเหตุการย้าย SDK Local Foundry

## ภาพรวม

ไฟล์ Python ทั้งหมดในโฟลเดอร์ Workshop ได้รับการอัปเดตให้สอดคล้องกับรูปแบบล่าสุดจาก [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) อย่างเป็นทางการ

## สรุปการเปลี่ยนแปลง

### โครงสร้างหลัก (`workshop_utils.py`)

#### คุณสมบัติที่ปรับปรุง:
- **รองรับการกำหนดค่า Endpoint**: เพิ่มการรองรับตัวแปรสภาพแวดล้อม `FOUNDRY_LOCAL_ENDPOINT`
- **การจัดการข้อผิดพลาดที่ดีขึ้น**: ปรับปรุงการจัดการข้อยกเว้นพร้อมข้อความแสดงข้อผิดพลาดที่ละเอียดขึ้น
- **การแคชที่ดีขึ้น**: คีย์แคชตอนนี้รวม Endpoint เพื่อรองรับสถานการณ์หลาย Endpoint
- **การหน่วงเวลาแบบ Exponential Backoff**: ตรรกะการลองใหม่ใช้ Exponential Backoff เพื่อเพิ่มความน่าเชื่อถือ
- **การใส่คำอธิบายประเภท**: เพิ่มคำอธิบายประเภทที่ครอบคลุมเพื่อรองรับ IDE ได้ดีขึ้น

#### ความสามารถใหม่:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### ตัวอย่างแอปพลิเคชัน

#### เซสชัน 01: การเริ่มต้นแชท (`chat_bootstrap.py`)
- อัปเดตรุ่นเริ่มต้นจาก `phi-3.5-mini` เป็น `phi-4-mini`
- เพิ่มการรองรับการกำหนดค่า Endpoint
- ปรับปรุงเอกสารด้วยการอ้างอิง SDK

#### เซสชัน 02: RAG Pipeline (`rag_pipeline.py`)
- อัปเดตให้ใช้ `phi-4-mini` เป็นค่าเริ่มต้น
- เพิ่มการรองรับการกำหนดค่า Endpoint
- ปรับปรุงเอกสารด้วยรายละเอียดตัวแปรสภาพแวดล้อม

#### เซสชัน 02: การประเมิน RAG (`rag_eval_ragas.py`)
- อัปเดตรุ่นเริ่มต้น
- เพิ่มการกำหนดค่า Endpoint
- ปรับปรุงการจัดการข้อผิดพลาด

#### เซสชัน 03: การวัดประสิทธิภาพ (`benchmark_oss_models.py`)
- อัปเดตรายการรุ่นเริ่มต้นเพื่อรวม `phi-4-mini`
- เพิ่มเอกสารตัวแปรสภาพแวดล้อมที่ครอบคลุม
- ปรับปรุงเอกสารฟังก์ชัน
- เพิ่มการรองรับการกำหนดค่า Endpoint ทั่วทั้งไฟล์

#### เซสชัน 04: การเปรียบเทียบรุ่น (`model_compare.py`)
- อัปเดตรุ่น LLM เริ่มต้นจาก `gpt-oss-20b` เป็น `qwen2.5-7b`
- เพิ่มการกำหนดค่า Endpoint
- ปรับปรุงเอกสาร

#### เซสชัน 05: การจัดการหลายตัวแทน (`agents_orchestrator.py`)
- เพิ่มคำอธิบายประเภท (เปลี่ยน `str | None` เป็น `Optional[str]`)
- ปรับปรุงเอกสารคลาส Agent
- เพิ่มการรองรับการกำหนดค่า Endpoint
- ปรับปรุงรูปแบบการเริ่มต้นใช้งาน

#### เซสชัน 06: ตัวจัดการรุ่น (`models_router.py`)
- เพิ่มการกำหนดค่า Endpoint
- ปรับปรุงเอกสารการตรวจจับเจตนา
- ปรับปรุงเอกสารตรรกะการจัดเส้นทาง

#### เซสชัน 06: Pipeline (`models_pipeline.py`)
- เพิ่มเอกสารฟังก์ชันที่ครอบคลุม
- ปรับปรุงเอกสารทีละขั้นตอน
- ปรับปรุงการจัดการข้อผิดพลาด

### สคริปต์

#### การส่งออกการวัดประสิทธิภาพ (`export_benchmark_markdown.py`)
- เพิ่มการรองรับการกำหนดค่า Endpoint
- อัปเดตรุ่นเริ่มต้น
- ปรับปรุงเอกสารฟังก์ชัน
- ปรับปรุงการจัดการข้อผิดพลาด

#### CLI Linter (`lint_markdown_cli.py`)
- เพิ่มลิงก์อ้างอิง SDK
- ปรับปรุงเอกสารการใช้งาน

### การทดสอบ

#### การทดสอบเบื้องต้น (`smoke.py`)
- เพิ่มการรองรับการกำหนดค่า Endpoint
- ปรับปรุงเอกสาร
- ปรับปรุงเอกสารกรณีทดสอบ
- รายงานข้อผิดพลาดได้ดีขึ้น

## ตัวแปรสภาพแวดล้อม

ตัวอย่างทั้งหมดตอนนี้รองรับตัวแปรสภาพแวดล้อมเหล่านี้:

### การกำหนดค่าหลัก
- `FOUNDRY_LOCAL_ALIAS` - ชื่อเรียกรุ่นที่จะใช้ (ค่าเริ่มต้นแตกต่างกันไปตามตัวอย่าง)
- `FOUNDRY_LOCAL_ENDPOINT` - กำหนดค่า Endpoint ของบริการ (ไม่บังคับ)
- `SHOW_USAGE` - แสดงสถิติการใช้โทเค็น (ค่าเริ่มต้น: "0")
- `RETRY_ON_FAIL` - เปิดใช้งานตรรกะการลองใหม่ (ค่าเริ่มต้น: "1")
- `RETRY_BACKOFF` - ความล่าช้าเริ่มต้นในการลองใหม่ในวินาที (ค่าเริ่มต้น: "1.0")

### เฉพาะตัวอย่าง
- `EMBED_MODEL` - รุ่นฝังสำหรับตัวอย่าง RAG
- `BENCH_MODELS` - รุ่นที่คั่นด้วยเครื่องหมายจุลภาคสำหรับการวัดประสิทธิภาพ
- `BENCH_ROUNDS` - จำนวนรอบการวัดประสิทธิภาพ
- `BENCH_PROMPT` - ข้อความทดสอบสำหรับการวัดประสิทธิภาพ
- `BENCH_STREAM` - วัดความล่าช้าของโทเค็นแรก
- `RAG_QUESTION` - คำถามทดสอบสำหรับตัวอย่าง RAG
- `AGENT_MODEL_PRIMARY` - รุ่นตัวแทนหลัก
- `AGENT_MODEL_EDITOR` - รุ่นตัวแทนแก้ไข
- `SLM_ALIAS` - ชื่อเรียกรุ่นภาษาขนาดเล็ก
- `LLM_ALIAS` - ชื่อเรียกรุ่นภาษาขนาดใหญ่

## แนวทางปฏิบัติที่ดีที่สุดของ SDK ที่นำมาใช้

### 1. การเริ่มต้นไคลเอนต์อย่างเหมาะสม
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

### 2. การดึงข้อมูลรุ่น
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. การจัดการข้อผิดพลาด
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. ตรรกะการลองใหม่ด้วย Exponential Backoff
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

### 5. รองรับการสตรีม
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

## คู่มือการย้ายสำหรับตัวอย่างที่กำหนดเอง

หากคุณกำลังสร้างตัวอย่างใหม่หรืออัปเดตตัวอย่างที่มีอยู่:

1. **ใช้ตัวช่วยใน `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **รองรับการกำหนดค่า Endpoint**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **เพิ่มเอกสารที่ครอบคลุม**:
   - ตัวแปรสภาพแวดล้อมใน docstring
   - ลิงก์อ้างอิง SDK
   - ตัวอย่างการใช้งาน

4. **ใช้คำอธิบายประเภท**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **นำการจัดการข้อผิดพลาดที่เหมาะสมมาใช้**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## การทดสอบ

ตัวอย่างทั้งหมดสามารถทดสอบได้ด้วย:

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

## การอ้างอิงเอกสาร SDK

- **ที่เก็บหลัก**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **เอกสาร API**: ตรวจสอบที่เก็บ SDK สำหรับเอกสาร API ล่าสุด

## การเปลี่ยนแปลงที่อาจทำให้เกิดปัญหา

### ไม่มีที่คาดไว้
การเปลี่ยนแปลงทั้งหมดเข้ากันได้ย้อนหลัง การอัปเดตส่วนใหญ่:
- เพิ่มคุณสมบัติใหม่ที่ไม่บังคับ (การกำหนดค่า Endpoint)
- ปรับปรุงการจัดการข้อผิดพลาด
- ปรับปรุงเอกสาร
- อัปเดตชื่อรุ่นเริ่มต้นให้เป็นคำแนะนำปัจจุบัน

### การปรับปรุงที่ไม่บังคับ
คุณอาจต้องการอัปเดตโค้ดของคุณเพื่อใช้:
- `FOUNDRY_LOCAL_ENDPOINT` สำหรับการควบคุม Endpoint อย่างชัดเจน
- `SHOW_USAGE=1` เพื่อดูการใช้โทเค็น
- รุ่นเริ่มต้นที่อัปเดต (`phi-4-mini` แทน `phi-3.5-mini`)

## ปัญหาทั่วไปและวิธีแก้ไข

### ปัญหา: "การเริ่มต้นไคลเอนต์ล้มเหลว"
**วิธีแก้ไข**: ตรวจสอบให้แน่ใจว่าบริการ Foundry Local กำลังทำงาน:
```bash
foundry service start
foundry model run phi-4-mini
```

### ปัญหา: "ไม่พบรุ่น"
**วิธีแก้ไข**: ตรวจสอบรุ่นที่มีอยู่:
```bash
foundry model list
```

### ปัญหา: ข้อผิดพลาดการเชื่อมต่อ Endpoint
**วิธีแก้ไข**: ตรวจสอบ Endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## ขั้นตอนถัดไป

1. **อัปเดตตัวอย่าง Module08**: ใช้รูปแบบที่คล้ายกันกับ Module08/samples
2. **เพิ่มการทดสอบการรวม**: สร้างชุดทดสอบที่ครอบคลุม
3. **การวัดประสิทธิภาพ**: เปรียบเทียบประสิทธิภาพก่อน/หลัง
4. **อัปเดตเอกสาร**: อัปเดต README หลักด้วยรูปแบบใหม่

## แนวทางการมีส่วนร่วม

เมื่อเพิ่มตัวอย่างใหม่:
1. ใช้ `workshop_utils.py` เพื่อความสม่ำเสมอ
2. ปฏิบัติตามรูปแบบในตัวอย่างที่มีอยู่
3. เพิ่ม docstring ที่ครอบคลุม
4. รวมลิงก์อ้างอิง SDK
5. รองรับการกำหนดค่า Endpoint
6. เพิ่มคำอธิบายประเภทที่เหมาะสม
7. รวมตัวอย่างการใช้งานใน docstring

## ความเข้ากันได้ของเวอร์ชัน

การอัปเดตเหล่านี้เข้ากันได้กับ:
- `foundry-local-sdk` (ล่าสุด)
- `openai>=1.30.0`
- Python 3.8+

---

**อัปเดตล่าสุด**: 2025-01-08  
**ผู้ดูแล**: ทีม EdgeAI Workshop  
**เวอร์ชัน SDK**: Foundry Local SDK (ล่าสุด 0.7.117+67073234e7)

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้