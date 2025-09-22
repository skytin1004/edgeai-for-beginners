<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-22T21:54:49+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "vi"
}
-->
# Foundry Local trên Windows (Đã xác thực)

Hướng dẫn này giúp bạn cài đặt, chạy và tích hợp Microsoft Foundry Local trên Windows. Tất cả các bước và lệnh đều đã được xác thực dựa trên tài liệu Microsoft Learn.

- Bắt đầu: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Kiến trúc: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Tham khảo CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Tích hợp SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Biên dịch mô hình HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Local vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Cài đặt / Nâng cấp trên Windows

- Cài đặt:
```cmd
winget install Microsoft.FoundryLocal
```
- Nâng cấp:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Kiểm tra phiên bản:
```cmd
foundry --version
```

## 2) Cơ bản về CLI (Ba danh mục)

- Mô hình:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Dịch vụ:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Bộ nhớ đệm:
```cmd
foundry cache --help
foundry cache list
```

Ghi chú:
- Dịch vụ cung cấp một API REST tương thích với OpenAI. Cổng endpoint được cấp phát động; sử dụng `foundry service status` để tìm ra cổng này.
- Sử dụng SDKs để tiện lợi hơn; chúng tự động xử lý việc tìm kiếm endpoint khi được hỗ trợ.

## 3) Tìm endpoint cục bộ (Cổng động)

Foundry Local cấp phát một cổng động mỗi lần dịch vụ khởi động:
```cmd
foundry service status
```
Sử dụng `http://localhost:<PORT>` được báo cáo làm `base_url` của bạn với các đường dẫn tương thích OpenAI (ví dụ, `/v1/chat/completions`).

## 4) Kiểm tra nhanh qua OpenAI Python SDK

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
Tham khảo:
- Tích hợp SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Mang theo mô hình của bạn (Biên dịch với Olive)

Nếu bạn cần một mô hình không có trong danh mục, hãy biên dịch nó sang ONNX cho Foundry Local bằng Olive.

Quy trình tổng quan (xem tài liệu để biết các bước):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Tài liệu:
- Biên dịch BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Xử lý sự cố

- Kiểm tra trạng thái dịch vụ và nhật ký:
```cmd
foundry service status
foundry service diag
```
- Xóa hoặc di chuyển bộ nhớ đệm:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Cập nhật lên bản xem trước mới nhất:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Trải nghiệm phát triển liên quan trên Windows

- Lựa chọn AI cục bộ vs đám mây trên Windows, bao gồm Foundry Local và Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- Bộ công cụ AI của VS Code với Foundry Local (sử dụng `foundry service status` để lấy URL endpoint chat):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

