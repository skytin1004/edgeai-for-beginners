<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:35:35+00:00",
  "source_file": "AGENTS.md",
  "language_code": "th"
}
-->
# AGENTS.md

## ภาพรวมโครงการ

EdgeAI for Beginners เป็นคลังข้อมูลการศึกษาแบบครบวงจรที่สอนการพัฒนา Edge AI ด้วย Small Language Models (SLMs) หลักสูตรครอบคลุมพื้นฐาน EdgeAI การปรับใช้โมเดล เทคนิคการปรับแต่ง และการนำไปใช้งานในระดับผลิตจริงโดยใช้ Microsoft Foundry Local และเฟรมเวิร์ก AI ต่างๆ

**เทคโนโลยีสำคัญ:**
- Python 3.8+ (ภาษาโปรแกรมหลักสำหรับตัวอย่าง AI/ML)
- .NET C# (ตัวอย่าง AI/ML)
- JavaScript/Node.js กับ Electron (สำหรับแอปพลิเคชันเดสก์ท็อป)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- เฟรมเวิร์ก AI: LangChain, Semantic Kernel, Chainlit
- การปรับแต่งโมเดล: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**ประเภทคลังข้อมูล:** คลังข้อมูลการศึกษา พร้อมโมดูล 8 โมดูล และตัวอย่างแอปพลิเคชัน 10 ตัวอย่างที่ครอบคลุม

**สถาปัตยกรรม:** เส้นทางการเรียนรู้แบบหลายโมดูล พร้อมตัวอย่างการใช้งานจริงที่แสดงรูปแบบการปรับใช้ Edge AI

## โครงสร้างคลังข้อมูล

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## คำสั่งการตั้งค่า

### การตั้งค่าคลังข้อมูล

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### การตั้งค่าตัวอย่าง Python (Module08 และตัวอย่าง Python)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### การตั้งค่าตัวอย่าง Node.js (ตัวอย่าง 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### การตั้งค่า Foundry Local

Foundry Local จำเป็นสำหรับการรันตัวอย่างใน Module08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## เวิร์กโฟลว์การพัฒนา

### การพัฒนาคอนเทนต์

คลังข้อมูลนี้ประกอบด้วย **คอนเทนต์การศึกษาในรูปแบบ Markdown** เป็นหลัก เมื่อมีการเปลี่ยนแปลง:

1. แก้ไขไฟล์ `.md` ในไดเรกทอรีโมดูลที่เหมาะสม
2. ปฏิบัติตามรูปแบบการจัดรูปแบบที่มีอยู่
3. ตรวจสอบให้แน่ใจว่าตัวอย่างโค้ดถูกต้องและผ่านการทดสอบ
4. อัปเดตคอนเทนต์ที่แปลแล้วหากจำเป็น (หรือปล่อยให้ระบบอัตโนมัติจัดการ)

### การพัฒนาแอปพลิเคชันตัวอย่าง

สำหรับตัวอย่าง Python (ตัวอย่าง 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

สำหรับตัวอย่าง Electron (ตัวอย่าง 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### การทดสอบแอปพลิเคชันตัวอย่าง

ตัวอย่าง Python ไม่มีการทดสอบอัตโนมัติ แต่สามารถตรวจสอบได้โดยการรัน:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

ตัวอย่าง Electron มีโครงสร้างการทดสอบ:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## คำแนะนำการทดสอบ

### การตรวจสอบคอนเทนต์

คลังข้อมูลใช้เวิร์กโฟลว์การแปลอัตโนมัติ ไม่จำเป็นต้องทดสอบการแปลด้วยตนเอง

**การตรวจสอบด้วยตนเองสำหรับการเปลี่ยนแปลงคอนเทนต์:**
1. ตรวจสอบการแสดงผล Markdown โดยการดูตัวอย่างไฟล์ `.md`
2. ตรวจสอบให้แน่ใจว่าลิงก์ทั้งหมดชี้ไปยังเป้าหมายที่ถูกต้อง
3. ทดสอบโค้ดตัวอย่างที่รวมอยู่ในเอกสาร
4. ตรวจสอบว่าโหลดภาพได้ถูกต้อง

### การทดสอบแอปพลิเคชันตัวอย่าง

**Module08/samples/08 (แอป Electron) มีการทดสอบที่ครอบคลุม:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**ตัวอย่าง Python ควรทดสอบด้วยตนเอง:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## แนวทางการเขียนโค้ด

### คอนเทนต์ Markdown

- ใช้ลำดับชั้นหัวข้อที่สม่ำเสมอ (# สำหรับชื่อเรื่อง, ## สำหรับส่วนหลัก, ### สำหรับส่วนย่อย)
- รวมบล็อกโค้ดพร้อมตัวระบุภาษา: ```python, ```bash, ```javascript
- ปฏิบัติตามรูปแบบการจัดรูปแบบที่มีอยู่สำหรับตาราง รายการ และการเน้นข้อความ
- ทำให้บรรทัดอ่านง่าย (~80-100 ตัวอักษร แต่ไม่เคร่งครัด)
- ใช้ลิงก์สัมพัทธ์สำหรับการอ้างอิงภายใน

### รูปแบบโค้ด Python

- ปฏิบัติตามมาตรฐาน PEP 8
- ใช้ type hints เมื่อเหมาะสม
- รวม docstrings สำหรับฟังก์ชันและคลาส
- ใช้ชื่อตัวแปรที่มีความหมาย
- ทำให้ฟังก์ชันมีความกระชับและมุ่งเน้น

### รูปแบบโค้ด JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**แนวทางสำคัญ:**
- มีการตั้งค่า ESLint ในตัวอย่าง 08
- ใช้ Prettier สำหรับการจัดรูปแบบโค้ด
- ใช้ไวยากรณ์ ES6+ สมัยใหม่
- ปฏิบัติตามรูปแบบที่มีอยู่ในฐานโค้ด

## แนวทางการส่ง Pull Request

### รูปแบบชื่อเรื่อง
```
[ModuleXX] Brief description of change
```
หรือ
```
[Module08/samples/XX] Description for sample changes
```

### ก่อนการส่ง

**สำหรับการเปลี่ยนแปลงคอนเทนต์:**
- ดูตัวอย่างไฟล์ Markdown ที่แก้ไขทั้งหมด
- ตรวจสอบลิงก์และภาพว่าใช้งานได้
- ตรวจสอบการสะกดคำและข้อผิดพลาดทางไวยากรณ์

**สำหรับการเปลี่ยนแปลงโค้ดตัวอย่าง (Module08/samples/08):**
```bash
npm run lint
npm test
```

**สำหรับการเปลี่ยนแปลงตัวอย่าง Python:**
- ทดสอบว่าตัวอย่างรันได้สำเร็จ
- ตรวจสอบการจัดการข้อผิดพลาด
- ตรวจสอบความเข้ากันได้กับ Foundry Local

### กระบวนการตรวจสอบ

- การเปลี่ยนแปลงคอนเทนต์การศึกษาจะถูกตรวจสอบเพื่อความถูกต้องและความชัดเจน
- ตัวอย่างโค้ดจะถูกทดสอบเพื่อการทำงาน
- การอัปเดตการแปลจะถูกจัดการโดย GitHub Actions

## ระบบการแปล

**สำคัญ:** คลังข้อมูลนี้ใช้การแปลอัตโนมัติผ่าน GitHub Actions

- การแปลอยู่ในไดเรกทอรี `/translations/` (50+ ภาษา)
- อัตโนมัติผ่านเวิร์กโฟลว์ `co-op-translator.yml`
- **ห้ามแก้ไขไฟล์การแปลด้วยตนเอง** - ไฟล์จะถูกเขียนทับ
- แก้ไขเฉพาะไฟล์ต้นฉบับภาษาอังกฤษในไดเรกทอรีรากและโมดูล
- การแปลจะถูกสร้างอัตโนมัติเมื่อมีการ push ไปยัง branch `main`

## การรวม Foundry Local

ตัวอย่างใน Module08 ส่วนใหญ่ต้องการให้ Microsoft Foundry Local ทำงานอยู่:

### การเริ่มต้น Foundry Local
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### การตรวจสอบ Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### ตัวแปรสภาพแวดล้อมสำหรับตัวอย่าง

ตัวอย่างส่วนใหญ่ใช้ตัวแปรสภาพแวดล้อมเหล่านี้:
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## การสร้างและการปรับใช้

### การปรับใช้คอนเทนต์

คลังข้อมูลนี้เป็นเอกสารเป็นหลัก - ไม่จำเป็นต้องมีขั้นตอนการสร้างสำหรับคอนเทนต์

### การสร้างแอปพลิเคชันตัวอย่าง

**แอปพลิเคชัน Electron (Module08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**ตัวอย่าง Python:**
ไม่มีขั้นตอนการสร้าง - ตัวอย่างจะถูกรันโดยตรงด้วย Python interpreter

## ปัญหาทั่วไปและการแก้ไข

### Foundry Local ไม่ทำงาน
**ปัญหา:** ตัวอย่างล้มเหลวด้วยข้อผิดพลาดการเชื่อมต่อ

**วิธีแก้ไข:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### ปัญหาสภาพแวดล้อมเสมือน Python
**ปัญหา:** ข้อผิดพลาดการนำเข้าโมดูล

**วิธีแก้ไข:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### ปัญหาการสร้าง Electron
**ปัญหา:** npm install หรือข้อผิดพลาดการสร้าง

**วิธีแก้ไข:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### ความขัดแย้งในเวิร์กโฟลว์การแปล
**ปัญหา:** PR การแปลขัดแย้งกับการเปลี่ยนแปลงของคุณ

**วิธีแก้ไข:**
- แก้ไขเฉพาะไฟล์ต้นฉบับภาษาอังกฤษ
- ปล่อยให้เวิร์กโฟลว์การแปลอัตโนมัติจัดการการแปล
- หากเกิดความขัดแย้ง ให้ merge `main` เข้าสู่ branch ของคุณหลังจากการแปลถูก merge

## แหล่งข้อมูลเพิ่มเติม

### เส้นทางการเรียนรู้
- **เส้นทางสำหรับผู้เริ่มต้น:** โมดูล 01-02 (7-9 ชั่วโมง)
- **เส้นทางระดับกลาง:** โมดูล 03-04 (9-11 ชั่วโมง)
- **เส้นทางขั้นสูง:** โมดูล 05-07 (12-15 ชั่วโมง)
- **เส้นทางระดับผู้เชี่ยวชาญ:** โมดูล 08 (8-10 ชั่วโมง)

### คอนเทนต์โมดูลสำคัญ
- **Module01:** พื้นฐาน EdgeAI และกรณีศึกษาในโลกจริง
- **Module02:** ตระกูล Small Language Model (SLM) และสถาปัตยกรรม
- **Module03:** กลยุทธ์การปรับใช้ในพื้นที่และคลาวด์
- **Module04:** การปรับแต่งโมเดลด้วยเฟรมเวิร์กหลายตัว
- **Module05:** SLMOps - การดำเนินงานในระดับผลิต
- **Module06:** ตัวแทน AI และการเรียกฟังก์ชัน
- **Module07:** การปรับใช้เฉพาะแพลตฟอร์ม
- **Module08:** เครื่องมือ Foundry Local พร้อมตัวอย่างที่ครอบคลุม 10 ตัวอย่าง

### การพึ่งพาภายนอก
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - รันไทม์โมเดล AI ในพื้นที่
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - เฟรมเวิร์กการปรับแต่ง
- [Microsoft Olive](https://microsoft.github.io/Olive/) - เครื่องมือปรับแต่งโมเดล
- [OpenVINO](https://docs.openvino.ai/) - เครื่องมือปรับแต่งของ Intel

## หมายเหตุเฉพาะโครงการ

### แอปพลิเคชันตัวอย่าง Module08

คลังข้อมูลนี้รวมตัวอย่างแอปพลิเคชันที่ครอบคลุม 10 ตัวอย่าง:

1. **01-REST Chat Quickstart** - การรวม OpenAI SDK เบื้องต้น
2. **02-OpenAI SDK Integration** - ฟีเจอร์ SDK ขั้นสูง
3. **03-Model Discovery & Benchmarking** - เครื่องมือเปรียบเทียบโมเดล
4. **04-Chainlit RAG Application** - การสร้างแบบ Retrieval-augmented
5. **05-Multi-Agent Orchestration** - การประสานงานตัวแทนเบื้องต้น
6. **06-Models-as-Tools Router** - การกำหนดเส้นทางโมเดลอัจฉริยะ
7. **07-Direct API Client** - การรวม API ระดับต่ำ
8. **08-Windows 11 Chat App** - แอปพลิเคชันเดสก์ท็อป Electron แบบเนทีฟ
9. **09-Advanced Multi-Agent System** - การประสานงานตัวแทนที่ซับซ้อน
10. **10-Foundry Tools Framework** - การรวม LangChain/Semantic Kernel

แต่ละตัวอย่างแสดงให้เห็นแง่มุมต่างๆ ของการพัฒนา Edge AI ด้วย Foundry Local

### ข้อพิจารณาด้านประสิทธิภาพ

- SLMs ได้รับการปรับแต่งสำหรับการปรับใช้ในพื้นที่ (RAM 2-16GB)
- การอนุมานในพื้นที่ให้เวลาตอบสนอง 50-500ms
- เทคนิคการลดขนาดช่วยลดขนาดได้ 75% พร้อมการรักษาประสิทธิภาพ 85%
- ความสามารถในการสนทนาแบบเรียลไทม์ด้วยโมเดลในพื้นที่

### ความปลอดภัยและความเป็นส่วนตัว

- การประมวลผลทั้งหมดเกิดขึ้นในพื้นที่ - ไม่มีข้อมูลถูกส่งไปยังคลาวด์
- เหมาะสำหรับแอปพลิเคชันที่ต้องการความเป็นส่วนตัว (การดูแลสุขภาพ การเงิน)
- ตรงตามข้อกำหนดด้านอธิปไตยข้อมูล
- Foundry Local ทำงานทั้งหมดบนฮาร์ดแวร์ในพื้นที่

---

**นี่คือคลังข้อมูลการศึกษาที่มุ่งเน้นการสอนการพัฒนา Edge AI รูปแบบการมีส่วนร่วมหลักคือการปรับปรุงคอนเทนต์การศึกษาและการเพิ่ม/ปรับปรุงตัวอย่างแอปพลิเคชันที่แสดงแนวคิด Edge AI**

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่เป็นมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้