<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-22T19:23:04+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "th"
}
-->
# ตัวอย่างเซสชัน 5: การจัดการหลายตัวแทน

ตัวอย่างนี้แสดงรูปแบบผู้ประสานงาน + ผู้เชี่ยวชาญ โดยใช้ปลายทางที่เข้ากันได้กับ OpenAI ของ Foundry Local

## การรัน (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## การตรวจสอบ
```cmd
curl http://localhost:8000/v1/models
```

## การแก้ไขปัญหา
- หาก VS Code แสดง `import specialists` ว่าไม่สามารถแก้ไขได้ใน `coordinator.py` ให้ตรวจสอบว่าคุณรันเป็นโมดูลและตัวแปลภาษาเชื่อมโยงไปยัง `Module08/.venv`:
	- รัน: `python -m samples.05.agents.coordinator`
	- เลือกตัวแปลภาษา: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## อ้างอิง
- Foundry Local (เรียนรู้): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- ภาพรวม Azure AI Agents: https://learn.microsoft.com/azure/ai-services/agents/overview
- ตัวอย่างการเรียกฟังก์ชัน (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

