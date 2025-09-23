<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c0cb9f7bcff2bc170532d8870a891f38",
  "translation_date": "2025-09-18T12:44:58+00:00",
  "source_file": "Module04/README.md",
  "language_code": "vi"
}
-->
# Chương 04: Chuyển đổi định dạng mô hình và lượng hóa - Tổng quan chương

Sự xuất hiện của EdgeAI đã khiến việc chuyển đổi định dạng mô hình và lượng hóa trở thành những công nghệ thiết yếu để triển khai các khả năng học máy tiên tiến trên các thiết bị có tài nguyên hạn chế. Chương này cung cấp hướng dẫn toàn diện để hiểu, triển khai và tối ưu hóa mô hình cho các kịch bản triển khai tại biên.

## 📚 Cấu trúc chương và lộ trình học tập

Chương này được tổ chức thành sáu phần tiến triển, mỗi phần xây dựng dựa trên phần trước để tạo ra sự hiểu biết toàn diện về tối ưu hóa mô hình cho tính toán tại biên:

---

## [Phần 1: Nền tảng chuyển đổi định dạng mô hình và lượng hóa](./01.Introduce.md)

### 🎯 Tổng quan
Phần nền tảng này thiết lập khung lý thuyết cho tối ưu hóa mô hình trong môi trường tính toán tại biên, bao gồm các mức độ lượng hóa từ 1-bit đến 8-bit và các chiến lược chuyển đổi định dạng chính.

**Các chủ đề chính:**
- Khung phân loại độ chính xác (siêu thấp, thấp, trung bình)
- Lợi ích và trường hợp sử dụng của định dạng GGUF và ONNX
- Lợi ích của lượng hóa đối với hiệu quả hoạt động và tính linh hoạt khi triển khai
- So sánh hiệu suất và dấu chân bộ nhớ

**Kết quả học tập:**
- Hiểu các mức độ lượng hóa và phân loại
- Xác định các kỹ thuật chuyển đổi định dạng phù hợp
- Học các chiến lược tối ưu hóa tiên tiến cho triển khai tại biên

---

## [Phần 2: Hướng dẫn triển khai Llama.cpp](./02.Llamacpp.md)

### 🎯 Tổng quan
Hướng dẫn toàn diện về triển khai Llama.cpp, một framework C++ mạnh mẽ cho phép suy luận mô hình ngôn ngữ lớn hiệu quả với thiết lập tối thiểu trên nhiều cấu hình phần cứng.

**Các chủ đề chính:**
- Cài đặt trên các nền tảng Windows, macOS và Linux
- Chuyển đổi định dạng GGUF và các mức lượng hóa khác nhau (Q2_K đến Q8_0)
- Tăng tốc phần cứng với CUDA, Metal, OpenCL và Vulkan
- Tích hợp Python và chiến lược triển khai sản xuất

**Kết quả học tập:**
- Thành thạo cài đặt đa nền tảng và xây dựng từ mã nguồn
- Triển khai các kỹ thuật lượng hóa và tối ưu hóa mô hình
- Triển khai mô hình ở chế độ máy chủ với tích hợp REST API

---

## [Phần 3: Bộ công cụ tối ưu hóa Microsoft Olive](./03.MicrosoftOlive.md)

### 🎯 Tổng quan
Khám phá Microsoft Olive, một bộ công cụ tối ưu hóa mô hình nhận thức phần cứng với hơn 40 thành phần tối ưu hóa tích hợp, được thiết kế cho triển khai mô hình cấp doanh nghiệp trên nhiều nền tảng phần cứng.

**Các chủ đề chính:**
- Tính năng tự động tối ưu hóa với lượng hóa động và tĩnh
- Trí tuệ nhận thức phần cứng cho triển khai CPU, GPU và NPU
- Hỗ trợ mô hình phổ biến (Llama, Phi, Qwen, Gemma) sẵn có
- Tích hợp doanh nghiệp với Azure ML và quy trình sản xuất

**Kết quả học tập:**
- Tận dụng tối ưu hóa tự động cho các kiến trúc mô hình khác nhau
- Triển khai chiến lược đa nền tảng
- Thiết lập các quy trình tối ưu hóa sẵn sàng cho doanh nghiệp

---

## [Phần 4: Bộ công cụ tối ưu hóa OpenVINO](./04.openvino.md)

### 🎯 Tổng quan
Khám phá toàn diện bộ công cụ OpenVINO của Intel, một nền tảng mã nguồn mở để triển khai các giải pháp AI hiệu suất cao trên môi trường đám mây, tại chỗ và biên với các khả năng tiên tiến của Khung nén mạng nơ-ron (NNCF).

**Các chủ đề chính:**
- Triển khai đa nền tảng với tăng tốc phần cứng (CPU, GPU, VPU, bộ tăng tốc AI)
- Khung nén mạng nơ-ron (NNCF) cho lượng hóa và cắt tỉa tiên tiến
- OpenVINO GenAI cho tối ưu hóa và triển khai mô hình ngôn ngữ lớn
- Khả năng máy chủ mô hình cấp doanh nghiệp và chiến lược triển khai mở rộng

**Kết quả học tập:**
- Thành thạo quy trình chuyển đổi và tối ưu hóa mô hình OpenVINO
- Triển khai các kỹ thuật lượng hóa tiên tiến với NNCF
- Triển khai mô hình tối ưu hóa trên nhiều nền tảng phần cứng với Máy chủ Mô hình

---

## [Phần 5: Khám phá sâu Framework Apple MLX](./05.AppleMLX.md)

### 🎯 Tổng quan
Phạm vi toàn diện về Apple MLX, một framework cách mạng được thiết kế đặc biệt cho học máy hiệu quả trên Apple Silicon, với trọng tâm là khả năng mô hình ngôn ngữ lớn và triển khai cục bộ.

**Các chủ đề chính:**
- Lợi ích của kiến trúc bộ nhớ hợp nhất và Metal Performance Shaders
- Hỗ trợ các mô hình LLaMA, Mistral, Phi-3, Qwen và Code Llama
- Tinh chỉnh LoRA để tùy chỉnh mô hình hiệu quả
- Tích hợp Hugging Face và hỗ trợ lượng hóa (4-bit và 8-bit)

**Kết quả học tập:**
- Thành thạo tối ưu hóa Apple Silicon cho triển khai LLM
- Triển khai các kỹ thuật tinh chỉnh và tùy chỉnh mô hình
- Xây dựng ứng dụng AI cấp doanh nghiệp với các tính năng bảo mật nâng cao

---

## [Phần 6: Tổng hợp quy trình phát triển Edge AI](./06.workflow-synthesis.md)

### 🎯 Tổng quan
Tổng hợp toàn diện tất cả các framework tối ưu hóa thành các quy trình thống nhất, ma trận quyết định và các thực tiễn tốt nhất cho triển khai Edge AI sẵn sàng sản xuất trên nhiều nền tảng và trường hợp sử dụng.

**Các chủ đề chính:**
- Kiến trúc quy trình thống nhất tích hợp nhiều framework tối ưu hóa
- Cây quyết định lựa chọn framework và phân tích đánh đổi hiệu suất
- Xác thực sẵn sàng sản xuất và chiến lược triển khai toàn diện
- Chiến lược tương lai hóa cho phần cứng và kiến trúc mô hình mới nổi

**Kết quả học tập:**
- Thành thạo lựa chọn framework có hệ thống dựa trên yêu cầu và hạn chế
- Triển khai các quy trình Edge AI cấp sản xuất với giám sát toàn diện
- Thiết kế các quy trình thích ứng phát triển cùng với công nghệ và yêu cầu mới

---

## 🎯 Kết quả học tập của chương

Sau khi hoàn thành chương toàn diện này, người đọc sẽ đạt được:

### **Thành thạo kỹ thuật**
- Hiểu sâu về các mức lượng hóa và ứng dụng thực tế
- Kinh nghiệm thực hành với nhiều framework tối ưu hóa
- Kỹ năng triển khai sản xuất cho môi trường tính toán tại biên

### **Hiểu biết chiến lược**
- Khả năng lựa chọn tối ưu hóa nhận thức phần cứng
- Ra quyết định thông minh về các đánh đổi hiệu suất
- Chiến lược triển khai và giám sát sẵn sàng cho doanh nghiệp

### **Các tiêu chuẩn hiệu suất**

| Framework   | Lượng hóa | Sử dụng bộ nhớ | Cải thiện tốc độ | Trường hợp sử dụng            |
|-------------|-----------|----------------|------------------|-------------------------------|
| Llama.cpp   | Q4_K_M    | ~4GB           | 2-3x            | Triển khai đa nền tảng        |
| Olive       | INT4      | Giảm 60-75%    | 2-6x            | Quy trình công việc doanh nghiệp |
| OpenVINO    | INT8/INT4 | Giảm 50-75%    | 2-5x            | Tối ưu hóa phần cứng Intel    |
| MLX         | 4-bit     | ~4GB           | 2-4x            | Tối ưu hóa Apple Silicon      |

## 🚀 Bước tiếp theo và ứng dụng nâng cao

Chương này cung cấp nền tảng hoàn chỉnh cho:
- Phát triển mô hình tùy chỉnh cho các lĩnh vực cụ thể
- Nghiên cứu về tối ưu hóa Edge AI
- Phát triển ứng dụng AI thương mại
- Triển khai Edge AI quy mô lớn cấp doanh nghiệp

Kiến thức từ sáu phần này mang lại bộ công cụ toàn diện để điều hướng bối cảnh đang phát triển nhanh chóng của tối ưu hóa và triển khai mô hình Edge AI.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.