<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T19:22:53+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "th"
}
-->
# ตัวอย่างเซสชัน 1: แชทอย่างรวดเร็วผ่าน REST

เรียกใช้คำขอแชทแบบง่ายไปยัง Foundry Local โดยใช้ Python `requests`

## สิ่งที่ต้องเตรียม
- บริการ Foundry Local ที่กำลังรันโมเดล (เช่น `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## การรัน (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## อ้างอิง
- Foundry Local (Learn): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- ภาพรวม API ที่เข้ากันได้กับ OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

