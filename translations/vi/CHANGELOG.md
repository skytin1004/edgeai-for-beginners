<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T21:47:13+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "vi"
}
-->
# Changelog

Tất cả các thay đổi đáng chú ý đối với EdgeAI for Beginners được ghi lại tại đây. Dự án này sử dụng các mục nhập theo ngày và phong cách Keep a Changelog (Added, Changed, Fixed, Removed, Docs, Moved).

## 2025-09-18

### Added
- Module 08: Microsoft Foundry Local – Bộ công cụ phát triển hoàn chỉnh
  - Sáu phiên: thiết lập, tích hợp Azure AI Foundry, mô hình mã nguồn mở, các bản demo tiên tiến, tác nhân, và mô hình như công cụ
  - Các mẫu có thể chạy được trong `Module08/samples/01`–`06` với hướng dẫn cmd trên Windows
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart với OpenAI/Foundry Local và hỗ trợ Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Điều phối đa tác nhân (`python -m samples.05.agents.coordinator`)
    - `06` Router mô hình như công cụ (`router.py`)
- Hỗ trợ Azure OpenAI trong mẫu SDK của Phiên 2 với cấu hình biến môi trường
- `.vscode/settings.json` trỏ đến `Module08/.venv` để cải thiện độ phân giải phân tích Python
- `.env` với gợi ý `PYTHONPATH` cho nhận thức của VS Code/Pylance

### Changed
- Mô hình mặc định được cập nhật thành `phi-4-mini` trong tài liệu và mẫu của Module 08; loại bỏ các đề cập còn lại về `phi-3.5` trong Module 08
- Cải tiến Router (`Module08/samples/06/router.py`):
  - Khám phá điểm cuối qua `foundry service status` với phân tích regex
  - Kiểm tra sức khỏe `/v1/models` khi khởi động
  - Đăng ký mô hình có thể cấu hình qua môi trường (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Yêu cầu được cập nhật: `Module08/requirements.txt` hiện bao gồm `openai` (cùng với `requests`, `chainlit`)
- Hướng dẫn mẫu Chainlit được làm rõ và thêm phần khắc phục sự cố; giải quyết nhập khẩu qua cài đặt workspace

### Fixed
- Đã giải quyết các vấn đề nhập khẩu:
  - Router không còn phụ thuộc vào module `utils` không tồn tại; các hàm được tích hợp trực tiếp
  - Coordinator sử dụng nhập khẩu tương đối (`from .specialists import ...`) và được gọi qua đường dẫn module
  - Cấu hình VS Code/Pylance để giải quyết `chainlit` và các nhập khẩu gói
- Sửa lỗi chính tả nhỏ trong `STUDY_GUIDE.md` và thêm phạm vi Module 08

### Removed
- Xóa `Module08/infra/obs.py` không sử dụng và loại bỏ thư mục `infra/` trống; các mẫu quan sát được giữ lại như tùy chọn trong tài liệu

### Moved
- Hợp nhất các bản demo của Module 08 vào `Module08/samples` với các thư mục đánh số theo phiên
  - Di chuyển ứng dụng Chainlit đến `samples/04`
  - Di chuyển các tác nhân đến `samples/05` và thêm các tệp `__init__.py` để giải quyết gói

### Docs
- Tài liệu phiên của Module 08 và tất cả README mẫu được bổ sung với các tham chiếu từ Microsoft Learn và các nhà cung cấp đáng tin cậy
- `Module08/README.md` được cập nhật với Tổng quan về Mẫu, cấu hình router, và mẹo xác thực
- Phần Windows Foundry Local trong `Module07/README.md` được xác thực với tài liệu Learn
- `STUDY_GUIDE.md` được cập nhật:
  - Thêm Module 08 vào tổng quan, lịch trình, trình theo dõi tiến độ
  - Thêm phần Tham khảo toàn diện (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historical (summary)
- Kiến trúc khóa học và các module được thiết lập (Modules 01–07)
- Hiện đại hóa nội dung theo từng bước, chuẩn hóa định dạng, và thêm các nghiên cứu điển hình
- Mở rộng phạm vi các khung tối ưu hóa (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Unreleased / Backlog (proposals)
- Các bài kiểm tra khói tùy chọn cho từng mẫu để xác thực tính khả dụng của Foundry Local
- Xem xét các bản dịch để phù hợp với các tham chiếu mô hình (ví dụ: `phi-4-mini`) khi thích hợp
- Thêm cấu hình pyright tối thiểu nếu các nhóm muốn độ nghiêm ngặt trên toàn workspace

---

