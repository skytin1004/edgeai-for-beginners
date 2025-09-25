<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-25T00:03:01+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "vi"
}
-->
# Changelog

Tất cả các thay đổi đáng chú ý đối với EdgeAI for Beginners được ghi lại tại đây. Dự án này sử dụng các mục nhập theo ngày và phong cách Keep a Changelog (Added, Changed, Fixed, Removed, Docs, Moved).

## 2025-09-23

### Changed - Hiện đại hóa lớn Module 08
- **Căn chỉnh toàn diện với các mẫu kho lưu trữ Microsoft Foundry-Local**
  - Cập nhật tất cả các ví dụ mã để sử dụng `FoundryLocalManager` hiện đại và tích hợp OpenAI SDK
  - Thay thế các lệnh gọi `requests` thủ công đã lỗi thời bằng cách sử dụng SDK đúng cách
  - Căn chỉnh các mẫu triển khai với tài liệu và mẫu chính thức của Microsoft

- **Hiện đại hóa 05.AIPoweredAgents.md**:
  - Cập nhật điều phối đa tác nhân để sử dụng các mẫu SDK hiện đại
  - Nâng cao triển khai điều phối viên với các tính năng tiên tiến (vòng phản hồi, giám sát hiệu suất)
  - Thêm xử lý lỗi toàn diện và kiểm tra sức khỏe dịch vụ
  - Tích hợp các tham chiếu phù hợp đến các mẫu cục bộ (`samples/05/multi_agent_orchestration.ipynb`)
  - Cập nhật các ví dụ gọi hàm để sử dụng tham số `tools` hiện đại thay vì `functions` đã lỗi thời
  - Thêm các mẫu sẵn sàng sản xuất với giám sát và theo dõi thống kê

- **Viết lại hoàn toàn 06.ModelsAsTools.md**:
  - Thay thế đăng ký công cụ cơ bản bằng triển khai bộ định tuyến mô hình thông minh
  - Thêm lựa chọn mô hình dựa trên từ khóa cho các loại nhiệm vụ khác nhau (tổng quát, lý luận, mã, sáng tạo)
  - Tích hợp cấu hình dựa trên môi trường với phân bổ mô hình linh hoạt
  - Nâng cao với giám sát sức khỏe dịch vụ toàn diện và xử lý lỗi
  - Thêm các mẫu triển khai sản xuất với giám sát yêu cầu và theo dõi hiệu suất
  - Căn chỉnh với triển khai cục bộ trong `samples/06/router.py` và `samples/06/model_router.ipynb`

- **Cải tiến cấu trúc tài liệu**:
  - Thêm các phần tổng quan làm nổi bật sự hiện đại hóa và căn chỉnh SDK
  - Nâng cao với biểu tượng cảm xúc và định dạng tốt hơn để cải thiện khả năng đọc
  - Thêm các tham chiếu phù hợp đến các tệp mẫu cục bộ trong toàn bộ tài liệu
  - Bao gồm hướng dẫn triển khai sẵn sàng sản xuất và các thực tiễn tốt nhất

### Added
- Các phần tổng quan toàn diện trong các tệp Module 08 làm nổi bật tích hợp SDK hiện đại
- Điểm nổi bật kiến trúc giới thiệu các tính năng tiên tiến (hệ thống đa tác nhân, định tuyến thông minh)
- Các tham chiếu trực tiếp đến các triển khai mẫu cục bộ để trải nghiệm thực hành
- Hướng dẫn triển khai sản xuất với các mẫu giám sát và xử lý lỗi
- Các ví dụ Jupyter notebook tương tác với các tính năng tiên tiến và điểm chuẩn

### Fixed
- Các điểm không khớp giữa tài liệu và các triển khai mẫu thực tế
- Các mẫu sử dụng SDK lỗi thời trong toàn bộ Module 08
- Các tham chiếu bị thiếu đến thư viện mẫu cục bộ toàn diện
- Các cách tiếp cận triển khai không nhất quán giữa các phần khác nhau

---

## 2025-09-18

### Added
- Module 08: Microsoft Foundry Local – Bộ công cụ dành cho nhà phát triển hoàn chỉnh
  - Sáu phiên: thiết lập, tích hợp Azure AI Foundry, mô hình mã nguồn mở, các bản demo tiên tiến, tác nhân và mô hình như công cụ
  - Các mẫu có thể chạy dưới `Module08/samples/01`–`06` với hướng dẫn cmd Windows
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart với OpenAI/Foundry Local và hỗ trợ Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Điều phối đa tác nhân (`python -m samples.05.agents.coordinator`)
    - `06` Bộ định tuyến Models-as-Tools (`router.py`)
- Hỗ trợ Azure OpenAI trong mẫu SDK Phiên 2 với cấu hình biến môi trường
- `.vscode/settings.json` trỏ đến `Module08/.venv` và cải thiện độ phân giải phân tích Python
- `.env` với gợi ý `PYTHONPATH` cho nhận thức VS Code/Pylance

### Changed
- Mô hình mặc định được cập nhật thành `phi-4-mini` trong toàn bộ tài liệu và mẫu Module 08; loại bỏ các đề cập còn lại đến `phi-3.5` trong Module 08
- Cải tiến bộ định tuyến (`Module08/samples/06/router.py`):
  - Khám phá điểm cuối qua `foundry service status` với phân tích regex
  - Kiểm tra sức khỏe `/v1/models` khi khởi động
  - Đăng ký mô hình có thể cấu hình qua môi trường (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Yêu cầu được cập nhật: `Module08/requirements.txt` hiện bao gồm `openai` (cùng với `requests`, `chainlit`)
- Hướng dẫn mẫu Chainlit được làm rõ và thêm xử lý sự cố; giải quyết nhập khẩu qua cài đặt không gian làm việc

### Fixed
- Giải quyết các vấn đề nhập khẩu:
  - Bộ định tuyến không còn phụ thuộc vào mô-đun `utils` không tồn tại; các hàm được nội tuyến
  - Điều phối viên sử dụng nhập khẩu tương đối (`from .specialists import ...`) và được gọi qua đường dẫn mô-đun
  - Cấu hình VS Code/Pylance để giải quyết `chainlit` và các nhập khẩu gói
- Sửa lỗi nhỏ trong `STUDY_GUIDE.md` và thêm phạm vi Module 08

### Removed
- Xóa `Module08/infra/obs.py` không sử dụng và loại bỏ thư mục `infra/` trống; các mẫu quan sát được giữ lại như tùy chọn trong tài liệu

### Moved
- Hợp nhất các bản demo Module 08 dưới `Module08/samples` với các thư mục đánh số phiên
  - Di chuyển ứng dụng Chainlit đến `samples/04`
  - Di chuyển các tác nhân đến `samples/05` và thêm các tệp `__init__.py` để giải quyết gói

### Docs
- Tài liệu phiên Module 08 và tất cả README mẫu được làm phong phú với các tham chiếu Microsoft Learn và nhà cung cấp đáng tin cậy
- `Module08/README.md` được cập nhật với Tổng quan về Mẫu, cấu hình bộ định tuyến và mẹo xác thực
- `Module07/README.md` phần Windows Foundry Local được xác thực với tài liệu Learn
- `STUDY_GUIDE.md` được cập nhật:
  - Thêm Module 08 vào tổng quan, lịch trình, trình theo dõi tiến độ
  - Thêm phần Tham khảo toàn diện (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historical (summary)
- Kiến trúc khóa học và các module được thiết lập (Modules 01–07)
- Hiện đại hóa nội dung lặp lại, chuẩn hóa định dạng và thêm các nghiên cứu trường hợp
- Mở rộng phạm vi khung tối ưu hóa (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Unreleased / Backlog (proposals)
- Các bài kiểm tra khói tùy chọn cho từng mẫu để xác thực tính khả dụng của Foundry Local
- Xem xét các bản dịch để căn chỉnh các tham chiếu mô hình (ví dụ: `phi-4-mini`) khi phù hợp
- Thêm cấu hình pyright tối thiểu nếu các nhóm thích sự nghiêm ngặt trên toàn không gian làm việc

---

