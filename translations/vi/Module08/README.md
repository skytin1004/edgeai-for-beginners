<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T21:48:28+00:00",
  "source_file": "Module08/README.md",
  "language_code": "vi"
}
-->
# Module 08: Thực hành với Microsoft Foundry Local - Bộ công cụ hoàn chỉnh cho nhà phát triển

## Tổng quan

Microsoft Foundry Local đại diện cho thế hệ tiếp theo của phát triển AI tại biên, cung cấp cho các nhà phát triển các công cụ mạnh mẽ để xây dựng, triển khai và mở rộng ứng dụng AI tại chỗ, đồng thời duy trì tích hợp liền mạch với Azure AI Foundry. Module này cung cấp hướng dẫn toàn diện về Foundry Local từ cài đặt đến phát triển tác nhân nâng cao.

**Công nghệ chính:**
- Microsoft Foundry Local CLI và SDK
- Tích hợp Azure AI Foundry
- Suy luận mô hình trên thiết bị
- Bộ nhớ đệm và tối ưu hóa mô hình cục bộ
- Kiến trúc dựa trên tác nhân

## Mục tiêu học tập của module

Khi hoàn thành module này, bạn sẽ:

- **Thành thạo cài đặt Foundry Local**: Cài đặt, cấu hình và tối ưu hóa Foundry Local cho phát triển trên Windows 11
- **Triển khai các mô hình đa dạng**: Chạy các mô hình phi, qwen, deepseek và GPT-OSS-20B tại chỗ bằng lệnh CLI
- **Xây dựng giải pháp sản xuất**: Tạo ứng dụng AI với kỹ thuật nhắc nâng cao và tích hợp dữ liệu
- **Tận dụng hệ sinh thái mã nguồn mở**: Tích hợp các mô hình Hugging Face và các đóng góp từ cộng đồng
- **So sánh kiến trúc AI**: Hiểu các điểm mạnh và yếu của LLMs so với SLMs và chiến lược triển khai
- **Phát triển tác nhân AI**: Xây dựng các tác nhân thông minh sử dụng kiến trúc và khả năng nền tảng của Foundry Local
- **Triển khai mô hình như công cụ**: Tạo các giải pháp AI mô-đun, tùy chỉnh cho ứng dụng doanh nghiệp

## Cấu trúc buổi học

### [1: Bắt đầu với Foundry Local](./01.FoundryLocalSetup.md)
**Trọng tâm**: Cài đặt, thiết lập CLI, bộ nhớ đệm mô hình và tăng tốc phần cứng

**Những gì bạn sẽ học:**
- Hoàn thành cài đặt Foundry Local trên Windows 11
- Cấu hình CLI và cấu trúc lệnh
- Chiến lược bộ nhớ đệm mô hình để đạt hiệu suất tối ưu
- Thiết lập và tối ưu hóa tăng tốc phần cứng
- Triển khai thực hành các mô hình phi, qwen, deepseek và GPT-OSS-20B

**Thời lượng**: 2-3 giờ  
**Yêu cầu trước**: Windows 11, kiến thức cơ bản về dòng lệnh

---

### [2: Xây dựng giải pháp AI với Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Trọng tâm**: Kỹ thuật nhắc nâng cao, tích hợp dữ liệu và nhiệm vụ hành động

**Những gì bạn sẽ học:**
- Kỹ thuật nhắc nâng cao
- Mẫu tích hợp dữ liệu và các thực hành tốt nhất
- Xây dựng nhiệm vụ AI hành động với Foundry Local
- Quy trình tích hợp liền mạch với Azure AI Foundry
- Tối ưu hóa hiệu suất và giám sát

**Thời lượng**: 2-3 giờ  
**Yêu cầu trước**: Hoàn thành buổi học 1, tài khoản Azure (tùy chọn)

---

### [3: Mô hình mã nguồn mở với Foundry Local](./03.OpenSourceModels.md)
**Trọng tâm**: Tích hợp Hugging Face, chiến lược chọn mô hình và các đóng góp từ cộng đồng

**Những gì bạn sẽ học:**
- Tích hợp mô hình Hugging Face với Foundry Local
- Chiến lược và triển khai "Mang theo mô hình của bạn" (BYOM)
- Thông tin từ chuỗi Model Mondays và các đóng góp từ cộng đồng
- Triển khai và tối ưu hóa mô hình tùy chỉnh
- Tiêu chí đánh giá và chọn mô hình từ cộng đồng

**Thời lượng**: 2-3 giờ  
**Yêu cầu trước**: Hoàn thành buổi học 1-2, tài khoản Hugging Face

---

### [4: Khám phá các mô hình tiên tiến - LLMs, SLMs và suy luận trên thiết bị](./04.CuttingEdgeModels.md)
**Trọng tâm**: So sánh mô hình, EdgeAI với Phi và ONNX Runtime, các demo nâng cao

**Những gì bạn sẽ học:**
- So sánh toàn diện giữa LLMs và SLMs và các trường hợp sử dụng
- Cân nhắc giữa suy luận cục bộ và trên đám mây, khung quyết định
- Triển khai EdgeAI với Phi và ONNX Runtime
- Phát triển và triển khai ứng dụng Chainlit RAG Chat
- Kỹ thuật tối ưu hóa suy luận WebGPU
- Tích hợp và khả năng của AI PC SDK

**Thời lượng**: 3-4 giờ  
**Yêu cầu trước**: Hoàn thành buổi học 1-3, hiểu các khái niệm về suy luận

---

### [5: Xây dựng tác nhân AI nhanh chóng với Foundry Local](./05.AIPoweredAgents.md)
**Trọng tâm**: Phát triển ứng dụng GenAI nhanh chóng, nhắc hệ thống, nền tảng và kiến trúc tác nhân

**Những gì bạn sẽ học:**
- Kiến trúc và mẫu thiết kế tác nhân của Foundry Local
- Kỹ thuật nhắc hệ thống để định hình hành vi tác nhân
- Kỹ thuật nền tảng để đảm bảo phản hồi đáng tin cậy của tác nhân
- Quy trình phát triển ứng dụng GenAI nhanh chóng
- Điều phối tác nhân và hệ thống đa tác nhân
- Chiến lược triển khai sản xuất cho các tác nhân AI

**Thời lượng**: 3-4 giờ  
**Yêu cầu trước**: Hoàn thành buổi học 1-4, hiểu cơ bản về tác nhân AI

---

### [6: Foundry Local - Mô hình như công cụ](./06.ModelsAsTools.md)
**Trọng tâm**: Giải pháp AI mô-đun, triển khai trên thiết bị và mở rộng doanh nghiệp

**Những gì bạn sẽ học:**
- Xem mô hình AI như các công cụ mô-đun, tùy chỉnh
- Triển khai trên thiết bị mà không cần phụ thuộc vào đám mây
- Suy luận với độ trễ thấp, chi phí hiệu quả và bảo vệ quyền riêng tư
- Mẫu tích hợp SDK, API và CLI
- Tùy chỉnh mô hình cho các trường hợp sử dụng cụ thể
- Chiến lược mở rộng từ cục bộ đến Azure AI Foundry
- Kiến trúc ứng dụng AI sẵn sàng cho doanh nghiệp

**Thời lượng**: 3-4 giờ  
**Yêu cầu trước**: Tất cả các buổi học trước, kinh nghiệm phát triển doanh nghiệp hữu ích

## Yêu cầu trước

### Yêu cầu hệ thống
- **Hệ điều hành**: Windows 11 (22H2 hoặc mới hơn)
- **Bộ nhớ**: RAM 16GB (khuyến nghị 32GB cho các mô hình lớn hơn)
- **Dung lượng lưu trữ**: 50GB trống để lưu bộ nhớ đệm mô hình
- **Phần cứng**: Thiết bị hỗ trợ NPU được khuyến nghị (Copilot+ PC), GPU tùy chọn
- **Mạng**: Internet tốc độ cao để tải mô hình ban đầu

### Môi trường phát triển
- Visual Studio Code với tiện ích mở rộng AI Toolkit
- Python 3.10+ và pip
- Git để kiểm soát phiên bản
- PowerShell hoặc Command Prompt
- Azure CLI (tùy chọn cho tích hợp đám mây)

### Kiến thức yêu cầu
- Hiểu cơ bản về các khái niệm AI/ML
- Quen thuộc với dòng lệnh
- Kiến thức cơ bản về lập trình Python
- Khái niệm REST API
- Kiến thức cơ bản về nhắc và suy luận mô hình

## Lộ trình module

**Thời gian ước tính tổng cộng**: 15-20 giờ

| Buổi học | Khu vực trọng tâm | Thời gian | Độ phức tạp |
|----------|-------------------|-----------|-------------|
|  1 | Cài đặt & Cơ bản | 2-3 giờ | Người mới bắt đầu |
|  2 | Giải pháp AI | 2-3 giờ | Trung cấp |
|  3 | Mã nguồn mở | 2-3 giờ | Trung cấp |
|  4 | Mô hình nâng cao | 3-4 giờ | Nâng cao |
|  5 | Tác nhân AI | 3-4 giờ | Nâng cao |
|  6 | Công cụ doanh nghiệp | 3-4 giờ | Chuyên gia |

## Tài nguyên chính

### Tài liệu chính
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Tài liệu Azure AI Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Chuỗi Model Mondays](https://aka.ms/model-mondays)

### Tài nguyên cộng đồng
- [Thảo luận cộng đồng Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Mẫu Azure AI Foundry](https://github.com/Azure-Samples/ai-foundry)
- [Cộng đồng nhà phát triển AI của Microsoft](https://techcommunity.microsoft.com/category/artificialintelligence)

## Kết quả học tập

Khi hoàn thành module này, bạn sẽ có khả năng:

### Thành thạo kỹ thuật
- **Triển khai và quản lý**: Cài đặt Foundry Local trên các môi trường phát triển và sản xuất
- **Tích hợp mô hình**: Làm việc liền mạch với các họ mô hình đa dạng từ Microsoft, Hugging Face và nguồn cộng đồng
- **Xây dựng ứng dụng**: Tạo ứng dụng AI sẵn sàng sản xuất với các tính năng và tối ưu hóa nâng cao
- **Phát triển tác nhân**: Triển khai các tác nhân AI tinh vi với nền tảng, lý luận và tích hợp công cụ

### Hiểu biết chiến lược
- **Quyết định kiến trúc**: Đưa ra lựa chọn thông minh giữa triển khai cục bộ và trên đám mây
- **Tối ưu hóa hiệu suất**: Tối ưu hóa hiệu suất suy luận trên các cấu hình phần cứng khác nhau
- **Mở rộng doanh nghiệp**: Thiết kế ứng dụng mở rộng từ nguyên mẫu cục bộ đến triển khai doanh nghiệp
- **Quyền riêng tư và bảo mật**: Triển khai các giải pháp AI bảo vệ quyền riêng tư với suy luận cục bộ

### Khả năng đổi mới
- **Phát triển nhanh**: Nhanh chóng xây dựng và thử nghiệm các ý tưởng ứng dụng AI
- **Tích hợp cộng đồng**: Tận dụng các mô hình mã nguồn mở và đóng góp vào hệ sinh thái
- **Mẫu nâng cao**: Triển khai các mẫu AI tiên tiến bao gồm RAG, tác nhân và tích hợp công cụ
- **Phát triển sẵn sàng cho tương lai**: Xây dựng ứng dụng sẵn sàng cho các công nghệ và mẫu AI mới nổi

## Bắt đầu

1. **Chuẩn bị môi trường của bạn**: Đảm bảo Windows 11 với thông số phần cứng được khuyến nghị
2. **Cài đặt yêu cầu trước**: Thiết lập các công cụ và phụ thuộc phát triển
3. **Bắt đầu với buổi học 1**: Bắt đầu với cài đặt và thiết lập cơ bản của Foundry Local
4. **Tiến hành tuần tự**: Hoàn thành các buổi học theo thứ tự để đạt tiến trình học tập tối ưu
5. **Thực hành liên tục**: Áp dụng các khái niệm thông qua bài tập thực hành và dự án

## Chỉ số thành công

Theo dõi tiến trình của bạn qua module:

- [ ] Cài đặt và cấu hình Foundry Local thành công
- [ ] Triển khai và chạy ít nhất 4 họ mô hình khác nhau
- [ ] Xây dựng một giải pháp AI hoàn chỉnh với tích hợp dữ liệu
- [ ] Tích hợp ít nhất 2 mô hình mã nguồn mở
- [ ] Tạo một ứng dụng chat RAG hoạt động
- [ ] Phát triển và triển khai một tác nhân AI
- [ ] Triển khai kiến trúc mô hình như công cụ

## Bắt đầu nhanh với mẫu

### 1) Thiết lập môi trường (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Khởi động một mô hình cục bộ (terminal mới)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Chạy demo Chainlit (Buổi học 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Chạy điều phối viên đa tác nhân (Buổi học 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Nếu bạn thấy lỗi kết nối, hãy xác thực Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Cấu hình router (Buổi học 6)
Router thực hiện kiểm tra nhanh sức khỏe và hỗ trợ cấu hình dựa trên môi trường:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Module này đại diện cho sự tiên tiến trong phát triển AI tại biên, kết hợp các công cụ cấp doanh nghiệp của Microsoft với sự linh hoạt và đổi mới của hệ sinh thái mã nguồn mở. Bằng cách thành thạo Foundry Local, bạn sẽ đứng ở vị trí tiên phong trong phát triển ứng dụng AI.

Đối với Azure OpenAI (Buổi học 2), xem README mẫu để biết các biến môi trường cần thiết và cài đặt phiên bản API.

## Tổng quan về mẫu

- `samples/01`: Chat REST nhanh với Foundry Local (`chat_quickstart.py`).
- `samples/02`: Tích hợp SDK OpenAI (`sdk_quickstart.py`).
- `samples/03`: Khám phá mô hình + kiểm tra nhanh (`list_and_bench.cmd`).
- `samples/04`: Demo Chainlit RAG (`app.py`).
- `samples/05`: Điều phối đa tác nhân (`python -m samples.05.agents.coordinator`).
- `samples/06`: Router mô hình như công cụ (`python samples\06\router.py`).

---

