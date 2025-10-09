<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T12:46:54+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "th"
}
-->
# อัปเดต Foundry Local SDK

## ภาพรวม

ได้ปรับปรุงโน้ตบุ๊ก Workshop และเครื่องมือให้ใช้งาน **Foundry Local Python SDK อย่างเป็นทางการ** ตามรูปแบบจาก:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## ไฟล์ที่แก้ไข

### 1. `Workshop/samples/workshop_utils.py`

**การเปลี่ยนแปลง:**
- ✅ เพิ่มการจัดการข้อผิดพลาดการนำเข้าแพ็กเกจ `foundry-local-sdk`
- ✅ ปรับปรุงเอกสารให้สอดคล้องกับรูปแบบ SDK อย่างเป็นทางการ
- ✅ เพิ่มการล็อกด้วยสัญลักษณ์ Unicode (✓, ✗, ⚠)
- ✅ เพิ่ม docstring ที่ครอบคลุมพร้อมตัวอย่าง
- ✅ ข้อความแสดงข้อผิดพลาดที่ดีขึ้นพร้อมคำแนะนำ CLI
- ✅ อัปเดตความคิดเห็นให้ตรงกับเอกสาร SDK อย่างเป็นทางการ

**การปรับปรุงสำคัญ:**

#### การจัดการข้อผิดพลาดการนำเข้า
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### ฟังก์ชัน `get_client()` ที่ปรับปรุง
- เพิ่มเอกสารรายละเอียดเกี่ยวกับรูปแบบการเริ่มต้น SDK
- ชี้แจงว่า `FoundryLocalManager` เริ่มบริการโดยอัตโนมัติ
- อธิบายการแก้ไขชื่อโมเดลให้เป็นเวอร์ชันที่ปรับแต่งฮาร์ดแวร์
- ปรับปรุงการล็อกด้วยข้อมูล endpoint
- ข้อความแสดงข้อผิดพลาดที่ดีขึ้นพร้อมคำแนะนำการแก้ไขปัญหา

#### ฟังก์ชัน `chat_once()` ที่ปรับปรุง
- เพิ่ม docstring ที่ครอบคลุมพร้อมตัวอย่างการใช้งาน
- ชี้แจงความเข้ากันได้กับ OpenAI SDK
- เอกสารการรองรับการสตรีม (ผ่าน kwargs)
- ข้อความแสดงข้อผิดพลาดที่ดีขึ้นพร้อมคำแนะนำ CLI
- เพิ่มหมายเหตุเกี่ยวกับการตรวจสอบความพร้อมใช้งานของโมเดล

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**การเปลี่ยนแปลง:**
- ✅ อัปเดตเซลล์ markdown ทั้งหมดด้วยการอ้างอิง SDK
- ✅ ปรับปรุงความคิดเห็นในโค้ดด้วยคำอธิบายรูปแบบ SDK
- ✅ ปรับปรุงเอกสารและคำอธิบายในเซลล์
- ✅ เพิ่มคำแนะนำการแก้ไขปัญหา
- ✅ อัปเดตแคตตาล็อกโมเดล (แทนที่ 'gpt-oss-20b' ด้วย 'phi-3.5-mini')
- ✅ รูปแบบผลลัพธ์ที่ดีขึ้นพร้อมตัวบ่งชี้ภาพ
- ✅ เพิ่มลิงก์และการอ้างอิง SDK ตลอดทั้งไฟล์

**การอัปเดตเซลล์ทีละเซลล์:**

#### เซลล์ 1 (หัวข้อ)
- เพิ่มลิงก์เอกสาร SDK
- อ้างอิงที่เก็บ GitHub อย่างเป็นทางการ

#### เซลล์ 2 (สถานการณ์)
- ปรับรูปแบบด้วยขั้นตอนที่มีหมายเลข
- ชี้แจงรูปแบบการกำหนดเส้นทางตามเจตนา
- เน้นประโยชน์ของการดำเนินการในเครื่อง

#### เซลล์ 3 (การติดตั้ง Dependency)
- เพิ่มคำอธิบายว่าแต่ละแพ็กเกจให้บริการอะไร
- เอกสารความสามารถของ SDK (การแก้ไขชื่อ, การปรับแต่งฮาร์ดแวร์)

#### เซลล์ 4 (การตั้งค่าสภาพแวดล้อม)
- docstring ฟังก์ชันที่ปรับปรุง
- เพิ่มความคิดเห็นในบรรทัดที่อธิบายรูปแบบ SDK
- เอกสารโครงสร้างแคตตาล็อกโมเดล
- ชี้แจงการจับคู่ลำดับความสำคัญ/ความสามารถ

#### เซลล์ 5 (การตรวจสอบแคตตาล็อก)
- เพิ่มเครื่องหมายตรวจสอบภาพ (✓)
- รูปแบบผลลัพธ์ที่ดีขึ้น

#### เซลล์ 6 (การทดสอบการตรวจจับเจตนา)
- รูปแบบผลลัพธ์เป็นแบบตาราง
- แสดงทั้งเจตนาและโมเดลที่เลือก

#### เซลล์ 7 (ฟังก์ชันการกำหนดเส้นทาง)
- คำอธิบายรูปแบบ SDK ที่ครอบคลุม
- เอกสารการไหลของการเริ่มต้น
- แสดงรายการคุณสมบัติทั้งหมด (การลองใหม่, การติดตาม, ข้อผิดพลาด)
- เพิ่มลิงก์อ้างอิง SDK

#### เซลล์ 8 (การสาธิตแบบแบตช์)
- คำอธิบายที่ปรับปรุงเกี่ยวกับสิ่งที่คาดหวัง
- เพิ่มส่วนการแก้ไขปัญหา
- รวมคำสั่ง CLI สำหรับการดีบัก
- รูปแบบการแสดงผลที่ดีขึ้น

### 3. `Workshop/notebooks/session06_README.md` (ไฟล์ใหม่)

**สร้างเอกสารที่ครอบคลุมครอบคลุม:**

1. **ภาพรวม**: แผนภาพสถาปัตยกรรมและคำอธิบายส่วนประกอบ
2. **การรวม SDK**: ตัวอย่างโค้ดตามรูปแบบอย่างเป็นทางการ
3. **ข้อกำหนดเบื้องต้น**: คำแนะนำการตั้งค่าแบบทีละขั้นตอน
4. **การใช้งาน**: วิธีการเรียกใช้และปรับแต่งโน้ตบุ๊ก
5. **ชื่อโมเดล**: คำอธิบายของเวอร์ชันที่ปรับแต่งฮาร์ดแวร์
6. **การแก้ไขปัญหา**: ปัญหาทั่วไปและวิธีแก้ไข
7. **การขยาย**: วิธีเพิ่มเจตนา โมเดล และตรรกะที่กำหนดเอง
8. **เคล็ดลับประสิทธิภาพ**: แนวทางปฏิบัติที่ดีที่สุดสำหรับการใช้งานในระดับการผลิต
9. **ทรัพยากร**: ลิงก์ไปยังเอกสารและชุมชนอย่างเป็นทางการ

## การนำรูปแบบ SDK ไปใช้

### รูปแบบอย่างเป็นทางการ (จากเอกสาร Foundry Local)

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

### การนำไปใช้ของเรา (ใน workshop_utils)

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

**ประโยชน์ของวิธีการของเรา:**
- ✅ ปฏิบัติตามรูปแบบ SDK อย่างเป็นทางการอย่างเคร่งครัด
- ✅ เพิ่มการแคชเพื่อหลีกเลี่ยงการเริ่มต้นซ้ำ
- ✅ รวมตรรกะการลองใหม่เพื่อความแข็งแกร่งในการผลิต
- ✅ รองรับการติดตามการใช้งานโทเค็น
- ✅ ข้อความแสดงข้อผิดพลาดที่ดีขึ้น
- ✅ เข้ากันได้กับตัวอย่างอย่างเป็นทางการ

## การเปลี่ยนแปลงแคตตาล็อกโมเดล

### ก่อน
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### หลัง
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**เหตุผล:** แทนที่ 'gpt-oss-20b' (ชื่อที่ไม่เป็นมาตรฐาน) ด้วย 'phi-3.5-mini' (ชื่ออย่างเป็นทางการของ Foundry Local)

## Dependencies

### อัปเดต requirements.txt

ไฟล์ requirements.txt ของ Workshop มีอยู่แล้ว:
```
foundry-local-sdk
openai>=1.30.0
```

นี่คือแพ็กเกจเดียวที่จำเป็นสำหรับการรวม Foundry Local

## การทดสอบการอัปเดต

### 1. ตรวจสอบว่า Foundry Local กำลังทำงานอยู่

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. ตรวจสอบโมเดลที่มีอยู่

```bash
foundry model ls
```

ตรวจสอบให้แน่ใจว่าโมเดลเหล่านี้พร้อมใช้งานหรือจะดาวน์โหลดโดยอัตโนมัติ:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. เรียกใช้โน้ตบุ๊ก

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

หรือเปิดใน VS Code และเรียกใช้ทุกเซลล์

### 4. พฤติกรรมที่คาดหวัง

**เซลล์ 1 (ติดตั้ง):** ติดตั้งแพ็กเกจสำเร็จ  
**เซลล์ 2 (ตั้งค่า):** ไม่มีข้อผิดพลาด การนำเข้าทำงาน  
**เซลล์ 3 (ตรวจสอบ):** แสดง ✓ พร้อมรายการโมเดล  
**เซลล์ 4 (ทดสอบเจตนา):** แสดงผลการตรวจจับเจตนา  
**เซลล์ 5 (Router):** แสดง ✓ ฟังก์ชันการกำหนดเส้นทางพร้อม  
**เซลล์ 6 (ดำเนินการ):** กำหนดเส้นทางข้อความไปยังโมเดล แสดงผลลัพธ์  

### 5. การแก้ไขปัญหาข้อผิดพลาดการเชื่อมต่อ

หากคุณเห็น `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## ตัวแปรสภาพแวดล้อม

รองรับตัวแปรสภาพแวดล้อมต่อไปนี้:

| ตัวแปร | ค่าเริ่มต้น | คำอธิบาย |
|--------|-------------|-----------|
| `SHOW_USAGE` | `0` | ตั้งค่าเป็น `1` เพื่อพิมพ์การใช้งานโทเค็น |
| `RETRY_ON_FAIL` | `1` | เปิดใช้งานตรรกะการลองใหม่ |
| `RETRY_BACKOFF` | `1.0` | ความล่าช้าในการลองใหม่ครั้งแรก (วินาที) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | แทนที่ endpoint บริการ |

### ตัวอย่างการใช้งาน

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## การย้ายจากรูปแบบเก่า

หากคุณมีโค้ดที่มีอยู่ซึ่งใช้การเรียก API โดยตรง นี่คือวิธีการย้าย:

### ก่อน (API โดยตรง)
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

### หลัง (SDK)
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

### ประโยชน์ของการย้าย
- ✅ การจัดการบริการอัตโนมัติ
- ✅ การแก้ไขชื่อโมเดล
- ✅ การเลือกการปรับแต่งฮาร์ดแวร์
- ✅ การจัดการข้อผิดพลาดที่ดีขึ้น
- ✅ ความเข้ากันได้กับ OpenAI SDK
- ✅ การรองรับการสตรีม

## อ้างอิง

### เอกสารอย่างเป็นทางการ
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK Source**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Troubleshooting**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### ทรัพยากร Workshop
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Sample Notebook**: `Workshop/notebooks/session06_models_router.ipynb`

### ชุมชน
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## ขั้นตอนถัดไป

1. **ตรวจสอบการเปลี่ยนแปลง**: อ่านไฟล์ที่อัปเดต
2. **ทดสอบโน้ตบุ๊ก**: เรียกใช้ session06_models_router.ipynb
3. **ตรวจสอบ SDK**: ตรวจสอบว่า foundry-local-sdk ติดตั้งแล้ว
4. **ตรวจสอบบริการ**: ยืนยันว่า Foundry Local กำลังทำงานอยู่
5. **สำรวจเอกสาร**: อ่าน session06_README.md ใหม่

## สรุป

การอัปเดตเหล่านี้ทำให้วัสดุ Workshop ปฏิบัติตาม **รูปแบบ SDK Foundry Local อย่างเป็นทางการ** ตามที่ระบุไว้ในที่เก็บ GitHub ตัวอย่างโค้ด เอกสาร และเครื่องมือทั้งหมดตอนนี้สอดคล้องกับแนวทางปฏิบัติที่ดีที่สุดที่ Microsoft แนะนำสำหรับการปรับใช้โมเดล AI ในเครื่อง

การเปลี่ยนแปลงช่วยปรับปรุง:
- ✅ **ความถูกต้อง**: ใช้รูปแบบ SDK อย่างเป็นทางการ
- ✅ **เอกสาร**: คำอธิบายและตัวอย่างที่ครอบคลุม
- ✅ **การจัดการข้อผิดพลาด**: ข้อความและคำแนะนำการแก้ไขปัญหาที่ดีขึ้น
- ✅ **การบำรุงรักษา**: ปฏิบัติตามข้อกำหนดอย่างเป็นทางการ
- ✅ **ประสบการณ์ผู้ใช้**: คำแนะนำที่ชัดเจนและความช่วยเหลือในการดีบัก

---

**อัปเดต:** 8 ตุลาคม 2025  
**เวอร์ชัน SDK:** foundry-local-sdk (ล่าสุด)  
**สาขา Workshop:** Reactor

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้