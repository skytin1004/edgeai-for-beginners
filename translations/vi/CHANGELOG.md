<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T16:33:16+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "vi"
}
-->
# Nhật ký thay đổi

Tất cả các thay đổi đáng chú ý đối với EdgeAI for Beginners được ghi lại tại đây. Dự án này sử dụng các mục nhập theo ngày và phong cách Keep a Changelog (Thêm mới, Thay đổi, Sửa lỗi, Xóa bỏ, Tài liệu, Di chuyển).

## 2025-10-08

### Thêm mới - Cập nhật toàn diện Workshop
- **Viết lại hoàn toàn README.md của Workshop**:
  - Thêm phần giới thiệu toàn diện giải thích giá trị của Edge AI (bảo mật, hiệu suất, chi phí)
  - Tạo 6 mục tiêu học tập cốt lõi với các năng lực chi tiết
  - Thêm bảng kết quả học tập với các sản phẩm và ma trận năng lực
  - Bao gồm phần kỹ năng sẵn sàng cho nghề nghiệp để tăng tính liên quan trong ngành
  - Thêm hướng dẫn bắt đầu nhanh với các yêu cầu và thiết lập 3 bước
  - Tạo bảng tài nguyên cho các mẫu Python (8 tệp với thời gian chạy)
  - Thêm bảng Jupyter notebooks (8 notebooks với đánh giá độ khó)
  - Tạo bảng tài liệu (7 tài liệu chính với hướng dẫn "Sử dụng khi nào")
  - Thêm các khuyến nghị lộ trình học tập cho các cấp độ kỹ năng khác nhau

- **Hạ tầng kiểm tra và xác thực Workshop**:
  - Tạo `scripts/validate_samples.py` - Công cụ xác thực toàn diện cho cú pháp, nhập khẩu và các thực hành tốt nhất
  - Tạo `scripts/test_samples.py` - Công cụ kiểm tra nhanh cho tất cả các mẫu Python
  - Thêm tài liệu xác thực vào `scripts/README.md`

- **Tài liệu toàn diện**:
  - Tạo `SAMPLES_UPDATE_SUMMARY.md` - Hướng dẫn chi tiết hơn 400 dòng về tất cả các cải tiến
  - Tạo `UPDATE_COMPLETE.md` - Tóm tắt điều hành về việc hoàn thành cập nhật
  - Tạo `QUICK_REFERENCE.md` - Thẻ tham khảo nhanh cho Workshop

### Thay đổi - Hiện đại hóa mẫu Python của Workshop
- **Cập nhật tất cả 8 mẫu Python với các thực hành tốt nhất**:
  - Nâng cao xử lý lỗi với các khối try-except xung quanh tất cả các thao tác I/O
  - Thêm gợi ý kiểu và docstring toàn diện
  - Triển khai mẫu ghi nhật ký nhất quán [INFO]/[ERROR]/[RESULT]
  - Bảo vệ các nhập khẩu tùy chọn với gợi ý cài đặt
  - Cải thiện phản hồi người dùng trong tất cả các mẫu

- **session01/chat_bootstrap.py**:
  - Nâng cao khởi tạo client với các thông báo lỗi toàn diện
  - Cải thiện xử lý lỗi streaming với xác thực từng phần
  - Thêm xử lý ngoại lệ tốt hơn khi dịch vụ không khả dụng

- **session02/rag_pipeline.py**:
  - Thêm bảo vệ nhập khẩu cho sentence-transformers với gợi ý cài đặt
  - Nâng cao xử lý lỗi cho các thao tác nhúng và tạo
  - Cải thiện định dạng đầu ra với kết quả có cấu trúc

- **session02/rag_eval_ragas.py**:
  - Bảo vệ các nhập khẩu tùy chọn (ragas, datasets) với thông báo lỗi thân thiện
  - Thêm xử lý lỗi cho các chỉ số đánh giá
  - Nâng cao định dạng đầu ra cho kết quả đánh giá

- **session03/benchmark_oss_models.py**:
  - Triển khai giảm thiểu lỗi một cách duyên dáng (tiếp tục khi mô hình gặp lỗi)
  - Thêm báo cáo tiến độ chi tiết và xử lý lỗi từng mô hình
  - Nâng cao tính toán thống kê với khả năng phục hồi lỗi toàn diện

- **session04/model_compare.py**:
  - Thêm gợi ý kiểu (kiểu trả về Tuple)
  - Nâng cao định dạng đầu ra với kết quả JSON có cấu trúc
  - Triển khai xử lý lỗi từng mô hình với khả năng phục hồi

- **session05/agents_orchestrator.py**:
  - Nâng cao Agent.act() với docstring toàn diện
  - Thêm xử lý lỗi pipeline với ghi nhật ký từng giai đoạn
  - Cải thiện quản lý bộ nhớ và theo dõi trạng thái

- **session06/models_router.py**:
  - Nâng cao tài liệu chức năng cho tất cả các thành phần định tuyến
  - Thêm ghi nhật ký chi tiết trong hàm route()
  - Cải thiện đầu ra kiểm tra với kết quả có cấu trúc

- **session06/models_pipeline.py**:
  - Thêm xử lý lỗi vào hàm trợ giúp chat()
  - Nâng cao pipeline() với ghi nhật ký từng giai đoạn và báo cáo tiến độ
  - Cải thiện main() với khả năng phục hồi lỗi toàn diện

### Tài liệu - Nâng cao tài liệu Workshop
- Cập nhật README.md chính với phần Workshop nhấn mạnh lộ trình học tập thực hành
- Nâng cao STUDY_GUIDE.md với phần Workshop toàn diện bao gồm:
  - Mục tiêu học tập và các lĩnh vực tập trung học tập
  - Câu hỏi tự đánh giá
  - Bài tập thực hành với ước tính thời gian
  - Phân bổ thời gian cho học tập tập trung và bán thời gian
  - Thêm Workshop vào mẫu theo dõi tiến độ
- Cập nhật hướng dẫn phân bổ thời gian từ 20 giờ lên 30 giờ (bao gồm Workshop)
- Thêm mô tả mẫu Workshop và kết quả học tập vào README

### Sửa lỗi
- Giải quyết các mẫu xử lý lỗi không nhất quán trong các mẫu Workshop
- Sửa lỗi nhập khẩu phụ thuộc tùy chọn với các bảo vệ thích hợp
- Sửa các gợi ý kiểu bị thiếu trong các hàm quan trọng
- Khắc phục phản hồi người dùng không đủ trong các tình huống lỗi
- Sửa các vấn đề xác thực với hạ tầng kiểm tra toàn diện

---

## 2025-09-23

### Thay đổi - Hiện đại hóa Module 08 lớn
- **Căn chỉnh toàn diện với các mẫu kho lưu trữ Microsoft Foundry-Local**:
  - Cập nhật tất cả các ví dụ mã để sử dụng `FoundryLocalManager` hiện đại và tích hợp SDK OpenAI
  - Thay thế các cuộc gọi `requests` thủ công đã lỗi thời bằng cách sử dụng SDK thích hợp
  - Căn chỉnh các mẫu triển khai với tài liệu và mẫu chính thức của Microsoft

- **Hiện đại hóa 05.AIPoweredAgents.md**:
  - Cập nhật điều phối đa tác nhân để sử dụng các mẫu SDK hiện đại
  - Nâng cao triển khai điều phối viên với các tính năng tiên tiến (vòng phản hồi, giám sát hiệu suất)
  - Thêm xử lý lỗi toàn diện và kiểm tra sức khỏe dịch vụ
  - Tích hợp các tham chiếu thích hợp đến các mẫu cục bộ (`samples/05/multi_agent_orchestration.ipynb`)
  - Cập nhật các ví dụ gọi hàm để sử dụng tham số `tools` hiện đại thay vì `functions` đã lỗi thời
  - Thêm các mẫu sẵn sàng sản xuất với giám sát và theo dõi thống kê

- **Viết lại hoàn toàn 06.ModelsAsTools.md**:
  - Thay thế đăng ký công cụ cơ bản bằng triển khai bộ định tuyến mô hình thông minh
  - Thêm lựa chọn mô hình dựa trên từ khóa cho các loại nhiệm vụ khác nhau (chung, lý luận, mã, sáng tạo)
  - Tích hợp cấu hình dựa trên môi trường với phân công mô hình linh hoạt
  - Nâng cao với giám sát sức khỏe dịch vụ toàn diện và xử lý lỗi
  - Thêm các mẫu triển khai sản xuất với giám sát yêu cầu và theo dõi hiệu suất
  - Căn chỉnh với triển khai cục bộ trong `samples/06/router.py` và `samples/06/model_router.ipynb`

- **Cải tiến cấu trúc tài liệu**:
  - Thêm các phần tổng quan nhấn mạnh hiện đại hóa và căn chỉnh SDK
  - Nâng cao với biểu tượng cảm xúc và định dạng tốt hơn để cải thiện khả năng đọc
  - Thêm các tham chiếu thích hợp đến các tệp mẫu cục bộ trong toàn bộ tài liệu
  - Bao gồm hướng dẫn triển khai sẵn sàng sản xuất và các thực hành tốt nhất

### Thêm mới
- Các phần tổng quan toàn diện trong các tệp Module 08 nhấn mạnh tích hợp SDK hiện đại
- Điểm nổi bật về kiến trúc giới thiệu các tính năng tiên tiến (hệ thống đa tác nhân, định tuyến thông minh)
- Các tham chiếu trực tiếp đến các triển khai mẫu cục bộ để trải nghiệm thực hành
- Hướng dẫn triển khai sản xuất với các mẫu giám sát và xử lý lỗi
- Các ví dụ Jupyter notebook tương tác với các tính năng tiên tiến và đánh giá hiệu suất

### Sửa lỗi
- Các điểm không khớp giữa tài liệu và các triển khai mẫu thực tế
- Các mẫu sử dụng SDK lỗi thời trong toàn bộ Module 08
- Các tham chiếu bị thiếu đến thư viện mẫu cục bộ toàn diện
- Các cách tiếp cận triển khai không nhất quán giữa các phần khác nhau

---

## 2025-09-18

### Thêm mới
- Module 08: Microsoft Foundry Local – Bộ công cụ phát triển hoàn chỉnh
  - Sáu buổi: thiết lập, tích hợp Azure AI Foundry, mô hình mã nguồn mở, demo tiên tiến, tác nhân, và mô hình như công cụ
  - Các mẫu có thể chạy dưới `Module08/samples/01`–`06` với hướng dẫn cmd Windows
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart với OpenAI/Foundry Local và hỗ trợ Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Điều phối đa tác nhân (`python -m samples.05.agents.coordinator`)
    - `06` Bộ định tuyến Models-as-Tools (`router.py`)
- Hỗ trợ Azure OpenAI trong mẫu SDK Session 2 với cấu hình biến môi trường
- `.vscode/settings.json` để trỏ đến `Module08/.venv` và cải thiện độ phân giải phân tích Python
- `.env` với gợi ý `PYTHONPATH` cho nhận thức của VS Code/Pylance

### Thay đổi
- Mô hình mặc định được cập nhật thành `phi-4-mini` trong toàn bộ tài liệu và mẫu Module 08; xóa các đề cập còn lại đến `phi-3.5` trong Module 08
- Cải tiến bộ định tuyến (`Module08/samples/06/router.py`):
  - Khám phá điểm cuối qua `foundry service status` với phân tích regex
  - Kiểm tra sức khỏe `/v1/models` khi khởi động
  - Đăng ký mô hình có thể cấu hình qua môi trường (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Yêu cầu được cập nhật: `Module08/requirements.txt` hiện bao gồm `openai` (cùng với `requests`, `chainlit`)
- Hướng dẫn mẫu Chainlit được làm rõ và thêm khắc phục sự cố; giải quyết nhập khẩu qua cài đặt workspace

### Sửa lỗi
- Giải quyết các vấn đề nhập khẩu:
  - Bộ định tuyến không còn phụ thuộc vào mô-đun `utils` không tồn tại; các hàm được nội tuyến
  - Điều phối viên sử dụng nhập khẩu tương đối (`from .specialists import ...`) và được gọi qua đường dẫn mô-đun
  - Cấu hình VS Code/Pylance để giải quyết `chainlit` và các nhập khẩu gói
- Sửa lỗi chính tả nhỏ trong `STUDY_GUIDE.md` và thêm phạm vi Module 08

### Xóa bỏ
- Xóa `Module08/infra/obs.py` không sử dụng và xóa thư mục `infra/` trống; các mẫu quan sát được giữ lại như tùy chọn trong tài liệu

### Di chuyển
- Hợp nhất các demo Module 08 dưới `Module08/samples` với các thư mục đánh số theo buổi
  - Di chuyển ứng dụng Chainlit đến `samples/04`
  - Di chuyển các tác nhân đến `samples/05` và thêm các tệp `__init__.py` để giải quyết gói

### Tài liệu
- Tài liệu buổi Module 08 và tất cả README mẫu được làm phong phú với các tham chiếu Microsoft Learn và nhà cung cấp đáng tin cậy
- `Module08/README.md` được cập nhật với Tổng quan về Mẫu, cấu hình bộ định tuyến, và mẹo xác thực
- `Module07/README.md` phần Windows Foundry Local được xác thực với tài liệu Learn
- `STUDY_GUIDE.md` được cập nhật:
  - Thêm Module 08 vào tổng quan, lịch trình, trình theo dõi tiến độ
  - Thêm phần Tham khảo toàn diện (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Lịch sử (tóm tắt)
- Kiến trúc khóa học và các module được thiết lập (Modules 01–07)
- Hiện đại hóa nội dung lặp lại, chuẩn hóa định dạng, và thêm các nghiên cứu trường hợp
- Mở rộng phạm vi khung tối ưu hóa (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Chưa phát hành / Dự kiến
- Các kiểm tra nhanh tùy chọn cho từng mẫu để xác thực tính khả dụng của Foundry Local
- Xem xét các bản dịch để căn chỉnh các tham chiếu mô hình (ví dụ: `phi-4-mini`) khi thích hợp
- Thêm cấu hình pyright tối thiểu nếu các nhóm thích độ nghiêm ngặt trên toàn workspace

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.