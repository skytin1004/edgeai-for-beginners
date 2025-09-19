<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "142e0d1a5b794b8333cfd4895804ced5",
  "translation_date": "2025-09-18T13:15:41+00:00",
  "source_file": "Module07/README.md",
  "language_code": "vi"
}
-->
# Chương 07: Các Mẫu EdgeAI

Edge AI là sự kết hợp giữa trí tuệ nhân tạo và điện toán biên, cho phép xử lý thông minh trực tiếp trên thiết bị mà không cần kết nối với đám mây. Chương này khám phá năm triển khai EdgeAI khác nhau trên các nền tảng và framework, thể hiện sự linh hoạt và sức mạnh của việc chạy các mô hình AI tại biên.

## 1. EdgeAI trên NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano là một bước đột phá trong điện toán AI biên dễ tiếp cận, cung cấp hiệu suất AI lên đến 67 TOPS trong một thiết bị nhỏ gọn, kích thước bằng thẻ tín dụng. Nền tảng AI biên mạnh mẽ này mang lại khả năng phát triển AI tạo sinh cho người đam mê, sinh viên và nhà phát triển chuyên nghiệp.

### Các Tính Năng Chính
- Cung cấp hiệu suất AI lên đến 67 TOPS—cải thiện 1.7 lần so với phiên bản trước
- 1024 lõi CUDA và lên đến 32 lõi Tensor để xử lý AI
- CPU Arm Cortex-A78AE v8.2 64-bit 6 lõi với tần số tối đa 1.5 GHz
- Giá chỉ $249, mang lại nền tảng dễ tiếp cận và tiết kiệm nhất cho nhà phát triển, sinh viên và người sáng tạo

### Ứng Dụng
Jetson Orin Nano vượt trội trong việc chạy các mô hình AI tạo sinh hiện đại bao gồm transformers hình ảnh, mô hình ngôn ngữ lớn, và mô hình kết hợp hình ảnh-ngôn ngữ. Nó được thiết kế đặc biệt cho các trường hợp sử dụng GenAI và giờ đây bạn có thể chạy nhiều LLM trên một thiết bị nhỏ gọn. Các trường hợp sử dụng phổ biến bao gồm robot thông minh, drone thông minh, camera thông minh, và thiết bị biên tự động.

**Tìm Hiểu Thêm**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI trong Ứng Dụng Di Động với .NET MAUI và ONNX Runtime GenAI

Giải pháp này minh họa cách tích hợp AI tạo sinh và các mô hình ngôn ngữ lớn (LLMs) vào ứng dụng di động đa nền tảng bằng .NET MAUI (Multi-platform App UI) và ONNX Runtime GenAI. Cách tiếp cận này cho phép các nhà phát triển .NET xây dựng ứng dụng di động AI mạnh mẽ chạy natively trên thiết bị Android và iOS.

### Các Tính Năng Chính
- Xây dựng trên framework .NET MAUI, cung cấp một codebase duy nhất cho cả ứng dụng Android và iOS
- Tích hợp ONNX Runtime GenAI cho phép chạy các mô hình AI tạo sinh trực tiếp trên thiết bị di động
- Hỗ trợ các bộ tăng tốc phần cứng khác nhau dành cho thiết bị di động, bao gồm CPU, GPU, và bộ xử lý AI chuyên dụng
- Tối ưu hóa theo nền tảng như CoreML cho iOS và NNAPI cho Android thông qua ONNX Runtime
- Thực hiện toàn bộ vòng lặp AI tạo sinh bao gồm tiền xử lý, hậu xử lý, suy luận, xử lý logits, tìm kiếm và sampling, và quản lý bộ nhớ KV cache

### Lợi Ích Phát Triển
Cách tiếp cận .NET MAUI cho phép nhà phát triển tận dụng kỹ năng C# và .NET hiện có trong khi xây dựng ứng dụng AI đa nền tảng. Framework ONNX Runtime GenAI hỗ trợ nhiều kiến trúc mô hình bao gồm Llama, Mistral, Phi, Gemma, và nhiều mô hình khác. Các kernel ARM64 được tối ưu hóa tăng tốc nhân ma trận INT4, đảm bảo hiệu suất hiệu quả trên phần cứng di động trong khi vẫn duy trì trải nghiệm phát triển .NET quen thuộc.

### Các Trường Hợp Sử Dụng
Giải pháp này lý tưởng cho các nhà phát triển muốn xây dựng ứng dụng di động AI bằng công nghệ .NET, bao gồm chatbot thông minh, ứng dụng nhận diện hình ảnh, công cụ dịch ngôn ngữ, và hệ thống gợi ý cá nhân hóa chạy hoàn toàn trên thiết bị để tăng cường quyền riêng tư và khả năng hoạt động offline.

**Tìm Hiểu Thêm**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI trên Azure với Small Language Models Engine

Giải pháp EdgeAI dựa trên Azure của Microsoft tập trung vào việc triển khai các mô hình ngôn ngữ nhỏ (SLMs) một cách hiệu quả trong môi trường kết hợp giữa đám mây và biên. Cách tiếp cận này thu hẹp khoảng cách giữa các dịch vụ AI quy mô đám mây và yêu cầu triển khai tại biên.

### Lợi Thế Kiến Trúc
- Tích hợp liền mạch với các dịch vụ AI của Azure
- Chạy SLMs/LLMs và các mô hình đa phương tiện trên thiết bị và trong đám mây với ONNX Runtime
- Tối ưu hóa cho triển khai quy mô doanh nghiệp
- Hỗ trợ cập nhật và quản lý mô hình liên tục

### Các Trường Hợp Sử Dụng
Triển khai EdgeAI trên Azure vượt trội trong các kịch bản yêu cầu triển khai AI cấp doanh nghiệp với khả năng quản lý đám mây. Điều này bao gồm xử lý tài liệu thông minh, phân tích thời gian thực, và quy trình AI kết hợp tận dụng cả tài nguyên đám mây và biên.

**Tìm Hiểu Thêm**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI với Windows ML

Windows ML là runtime tiên tiến của Microsoft được tối ưu hóa cho suy luận mô hình trên thiết bị và triển khai đơn giản, đóng vai trò là nền tảng của Windows AI Foundry. Nền tảng này cho phép nhà phát triển tạo ứng dụng Windows tích hợp AI tận dụng toàn bộ khả năng của phần cứng PC.

### Khả Năng Nền Tảng
- Hoạt động trên tất cả các PC Windows 11 chạy phiên bản 24H2 (build 26100) hoặc cao hơn
- Hoạt động trên tất cả phần cứng PC x64 và ARM64, ngay cả các PC không có NPU hoặc GPU
- Cho phép nhà phát triển mang mô hình của riêng họ và triển khai hiệu quả trên hệ sinh thái đối tác silicon bao gồm AMD, Intel, NVIDIA và Qualcomm, trải dài CPU, GPU, NPU
- Nhờ các API hạ tầng, nhà phát triển không cần tạo nhiều bản build của ứng dụng để nhắm mục tiêu các loại silicon khác nhau

### Lợi Ích Cho Nhà Phát Triển
Windows ML trừu tượng hóa phần cứng và các nhà cung cấp thực thi, giúp bạn tập trung vào việc viết mã. Ngoài ra, Windows ML tự động cập nhật để hỗ trợ các NPU, GPU, và CPU mới nhất khi chúng được phát hành. Nền tảng này cung cấp framework thống nhất cho phát triển AI trên hệ sinh thái phần cứng Windows đa dạng.

**Tìm Hiểu Thêm**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](../windowdeveloper.md) - Hướng dẫn toàn diện cho phát triển Edge AI trên Windows

## 5. EdgeAI với Ứng Dụng Foundry Local

Foundry Local cho phép nhà phát triển xây dựng các ứng dụng Retrieval Augmented Generation (RAG) sử dụng tài nguyên cục bộ trong .NET, kết hợp các mô hình ngôn ngữ cục bộ với khả năng tìm kiếm ngữ nghĩa. Cách tiếp cận này cung cấp các giải pháp AI tập trung vào quyền riêng tư hoạt động hoàn toàn trên cơ sở hạ tầng cục bộ.

### Kiến Trúc Kỹ Thuật
- Kết hợp mô hình ngôn ngữ Phi-3, Local Embeddings, và Semantic Kernel để tạo kịch bản RAG
- Sử dụng embeddings dưới dạng vector (mảng) giá trị dấu phẩy động đại diện cho nội dung và ý nghĩa ngữ nghĩa của nó
- Semantic Kernel đóng vai trò là bộ điều phối chính, tích hợp Phi-3 và Smart Components để tạo pipeline RAG liền mạch
- Hỗ trợ cơ sở dữ liệu vector cục bộ bao gồm SQLite và Qdrant

### Lợi Ích Triển Khai
RAG, hay Retrieval Augmented Generation, chỉ đơn giản là cách nói "tra cứu một số thông tin và đưa vào prompt". Triển khai cục bộ này đảm bảo quyền riêng tư dữ liệu trong khi cung cấp các phản hồi thông minh dựa trên cơ sở kiến thức tùy chỉnh. Cách tiếp cận này đặc biệt có giá trị cho các kịch bản doanh nghiệp yêu cầu chủ quyền dữ liệu và khả năng hoạt động offline.

**Tìm Hiểu Thêm**: [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## Tài Nguyên Phát Triển Windows EdgeAI

Đối với các nhà phát triển nhắm mục tiêu nền tảng Windows, chúng tôi đã tạo một hướng dẫn toàn diện bao gồm toàn bộ hệ sinh thái Windows EdgeAI. Tài nguyên này cung cấp thông tin chi tiết về Windows AI Foundry, bao gồm các API, công cụ, và thực tiễn tốt nhất cho phát triển EdgeAI trên Windows.

### Nền Tảng Windows AI Foundry
Nền tảng Windows AI Foundry cung cấp một bộ công cụ và API toàn diện được thiết kế đặc biệt cho phát triển Edge AI trên các thiết bị Windows. Điều này bao gồm hỗ trợ chuyên biệt cho phần cứng tăng tốc NPU, tích hợp Windows ML, và các kỹ thuật tối ưu hóa theo nền tảng.

**Hướng Dẫn Toàn Diện**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

Hướng dẫn này bao gồm:
- Tổng quan và các thành phần của nền tảng Windows AI Foundry
- API Phi Silica cho suy luận hiệu quả trên phần cứng NPU
- API Computer Vision cho xử lý hình ảnh và OCR
- Tích hợp và tối ưu hóa runtime Windows ML
- Foundry Local CLI cho phát triển và kiểm thử cục bộ
- Chiến lược tối ưu hóa phần cứng cho các thiết bị Windows
- Ví dụ triển khai thực tế và thực tiễn tốt nhất

### Bộ Công Cụ AI cho Phát Triển Edge AI
Đối với các nhà phát triển sử dụng Visual Studio Code, tiện ích mở rộng AI Toolkit cung cấp môi trường phát triển toàn diện được thiết kế đặc biệt để xây dựng, kiểm thử, và triển khai ứng dụng Edge AI. Bộ công cụ này hợp lý hóa toàn bộ quy trình phát triển Edge AI trong VS Code.

**Hướng Dẫn Phát Triển**: [AI Toolkit for Edge AI Development](../aitoolkit.md)

Hướng dẫn AI Toolkit bao gồm:
- Khám phá và lựa chọn mô hình cho triển khai biên
- Quy trình kiểm thử và tối ưu hóa cục bộ
- Tích hợp ONNX và Ollama cho các mô hình biên
- Kỹ thuật chuyển đổi và lượng tử hóa mô hình
- Phát triển agent cho các kịch bản biên
- Đánh giá hiệu suất và giám sát
- Chuẩn bị triển khai và thực tiễn tốt nhất

## Kết Luận

Năm triển khai EdgeAI này thể hiện sự trưởng thành và đa dạng của các giải pháp AI biên hiện nay. Từ các thiết bị biên tăng tốc phần cứng như Jetson Orin Nano đến các framework phần mềm như ONNX Runtime GenAI và Windows ML, các nhà phát triển có những lựa chọn chưa từng có để triển khai ứng dụng thông minh tại biên.

Điểm chung giữa tất cả các nền tảng này là sự dân chủ hóa khả năng AI, làm cho học máy tiên tiến trở nên dễ tiếp cận với các nhà phát triển ở các cấp độ kỹ năng và trường hợp sử dụng khác nhau. Dù xây dựng ứng dụng di động, phần mềm máy tính, hay hệ thống nhúng, các giải pháp EdgeAI này cung cấp nền tảng cho thế hệ tiếp theo của các ứng dụng thông minh hoạt động hiệu quả và riêng tư tại biên.

Mỗi nền tảng mang lại lợi thế riêng: Jetson Orin Nano cho điện toán biên tăng tốc phần cứng, ONNX Runtime GenAI cho phát triển di động đa nền tảng, Azure EdgeAI cho tích hợp đám mây-biên cấp doanh nghiệp, Windows ML cho ứng dụng native trên Windows, và Foundry Local cho triển khai RAG tập trung vào quyền riêng tư. Cùng nhau, chúng tạo thành một hệ sinh thái toàn diện cho phát triển EdgeAI.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.