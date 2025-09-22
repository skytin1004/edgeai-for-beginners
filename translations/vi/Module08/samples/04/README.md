<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T21:54:02+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "vi"
}
-->
# Phiên 4 Mẫu: Demo Chainlit RAG

Chạy ứng dụng Chainlit tối giản với Foundry Local.

## Yêu cầu trước
- Windows 11, Python 3.10+
- Đã cài đặt Foundry Local và có sẵn một mô hình (ví dụ: `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Chạy (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Xác minh
```cmd
curl http://localhost:8000/v1/models
```

## Xử lý sự cố
- Nếu VS Code hiển thị "chainlit could not be resolved":
	- Chọn trình thông dịch `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Đảm bảo các phụ thuộc đã được cài đặt: `pip install -r Module08\requirements.txt`

## Tham khảo
- Hướng dẫn mở WebUI (ứng dụng chat với Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Học): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

