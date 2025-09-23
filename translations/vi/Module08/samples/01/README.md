<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T21:53:32+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "vi"
}
-->
# Phiên 1 Mẫu: Trò chuyện nhanh qua REST

Thực hiện một yêu cầu trò chuyện tối giản đến Foundry Local bằng Python `requests`.

## Yêu cầu trước
- Dịch vụ Foundry Local đang chạy một mô hình (ví dụ: `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Chạy (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Tham khảo
- Foundry Local (Learn): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Tổng quan API tương thích OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

