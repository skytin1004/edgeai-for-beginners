<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-18T13:24:17+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "vi"
}
-->
# Hướng dẫn phát triển AI Toolkit cho Visual Studio Code - Edge AI

## Giới thiệu

Chào mừng bạn đến với hướng dẫn toàn diện về cách sử dụng AI Toolkit cho Visual Studio Code trong phát triển Edge AI. Khi trí tuệ nhân tạo chuyển từ điện toán đám mây tập trung sang các thiết bị biên phân tán, các nhà phát triển cần những công cụ mạnh mẽ, tích hợp để xử lý các thách thức độc đáo của triển khai biên - từ hạn chế tài nguyên đến yêu cầu hoạt động ngoại tuyến.

AI Toolkit cho Visual Studio Code lấp đầy khoảng trống này bằng cách cung cấp một môi trường phát triển hoàn chỉnh, được thiết kế đặc biệt để xây dựng, kiểm thử và tối ưu hóa các ứng dụng AI hoạt động hiệu quả trên các thiết bị biên. Dù bạn đang phát triển cho cảm biến IoT, thiết bị di động, hệ thống nhúng hay máy chủ biên, bộ công cụ này giúp đơn giản hóa toàn bộ quy trình phát triển của bạn trong môi trường VS Code quen thuộc.

Hướng dẫn này sẽ đưa bạn qua các khái niệm cơ bản, công cụ và thực tiễn tốt nhất để tận dụng AI Toolkit trong các dự án Edge AI của bạn, từ việc chọn mô hình ban đầu đến triển khai sản xuất.

## Tổng quan

AI Toolkit cung cấp một môi trường phát triển tích hợp cho toàn bộ vòng đời ứng dụng Edge AI trong VS Code. Nó tích hợp liền mạch với các mô hình AI phổ biến từ các nhà cung cấp như OpenAI, Anthropic, Google và GitHub, đồng thời hỗ trợ triển khai mô hình cục bộ thông qua ONNX và Ollama - những khả năng quan trọng cho các ứng dụng Edge AI yêu cầu suy luận trên thiết bị.

Điểm nổi bật của AI Toolkit trong phát triển Edge AI là tập trung vào toàn bộ quy trình triển khai biên. Không giống như các công cụ phát triển AI truyền thống chủ yếu nhắm đến triển khai đám mây, AI Toolkit bao gồm các tính năng chuyên biệt cho tối ưu hóa mô hình, kiểm thử trong điều kiện hạn chế tài nguyên và đánh giá hiệu suất cụ thể cho biên. Bộ công cụ hiểu rằng phát triển Edge AI đòi hỏi các cân nhắc khác biệt - kích thước mô hình nhỏ hơn, thời gian suy luận nhanh hơn, khả năng hoạt động ngoại tuyến và tối ưu hóa phần cứng cụ thể.

Nền tảng này hỗ trợ nhiều kịch bản triển khai, từ suy luận trên thiết bị đơn giản đến kiến trúc biên đa mô hình phức tạp. Nó cung cấp các công cụ chuyển đổi, lượng hóa và tối ưu hóa mô hình cần thiết cho triển khai biên thành công, đồng thời duy trì năng suất của nhà phát triển mà VS Code nổi tiếng.

## Mục tiêu học tập

Khi hoàn thành hướng dẫn này, bạn sẽ có thể:

### Năng lực cốt lõi
- **Cài đặt và cấu hình** AI Toolkit cho Visual Studio Code để phát triển Edge AI
- **Điều hướng và sử dụng** giao diện AI Toolkit, bao gồm Model Catalog, Playground và Agent Builder
- **Chọn và đánh giá** các mô hình AI phù hợp cho triển khai biên dựa trên hiệu suất và hạn chế tài nguyên
- **Chuyển đổi và tối ưu hóa** mô hình bằng định dạng ONNX và kỹ thuật lượng hóa cho thiết bị biên

### Kỹ năng phát triển Edge AI
- **Thiết kế và triển khai** ứng dụng Edge AI bằng môi trường phát triển tích hợp
- **Kiểm thử mô hình** trong điều kiện giống biên bằng suy luận cục bộ và giám sát tài nguyên
- **Tạo và tùy chỉnh** các tác nhân AI được tối ưu hóa cho các kịch bản triển khai biên
- **Đánh giá hiệu suất mô hình** bằng các chỉ số liên quan đến điện toán biên (độ trễ, sử dụng bộ nhớ, độ chính xác)

### Tối ưu hóa và triển khai
- **Áp dụng kỹ thuật lượng hóa và cắt giảm** để giảm kích thước mô hình trong khi duy trì hiệu suất chấp nhận được
- **Tối ưu hóa mô hình** cho các nền tảng phần cứng biên cụ thể bao gồm CPU, GPU và tăng tốc NPU
- **Thực hiện các thực tiễn tốt nhất** cho phát triển Edge AI bao gồm quản lý tài nguyên và chiến lược dự phòng
- **Chuẩn bị mô hình và ứng dụng** cho triển khai sản xuất trên thiết bị biên

### Các khái niệm nâng cao về Edge AI
- **Tích hợp với các framework Edge AI** bao gồm ONNX Runtime, Windows ML và TensorFlow Lite
- **Triển khai kiến trúc đa mô hình** và các kịch bản học liên kết cho môi trường biên
- **Khắc phục các vấn đề phổ biến của Edge AI** bao gồm hạn chế bộ nhớ, tốc độ suy luận và tương thích phần cứng
- **Thiết kế chiến lược giám sát và ghi nhật ký** cho các ứng dụng Edge AI trong sản xuất

### Ứng dụng thực tiễn
- **Xây dựng giải pháp Edge AI toàn diện** từ việc chọn mô hình đến triển khai
- **Thể hiện sự thành thạo** trong quy trình phát triển và kỹ thuật tối ưu hóa cụ thể cho biên
- **Áp dụng các khái niệm đã học** vào các trường hợp sử dụng Edge AI thực tế bao gồm IoT, di động và ứng dụng nhúng
- **Đánh giá và so sánh** các chiến lược triển khai Edge AI khác nhau và các đánh đổi của chúng

## Các tính năng chính cho phát triển Edge AI

### 1. Danh mục và khám phá mô hình
- **Hỗ trợ mô hình cục bộ**: Khám phá và truy cập các mô hình AI được tối ưu hóa đặc biệt cho triển khai biên
- **Tích hợp ONNX**: Truy cập các mô hình ở định dạng ONNX để suy luận hiệu quả trên biên
- **Hỗ trợ Ollama**: Tận dụng các mô hình chạy cục bộ thông qua Ollama để bảo mật và hoạt động ngoại tuyến
- **So sánh mô hình**: So sánh các mô hình cạnh nhau để tìm sự cân bằng tối ưu giữa hiệu suất và tiêu thụ tài nguyên cho thiết bị biên

### 2. Playground tương tác
- **Môi trường kiểm thử cục bộ**: Kiểm thử mô hình cục bộ trước khi triển khai biên
- **Thử nghiệm đa phương thức**: Kiểm thử với hình ảnh, văn bản và các đầu vào khác thường gặp trong các kịch bản biên
- **Điều chỉnh tham số**: Thử nghiệm với các tham số mô hình khác nhau để tối ưu hóa cho các hạn chế biên
- **Giám sát hiệu suất thời gian thực**: Quan sát tốc độ suy luận và sử dụng tài nguyên trong quá trình phát triển

### 3. Agent Builder cho ứng dụng biên
- **Kỹ thuật tạo prompt**: Tạo các prompt được tối ưu hóa hoạt động hiệu quả với các mô hình biên nhỏ hơn
- **Tích hợp công cụ MCP**: Tích hợp các công cụ Model Context Protocol để tăng cường khả năng của tác nhân biên
- **Tạo mã**: Tạo mã sẵn sàng sản xuất được tối ưu hóa cho các kịch bản triển khai biên
- **Đầu ra có cấu trúc**: Thiết kế các tác nhân cung cấp phản hồi nhất quán, có cấu trúc phù hợp cho các ứng dụng biên

### 4. Đánh giá và kiểm thử mô hình
- **Chỉ số hiệu suất**: Đánh giá mô hình bằng các chỉ số liên quan đến triển khai biên (độ trễ, sử dụng bộ nhớ, độ chính xác)
- **Kiểm thử hàng loạt**: Kiểm thử đồng thời nhiều cấu hình mô hình để tìm cài đặt biên tối ưu
- **Đánh giá tùy chỉnh**: Tạo tiêu chí đánh giá tùy chỉnh cụ thể cho các trường hợp sử dụng Edge AI
- **Hồ sơ tài nguyên**: Phân tích yêu cầu bộ nhớ và tính toán để lập kế hoạch triển khai biên

### 5. Chuyển đổi và tối ưu hóa mô hình
- **Chuyển đổi ONNX**: Chuyển đổi mô hình từ các định dạng khác nhau sang ONNX để tương thích với biên
- **Lượng hóa**: Giảm kích thước mô hình và cải thiện tốc độ suy luận thông qua các kỹ thuật lượng hóa
- **Tối ưu hóa phần cứng**: Tối ưu hóa mô hình cho phần cứng biên cụ thể (CPU, GPU, NPU)
- **Chuyển đổi định dạng**: Chuyển đổi mô hình từ Hugging Face và các nguồn khác để triển khai biên

### 6. Tinh chỉnh cho các kịch bản biên
- **Thích ứng theo miền**: Tùy chỉnh mô hình cho các trường hợp sử dụng và môi trường biên cụ thể
- **Đào tạo cục bộ**: Đào tạo mô hình cục bộ với hỗ trợ GPU cho các yêu cầu cụ thể của biên
- **Tích hợp Azure**: Tận dụng Azure Container Apps để tinh chỉnh trên đám mây trước khi triển khai biên
- **Học chuyển giao**: Thích ứng các mô hình đã được đào tạo trước cho các nhiệm vụ và hạn chế cụ thể của biên

### 7. Giám sát và theo dõi hiệu suất
- **Phân tích hiệu suất biên**: Giám sát hiệu suất mô hình trong điều kiện giống biên
- **Thu thập dấu vết**: Thu thập dữ liệu hiệu suất chi tiết để tối ưu hóa
- **Xác định nút thắt**: Xác định các vấn đề hiệu suất trước khi triển khai lên thiết bị biên
- **Theo dõi sử dụng tài nguyên**: Giám sát bộ nhớ, CPU và thời gian suy luận để tối ưu hóa biên

## Quy trình phát triển Edge AI

### Giai đoạn 1: Khám phá và chọn mô hình
1. **Khám phá danh mục mô hình**: Sử dụng danh mục mô hình để tìm các mô hình phù hợp cho triển khai biên
2. **So sánh hiệu suất**: Đánh giá mô hình dựa trên kích thước, độ chính xác và tốc độ suy luận
3. **Kiểm thử cục bộ**: Sử dụng mô hình Ollama hoặc ONNX để kiểm thử cục bộ trước khi triển khai biên
4. **Đánh giá yêu cầu tài nguyên**: Xác định nhu cầu bộ nhớ và tính toán cho các thiết bị biên mục tiêu

### Giai đoạn 2: Tối ưu hóa mô hình
1. **Chuyển đổi sang ONNX**: Chuyển đổi các mô hình đã chọn sang định dạng ONNX để tương thích với biên
2. **Áp dụng lượng hóa**: Giảm kích thước mô hình thông qua lượng hóa INT8 hoặc INT4
3. **Tối ưu hóa phần cứng**: Tối ưu hóa cho phần cứng biên mục tiêu (ARM, x86, bộ tăng tốc chuyên dụng)
4. **Xác nhận hiệu suất**: Xác nhận các mô hình được tối ưu hóa duy trì độ chính xác chấp nhận được

### Giai đoạn 3: Phát triển ứng dụng
1. **Thiết kế tác nhân**: Sử dụng Agent Builder để tạo các tác nhân AI được tối ưu hóa cho biên
2. **Kỹ thuật tạo prompt**: Phát triển các prompt hoạt động hiệu quả với các mô hình nhỏ hơn
3. **Kiểm thử tích hợp**: Kiểm thử các tác nhân trong điều kiện biên mô phỏng
4. **Tạo mã**: Tạo mã sản xuất được tối ưu hóa cho triển khai biên

### Giai đoạn 4: Đánh giá và kiểm thử
1. **Đánh giá hàng loạt**: Kiểm thử nhiều cấu hình để tìm cài đặt biên tối ưu
2. **Hồ sơ hiệu suất**: Phân tích tốc độ suy luận, sử dụng bộ nhớ và độ chính xác
3. **Mô phỏng biên**: Kiểm thử trong điều kiện tương tự môi trường triển khai biên mục tiêu
4. **Kiểm thử áp lực**: Đánh giá hiệu suất dưới các điều kiện tải khác nhau

### Giai đoạn 5: Chuẩn bị triển khai
1. **Tối ưu hóa cuối cùng**: Áp dụng các tối ưu hóa cuối cùng dựa trên kết quả kiểm thử
2. **Đóng gói triển khai**: Đóng gói mô hình và mã cho triển khai biên
3. **Tài liệu hóa**: Tài liệu hóa các yêu cầu và cấu hình triển khai
4. **Thiết lập giám sát**: Chuẩn bị giám sát và ghi nhật ký cho triển khai sản xuất

## Đối tượng mục tiêu cho phát triển Edge AI

### Nhà phát triển Edge AI
- Các nhà phát triển ứng dụng xây dựng thiết bị biên và giải pháp IoT tích hợp AI
- Các nhà phát triển hệ thống nhúng tích hợp khả năng AI vào các thiết bị hạn chế tài nguyên
- Các nhà phát triển di động tạo ứng dụng AI trên thiết bị cho điện thoại thông minh và máy tính bảng

### Kỹ sư Edge AI
- Các kỹ sư AI tối ưu hóa mô hình cho triển khai biên và quản lý các pipeline suy luận
- Các kỹ sư DevOps triển khai và quản lý mô hình AI trên cơ sở hạ tầng biên phân tán
- Các kỹ sư hiệu suất tối ưu hóa khối lượng công việc AI cho các hạn chế phần cứng biên

### Nhà nghiên cứu và giáo dục
- Các nhà nghiên cứu AI phát triển mô hình và thuật toán hiệu quả cho điện toán biên
- Các nhà giáo dục giảng dạy các khái niệm Edge AI và trình diễn các kỹ thuật tối ưu hóa
- Sinh viên học về các thách thức và giải pháp trong triển khai Edge AI

## Các trường hợp sử dụng Edge AI

### Thiết bị IoT thông minh
- **Nhận diện hình ảnh thời gian thực**: Triển khai mô hình thị giác máy tính trên camera và cảm biến IoT
- **Xử lý giọng nói**: Thực hiện nhận diện giọng nói và xử lý ngôn ngữ tự nhiên trên loa thông minh
- **Bảo trì dự đoán**: Chạy mô hình phát hiện bất thường trên các thiết bị biên công nghiệp
- **Giám sát môi trường**: Triển khai mô hình phân tích dữ liệu cảm biến cho các ứng dụng môi trường

### Ứng dụng di động và nhúng
- **Dịch thuật trên thiết bị**: Thực hiện mô hình dịch ngôn ngữ hoạt động ngoại tuyến
- **Thực tế tăng cường**: Triển khai nhận diện và theo dõi đối tượng thời gian thực cho các ứng dụng AR
- **Giám sát sức khỏe**: Chạy mô hình phân tích sức khỏe trên thiết bị đeo và thiết bị y tế
- **Hệ thống tự động**: Thực hiện mô hình ra quyết định cho drone, robot và phương tiện

### Cơ sở hạ tầng điện toán biên
- **Trung tâm dữ liệu biên**: Triển khai mô hình AI trong các trung tâm dữ liệu biên cho các ứng dụng độ trễ thấp
- **Tích hợp CDN**: Tích hợp khả năng xử lý AI vào các mạng phân phối nội dung
- **Biên 5G**: Tận dụng điện toán biên 5G cho các ứng dụng tích hợp AI
- **Điện toán sương mù**: Thực hiện xử lý AI trong các môi trường điện toán sương mù

## Cài đặt và thiết lập

### Cài đặt nhanh
Cài đặt tiện ích mở rộng AI Toolkit trực tiếp từ Visual Studio Code Marketplace:

```
Install: AI Toolkit for Visual Studio Code (ms-windows-ai-studio.windows-ai-studio)
```

### Yêu cầu trước cho phát triển Edge AI
- **ONNX Runtime**: Cài đặt ONNX Runtime để suy luận mô hình
- **Ollama** (Tùy chọn): Cài đặt Ollama để phục vụ mô hình cục bộ
- **Môi trường Python**: Thiết lập Python với các thư viện AI cần thiết
- **Công cụ phần cứng biên**: Cài đặt các công cụ phát triển phần cứng cụ thể (CUDA, OpenVINO, v.v.)

### Cấu hình ban đầu
1. Mở VS Code và cài đặt tiện ích mở rộng AI Toolkit
2. Cấu hình nguồn mô hình (ONNX, Ollama, nhà cung cấp đám mây)
3. Thiết lập môi trường phát triển cục bộ để kiểm thử biên
4. Cấu hình các tùy chọn tăng tốc phần cứng cho máy phát triển của bạn

## Bắt đầu với phát triển Edge AI

### Bước 1: Chọn mô hình
1. Mở giao diện AI Toolkit trong Activity Bar
2. Duyệt danh mục mô hình để tìm các mô hình tương thích với biên
3. Lọc theo kích thước mô hình, định dạng (ONNX) và đặc điểm hiệu suất
4. So sánh các mô hình bằng công cụ so sánh tích hợp

### Bước 2: Kiểm thử cục bộ
1. Sử dụng Playground để kiểm thử các mô hình đã chọn cục bộ
2. Thử nghiệm với các prompt và tham số khác nhau
3. Giám sát các chỉ số hiệu suất trong quá trình kiểm thử
4. Đánh giá phản hồi mô hình cho các yêu cầu trường hợp sử dụng biên

### Bước 3: Tối ưu hóa mô hình
1. Sử dụng công cụ chuyển đổi mô hình để tối ưu hóa cho triển khai biên
2. Áp dụng lượng hóa để giảm kích thước mô hình
3. Kiểm thử các mô hình được tối ưu hóa để đảm bảo hiệu suất chấp nhận được
4. Tài liệu hóa các cài đặt tối ưu hóa và đánh đổi hiệu suất

### Bước 4: Phát triển tác nhân
1. Sử dụng Agent Builder để tạo các tác nhân AI được tối ưu hóa cho biên
2. Phát triển các prompt hoạt động hiệu quả với các mô hình nhỏ hơn
3. Tích hợp các công cụ và API cần thiết cho các kịch bản biên
4. Kiểm thử các tác nhân trong điều kiện biên mô phỏng

### Bước 5: Đánh giá và triển khai
1. Sử dụng đánh giá hàng loạt để kiểm thử nhiều cấu hình
2. Hồ sơ hiệu suất dưới các điều kiện khác nhau
3. Chuẩn bị các gói triển khai cho các thiết bị biên mục tiêu
4. Thiết lập giám sát và ghi nhật ký cho
- **Bảo mật**: Triển khai các biện pháp bảo mật phù hợp cho các ứng dụng AI tại biên

## Tích hợp với các khung AI tại biên

### ONNX Runtime
- **Triển khai đa nền tảng**: Triển khai các mô hình ONNX trên các nền tảng biên khác nhau
- **Tối ưu hóa phần cứng**: Tận dụng các tối ưu hóa phần cứng cụ thể của ONNX Runtime
- **Hỗ trợ di động**: Sử dụng ONNX Runtime Mobile cho các ứng dụng trên điện thoại thông minh và máy tính bảng
- **Tích hợp IoT**: Triển khai trên các thiết bị IoT bằng các phiên bản nhẹ của ONNX Runtime

### Windows ML
- **Thiết bị Windows**: Tối ưu hóa cho các thiết bị biên và PC chạy Windows
- **Tăng tốc NPU**: Tận dụng các Neural Processing Units trên thiết bị Windows
- **DirectML**: Sử dụng DirectML để tăng tốc GPU trên các nền tảng Windows
- **Tích hợp UWP**: Tích hợp với các ứng dụng Universal Windows Platform

### TensorFlow Lite
- **Tối ưu hóa di động**: Triển khai các mô hình TensorFlow Lite trên thiết bị di động và nhúng
- **Đại biểu phần cứng**: Sử dụng các đại biểu phần cứng chuyên dụng để tăng tốc
- **Vi điều khiển**: Triển khai trên các vi điều khiển bằng TensorFlow Lite Micro
- **Hỗ trợ đa nền tảng**: Triển khai trên Android, iOS và các hệ thống Linux nhúng

### Azure IoT Edge
- **Kết hợp đám mây-biên**: Kết hợp huấn luyện trên đám mây với suy luận tại biên
- **Triển khai module**: Triển khai các mô hình AI dưới dạng các module IoT Edge
- **Quản lý thiết bị**: Quản lý thiết bị biên và cập nhật mô hình từ xa
- **Thu thập dữ liệu**: Thu thập dữ liệu hiệu suất và các chỉ số mô hình từ các triển khai tại biên

## Các kịch bản AI tại biên nâng cao

### Triển khai đa mô hình
- **Tập hợp mô hình**: Triển khai nhiều mô hình để cải thiện độ chính xác hoặc tăng tính dự phòng
- **Thử nghiệm A/B**: Thử nghiệm các mô hình khác nhau đồng thời trên các thiết bị biên
- **Lựa chọn động**: Chọn mô hình dựa trên điều kiện hiện tại của thiết bị
- **Chia sẻ tài nguyên**: Tối ưu hóa việc sử dụng tài nguyên giữa các mô hình được triển khai

### Học liên kết
- **Huấn luyện phân tán**: Huấn luyện mô hình trên nhiều thiết bị biên
- **Bảo vệ quyền riêng tư**: Giữ dữ liệu huấn luyện tại chỗ trong khi chia sẻ cải tiến mô hình
- **Học tập hợp tác**: Cho phép các thiết bị học hỏi từ kinh nghiệm chung
- **Phối hợp biên-đám mây**: Phối hợp học tập giữa các thiết bị biên và hạ tầng đám mây

### Xử lý thời gian thực
- **Xử lý luồng**: Xử lý các luồng dữ liệu liên tục trên thiết bị biên
- **Suy luận độ trễ thấp**: Tối ưu hóa để giảm thiểu độ trễ suy luận
- **Xử lý theo lô**: Xử lý hiệu quả các lô dữ liệu trên thiết bị biên
- **Xử lý thích ứng**: Điều chỉnh xử lý dựa trên khả năng hiện tại của thiết bị

## Khắc phục sự cố phát triển AI tại biên

### Các vấn đề thường gặp
- **Hạn chế bộ nhớ**: Mô hình quá lớn so với bộ nhớ của thiết bị mục tiêu
- **Tốc độ suy luận**: Suy luận mô hình quá chậm so với yêu cầu thời gian thực
- **Suy giảm độ chính xác**: Tối ưu hóa làm giảm độ chính xác của mô hình không chấp nhận được
- **Tương thích phần cứng**: Mô hình không tương thích với phần cứng mục tiêu

### Chiến lược gỡ lỗi
- **Phân tích hiệu suất**: Sử dụng các tính năng theo dõi của AI Toolkit để xác định các nút thắt
- **Giám sát tài nguyên**: Giám sát việc sử dụng bộ nhớ và CPU trong quá trình phát triển
- **Kiểm tra từng bước**: Kiểm tra các tối ưu hóa từng bước để cô lập vấn đề
- **Mô phỏng phần cứng**: Sử dụng các công cụ phát triển để mô phỏng phần cứng mục tiêu

### Giải pháp tối ưu hóa
- **Lượng tử hóa thêm**: Áp dụng các kỹ thuật lượng tử hóa mạnh mẽ hơn
- **Kiến trúc mô hình**: Xem xét các kiến trúc mô hình khác được tối ưu hóa cho biên
- **Tối ưu hóa tiền xử lý**: Tối ưu hóa tiền xử lý dữ liệu cho các hạn chế tại biên
- **Tối ưu hóa suy luận**: Sử dụng các tối ưu hóa suy luận cụ thể cho phần cứng

## Tài nguyên và bước tiếp theo

### Tài liệu
- [Hướng dẫn Mô hình AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/models)
- [Tài liệu Model Playground](https://code.visualstudio.com/docs/intelligentapps/playground)
- [Tài liệu ONNX Runtime](https://onnxruntime.ai/)
- [Tài liệu Windows ML](https://docs.microsoft.com/en-us/windows/ai/)

### Cộng đồng và hỗ trợ
- [GitHub AI Toolkit cho VS Code](https://github.com/microsoft/vscode-ai-toolkit)
- [Cộng đồng ONNX](https://github.com/onnx/onnx)
- [Cộng đồng Nhà phát triển Edge AI](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [Chợ tiện ích mở rộng VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Tài nguyên học tập
- [Khóa học Cơ bản về Edge AI](./Module01/README.md)
- [Hướng dẫn Mô hình Ngôn ngữ Nhỏ](./Module02/README.md)
- [Chiến lược Triển khai tại Biên](./Module03/README.md)
- [Phát triển AI tại Biên trên Windows](./windowdeveloper.md)

## Kết luận

AI Toolkit cho Visual Studio Code cung cấp một nền tảng toàn diện cho phát triển AI tại biên, từ khám phá và tối ưu hóa mô hình đến triển khai và giám sát. Bằng cách tận dụng các công cụ và quy trình làm việc tích hợp, các nhà phát triển có thể tạo, kiểm tra và triển khai các ứng dụng AI hoạt động hiệu quả trên các thiết bị biên có tài nguyên hạn chế.

Với sự hỗ trợ cho ONNX, Ollama và các nhà cung cấp đám mây khác nhau, cùng với các khả năng tối ưu hóa và đánh giá, đây là lựa chọn lý tưởng cho phát triển AI tại biên. Cho dù bạn đang xây dựng các ứng dụng IoT, tính năng AI di động hay hệ thống trí tuệ nhúng, AI Toolkit cung cấp các công cụ và quy trình làm việc cần thiết để triển khai AI tại biên thành công.

Khi AI tại biên tiếp tục phát triển, AI Toolkit cho VS Code vẫn luôn đi đầu, cung cấp cho các nhà phát triển các công cụ và khả năng tiên tiến để xây dựng thế hệ ứng dụng thông minh tại biên tiếp theo.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.