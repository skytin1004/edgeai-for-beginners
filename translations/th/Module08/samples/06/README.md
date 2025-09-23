<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T19:23:16+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "th"
}
-->
# ตัวอย่าง Session 6: ใช้โมเดลเป็นเครื่องมือ

ตัวอย่างนี้แสดงการใช้งาน router + tool registry แบบง่าย ๆ ที่เลือกโมเดลตามคำสั่งของผู้ใช้และเรียกใช้งาน Foundry Local ผ่าน endpoint ที่เข้ากันได้กับ OpenAI

## ไฟล์
- `router.py`: registry และ heuristic routing แบบง่าย ๆ; ค้นหา endpoint + ตรวจสอบสถานะการทำงาน

## การรัน (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## หมายเหตุ
- router ใช้ heuristic แบบคำสำคัญง่าย ๆ เพื่อเลือกเครื่องมือระหว่าง `general`, `reasoning`, และ `code` และพิมพ์ `/v1/models` เมื่อเริ่มต้น
- ตั้งค่าผ่าน environment variables:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-distill-qwen-7b"},"code":{"model":"qwen2.5-7b-instruct"}}
```

## อ้างอิง
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- การผสานรวมกับ inference SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

