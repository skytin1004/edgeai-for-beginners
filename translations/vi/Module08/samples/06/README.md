<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T21:53:52+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "vi"
}
-->
# Phiên 6 Mẫu: Mô hình như Công cụ

Mẫu này triển khai một bộ định tuyến tối giản + đăng ký công cụ, chọn mô hình dựa trên lời nhắc của người dùng và gọi điểm cuối tương thích OpenAI của Foundry Local.

## Tệp
- `router.py`: đăng ký đơn giản và định tuyến theo phương pháp heuristic; khám phá điểm cuối + kiểm tra sức khỏe.

## Chạy (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Ghi chú
- Bộ định tuyến sử dụng phương pháp heuristic từ khóa đơn giản để chọn giữa các công cụ `general`, `reasoning`, và `code`, đồng thời in `/v1/models` khi khởi động.
- Cấu hình thông qua các biến môi trường:
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

## Tham khảo
- Foundry Local (Học): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Tích hợp với SDK suy luận: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

