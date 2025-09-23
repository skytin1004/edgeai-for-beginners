<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T19:23:28+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "th"
}
-->
# ตัวอย่าง Session 4: Chainlit RAG Demo

รันแอป Chainlit แบบมินิมอลกับ Foundry Local

## สิ่งที่ต้องเตรียม
- Windows 11, Python 3.10+
- ติดตั้ง Foundry Local และมีโมเดลพร้อมใช้งาน (เช่น `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## การรัน (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## การตรวจสอบ
```cmd
curl http://localhost:8000/v1/models
```

## การแก้ไขปัญหา
- หาก VS Code แสดงข้อความ "chainlit could not be resolved":
	- เลือก interpreter `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- ตรวจสอบว่าติดตั้ง dependencies แล้ว: `pip install -r Module08\requirements.txt`

## แหล่งข้อมูลอ้างอิง
- วิธีเปิด WebUI (แอปแชทกับ Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (เรียนรู้เพิ่มเติม): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

