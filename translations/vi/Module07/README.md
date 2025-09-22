<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb6eadc312d5658a0cd71c0085b43742",
  "translation_date": "2025-09-22T21:44:28+00:00",
  "source_file": "Module07/README.md",
  "language_code": "vi"
}
-->
# Chương 07: Các mẫu EdgeAI

Edge AI là sự kết hợp giữa trí tuệ nhân tạo và điện toán biên, cho phép xử lý thông minh trực tiếp trên thiết bị mà không cần kết nối với đám mây. Chương này khám phá năm triển khai EdgeAI khác nhau trên các nền tảng và framework, thể hiện sự linh hoạt và sức mạnh của việc chạy các mô hình AI tại biên.

## 1. EdgeAI trên NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano là một bước đột phá trong điện toán AI biên, cung cấp hiệu suất AI lên đến 67 TOPS trong một thiết bị nhỏ gọn, kích thước bằng thẻ tín dụng. Nền tảng AI biên mạnh mẽ này mang lại khả năng phát triển AI tạo sinh cho các nhà phát triển, sinh viên và người đam mê công nghệ.

### Các tính năng chính
- Cung cấp hiệu suất AI lên đến 67 TOPS—tăng 1.7 lần so với phiên bản trước
- 1024 lõi CUDA và lên đến 32 lõi Tensor dành cho xử lý AI
- CPU Arm Cortex-A78AE v8.2 64-bit 6 lõi với tần số tối đa 1.5 GHz
- Giá chỉ $249, mang lại nền tảng dễ tiếp cận và tiết kiệm cho các nhà phát triển, sinh viên và người sáng tạo

### Ứng dụng
Jetson Orin Nano vượt trội trong việc chạy các mô hình AI tạo sinh hiện đại như vision transformers, mô hình ngôn ngữ lớn (LLM), và mô hình kết hợp hình ảnh-ngôn ngữ. Nó được thiết kế đặc biệt cho các trường hợp sử dụng GenAI và giờ đây bạn có thể chạy nhiều LLM trên một thiết bị nhỏ gọn. Các trường hợp sử dụng phổ biến bao gồm robot thông minh, máy bay không người lái, camera thông minh, và các thiết bị biên tự động.

**Tìm hiểu thêm**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI trong ứng dụng di động với .NET MAUI và ONNX Runtime GenAI

Giải pháp này minh họa cách tích hợp AI tạo sinh và các mô hình ngôn ngữ lớn (LLM) vào ứng dụng di động đa nền tảng bằng .NET MAUI (Multi-platform App UI) và ONNX Runtime GenAI. Phương pháp này cho phép các nhà phát triển .NET xây dựng ứng dụng di động AI mạnh mẽ chạy natively trên thiết bị Android và iOS.

### Các tính năng chính
- Xây dựng trên framework .NET MAUI, cung cấp một mã nguồn duy nhất cho cả ứng dụng Android và iOS
- Tích hợp ONNX Runtime GenAI cho phép chạy các mô hình AI tạo sinh trực tiếp trên thiết bị di động
- Hỗ trợ các bộ tăng tốc phần cứng khác nhau dành cho thiết bị di động, bao gồm CPU, GPU, và các bộ xử lý AI chuyên dụng
- Tối ưu hóa theo nền tảng như CoreML cho iOS và NNAPI cho Android thông qua ONNX Runtime
- Thực hiện toàn bộ vòng lặp AI tạo sinh bao gồm tiền xử lý, suy luận, xử lý logits, tìm kiếm và lấy mẫu, và quản lý bộ nhớ đệm KV

### Lợi ích phát triển
Phương pháp .NET MAUI cho phép các nhà phát triển tận dụng kỹ năng C# và .NET hiện có trong khi xây dựng ứng dụng AI đa nền tảng. Framework ONNX Runtime GenAI hỗ trợ nhiều kiến trúc mô hình bao gồm Llama, Mistral, Phi, Gemma, và nhiều mô hình khác. Các kernel ARM64 được tối ưu hóa tăng tốc nhân ma trận INT4, đảm bảo hiệu suất hiệu quả trên phần cứng di động trong khi vẫn giữ trải nghiệm phát triển .NET quen thuộc.

### Các trường hợp sử dụng
Giải pháp này lý tưởng cho các nhà phát triển muốn xây dựng ứng dụng di động AI bằng công nghệ .NET, bao gồm chatbot thông minh, ứng dụng nhận diện hình ảnh, công cụ dịch ngôn ngữ, và hệ thống gợi ý cá nhân hóa chạy hoàn toàn trên thiết bị để tăng cường quyền riêng tư và khả năng hoạt động offline.

**Tìm hiểu thêm**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI trên Azure với Small Language Models Engine

Giải pháp EdgeAI dựa trên Azure của Microsoft tập trung vào việc triển khai các mô hình ngôn ngữ nhỏ (SLM) một cách hiệu quả trong môi trường kết hợp giữa đám mây và biên. Phương pháp này kết nối các dịch vụ AI quy mô đám mây với yêu cầu triển khai tại biên.

### Ưu điểm kiến trúc
- Tích hợp liền mạch với các dịch vụ AI của Azure
- Chạy SLM/LLM và các mô hình đa phương tiện trên thiết bị và trong đám mây với ONNX Runtime
- Tối ưu hóa cho triển khai quy mô doanh nghiệp
- Hỗ trợ cập nhật và quản lý mô hình liên tục

### Các trường hợp sử dụng
Triển khai EdgeAI trên Azure vượt trội trong các tình huống yêu cầu triển khai AI cấp doanh nghiệp với khả năng quản lý đám mây. Điều này bao gồm xử lý tài liệu thông minh, phân tích thời gian thực, và các quy trình AI kết hợp tận dụng cả tài nguyên đám mây và biên.

**Tìm hiểu thêm**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI với Windows ML

Windows ML là runtime tiên tiến của Microsoft được tối ưu hóa cho suy luận mô hình trên thiết bị và triển khai đơn giản, đóng vai trò là nền tảng của Windows AI Foundry. Nền tảng này cho phép các nhà phát triển tạo ứng dụng Windows tích hợp AI tận dụng toàn bộ khả năng phần cứng PC.

### Khả năng nền tảng
- Hoạt động trên tất cả các PC Windows 11 chạy phiên bản 24H2 (build 26100) hoặc cao hơn
- Hoạt động trên tất cả phần cứng PC x64 và ARM64, ngay cả các PC không có NPU hoặc GPU
- Cho phép các nhà phát triển mang mô hình của riêng họ và triển khai hiệu quả trên hệ sinh thái silicon của các đối tác như AMD, Intel, NVIDIA và Qualcomm, bao gồm CPU, GPU, NPU
- Nhờ các API hạ tầng, các nhà phát triển không cần tạo nhiều bản build của ứng dụng để nhắm đến các loại silicon khác nhau

### Lợi ích cho nhà phát triển
Windows ML trừu tượng hóa phần cứng và các nhà cung cấp thực thi, giúp bạn tập trung vào việc viết mã. Ngoài ra, Windows ML tự động cập nhật để hỗ trợ các NPU, GPU, và CPU mới nhất khi chúng được phát hành. Nền tảng này cung cấp một framework thống nhất cho phát triển AI trên hệ sinh thái phần cứng Windows đa dạng.

**Tìm hiểu thêm**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](../windowdeveloper.md) - Hướng dẫn toàn diện về phát triển Edge AI trên Windows

## 5. EdgeAI với Foundry Local Applications

Foundry Local cho phép các nhà phát triển xây dựng ứng dụng Retrieval Augmented Generation (RAG) sử dụng tài nguyên cục bộ trong .NET, kết hợp các mô hình ngôn ngữ cục bộ với khả năng tìm kiếm ngữ nghĩa. Phương pháp này cung cấp các giải pháp AI tập trung vào quyền riêng tư hoạt động hoàn toàn trên hạ tầng cục bộ.

### Kiến trúc kỹ thuật
- Kết hợp mô hình ngôn ngữ Phi, Local Embeddings, và Semantic Kernel để tạo kịch bản RAG
- Sử dụng embeddings dưới dạng vector (mảng) các giá trị số thực đại diện cho nội dung và ý nghĩa ngữ nghĩa của nó
- Semantic Kernel đóng vai trò là bộ điều phối chính, tích hợp Phi và các thành phần thông minh để tạo pipeline RAG liền mạch
- Hỗ trợ các cơ sở dữ liệu vector cục bộ bao gồm SQLite và Qdrant

### Lợi ích triển khai
RAG, hay Retrieval Augmented Generation, chỉ đơn giản là cách nói "tra cứu một số thông tin và đưa vào prompt". Triển khai cục bộ này đảm bảo quyền riêng tư dữ liệu trong khi cung cấp các phản hồi thông minh dựa trên cơ sở kiến thức tùy chỉnh. Phương pháp này đặc biệt có giá trị trong các tình huống doanh nghiệp yêu cầu chủ quyền dữ liệu và khả năng hoạt động offline.

**Tìm hiểu thêm**: [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local cung cấp một máy chủ REST tương thích với OpenAI được hỗ trợ bởi ONNX Runtime để chạy các mô hình cục bộ trên Windows. Dưới đây là tóm tắt nhanh đã được xác thực; xem tài liệu chính thức để biết chi tiết đầy đủ.

- Bắt đầu: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Kiến trúc: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Tham khảo CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Hướng dẫn đầy đủ về Windows trong repo này: [foundrylocal.md](./foundrylocal.md)

Cài đặt hoặc nâng cấp trên Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Khám phá các danh mục CLI:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Chạy một mô hình và khám phá endpoint động:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Kiểm tra REST nhanh để liệt kê các mô hình (thay thế PORT từ trạng thái):
```cmd
curl -s http://localhost:PORT/v1/models
```

Mẹo:
- Tích hợp SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Mang mô hình của riêng bạn (biên dịch): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Tài nguyên phát triển Windows EdgeAI

Đối với các nhà phát triển nhắm đến nền tảng Windows, chúng tôi đã tạo một hướng dẫn toàn diện bao gồm toàn bộ hệ sinh thái Windows EdgeAI. Tài nguyên này cung cấp thông tin chi tiết về Windows AI Foundry, bao gồm các API, công cụ, và các thực tiễn tốt nhất để phát triển EdgeAI trên Windows.

### Nền tảng Windows AI Foundry
Nền tảng Windows AI Foundry cung cấp một bộ công cụ và API toàn diện được thiết kế đặc biệt cho phát triển AI biên trên các thiết bị Windows. Điều này bao gồm hỗ trợ chuyên biệt cho phần cứng tăng tốc NPU, tích hợp Windows ML, và các kỹ thuật tối ưu hóa theo nền tảng.

**Hướng dẫn toàn diện**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

Hướng dẫn này bao gồm:
- Tổng quan về nền tảng Windows AI Foundry và các thành phần
- API Phi Silica cho suy luận hiệu quả trên phần cứng NPU
- API Computer Vision cho xử lý hình ảnh và OCR
- Tích hợp và tối ưu hóa runtime Windows ML
- CLI Foundry Local cho phát triển và kiểm thử cục bộ
- Chiến lược tối ưu hóa phần cứng cho các thiết bị Windows
- Ví dụ triển khai thực tế và các thực tiễn tốt nhất

### Bộ công cụ AI cho phát triển Edge AI
Đối với các nhà phát triển sử dụng Visual Studio Code, tiện ích mở rộng AI Toolkit cung cấp môi trường phát triển toàn diện được thiết kế đặc biệt để xây dựng, kiểm thử, và triển khai ứng dụng Edge AI. Bộ công cụ này hợp lý hóa toàn bộ quy trình phát triển Edge AI trong VS Code.

**Hướng dẫn phát triển**: [AI Toolkit for Edge AI Development](../aitoolkit.md)

Hướng dẫn AI Toolkit bao gồm:
- Khám phá và lựa chọn mô hình cho triển khai biên
- Quy trình kiểm thử và tối ưu hóa cục bộ
- Tích hợp ONNX và Ollama cho các mô hình biên
- Kỹ thuật chuyển đổi và lượng tử hóa mô hình
- Phát triển agent cho các kịch bản biên
- Đánh giá hiệu suất và giám sát
- Chuẩn bị triển khai và các thực tiễn tốt nhất

## Kết luận

Năm triển khai EdgeAI này thể hiện sự trưởng thành và đa dạng của các giải pháp AI biên hiện nay. Từ các thiết bị biên tăng tốc phần cứng như Jetson Orin Nano đến các framework phần mềm như ONNX Runtime GenAI và Windows ML, các nhà phát triển có những lựa chọn chưa từng có để triển khai ứng dụng thông minh tại biên.

Điểm chung giữa tất cả các nền tảng này là sự dân chủ hóa khả năng AI, giúp các mô hình học máy tiên tiến trở nên dễ tiếp cận hơn với các nhà phát triển ở mọi cấp độ kỹ năng và trường hợp sử dụng. Dù xây dựng ứng dụng di động, phần mềm máy tính, hay hệ thống nhúng, các giải pháp EdgeAI này cung cấp nền tảng cho thế hệ tiếp theo của các ứng dụng thông minh hoạt động hiệu quả và bảo mật tại biên.

Mỗi nền tảng mang lại lợi thế riêng: Jetson Orin Nano cho điện toán biên tăng tốc phần cứng, ONNX Runtime GenAI cho phát triển di động đa nền tảng, Azure EdgeAI cho tích hợp đám mây-biên cấp doanh nghiệp, Windows ML cho ứng dụng native trên Windows, và Foundry Local cho triển khai RAG tập trung vào quyền riêng tư. Cùng nhau, chúng tạo thành một hệ sinh thái toàn diện cho phát triển EdgeAI.

---

