<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T19:14:27+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "th"
}
-->
# บันทึกการเปลี่ยนแปลง

การเปลี่ยนแปลงที่สำคัญทั้งหมดใน EdgeAI for Beginners จะถูกบันทึกไว้ที่นี่ โครงการนี้ใช้การบันทึกตามวันที่และรูปแบบ Keep a Changelog (Added, Changed, Fixed, Removed, Docs, Moved)

## 2025-09-18

### เพิ่ม
- โมดูล 08: Microsoft Foundry Local – ชุดเครื่องมือสำหรับนักพัฒนาแบบครบวงจร
  - หกเซสชัน: การตั้งค่า, การรวม Azure AI Foundry, โมเดลโอเพ่นซอร์ส, เดโมล้ำสมัย, เอเจนต์, และโมเดลในรูปแบบเครื่องมือ
  - ตัวอย่างที่สามารถรันได้ใน `Module08/samples/01`–`06` พร้อมคำสั่ง Windows cmd
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart พร้อมการสนับสนุน OpenAI/Foundry Local และ Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` การจัดการหลายเอเจนต์ (`python -m samples.05.agents.coordinator`)
    - `06` Router โมเดลในรูปแบบเครื่องมือ (`router.py`)
- การสนับสนุน Azure OpenAI ในตัวอย่าง SDK เซสชัน 2 พร้อมการตั้งค่าตัวแปรสภาพแวดล้อม
- `.vscode/settings.json` ชี้ไปที่ `Module08/.venv` เพื่อปรับปรุงการวิเคราะห์ Python
- `.env` พร้อมคำแนะนำ `PYTHONPATH` สำหรับการรับรู้ใน VS Code/Pylance

### เปลี่ยนแปลง
- โมเดลเริ่มต้นอัปเดตเป็น `phi-4-mini` ในเอกสารและตัวอย่างของ Module 08; ลบการกล่าวถึง `phi-3.5` ที่เหลือใน Module 08
- การปรับปรุง Router (`Module08/samples/06/router.py`):
  - การค้นหา Endpoint ผ่าน `foundry service status` พร้อมการวิเคราะห์ regex
  - การตรวจสอบสุขภาพ `/v1/models` เมื่อเริ่มต้นระบบ
  - การตั้งค่าระเบียนโมเดลผ่านตัวแปรสภาพแวดล้อม (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- อัปเดตข้อกำหนด: `Module08/requirements.txt` เพิ่ม `openai` (ควบคู่กับ `requests`, `chainlit`)
- ชี้แจงคำแนะนำตัวอย่าง Chainlit และเพิ่มการแก้ไขปัญหา; การแก้ไขการนำเข้าผ่านการตั้งค่าพื้นที่ทำงาน

### แก้ไข
- แก้ไขปัญหาการนำเข้า:
  - Router ไม่พึ่งพาโมดูล `utils` ที่ไม่มีอยู่จริงอีกต่อไป; ฟังก์ชันถูกนำมาใช้ในโค้ดโดยตรง
  - Coordinator ใช้การนำเข้าแบบสัมพัทธ์ (`from .specialists import ...`) และถูกเรียกใช้ผ่านเส้นทางโมดูล
  - การตั้งค่า VS Code/Pylance เพื่อแก้ไขการนำเข้า `chainlit` และแพ็กเกจ
- แก้ไขข้อผิดพลาดเล็กน้อยใน `STUDY_GUIDE.md` และเพิ่มการครอบคลุม Module 08

### ลบ
- ลบ `Module08/infra/obs.py` ที่ไม่ได้ใช้งานและลบไดเรกทอรี `infra/` ที่ว่างเปล่า; รูปแบบการสังเกตการณ์ยังคงอยู่ในเอกสารเป็นตัวเลือก

### ย้าย
- รวมเดโม Module 08 ไว้ใน `Module08/samples` พร้อมโฟลเดอร์ที่ระบุหมายเลขเซสชัน
  - ย้ายแอป Chainlit ไปที่ `samples/04`
  - ย้ายเอเจนต์ไปที่ `samples/05` และเพิ่มไฟล์ `__init__.py` เพื่อแก้ไขแพ็กเกจ

### เอกสาร
- เอกสารเซสชัน Module 08 และ README ตัวอย่างทั้งหมดเพิ่มข้อมูลอ้างอิงจาก Microsoft Learn และผู้ให้บริการที่เชื่อถือได้
- อัปเดต `Module08/README.md` พร้อมภาพรวมตัวอย่าง, การตั้งค่า router, และเคล็ดลับการตรวจสอบ
- ตรวจสอบส่วน Windows Foundry Local ใน `Module07/README.md` กับเอกสาร Learn
- อัปเดต `STUDY_GUIDE.md`:
  - เพิ่ม Module 08 ในภาพรวม, ตารางเวลา, ตัวติดตามความคืบหน้า
  - เพิ่มส่วนอ้างอิงที่ครอบคลุม (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## ประวัติ (สรุป)
- สร้างสถาปัตยกรรมหลักสูตรและโมดูล (Modules 01–07)
- การปรับปรุงเนื้อหาอย่างต่อเนื่อง, การปรับรูปแบบให้เป็นมาตรฐาน, และเพิ่มกรณีศึกษา
- ขยายการครอบคลุมกรอบการปรับแต่ง (Llama.cpp, Olive, OpenVINO, Apple MLX)

## ยังไม่ได้เผยแพร่ / งานที่รอดำเนินการ (ข้อเสนอ)
- การทดสอบแบบ smoke test ต่อแต่ละตัวอย่างเพื่อยืนยันความพร้อมใช้งานของ Foundry Local
- ทบทวนการแปลเพื่อให้สอดคล้องกับการอ้างอิงโมเดล (เช่น `phi-4-mini`) ตามความเหมาะสม
- เพิ่มการตั้งค่า pyright ขั้นต่ำหากทีมต้องการความเข้มงวดในระดับพื้นที่ทำงาน

---

